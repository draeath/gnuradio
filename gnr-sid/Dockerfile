FROM buildpack-deps:stretch

ENV DEBIAN_FRONTEND noninteractive

ARG dkuser=gnr
ARG dkgroup=gnr
ARG dkuid=1000
ARG dkgid=1000

COPY files/sources.list /etc/apt/sources.list
COPY files/local.conf /etc/fonts/local.conf
RUN groupadd -g $dkgid $dkgroup &&\
    useradd  -m -N -G dialout,audio,plugdev -g $dkgid -u $dkuid $dkuser &&\
    mkdir /etc/sudoers.d &&\
    echo "$dkuser ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/misc &&\
    chmod 755 /etc/sudoers.d &&\
    chmod 400 /etc/sudoers.d/misc
RUN apt-get update &&\
    apt-get install -y apt-utils &&\
    apt-get install -y reportbug sudo build-essential ca-certificates pulseaudio pavucontrol hackrf libhackrf0 libhackrf-dev soapysdr-module-hackrf python-dev python-setuptools &&\
    apt-mark auto ca-certificates &&\
    apt-get clean

COPY files/client.conf /etc/pulse/client.conf
RUN echo "default-server = unix:/run/user/$dkuid/pulse/native" >> /etc/pulse/client.conf

ADD files/pybombs /root/pybombs
WORKDIR /root/pybombs
RUN python setup.py install

USER $dkuser
WORKDIR /home/$dkuser
CMD ["bash"]
