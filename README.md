# yuzulib

# Getting Started

## Run Yuzu
```
$ cd docker
$ bash build.sh
$ bash run.sh
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