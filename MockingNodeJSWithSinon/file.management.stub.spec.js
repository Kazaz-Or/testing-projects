const { expect } = require("chai");
const sinon = require("sinon");
const fs = require("fs");
const proxyquire = require("proxyquire");


describe("File Management", () => {
    afterEach(() => {
        sinon.restore();
    });
    it("Should create a new file", () => {
        const writeStub = sinon.stub(fs, "writeFileSync");
        const fileManagement = proxyquire("./file.management", { fs });

        fileManagement.createFile("test.txt");
        
        expect(writeStub.callCount).to.equal(1);
    });

    it("Should throw an exception if file already exists", () => {
        const writeStub = sinon.stub(fs, "writeFileSync");
        writeStub.throws(new Error());
        const fileManagement = proxyquire("./file.management", { fs });

        expect(() => fileManagement.createFile("test.txt")).to.throw();
    });

    it("createFileSafe should create a file named test1 when test file already exists", () => {
        const writeStub = sinon.stub(fs, "writeFileSync");
        const readStub = sinon.stub(fs, "readdirSync");

        const fileManagement = proxyquire("./file.management", { fs });

        writeStub.withArgs("./data/test.txt").throws(new Error());
        writeStub.returns(undefined);
        readStub.returns(["test.txt"]);
    });

    it("Should not create a new file if no name is specified", () => {
        const writeStub = sinon.stub(fs, "writeFileSync");
        const fileManagement = proxyquire("./file.management", { fs });

        try {
            fileManagement.createFile();
        } catch (err) {}

        expect(writeStub.notCalled).to.be.true;
    });

    it("getAllFiles should return a list of files", () => {
        const readStub = sinon.stub(fs, "readdir");
        const fileManagement = proxyquire("./file.management", { fs });
        readStub.yields(null, ["test.txt"]);

        fileManagement.getAllFiles((err, data) => { 
            expect(data).to.eql(["test.txt"]);
        });
    });

    it("getAllFilesPromise should return a list of files", () => {
        const readStub = sinon.stub(fs, "readdir");

        const util = {
            promisify: sinon.stub().returns(readStub)
        };

        const fileManagement = proxyquire("./file.management", { fs, util });
        readStub.resolves(["test.txt"]);

        return fileManagement.getAllFilesPromise().then(files => expect(files).to.eql(["test.txt"]));
    });


});