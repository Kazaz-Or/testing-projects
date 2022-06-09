*** Settings ***
Documentation     This is Drag Test file
Resource         ../Library/Helper/CommonHelper.robot
Resource         ../Library/Helper/PageHelper.robot


Suite Setup         Launch Chromium Browser
Suite Teardown      Quit Opened Browser

Test Setup         Open Web Application
Test Teardown      Close Web Application

*** Test Cases ***
Drag And Drop Item Test Case
     Log  "This Is Drag And Drop Item Test Case"
     Menu.Navigate Menu For Others      'Drag and Drop'
     @{item_list}       Drag.Drag Ietms and Verify List
     Log   ${item_list}