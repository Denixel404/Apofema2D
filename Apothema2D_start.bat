@echo off
echo Start Apofema2D v2.3.1 ...

:loop
start /wait "" "Apofema2D 2.3.1.exe"
echo Execution completed. Code %errorlevel%

:: Перезапуск программы при коде 2
if %errorlevel% equ 2 (
    echo Restart programm ...
    timeout /t 1 /nobreak >nul
    goto loop
) else if %errorlevel% equ 0 (
    echo 
) else (
    echo Complete! code %errorlevel%
)