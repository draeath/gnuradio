FROM ubuntu:artful

# sane defaults, but should be overridden in your docker build command to match your host-side user
ARG dkuser=gnr
ARG dkgroup=gnr
ARG dkuid=1000
ARG dkgid=1000

# system setup stuff
RUN echo "deb http://archive.ubuntu.com/ubuntu/ artful main restricted universe multiverse" > /etc/apt/sources.list &&\
    echo "deb http://archive.ubuntu.com/ubuntu/ artful-updates main restricted universe multiverse" >> /etc/apt/sources.list &&\
    echo "deb http://archive.ubuntu.com/ubuntu/ artful-security main restricted universe multiverse" >> /etc/apt/sources.list
RUN groupadd -g $dkgid $dkgroup &&\
    useradd -m -N -G dialout,audio,plugdev -g $dkgid -u $dkuid $dkuser &&\
    mkdir /etc/sudoers.d &&\
    echo "$dkuser ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/misc &&\
    chmod 755 /etc/sudoers.d &&\
    chmod 400 /etc/sudoers.d/misc
RUN apt-get update &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends apt-utils &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends sudo ca-certificates python-apt python-pip python-setuptools python-wheel git pulseaudio xterm vim-nox &&\
    echo "daemon-binary = /bin/true" > /etc/pulse/client.conf &&\
    echo "enable-shm = false" >> /etc/pulse/client.conf &&\
    echo "autospawn = no" >> /etc/pulse/client.conf &&\
    echo "default-server = unix:/run/user/$dkuid/pulse/native" >> /etc/pulse/client.conf &&\
    pip install git+https://github.com/gnuradio/pybombs.git

# user environment stuff
USER $dkuser
WORKDIR /home/$dkuser
RUN pybombs auto-config &&\
    pybombs recipes add-defaults &&\
    pybombs prefix init ~/.gnuradio-default -a gnuradio-default -R gnuradio-default &&\
    echo "source ~/.gnuradio-default/setup_env.sh" >> ~/.bashrc &&\
    pybombs install gr-osmosdr &&\
    pybombs install gr-correctiq &&\
    pybombs install inspectrum &&\
    find ${HOME}/.gnuradio-default/src -mindepth 2 -maxdepth 2 -type d -name build -exec rm -Rf '{}' + &&\
    sudo ldconfig

# aaaand go! this container is interactive, contrary to the typical container pattern
CMD ["bash", "-i"]
