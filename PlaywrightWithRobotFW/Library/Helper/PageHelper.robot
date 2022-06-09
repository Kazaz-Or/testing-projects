*** Settings ***
Documentation    This is page helper file
Library         ../Page/Menu.py
Library         ../Page/TableSortSearch.py
Library         ../Page/FileDownload.py
Library         ../Page/DragDrop.py
Library         ../Page/Dialog.py
Library         ../Page/PagePopup.py

*** Keywords ***

Menu.Navigate Menu For Input Forms
    [Arguments]     ${secondary_menu_item_name}
    ${page}     get page handle
    navigate menu item    ${page}    'Input Forms'      ${secondary_menu_item_name}

Menu.Navigate Menu For Table
    [Arguments]     ${secondary_menu_item_name}
    ${page}     get page handle
    navigate menu item    ${page}    'Table'      ${secondary_menu_item_name}

Menu.Navigate Menu For Alerts
    [Arguments]     ${secondary_menu_item_name}
    ${page}     get page handle
    navigate menu item    ${page}    'Alerts & Modals'      ${secondary_menu_item_name}

Menu.Navigate Menu For Others
    [Arguments]     ${secondary_menu_item_name}
    ${page}     get page handle
    navigate menu item    ${page}    'Others'      ${secondary_menu_item_name}

Table.Get Data From Sorted Column
    [Arguments]     ${column_name}
    ${page}     get page handle
    select table entries    ${page}    50
    sort column     ${page}     ${column_name}
    @{data}   get sorted data list   ${page}
    [Return]  ${data}

Table.Search And Get Data From Column
    [Arguments]     ${search_data}    ${column_name}
    ${page}     get page handle
    select table entries    ${page}    50
    search table data    ${page}   ${search_data}
    sort column     ${page}     ${column_name}
    @{data}   get sorted data list   ${page}
    [Return]   ${data}

Download.Generate Link And Download File
    [Arguments]     ${data_to_enter}        ${save_file_name}
    ${page}     get page handle
    enter data in textarea      ${page}     ${data_to_enter}
    generate download link      ${page}
    ${path}     download file               ${page}     ${save_file_name}
    [Return]    ${path}

Drag.Drag Ietms and Verify List
    ${page}     get page handle
    drag item   ${page}    1
    drag item   ${page}    2
    drag item   ${page}    3
    @{dragged_list}   get dragged items    ${page}
    [Return]    ${dragged_list}

Dialog.Initialize Dialog Accept
    ${page}     get page handle
    init dialog accept    ${page}

Dialog.Verify Alert Box Accept
    ${page}     get page handle
    click for alert box    ${page}

Dialog.Verify Confirm Box Accept
    ${page}     get page handle
    click for confirm box   ${page}

Dialog.Verify Prompt Box Accept
    ${page}     get page handle
    set prompt message      'Playwright'
    click for prompt box   ${page}

#Upload.Upload File In Silent Mode
#    [Arguments]     ${filepath}
#    ${page}     get page handle
#    silent upload file    ${page}    ${filepath}
#    ${name}   get uploaded file name    ${page}
#    Log    ${name}
#
#Upload.Upload File In Interactive Mode
#    [Arguments]     ${filepath}
#    ${page}     get page handle
#    interactive file upload     ${page}    ${filepath}
#    ${name}   get uploaded file name    ${page}
#    Log    ${name}
#
#Upload.Upload File In Listener Mode
#    [Arguments]     ${filepath}
#    ${page}     get page handle
#    init listener file upload   ${page}
#    set filepath upload     ${filepath}
#    click on file upload    ${page}

PagePopup.Verify Page Popup Aceess
    ${page}     get page handle
    sign up twitter popup    ${page}
