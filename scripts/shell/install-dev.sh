#!/bin/sh

source ./prebuild.sh
export DEV_VER=dev0
export PKG_VERSION=$REL_VER.$DEV_VER

export SCRIPTS_DIR=$(pwd)
cd ../..

pip install . 

cd $SCRIPTS_DIR