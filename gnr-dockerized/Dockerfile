FROM ubuntu:artful

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
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends apt-utils &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends sudo ca-certificates python-apt python-pip python-setuptools python-wheel git pulseaudio hackrf libhackrf0 libhackrf-dev soapysdr-module-hackrf inspectrum &&\
    apt-get clean

COPY files/client.conf /etc/pulse/client.conf
RUN echo "default-server = unix:/run/user/$dkuid/pulse/native" >> /etc/pulse/client.conf

RUN pip install git+https://github.com/gnuradio/pybombs.git

USER $dkuser
WORKDIR /home/$dkuser
RUN pybombs auto-config &&\
    pybombs recipes add-defaults &&\
    pybombs prefix init ~/.gnuradio-default -a gnuradio-default -R gnuradio-default &&\
    echo "source ~/.gnuradio-default/setup_env.sh" >> ~/.bashrc &&\
    apt-get clean

CMD ["bash", "-i"]
