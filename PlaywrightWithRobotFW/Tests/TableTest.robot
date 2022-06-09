*** Settings ***
Documentation     This is Table Test file
Resource         ../Library/Helper/CommonHelper.robot
Resource         ../Library/Helper/PageHelper.robot


Suite Setup         Launch Chromium Browser
Suite Teardown      Quit Opened Browser

Test Setup         Open Web Application
Test Teardown      Close Web Application

*** Test Cases ***
Table Sort Example Test Case
     Log  "This is test for Table sort"
     Menu.Navigate Menu For Table       'Table Sort & Search'
     @{data}  Table.Get Data From Sorted Column   'Age'
     ${flag}  is list sorted     ${data}
     should be true   ${flag}


Table Search Example Test Case
     Log  "This is test for Table search"
     Menu.Navigate Menu For Table       'Table Sort & Search'
     @{data}   Table.Search And Get Data From Column      London    Office
     ${flag}   verify list with same values     ${data}
     should be true   ${flag}
