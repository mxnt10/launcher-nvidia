#!/bin/bash

install_root=${install_root:-""}

[ $install_root != "" ] && mkdir -p $install_root/usr/{bin,share/{applications,pixmaps,l-nvidia/tools},doc/l-nvidia} || mkdir -p /usr/{share/l-nvidia/tools,doc/l-nvidia}

install -Dm 0644 images/l-nvidia.png $install_root/usr/share/pixmaps
install -Dm 0644 images/l-nvidia.desktop $install_root/usr/share/applications
install -Dm 0644 src/*.py $install_root/usr/share/l-nvidia
install -Dm 0755 tools/* $install_root/usr/share/l-nvidia/tools

cp -a ChangeLog LICENSE README.md RELEASE $install_root/usr/doc/l-nvidia

echo "#!/bin/bash
cd /usr/share/l-nvidia
python3 l-nvidia.py" > $install_root/usr/bin/l-nvidia

chmod 755 $install_root/usr/bin/l-nvidia
