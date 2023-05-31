import { IncomingMessage, ServerResponse } from "http";

import { Authorizer } from "../../src/auth/Authorizer";
import { LoginHandler } from "../../src/handlers/LoginHandler";
import { Account } from "../../src/model/AuthModel";
import { HTTP_CODES, HTTP_METHODS } from "../../src/model/ServerModel";

const getRequestBodyMock = jest.fn();

jest.mock('../../src/utils/Utils', () => ({
    getRequestBody: () => getRequestBodyMock()
}));


describe('LoginHandler test suite', () => {
    let sut: LoginHandler;
    const request = {
        method: undefined
    };
    const responseMock = {
        writeHead: jest.fn(),
        write: jest.fn(),
        statusCode: 0
    };
    const authorizerMock = {
        login: jest.fn()
    }
    const someToken = '1234';
    const someAccount: Account = {
        id: '',
        password: 'somePassword',
        userName: 'someUserName'
    }

    beforeEach(() => {
        sut = new LoginHandler(
            request as IncomingMessage,
            responseMock as any as ServerResponse,
            authorizerMock as any as Authorizer
        );
    });

    afterEach(() => {
        jest.clearAllMocks()
    });

    test('should return token for valid accounts in requests', async () => {
        request.method = HTTP_METHODS.POST;
        getRequestBodyMock.mockResolvedValueOnce(someAccount);
        authorizerMock.login.mockResolvedValueOnce(someToken);

        await sut.handleRequest();

        expect(authorizerMock.login).toBeCalledWith(
            someAccount.userName,
            someAccount.password
        )
        expect(responseMock.statusCode).toBe(HTTP_CODES.CREATED);
        expect(responseMock.writeHead).toBeCalledWith(
            HTTP_CODES.CREATED, { 'Content-Type': 'application/json' }
        )
        expect(responseMock.write).toBeCalledWith(
            JSON.stringify({
                token: someToken
            })
        )
    });

    test('should return not found for invalid accounts in requests', async () => {
        request.method = HTTP_METHODS.POST;
        getRequestBodyMock.mockResolvedValueOnce(someAccount);
        authorizerMock.login.mockResolvedValueOnce(undefined);

        await sut.handleRequest();

        expect(authorizerMock.login).toBeCalledWith(
            someAccount.userName,
            someAccount.password
        )
        expect(responseMock.statusCode).toBe(HTTP_CODES.NOT_fOUND);
        expect(responseMock.write).toBeCalledWith(
            JSON.stringify('wrong username or password')
        )
    });

    test('should return bad request for invalid requests', async () => {
        request.method = HTTP_METHODS.POST;
        getRequestBodyMock.mockResolvedValueOnce({});

        await sut.handleRequest();

        expect(authorizerMock.login).not.toBeCalled();
        expect(responseMock.statusCode).toBe(HTTP_CODES.BAD_REQUEST);
        expect(responseMock.write).toBeCalledWith(
            JSON.stringify('userName and password required')
        )
    });

    test('should do nothing for not supported http methods', async () => {
        request.method = HTTP_METHODS.GET;
        await sut.handleRequest();

        expect(responseMock.writeHead).not.toBeCalled();
        expect(responseMock.write).not.toBeCalled();
        expect(getRequestBodyMock).not.toBeCalled();
    });

});
