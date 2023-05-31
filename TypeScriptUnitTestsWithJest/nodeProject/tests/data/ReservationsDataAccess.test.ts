import { ReservationsDataAccess } from "../../src/data/ReservationsDataAccess";
import { DataBase } from '../../src/data/DataBase';
import * as IdGenerator from '../../src/data/IdGenerator';
import { Reservation } from "../../src/model/ReservationModel";

const mockInsert = jest.fn();
const mockGetBy = jest.fn();
const mockUpdate = jest.fn();
const mockDelete = jest.fn();
const mockGetAllElements = jest.fn();

jest.mock('../../src/data/DataBase', () => {
    return {
        DataBase: jest.fn().mockImplementation(() => {
            return {
                insert: mockInsert,
                getBy: mockGetBy,
                update: mockUpdate,
                delete: mockDelete,
                getAllElements: mockGetAllElements
            }
        })
    }
});

describe('ReservationsDataAccess test suite', () => {
    let sut: ReservationsDataAccess;
    const someId = '1234';
    const someReservation: Reservation = {
        endDate: 'someEndDate',
        startDate: 'someStartDate',
        id: '',
        room: 'someRoom',
        user: 'someUser'
    }

    beforeEach(() => {
        sut = new ReservationsDataAccess();
        expect(DataBase).toHaveBeenCalledTimes(1);
        jest.spyOn(IdGenerator, 'generateRandomId').mockReturnValueOnce(someId);
    });

    afterEach(() => {
        jest.clearAllMocks();
        someReservation.id = '';
    });

    test('should return the id of newly created reservation', async () => {
        mockInsert.mockResolvedValueOnce(someId);

        const response = await sut.createReservation(someReservation);

        expect(response).toBe(someId);
        expect(mockInsert).toBeCalledWith(someReservation);
    });

    test('should make the update reservation call', async () => {
        await sut.updateReservation(
            someId,
            'endDate',
            'someOtherEndDate'
        )

        expect(mockUpdate).toBeCalledWith(
            someId,
            'endDate',
            'someOtherEndDate'
        )
    });

    test('should make the delete reservation call', async () => {
        await sut.deleteReservation(someId);

        expect(mockDelete).toBeCalledWith(someId);
    });

    test('should return reservation by id', async () => {
        mockGetBy.mockResolvedValueOnce(someReservation);

        const response = await sut.getReservation(someId);

        expect(response).toEqual(someReservation);
        expect(mockGetBy).toBeCalledWith('id', someId);
    });

    test('should return all reservations', async () => {
        mockGetAllElements.mockResolvedValueOnce([someReservation, someReservation]);

        const response = await sut.getAllReservations();

        expect(response).toEqual([someReservation, someReservation]);
        expect(mockGetAllElements).toBeCalledTimes(1);
    });

});
