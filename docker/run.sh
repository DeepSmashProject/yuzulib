docker run --privileged -it --rm --gpus all \
  -p 8081:8081 \
  -e RESOLUTION=1280x800 \
  -e VNCPASS=pass \
  -e DISPLAY=:1 \
  -e BUS_ID=13:0:0 \
  -e NOVNC_PORT=8081 \
  -v "/home/ruirui_nis/workspace/DeepSmashProject:/workspace" \
  -v "/mnt/bigdata/00_students/ruirui_nis/DeepSmashProject/games:/workspace/games" \
  -v "/mnt/bigdata/00_students/ruirui_nis/DeepSmashProject/keys:/root/.local/share/yuzu/keys" \
  --name yuzu_emu deepsmash/yuzu_emu