@echo off

@call .\version.bat
set PKG_VERSION=%REL_VER%%ALPHA_VER%

set SCRIPTS_DIR=%cd%
cd ..\..

set PACK_NAME=".\dist\%MOD_NAME%-%PKG_VERSION%-py38-none-any.whl"

if exist %PACK_NAME% (
    python -m pip install --upgrade twine
    python -m twine upload --repository testpypi %PACK_NAME%
) else (
    echo Could not found %PACK_NAME%
)

cd %SCRIPTS_DIR%

pause
