import { SessionTokenDataAccess } from "../../src/data/SessionTokenDataAccess";
import { DataBase } from '../../src/data/DataBase';
import * as IdGenerator from '../../src/data/IdGenerator';
import { Account } from "../../src/model/AuthModel";


const mockInsert = jest.fn();
const mockGetBy = jest.fn();
const mockUpdate = jest.fn();

jest.mock('../../src/data/DataBase', () => {
    return {
        DataBase: jest.fn().mockImplementation(() => {
            return {
                insert: mockInsert,
                getBy: mockGetBy,
                update: mockUpdate
            }
        })
    }
});

const someAccount: Account = {
    id: '',
    password: 'somePassword',
    userName: 'someUserName'
}

describe('SessionTokenDataAccess test suite', () => {
    let sut: SessionTokenDataAccess;
    const fakeId = '1234'

    beforeEach(() => {
        sut = new SessionTokenDataAccess();
        expect(DataBase).toHaveBeenCalledTimes(1);
        jest.spyOn(global.Date, 'now').mockReturnValue(0);
        jest.spyOn(IdGenerator, 'generateRandomId').mockReturnValueOnce(fakeId);
    });

    afterEach(() => {
        jest.clearAllMocks();
    });

    test('should generate token for account', async () => {
        mockInsert.mockResolvedValueOnce(fakeId);
        const tokenId = await sut.generateToken(someAccount);

        expect(tokenId).toBe(fakeId);
        expect(mockInsert).toBeCalledWith({
            id: '',
            userName: someAccount.userName,
            valid: true,
            expirationDate: new Date(1000 * 60 * 60)
        });
    });

    test('should invalidate token', async () => {
        await sut.invalidateToken(fakeId);

        expect(mockUpdate).toBeCalledWith(fakeId, 'valid', false);
    })

    test('should check valid token', async () => {
        mockGetBy.mockResolvedValueOnce({ valid: true });

        const response = await sut.isValidToken({} as any)

        expect(response).toBe(true);
    });

    test('should check invalid token', async () => {
        mockGetBy.mockResolvedValueOnce({ valid: false });

        const response = await sut.isValidToken({} as any)

        expect(response).toBe(false);
    });

    test('should check inexistent token', async () => {
        mockGetBy.mockResolvedValueOnce(undefined);

        const response = await sut.isValidToken({} as any)

        expect(response).toBe(false);
    });

});
