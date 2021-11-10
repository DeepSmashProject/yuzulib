# sudo apt install -y tigervnc-standalone-server tigervnc-scraping-server tigervnc-common tigervnc-xorg-extension
/usr/bin/vncserver -localhost no $DISPLAY -geometry 1280x800 -depth 24
websockify -D --web=/usr/share/novnc/ 80 localhost:5901
/bin/bash