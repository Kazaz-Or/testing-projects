import { DataBase } from "../../src/data/DataBase"
import * as IdGenerator from "../../src/data/IdGenerator";


type someTypeWithId = {
    id: string,
    name: string,
    color: string
};

describe("Database test suite", () => {
    let sut: DataBase<someTypeWithId>;
    const fakeId = '1234';
    const testObject = {
        id: '',
        name: 'testName',
        color: 'blue'
    }
    const testObject2 = {
        id: '',
        name: 'testOtherName',
        color: 'blue'
    }
    beforeEach(() => {
        sut = new DataBase<someTypeWithId>();
        jest.spyOn(IdGenerator, 'generateRandomId').mockReturnValue(fakeId);
    });

    test('Should return id after insert', async () => {
        const response = await sut.insert({
            id: ''
        }as any);
        
        expect(response).toBe(fakeId);
    });

    test('Should get element after insert', async () => {
        const id = await sut.insert(testObject);
        const response = await sut.getBy('id', id);
        
        expect(response).toBe(testObject);
    });

    test('Should find all elements with the same property', async () => {
        await sut.insert(testObject);
        await sut.insert(testObject2);
        
        const response = await sut.findAllBy('color', 'blue');
        
        expect(response).toEqual([testObject, testObject2]);
    });

    test('Should change color on object', async () => {
        const id = await sut.insert(testObject);

        await sut.update(id, 'color', 'yellow');
        const object = await sut.getBy('id', id);

        expect(object.color).toEqual('yellow');
    });

    test('Should delete object', async () => {
        const id = await sut.insert(testObject);

        await sut.delete(id);
        const response = await sut.getBy('id', id);

        expect(response).toBeUndefined();
    });

    test('should get all elements', async () => {
        await sut.insert(testObject);
        await sut.insert(testObject2);

        const response = await sut.getAllElements();

        expect(response).toEqual([testObject, testObject2]);
    });

});
