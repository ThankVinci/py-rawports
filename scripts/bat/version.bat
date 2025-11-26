@echo off

for /f "tokens=1,2 delims==" %%A in (..\..\version.env) do (
    if not "%%A"=="" if not "%%A:~0,1%"=="#" (
        set "%%A=%%B"
    )
)

set REL_VER=%MAJOR_VER%.%MINOR_VER%.%BUILD_VER%
