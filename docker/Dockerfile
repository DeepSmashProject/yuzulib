FROM nvidia/cudagl:11.4.2-runtime-ubuntu20.04

ENV DEBIAN_FRONTEND noninteractive
ENV USER root

# (1) Install Xorg and NVIDIA driver inside the container
# Almost same procesure as nvidia/driver https://gitlab.com/nvidia/driver/blob/master/ubuntu16.04/Dockerfile

# (1-1) Install prerequisites
RUN dpkg --add-architecture i386 && \
    apt-get update && apt-get install -y --no-install-recommends \
    apt-utils \
    build-essential \
    ca-certificates \
    curl \
    wget \
    vim \
    zip \
    unzip \
    git \
    python \
    kmod \
    libc6:i386 \
    pkg-config \
    libelf-dev


# (1-2) Install xorg server and xinit BEFORE INSTALLING NVIDIA DRIVER.
# After this installation, command Xorg and xinit can be used in the container
# if you need full ubuntu desktop environment, the line below should be added.
# ubuntu-desktop \
RUN apt-get install -y xinit

# (1-3) Install NVIDIA drivers, including X graphic drivers
# Same command as nvidia/driver, except --x-{prefix,module-path,library-path,sysconfig-path} are omitted in order to make use default path and enable X drivers.
# Driver version must be equal to host's driver
# Install the userspace components and copy the kernel module sources.
ENV DRIVER_VERSION=460.91.03
ENV DRIVER_VERSION_PATH=460.91.03
RUN cd /tmp && \
    curl -fSsl -O https://us.download.nvidia.com/tesla/$DRIVER_VERSION_PATH/NVIDIA-Linux-x86_64-$DRIVER_VERSION.run && \
    sh NVIDIA-Linux-x86_64-$DRIVER_VERSION.run -x && \
    cd NVIDIA-Linux-x86_64-$DRIVER_VERSION && \
    ./nvidia-installer --silent \
    --no-kernel-module \
    --install-compat32-libs \
    --no-nouveau-check \
    --no-nvidia-modprobe \
    --no-rpms \
    --no-backup \
    --no-check-for-alternate-installs \
    --no-libglx-indirect \
    --no-install-libglvnd && \
    mkdir -p /usr/src/nvidia-$DRIVER_VERSION && \
    mv LICENSE mkprecompiled kernel /usr/src/nvidia-$DRIVER_VERSION && \
    sed '9,${/^\(kernel\|LICENSE\)/!d}' .manifest > /usr/src/nvidia-$DRIVER_VERSION/.manifest

# (2) Configurate Xorg
# (2-1) Install some necessary softwares
#
# pkg-config: nvidia-xconfig requires this package
# mesa-utils: This package includes glxgears and glxinfo, which is useful for testing GLX drivers
# x11vnc: Make connection between x11 server and VNC client.
# x11-apps: xeyes can be used to make sure that X11 server is running.
#
# Note: x11vnc in ubuntu18.04 is useless beacuse of stack smashing bug. See below to manual compilation.
RUN apt-get install -y --no-install-recommends \
    mesa-utils \
    x11-apps

# solution for the `stack smashing detected` issue
# https://github.com/LibVNC/x11vnc/issues/61
RUN apt-get install -y --no-install-recommends \
    automake autoconf libssl-dev xorg-dev libvncserver-dev && \
    rm -rf /var/lib/apt/lists/* && \
    git clone https://github.com/LibVNC/x11vnc.git && \
    cd x11vnc && \
    ./autogen.sh && \
    make && \
    cp src/x11vnc /usr/bin/x11vnc

# novnc
# download websockify as well
RUN wget https://github.com/novnc/noVNC/archive/v1.1.0.zip && \
    unzip -q v1.1.0.zip && \
    rm -rf v1.1.0.zip && \
    git clone https://github.com/novnc/websockify /noVNC-1.1.0/utils/websockify

# Xorg segfault error
# dbus-core: error connecting to system bus: org.freedesktop.DBus.Error.FileNotFound (Failed to connect to socket /var/run/dbus/system_bus_socket: No such file or directory)
# related? https://github.com/Microsoft/WSL/issues/2016
RUN apt-get install -y --no-install-recommends \
    dbus-x11
#libdbus-c++-1-0v5

#ENV DISPLAY=:1

######### Install and Build yuzu #############\
RUN apt update && apt install -y sudo && \
    sudo apt install -y --no-install-recommends libpulse-dev autoconf \
    cmake g++-10 gcc-10 git glslang-tools libasound2 libboost-context-dev \
    libglu1-mesa-dev libhidapi-dev libtool libudev-dev libxcb-icccm4 libxcb-image0 \
    libxcb-keysyms1 libxcb-render-util0 libxcb-xinerama0 libxcb-xkb1 libxext-dev \
    libxkbcommon-x11-0 mesa-common-dev nasm ninja-build python3 python3-pip qtbase5-dev \
    qtbase5-private-dev qtwebengine5-dev libmbedtls-dev make automake

RUN git clone https://github.com/conan-io/conan.git conan_src 
RUN cd conan_src && pip install -e .

RUN sudo apt install -y ca-certificates
RUN git clone --recursive https://github.com/yuzu-emu/yuzu

RUN mkdir /yuzu/build
WORKDIR /yuzu/build
RUN cmake .. -GNinja -DCMAKE_C_COMPILER=gcc-10 -DCMAKE_CXX_COMPILER=g++-10
ENV LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64
RUN ninja

############# for NVIDIA ##################
ENV NVIDIA_VISIBLE_DEVICES ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

############ for Application ############
# for pyautogui
RUN apt -y install python3-tk python3-dev scrot vim
#RUN apt install -y --no-install-recommends ubuntu-desktop && \
#    apt install -y gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal
WORKDIR /workspace/yuzulib
COPY . .
#RUN git clone https://github.com/DeepSmashProject/yuzulib.git
RUN pip install -e .

COPY ./docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD /entrypoint.sh
# docker build -t yuzu_emu:latest . 
# docker run -it --rm --name yuzu_emu -p 5901:5901 -p 6080:80 -v $PWD:/workspace yuzu_emu:latest
# docker exec -it yuzu_emu bash