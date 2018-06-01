fail () {
   echo "Failed."
   exit 255
}

if [ ! $1 ]; then
   echo "You need to pass a valid version"
   exit 255
fi
VERSION=$1

echo "Downloading AppleNetInstall-$VERSION...\n"
curl -O https://ani.apple.com/Downloads/AppleNetInstall-$VERSION.dmg || fail

echo "\nMounting disk image...\n"
hdiutil attach AppleNetInstall-$VERSION.dmg || fail

echo "Terminating any running copies of Apple Net Install...\n"
pkill -9 -f Apple\ Net\ Install
launchctl remove com.apple.bni.applenetinstalld

echo "Copying into place...\n"
sudo rm -rf /AppleInternal/Applications/Apple\ Net\ Install.app
sudo ditto /Volumes/AppleNetInstall/Apple\ Net\ Install.app /AppleInternal/Applications/Apple\ Net\ Install.app || fail
sudo chown -R $USER:admin /AppleInternal/Applications/Apple\ Net\ Install.app

echo "Launching Apple Net Install\n"
open /AppleInternal/Applications/Apple\ Net\ Install.app

