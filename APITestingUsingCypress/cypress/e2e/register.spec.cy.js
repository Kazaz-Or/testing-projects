const registerEndpoint = 'http://localhost:3000/api/user/register';
const Guid = require('guid');


describe('User Registration - Sanity', () => {
  it('User Registration - Status Code 200', () => {
    let dynamicEmail = Guid.raw() + '@example.com'
    cy.request({
      method: 'POST', 
      url: registerEndpoint,
      body: {
        name: 'tester',
        email: dynamicEmail,
        password: '12345678'
      }
    })
    .then((response) => {
        expect(response.status).to.equal(200);
    } )
  });

  it('User Registration - Response', () => {
    let dynamicEmail = Guid.raw() + '@example.com'
    cy.request({
      method: 'POST', 
      url: registerEndpoint,
      body: {
        name: 'tester',
        email: dynamicEmail,
        password: '12345678'
      }
    })
    .then((response) => {
        expect(response.body.name).to.equal('tester');
        expect(response.body.email).to.equal(dynamicEmail);
        expect(response.body.password).to.not.equal('123456');
    } )
  });
});


describe('User Registration - Schema Fields Validation', () => {
  it('User Registration missing name field', () => {
    let dynamicEmail = Guid.raw() + '@example.com'
    cy.request({
      method: 'POST', 
      url: registerEndpoint,
      failOnStatusCode: false,
      body: {
        email: dynamicEmail,
        password: '12345678'
      }
    })
    .then((response) => {
        expect(response.status).to.equal(400);
        expect(response.body).to.equal('"name" is required');
    } )
  });

  it('User Registration missing email field', () => {
    cy.request({
      method: 'POST', 
      url: registerEndpoint,
      failOnStatusCode: false,
      body: {
        name: 'tester',
        password: '12345678'
      }
    })
    .then((response) => {
        expect(response.status).to.equal(400);
        expect(response.body).to.equal('"email" is required');
    } )
  });

  it('User Registration missing password field', () => {
    let dynamicEmail = Guid.raw() + '@example.com'
    cy.request({
      method: 'POST', 
      url: registerEndpoint,
      failOnStatusCode: false,
      body: {
        name: 'tester',
        email: dynamicEmail
      }
    })
    .then((response) => {
        expect(response.status).to.equal(400);
        expect(response.body).to.equal('"password" is required');
    } )
  });

  it('User Registration name field under minimum chars', () => {
    let dynamicEmail = Guid.raw() + '@example.com'
    cy.request({
      method: 'POST', 
      url: registerEndpoint,
      failOnStatusCode: false,
      body: {
        name: 't',
        email: dynamicEmail,
        password: '12345678'
      }
    })
    .then((response) => {
        expect(response.status).to.equal(400);
        expect(response.body).to.equal('"name" length must be at least 2 characters long');
    } )
  });

  it('User Registration email field invalid email', () => {
    cy.request({
      method: 'POST', 
      url: registerEndpoint,
      failOnStatusCode: false,
      body: {
        name: 'test-user',
        email: 'tester.example.com@',
        password: '12345678'
      }
    })
    .then((response) => {
        expect(response.status).to.equal(400);
        expect(response.body).to.equal('"email" must be a valid email');
    } )
  });

  it('User Registration password field under minimum chars', () => {
    let dynamicEmail = Guid.raw() + '@example.com'
    cy.request({
      method: 'POST', 
      url: registerEndpoint,
      failOnStatusCode: false,
      body: {
        name: 'test-user',
        email: dynamicEmail,
        password: '1234567'
      }
    })
    .then((response) => {
        expect(response.status).to.equal(400);
        expect(response.body).to.equal('"password" length must be at least 8 characters long');
    } )
  });

  it('User Registration name field wrong type', () => {
    let dynamicEmail = Guid.raw() + '@example.com'
    cy.request({
      method: 'POST', 
      url: registerEndpoint,
      failOnStatusCode: false,
      body: {
        name: 5352,
        email: dynamicEmail,
        password: '1234235967'
      }
    })
    .then((response) => {
        expect(response.status).to.equal(400);
        expect(response.body).to.equal('"name" must be a string');
    } )
  });

  it('User Registration password field wrong type', () => {
    let dynamicEmail = Guid.raw() + '@example.com'
    cy.request({
      method: 'POST', 
      url: registerEndpoint,
      failOnStatusCode: false,
      body: {
        name: '5352user',
        email: dynamicEmail,
        password: 1235674533
      }
    })
    .then((response) => {
        expect(response.status).to.equal(400);
        expect(response.body).to.equal('"password" must be a string');
    } )
  });

  it('User Registration email field wrong type', () => {
    cy.request({
      method: 'POST', 
      url: registerEndpoint,
      failOnStatusCode: false,
      body: {
        name: '5352user',
        email: true,
        password: '1235674pass'
      }
    })
    .then((response) => {
        expect(response.status).to.equal(400);
        expect(response.body).to.equal('"email" must be a string');
    } )
  });

});

describe('User Registration - Negative Cases', () => {
  it('User Registration without payload - Response 400', () => {
    cy.request({
      method: 'POST', 
      url: registerEndpoint, 
      failOnStatusCode: false
    })
    .then((response) => {
        expect(response.status).to.equal(400);
        expect(response.body).to.equal('"name" is required');
    } )
  });

  it('User Registration - Special chars in name field', () => {
    let dynamicEmail = Guid.raw() + '@example.com'
    cy.request({
      method: 'POST', 
      url: registerEndpoint,
      body: {
        name: 'tester!@#$%^&*()-_=+/.><~`  ',
        email: dynamicEmail,
        password: '12345678'
      }
    })
    .then((response) => {
        expect(response.status).to.equal(200);
    } )
  });

  it('User Registration - Special chars in password field', () => {
    let dynamicEmail = Guid.raw() + '@example.com'
    cy.request({
      method: 'POST', 
      url: registerEndpoint,
      body: {
        name: 'testerspecialchars',
        email: dynamicEmail,
        password: '123456!@#$%^&*()-_=+/.><~`  '
      }
    })
    .then((response) => {
        expect(response.status).to.equal(200);
    } )
  });

  it('User Registration - Registration with an already exists email', () => {
      cy.request({
        method: 'POST', 
        url: registerEndpoint,
        failOnStatusCode: false,
        body: {
          name: 'tester',
          email: 'tester@example.com',
          password: '12345678'
        }
      })
      .then((response) => {
          expect(response.status).to.equal(400);
          expect(response.body).to.equal('Email already exists');
      } )
    });

});