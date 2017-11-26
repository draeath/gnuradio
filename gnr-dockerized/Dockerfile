FROM buildpack-deps:stretch

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
    DEBIAN_FRONTEND=noninteractive apt-get install -y apt-utils &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y reportbug sudo ca-certificates pulseaudio hackrf libhackrf0 libhackrf-dev soapysdr-module-hackrf python-apt python-dev python-setuptools &&\
    DEBIAN_FRONTEND=noninteractive apt-get build-dep -y gnuradio &&\
    apt-get clean

COPY files/client.conf /etc/pulse/client.conf
RUN echo "default-server = unix:/run/user/$dkuid/pulse/native" >> /etc/pulse/client.conf

ADD files/pybombs /root/pybombs
WORKDIR /root/pybombs
RUN apt-get update &&\
    python setup.py install &&\
    apt-get clean

USER $dkuser
WORKDIR /home/$dkuser
RUN pybombs auto-config
RUN pybombs recipes add-defaults
RUN pybombs prefix init ~/.gnuradio-default -a gnuradio-default -R gnuradio-default
RUN echo "source ~/.gnuradio-default/setup_env.sh" >> ~/.bashrc

CMD ["bash", "-i"]
