const { expect } = require("chai");
const sinon = require("sinon");
const fs = require("fs");
const proxyquire = require("proxyquire");

// Spies

describe("File Management", () => {
  beforeEach(() => {});

  afterEach(() => {
    sinon.restore();
  });

  describe("When creating a file", () => {
    it("Should create a new file", () => {
      const writeSpy = sinon.spy(fs, "writeFileSync");
      const fileManagement = proxyquire("./file.management", { fs });

      fileManagement.createFile("test.txt");
      expect(writeSpy.calledWith("./data/test.txt", "")).to.be.true;
    });

// Spies are good for monitoring functions - such as tracking logs, check if a function is being called, etc.
// But there are some use cases where using spies can go wrong, note this example - the test will pass, but will fail on the 2nd attempt because test.txt will be already exist and we’ll get an exception.

//      Error: EEXIST: file already exists, open './data/test.txt'

// I assume there are ways to deal with that, but you should be aware that spies are not the best option in such cases. Or to be more accurate, spies are not good at block any side effects. In such cases it is more logical to use Stubs.

    it("Should not create a new file if no name is specified", () => {
      const writeSpy = sinon.spy(fs, "writeFileSync");
      const fileManagement = proxyquire("./file.management", { fs });

      try {
        fileManagement.createFile();
      } catch (err) {}
      expect(writeSpy.notCalled).to.be.true;
    });
  });
});
