*** Settings ***
Documentation     This is Table Test file
Resource         ../Library/Helper/CommonHelper.robot
Resource         ../Library/Helper/PageHelper.robot


Suite Setup         Launch Chromium Browser
Suite Teardown      Quit Opened Browser

Test Setup         Open Web Application
Test Teardown      Close Web Application

*** Test Cases ***
Download File Example Test Case
     Log  "This is download file example test case"
     ${text} =  Set Variable	    This is text to enter inside textarea element for the download test case
     Menu.Navigate Menu For Alerts      'File Download'
     ${filepath}    Download.Generate Link And Download File    ${text}     TextFile.txt
     ${flag}    check file content    ${filepath}    ${text}
     should be true   ${flag}