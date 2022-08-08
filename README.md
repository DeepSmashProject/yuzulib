# yuzulib

# Getting Started

## Run Yuzu on docker
```
$ cd docker
$ bash build.sh
$ bash run.sh -g /home/user/games -k /home/user/keys -v /home/user/workspace
(docker) $ /yuzu/build/bin/yuzu
```
You can screen at https://localhost:8081/vnc.html
Password is [pass]

## Run Controller
```
$ docker exec -it yuzu_emu bash
(docker) $ cd yuzulib && pip install -e yuzulib
(docker) $ cd libultimate && pip install -e libultimate
(docker) $ cd libultimate/examples
(docker) $ python3 develop.py
```
