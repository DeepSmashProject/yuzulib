# 0. generate xorg.conf
#BUS_ID=$(nvidia-xconfig --query-gpu-info | grep 'PCI BusID' | sed -r 's/\s*PCI BusID : PCI:(.*)/\1/')
#nvidia-xconfig -a --virtual=$RESOLUTION --allow-empty-initial-configuration --enable-all-gpus --busid $BUS_ID

# 1. Run VNC Server
/usr/bin/vncserver -localhost no $DISPLAY -geometry 1280x800 -depth 24

# 2. Run noVNC Server
websockify -D --web=/usr/share/novnc/ 80 localhost:5901

/bin/bash