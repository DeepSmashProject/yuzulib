docker run --privileged -it --rm --gpus all \
  -p 8081:8081 \
  -e RESOLUTION=1280x800 \
  -e VNCPASS=pass \
  -e BUS_ID=13:0:0 \
  -e NOVNC_PORT=8081 \
  -v "/Users/ruihirano/MyProjects/DeepSmashProject/:/workspace" \
  -v "/Users/ruihirano/MyProjects/DeepSmashProject/data/keys:/root/.local/share/yuzu/keys" \
  --name yuzu_emu yuzu_emu