import { generateRandomId } from "../../src/data/IdGenerator";


describe('IdGenerator test suite', ()=>{
    test('should return a random string', ()=>{
        const randomId = generateRandomId();
        expect(randomId.length).toBe(20);
    })
});
