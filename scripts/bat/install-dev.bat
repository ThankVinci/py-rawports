@echo off

@call .\prebuild.bat
set DEV_VER=dev0
set PKG_VERSION=%REL_VER%.%DEV_VER%

set SCRIPTS_DIR=%cd%
cd ..\..

pip install . 

cd %SCRIPTS_DIR%

pause