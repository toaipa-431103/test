*** Settings ***
Library        AppiumLibrary
*** Variables ***
${btn_confirm}            resource_id=Xác nhận
${btn_start}            resource_id=Bắt đầu ngày
${timeout}                30s
${input_phone_number}        resource_id=Phonenumber
${phone_number}            0342784232

*** Test Cases ***
TC1_Chuyen_tien_den_so_dien_thoai_nguon_VTP
    Log To Console            ${TEST_NAME}
    Log           ${TEST_NAME}
TC2+Chuyen_tien_den_so_dien_thoai_nguon_MM+
    Log To Console            ${TEST_NAME}
    Log           ${TEST_NAME}
#    Open Application                
#    Wait Until Element Is Visible             ${btn_start}          ${timeout}    
#    Click Element       ${btn_start}  
#    Wait Until Element Is Visible             ${input_phone_number}          ${timeout}    
#   Input Text         ${input_phone_number}                ${phone_number}
#   Wait Until Element Is Visible             ${input_phone_number}          ${timeout}    
#   Input Text         ${input_phone_number}                ${phone_number}
*** Keywords ***

