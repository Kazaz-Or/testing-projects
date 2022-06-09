*** Settings ***
Documentation    Common helper file
Library          ../PyLib/PlaywrightCore.py
Library          ../PyLib/UtilityCore.py

*** Keywords ***
Launch Chromium Browser
    launch browser    browser_name=chromium

Launch Firefox Browser
    launch browser    browser_name=firefox

Launch Webkit Browser
    launch browser    browser_name=webkit

Quit Opened Browser
    close browser

Open Web Application
    open application

Close Web Application
    close application

Get Page Handle
    ${page_handle}     get page object
    [Return]    ${page_handle}

Is List Sorted
    [Arguments]     ${list_data}
    ${flag}  verify list ascending order     ${list_data}
    [Return]   ${flag}
