@echo off

source ./version.sh
export PKG_VERSION=$REL_VER$ALPHA_VER

export SCRIPTS_DIR=$(pwd)
cd ../..

set PACK_NAME="./dist/py_hidreport-$PKG_VERSION-py38-none-any.whl"

if [ -e $PACK_NAME ]; then
    python -m pip install --upgrade twine
    python -m twine upload $PACK_NAME
else
    echo Could not found $PACK_NAME
fi

cd $SCRIPTS_DIR
