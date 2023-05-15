import { OtherStringUtils, calculateComplexity, toUpperCaseWithCallBack } from "../src/app/doubles/OtherUtils";

describe('Other utils test suite', () => {
    const callBackMock = jest.fn();
    let sut: OtherStringUtils;

    beforeEach(()=>{
        sut = new OtherStringUtils();
    });
    
    afterEach(() => {
        jest.clearAllMocks();
    })

    test('Calculates complexity', () => {
        const someInfo = {
            length: 5,
            extraInfo: {
                field1: 'someInfo',
                field2: 'someOtherInfo',
            }
        }
        const response = calculateComplexity(someInfo as any);
        expect(response).toBe(10);
    });

    test('ToUpperCase - Calls callback for invalid argument', () => {
        const response = toUpperCaseWithCallBack('', () => {});
        expect(response).toBeUndefined();
    });

    test('ToUpperCase - Calls callback for invalid argument - Track calls', () => {
        const response = toUpperCaseWithCallBack('', callBackMock);
        expect(response).toBeUndefined();
        expect(callBackMock).toBeCalledWith('Invalid argument!');
        expect(callBackMock).toBeCalledTimes(1);
    });

    test('ToUpperCase - Calls callback for valid argument', () => {
        const response = toUpperCaseWithCallBack('abc', () => {});
        expect(response).toBe('ABC');
    });

    test('ToUpperCase - Calls callback for valid argument - Track calls', () => {
        const response = toUpperCaseWithCallBack('abc', callBackMock);
        expect(response).toBe('ABC');
        expect(callBackMock).toBeCalledWith('called function with abc');
        expect(callBackMock).toBeCalledTimes(1);
    });

    test('Use a spy to track calls', () => {
        const toUpperCaseSpy = jest.spyOn(sut, 'toUpperCase');
        sut.toUpperCase('asa');
        expect(toUpperCaseSpy).toBeCalledWith('asa');
    });

    test('Use a spy to track calls to other module', () => {
        const consoleLogSpy = jest.spyOn(console, 'log');
        sut.logString('abc');
        expect(consoleLogSpy).toBeCalledWith('abc');
    });

    test('Use a spy to replace the implementation of a method', () => {
        jest.spyOn(sut, 'callExternalService').mockImplementation(() => {
            console.log('calling mocked implementation!!!')
        });
        sut.callExternalService();
    });

});