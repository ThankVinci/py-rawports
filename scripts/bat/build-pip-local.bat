@echo off

@call .\prebuild.bat
set PKG_VERSION=%REL_VER%%ALPHA_VER%

set SCRIPTS_DIR=%cd%
cd ..\..

python -m pip install --upgrade pip build setuptools wheel
python -m build --wheel --no-isolation

cd %SCRIPTS_DIR%

pause