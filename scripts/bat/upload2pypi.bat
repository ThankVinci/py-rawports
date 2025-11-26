@echo off

@call .\version.bat
set PKG_VERSION=%REL_VER%%ALPHA_VER%
set PACK_NAME=".\dist\py_hidreport-%PKG_VERSION%-py38-none-any.whl"

if exist %PACK_NAME% (
    python -m pip install --upgrade twine
    python -m twine upload %PACK_NAME%
) else (
    echo Could not found %PACK_NAME%
)

pause
