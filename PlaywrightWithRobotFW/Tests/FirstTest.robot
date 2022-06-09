*** Settings ***
Documentation    This is first robot test file
Resource          ../Library/Helper/CommonHelper.robot
Resource          ../Library/Helper/PageHelper.robot

Suite Setup       Launch Chromium Browser
Suite Teardown    Quit Opened Browser

Test Setup         Open Web Application
Test Teardown      Close Web Application

*** Test Cases ***
My First Test Case
    Log  "This is first test case"
    Menu.Navigate Menu For Input Forms      'Simple Form Demo'

My Second Test Case
    Log  "This is second test case"
    Menu.Navigate Menu For Table            'Table Pagination'