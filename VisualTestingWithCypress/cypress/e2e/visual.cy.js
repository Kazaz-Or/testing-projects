/// <reference types="cypress" />

describe("home page", () => {
  beforeEach(() => {
    cy.visit("/");
    cy.scrollTo('bottom', { duration: 5000 });     // lazy loading
    cy.scrollTo('top', { duration: 2000 });
  });

  it("looks good", () => {
    // inspect the caught error that comes from RocketLazyLoadScripts which is somekind of a wordpress extension
    cy.on('uncaught:exception', (e) => {
      return false;
    })
    cy.happoHideDynamicElements({selectors: ['#scroll']});
    cy.get("body").happoScreenshot();
  });
});
