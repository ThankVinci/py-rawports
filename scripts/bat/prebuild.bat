@echo off

@call .\version.bat

set SCRIPTS_DIR=%cd%
cd ..\..

if exist ".\build\bdist.win32" (
    @rmdir /Q /S ".\build\bdist.win32"
)

if exist ".\build\bdist.win-amd64" (
    @rmdir /Q /S ".\build\bdist.win-amd64"
)

if exist ".\build\lib" (
    @rmdir /Q /S ".\build\lib"
)

cd %SCRIPTS_DIR%