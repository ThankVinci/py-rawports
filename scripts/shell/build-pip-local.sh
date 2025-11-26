#!/bin/sh

source ./prebuild.sh
export PKG_VERSION=$REL_VER$ALPHA_VER

export SCRIPTS_DIR=$(pwd)
cd ../..

python -m pip install --upgrade pip build setuptools wheel
python -m build --wheel --no-isolation

cd $SCRIPTS_DIR