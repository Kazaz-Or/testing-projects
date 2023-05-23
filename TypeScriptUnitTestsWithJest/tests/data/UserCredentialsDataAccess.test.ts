import { DataBase } from "../../src/data/DataBase";
import { UserCredentialsDataAccess } from "../../src/data/UserCredentialsDataAccess"
import { Account } from "../../src/model/AuthModel";

const insertMock = jest.fn();
const getByMock = jest.fn();

jest.mock('../../src/data/DataBase', () => {
    return {
        DataBase : jest.fn().mockImplementation( () => {
            return {
                insert: insertMock,
                getBy: getByMock
            }
        })
    }
});


describe('UserCredentialsDataAccess test suite', () => {
    let sut: UserCredentialsDataAccess;
    const someAccount: Account = {
        id: '',
        password: 'somePassword',
        userName: 'someUserName'
    }
    const someId = '1234';

    beforeEach( () => {
        sut = new UserCredentialsDataAccess();
        expect(DataBase).toHaveBeenCalledTimes(1);
    });

    afterEach( () => {
        jest.clearAllMocks();
    });

    test('should add user and return the id', async () => {
        insertMock.mockResolvedValueOnce(someId);

        const id = await sut.addUser(someAccount);

        expect(id).toBe(someId);
        expect(insertMock).toHaveBeenCalledWith(someAccount);
    });

    test('should get user by id', async () => {
        getByMock.mockResolvedValueOnce(someAccount);

        const user = await sut.getUserById(someId);

        expect(user).toEqual(someAccount)
        expect(getByMock).toHaveBeenCalledWith('id', someId);
    });

    test('should get user by name', async () => {
        getByMock.mockResolvedValueOnce(someAccount);

        const user = await sut.getUserByUserName(someAccount.userName);

        expect(user).toEqual(someAccount)
        expect(getByMock).toHaveBeenCalledWith('userName', someAccount.userName);
    });

});
