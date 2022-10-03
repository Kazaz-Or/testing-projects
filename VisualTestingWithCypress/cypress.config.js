const { defineConfig } = require("cypress");
const happoTask = require('happo-cypress/task');


module.exports = defineConfig({
  e2e: {
    baseUrl:'http://www.ultimateqa.com/',
    setupNodeEvents(on, config) {
      happoTask.register(on);
    },
  },
});
