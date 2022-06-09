*** Settings ***
Documentation     This is Page Popup Test File
Resource         ../Library/Helper/CommonHelper.robot
Resource         ../Library/Helper/PageHelper.robot


Suite Setup         Launch Chromium Browser
Suite Teardown      Quit Opened Browser

Test Setup         Open Web Application
Test Teardown      Close Web Application

*** Test Cases ***
Page popup verufy test case
     Log  "This Page Popup Test Case"
     Menu.Navigate Menu For Alerts   'Window Popup Modal'
     PagePopup.Verify Page Popup Aceess
     Menu.Navigate Menu For Alerts   'Window Popup Modal'
