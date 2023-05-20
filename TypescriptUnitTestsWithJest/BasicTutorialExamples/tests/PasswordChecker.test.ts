import { PasswordChecker, PasswordErrors } from "../src/app/pass_checker/PasswordChecker"


describe('Password Checker Test Suite', () => {
    let sut: PasswordChecker;
    
    beforeEach(() => {
        sut = new PasswordChecker();
    });

    test('Invalid password - 8 Chars, no letters', () => {
        const response = sut.checkPassword('12345678');
        expect(response.valid).toBe(false);
        expect(response.reasons).toContain(PasswordErrors.NO_LOWER_CASE)
    });

    test('Invalid password - More than 8 Chars, no letters', () => {
        const response = sut.checkPassword('123456789');
        expect(response.valid).toBe(false);
        expect(response.reasons).toContain(PasswordErrors.NO_LOWER_CASE)
    });

    test('Password with less than 8 chars is invalid', () => {
        const response = sut.checkPassword('1234567');
        expect(response.valid).toBe(false);
        expect(response.reasons).toContain(PasswordErrors.SHORT)

    });

    test('Password with no upper case is invalid', () => {
        const response = sut.checkPassword('1234abcd');
        expect(response.valid).toBe(false);
        expect(response.reasons).toContain(PasswordErrors.NO_UPPER_CASE)

    });

    test('Password with upper case, lower case and 8 chars is valid', () => {
        const response = sut.checkPassword('1234abcD');
        expect(response.valid).toBe(true);
        expect(response.reasons).toHaveLength(0);
    });

    test('Password with upper case, lower case and more than 8 chars is valid', () => {
        const response = sut.checkPassword('1234abcDDBC');
        expect(response.valid).toBe(true);
        expect(response.reasons).toHaveLength(0);
    });

    test('Password with upper case and less than 8 chars is invalid', () => {
        const response = sut.checkPassword('1234abD');
        expect(response.valid).toBe(false);
        expect(response.reasons).toContain(PasswordErrors.SHORT)
    });
    
    test('Password with no lower case and more than 8 chars is invalid', () => {
        const response = sut.checkPassword('1234ABCDE');
        expect(response.valid).toBe(false);
        expect(response.reasons).toContain(PasswordErrors.NO_LOWER_CASE)
    });

    test('Admin password with no number is invalid', () => {
        const response = sut.checkAdminPassword('testTest');
        expect(response.valid).toBe(false);
        expect(response.reasons).toContain(PasswordErrors.NO_NUMBER)
    });
    
    test('Valid admin password', () => {
        const response = sut.checkAdminPassword('testTest1');
        expect(response.valid).toBe(true);
        expect(response.reasons).toHaveLength(0);
    });

});