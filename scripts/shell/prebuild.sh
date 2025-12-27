source ./version.sh

if [ -e "./build/bdist.macosx-15.0-arm64" ]; then
    rm -rf "./build/bdist.macosx-15.0-arm64"
fi

if [ -e "./build/bdist.linux-x86_64" ]; then
    rm -rf "./build/bdist.linux-x86_64"
fi

if [ -e "./build/lib" ]; then
    rm -rf "./build/lib"
fi