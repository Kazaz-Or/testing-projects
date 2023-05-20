import { StringUtils, getStringInfo, toUpperCase } from "../src/app/utils"


describe('utils test suite', () => {

    test.each([
        {input: 'test', expected: 'TEST'},
        {input: 'TEST', expected: 'TEST'},
        {input: 'test1$&*#()^41', expected: 'TEST1$&*#()^41'}
    ])('$input to UpperCase should return $expected', ({input, expected}) => {
        const result = toUpperCase(input);

        expect(result).toBe(expected);
    });

    test('should return info for valid string', () => {
        const result = getStringInfo('My-String');

        expect(result.extraInfo).toEqual({});
        expect(result.lowerCase).toBe('my-string');
        expect(result.length).toBe(9);

        expect(result.characters).toStrictEqual(["M", "y", "-", "S", "t", "r", "i", "n", "g"]);
        expect(result.characters).toHaveLength(9);
        expect(result.characters).toContain<string>('-');
    });

});


describe('StringUtils class', ()=> {
    let sut: StringUtils;

    beforeEach(()=>{
        sut = new StringUtils();
    });

    test('Sanity - valid string', () => {
        const result = sut.toUpperCase('abc');
        
        expect(result).toBe('ABC');
    });

    test('Should throw error on invalid argument (empty string) - function', () => {
        function expectError() {
            const result = sut.toUpperCase('');
        };
        
        expect(expectError).toThrow();
        expect(expectError).toThrowError('Invalid Argument');
    });

    test('Should throw error on invalid argument (empty string) - arrow function', () => {
        expect(() => {
            sut.toUpperCase('')
        }).toThrowError('Invalid Argument');
    });

    test('Should throw error on invalid argument (empty string) - try catch block', () => {
        try {
            sut.toUpperCase('');
            fail('GetStringInfo should throw error for invalid arg');
        } catch (error) {
            expect(error).toBeInstanceOf(Error);
            expect(error).toHaveProperty('message', 'Invalid Argument');
        }
    }); // This won't fail in case it doesn't reach the catch block due to a Jest bug - https://github.com/jestjs/jest/issues/11698, workaround test in the next test

    test('Should throw error on invalid argument (empty string) - try catch block (workaround)', (done) => {
        try {
            sut.toUpperCase('');
            done('GetStringInfo should throw error for invalid arg');
        } catch (error) {
            expect(error).toBeInstanceOf(Error);
            expect(error).toHaveProperty('message', 'Invalid Argument');
            done();
        }
    });

});
