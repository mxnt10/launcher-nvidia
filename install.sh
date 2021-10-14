#!/bin/bash

pkgver=$(< RELEASE) 
install_root=${install_root:-""}

[ $install_root != "" ] && mkdir -p $install_root/usr/{bin,share/{applications,pixmaps,l-nvidia/utils,locale},doc/l-nvidia-$pkgver} || mkdir -p /usr/{share/l-nvidia/utils,doc/l-nvidia}

install -Dm 0644 appdata/l-nvidia.png $install_root/usr/share/pixmaps
install -Dm 0644 appdata/l-nvidia.desktop $install_root/usr/share/applications

install -Dm 0755 utils/* $install_root/usr/share/l-nvidia/utils

cp -a ChangeLog LICENSE README.md RELEASE $install_root/usr/doc/l-nvidia-$pkgver
cp -Tr src $install_root/usr/share/l-nvidia
cp -Tr locale $install_root/usr/share/locale

echo "#!/bin/bash
cd /usr/share/l-nvidia
python3 l-nvidia.py" > $install_root/usr/bin/l-nvidia

chmod 755 $install_root/usr/bin/l-nvidia
