@call .\version.bat

pip uninstall %MOD_NAME%
pause
pip cache remove %MOD_NAME%
pause