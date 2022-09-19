const loginEndpoint = 'http://localhost:3000/api/user/login';


describe('User Login - Sanity', () => {
  it('User Login - Status Code 200', () => {
    cy.request({
      method: 'POST', 
      url: loginEndpoint,
      body: {
        email: 'static@test.io',
        password: 'simplepass'
      }
    })
    .then((response) => {
        expect(response.status).to.equal(200);
    } )
  });

  it('User Login - Response', () => {
    cy.request({
      method: 'POST', 
      url: loginEndpoint,
      body: {
        email: 'static@test.io',
        password: 'simplepass'
      }
    })
    .then((response) => {
        expect(response.body).to.equal('Logged in successfully');
    } )
  });

  it('User Login - Wrong email', () => {
    cy.request({
      method: 'POST', 
      url: loginEndpoint,
      failOnStatusCode: false,
      body: {
        email: 'static1@test.io',
        password: 'simplepass'
      }
    })
    .then((response) => {
        expect(response.status).to.equal(400);
        expect(response.body).to.equal('Email not found');
    } )
  });

  it('User Login - Wrong password', () => {
    cy.request({
      method: 'POST', 
      url: loginEndpoint,
      failOnStatusCode: false,
      body: {
        email: 'static@test.io',
        password: 'simplepass1'
      }
    })
    .then((response) => {
        expect(response.status).to.equal(401);
        expect(response.body).to.equal('Invalid password');
    } )
  });

});

describe('User Login - Error Cases', () => {
  it('User Login - Missing email field', () => {
    cy.request({
      method: 'POST', 
      url: loginEndpoint,
      failOnStatusCode: false,
      body: {
        password: 'simplepass'
      }
    })
    .then((response) => {
        expect(response.status).to.equal(400);
        expect(response.body).to.equal('"email" is required');
    } )
  });

  it('User Login - Missing password field', () => {
    cy.request({
      method: 'POST', 
      url: loginEndpoint,
      failOnStatusCode: false,
      body: {
        email: 'static@test.io'
      }
    })
    .then((response) => {
        expect(response.status).to.equal(400);
        expect(response.body).to.equal('"password" is required');
    } )
  });

});