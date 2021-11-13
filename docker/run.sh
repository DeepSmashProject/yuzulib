docker run --privileged -it --rm --gpus all \
  -p 8081:8081 \
  -e RESOLUTION=1280x800 \
  -e VNCPASS=pass \
  -v "/Users/ruihirano/MyProjects/DeepSmashProject/:/workspace" \
  -v "/Users/ruihirano/MyProjects/DeepSmashProject/data/keys:/root/.local/share/yuzu/keys" \
  --name yuzu_emu yuzu_emu