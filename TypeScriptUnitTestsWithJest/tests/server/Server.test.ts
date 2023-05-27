import { Authorizer } from "../../src/auth/Authorizer";
import { ReservationsDataAccess } from "../../src/data/ReservationsDataAccess";
import { Server } from "../../src/server/Server";
import { LoginHandler } from "../../src/handlers/LoginHandler";
import { RegisterHandler } from "../../src/handlers/RegisterHandler";
import { ReservationsHandler } from "../../src/handlers/ReservationsHandler";
import { HTTP_CODES } from "../../src/model/ServerModel";

jest.mock('../../src/auth/Authorizer');
jest.mock('../../src/data/ReservationsDataAccess');
jest.mock('../../src/handlers/LoginHandler');
jest.mock('../../src/handlers/RegisterHandler');
jest.mock('../../src/handlers/ReservationsHandler');

const requestMock = {
    url: '',
    headers: {
        'user-agent': 'jest-test'
    }
};

const responseMock = {
    end: jest.fn(),
    writeHead: jest.fn()
};

const serverMock = {
    listen: jest.fn(),
    close: jest.fn()
};

jest.mock('http', ()=>({
    createServer : (cb: Function) =>{
        cb(requestMock, responseMock)
        return serverMock
    }
}));


describe('Server test suite', ()=>{
    let sut: Server

    beforeEach(()=>{
        sut = new Server();
        expect(Authorizer).toBeCalledTimes(1);
        expect(ReservationsDataAccess).toBeCalledTimes(1);
    });

    afterEach(()=>{
        jest.clearAllMocks();
    });

    test('should start server on port 8080 and end the request', async ()=>{
        await sut.startServer();

        expect(serverMock.listen).toBeCalledWith(8080);

        console.log('checking response.end calls:')
        expect(responseMock.end).toBeCalled();
    });

    test('should handle register requests', async ()=>{
        requestMock.url = 'localhost:8080/register';
        const handleRequestSpy = jest.spyOn(RegisterHandler.prototype, 'handleRequest');

        await sut.startServer();

        expect(handleRequestSpy).toBeCalledTimes(1);
        expect(RegisterHandler).toBeCalledWith(requestMock, responseMock, expect.any(Authorizer));
    });

    test('should handle login requests', async ()=>{
        requestMock.url = 'localhost:8080/login';
        const handleRequestSpy = jest.spyOn(LoginHandler.prototype, 'handleRequest');

        await sut.startServer();

        expect(handleRequestSpy).toBeCalledTimes(1);
        expect(LoginHandler).toBeCalledWith(requestMock, responseMock, expect.any(Authorizer));
    });

    test('should handle reservation requests', async ()=>{
        requestMock.url = 'localhost:8080/reservation';
        const handleRequestSpy = jest.spyOn(ReservationsHandler.prototype, 'handleRequest');

        await sut.startServer();

        expect(handleRequestSpy).toBeCalledTimes(1);
        expect(ReservationsHandler).toBeCalledWith(
            requestMock, 
            responseMock, 
            expect.any(Authorizer),
            expect.any(ReservationsDataAccess));
    });

    test('should do nothing for not supported routes', async ()=>{
        requestMock.url = 'localhost:8080/someRandomRoute';
        const validateTokenSpy = jest.spyOn(Authorizer.prototype, 'validateToken');

        await sut.startServer();

        expect(validateTokenSpy).not.toBeCalled();
    });


    test('should handle errors in serving requests', async ()=>{
        requestMock.url = 'localhost:8080/reservation';
        const handleRequestSpy = jest.spyOn(ReservationsHandler.prototype, 'handleRequest');
        handleRequestSpy.mockRejectedValueOnce(
            new Error('Some error')
        )

        await sut.startServer();

        expect(responseMock.writeHead).toBeCalledWith(
            HTTP_CODES.INTERNAL_SERVER_ERROR, 
            JSON.stringify(`Internal server error: Some error`)
        )
    });

    test('should stop the server if started',async ()=>{
        await sut.startServer();

        await sut.stopServer();

        expect(serverMock.close).toBeCalledTimes(1);
    });

});
