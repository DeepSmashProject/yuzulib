FROM nvidia/cudagl:11.4.2-runtime-ubuntu20.04

ENV DEBIAN_FRONTEND noninteractive
ENV USER root

########## Install for XServer ##############
# DISPLAY number is :1
# if change password, Run $ vncpasswd, default is password

RUN apt update && \
    apt install -y --no-install-recommends ubuntu-desktop && \
    apt install -y gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal && \
    apt install -y tigervnc-standalone-server tigervnc-common novnc websockify && \
    mkdir /root/.vnc

ADD xstartup /root/.vnc/xstartup
ADD passwd /root/.vnc/passwd

RUN chmod 600 /root/.vnc/passwd
RUN chmod u+x /root/.vnc/xstartup

ENV DISPLAY=:1
EXPOSE 5901

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
RUN sudo apt -y install python3-tk python3-dev scrot vim
WORKDIR /workspace
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD /entrypoint.sh
# docker build -t yuzu_emu:latest . 
# docker run -it --rm --name yuzu_emu -p 5901:5901 -p 6080:80 -v $PWD:/workspace yuzu_emu:latest
# docker exec -it yuzu_emu bash