@echo off

if "%OS%" == "Windows_NT" setlocal

set RUNINFACMD_DIR=%cd%

for %%I in (%0) do set CMD_NAME=%%~nI
set CMD_NAME=%CMD_NAME%.bat

rem Get batch file dir from cmd line relative path, or from PATH
rem
for %%I in (%0) do set CMD_FILE_DIR=%%~dpI
if exist "%CMD_FILE_DIR%%CMD_NAME%" goto cdCmdDir
for %%I in (%CMD_NAME%) do set CMD_FILE_DIR=%%~dp$PATH:I

:cdCmdDir
chdir /D "%CMD_FILE_DIR%\..\.."
set INSTALL_DIR=%cd%

call "%INSTALL_DIR%\isp\bin\%CMD_NAME%" %%*%

:end
if "%OS%" == "Windows_NT" endlocal
