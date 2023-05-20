jest.mock('../doubles/OtherUtils', () => (
    {...jest.requireActual('../doubles/OtherUtils'),
    calculateComplexity: () => {return 10}
}
));

jest.mock('uuid', () => ({
    v4: () => '123'
}));

import * as OtherUtils from '../doubles/OtherUtils';

describe('module tests', ()=>{
    test('calculate complexity', ()=>{
        const result = OtherUtils.calculateComplexity({} as any);
        expect(result).toBe(10);
    });

    test('keep other functions', ()=>{
        const result = OtherUtils.toUpperCase('abc');
        expect(result).toBe('ABC');
    });

    test('string with id', ()=>{
        const result = OtherUtils.toLowerCaseWithId('ABC');
        expect(result).toBe('abc123');
    });
});
