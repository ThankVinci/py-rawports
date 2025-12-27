#!/bin/sh

source ./version.sh

pip uninstall $MOD_NAME
pip cache remove $MOD_NAME