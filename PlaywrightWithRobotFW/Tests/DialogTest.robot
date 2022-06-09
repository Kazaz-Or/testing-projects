*** Settings ***
Documentation     This is Dialog Test file
Resource         ../Library/Helper/CommonHelper.robot
Resource         ../Library/Helper/PageHelper.robot


Suite Setup         Launch Chromium Browser
Suite Teardown      Quit Opened Browser

Test Setup         Open Web Application
Test Teardown      Close Web Application

*** Test Cases ***
Dialog Check Test Case
     Log  "This Is Dialog Check Test Case"
     Menu.Navigate Menu For Alerts      'Javascript Alerts'
     Dialog.Initialize Dialog Accept
     Dialog.Verify Alert Box Accept
     Dialog.Verify Confirm Box Accept
     Dialog.Verify Prompt Box Accept