FROM debian:buster

# sane defaults, but should be overridden in your docker build command to match your host-side user
ARG dkuser=gnr
ARG dkgroup=gnr
ARG dkuid=1000
ARG dkgid=1000

# make apt shut up about not having a tty
RUN echo "set debconf/frontend noninteractive" | DEBIAN_FRONTEND=noninteractive debconf-communicate

# system environment
RUN groupadd -g $dkgid $dkgroup || true &&\
    useradd -m -N -G dialout,audio,plugdev -g $dkgid -u $dkuid $dkuser &&\
    mkdir /etc/sudoers.d &&\
    echo "$dkuser ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/misc &&\
    chmod 755 /etc/sudoers.d &&\
    chmod 400 /etc/sudoers.d/misc
RUN apt-get update &&\
    apt-get install -y apt-utils &&\
    apt-get dist-upgrade -y &&\
    apt-get install -y sudo ca-certificates curl dialog git less pulseaudio vim-nox wget xterm fonts-dejavu python3-apt python3-pip python3-wheel python3-setuptools virtualenv build-essential &&\
    rm -rf /var/lib/apt/lists/*
RUN echo "daemon-binary = /bin/true" > /etc/pulse/client.conf &&\
    echo "enable-shm = false" >> /etc/pulse/client.conf &&\
    echo "autospawn = no" >> /etc/pulse/client.conf &&\
    echo "default-server = unix:/run/user/$dkuid/pulse/native" >> /etc/pulse/client.conf

# gnuradio dependencies
RUN apt-get update &&\
    apt-get install -y --no-install-recommends python3-yaml python3-ruamel.yaml python3-mako python3-gi-cairo gir1.2-gtk-3.0 python3-pyqt5 python3-pyqt5.qwt &&\
    rm -rf /var/lib/apt/lists/*

# user environment
USER $dkuser
WORKDIR /home/$dkuser
RUN sudo pip3 install git+https://github.com/gnuradio/pybombs.git
RUN pybombs auto-config
RUN pybombs recipes add-defaults
RUN sudo apt-get update &&\
    pybombs recipes update &&\
    echo "replacing gnuradio.lwr with gnuradio38.lwr - see https://github.com/gnuradio/pybombs/issues/542" &&\
    cp -afv ~/.pybombs/recipes/gr-recipes/gnuradio38.lwr ~/.pybombs/recipes/gr-recipes/gnuradio.lwr &&\
    pybombs prefix init ~/.gnuradio -a gnuradio -R gnuradio-default --virtualenv &&\
    echo "source ~/.gnuradio/setup_env.sh" >> ~/.bashrc &&\
    source ~/.gnuradio/setup_env.sh &&\
    pybombs install gr-osmosdr &&\
    pybombs install gr-correctiq &&\
    pybombs install inspectrum &&\
    find ${HOME}/.gnuradio/src -mindepth 2 -maxdepth 2 -type d -name build -exec rm -Rf '{}' + &&\
    sudo rm -rf /var/lib/apt/lists/*

# prepare for interactive image use
RUN echo "set debconf/frontend dialog" | sudo DEBIAN_FRONTEND=noninteractive debconf-communicate
CMD ["bash", "-i"]
