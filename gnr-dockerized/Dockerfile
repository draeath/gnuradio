FROM debian:buster

# sane defaults, but should be overridden in your docker build command to match your host-side user
ARG dkuser=gnr
ARG dkgroup=gnr
ARG dkuid=1000
ARG dkgid=1000

# system setup stuff
RUN groupadd -g $dkgid $dkgroup || true &&\
    useradd -m -N -G dialout,audio,plugdev -g $dkgid -u $dkuid $dkuser &&\
    mkdir /etc/sudoers.d &&\
    echo "$dkuser ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/misc &&\
    chmod 755 /etc/sudoers.d &&\
    chmod 400 /etc/sudoers.d/misc
RUN echo "set debconf/frontend noninteractive" | DEBIAN_FRONTEND=noninteractive debconf-communicate
RUN apt-get update &&\
    apt-get install -y --no-install-recommends apt-utils &&\
    apt-get dist-upgrade -y &&\
    apt-get install -y --no-install-recommends sudo ca-certificates curl dialog git less pulseaudio vim-nox wget xterm \
        fonts-dejavu python3-apt python3-pip python3-wheel python3-setuptools python3-ruamel.yaml virtualenv \
        python3-mako python3-gi-cairo python3-yaml gir1.2-gtk-3.0 &&\
    rm -rf /var/lib/apt/lists/*
RUN echo "daemon-binary = /bin/true" > /etc/pulse/client.conf &&\
    echo "enable-shm = false" >> /etc/pulse/client.conf &&\
    echo "autospawn = no" >> /etc/pulse/client.conf &&\
    echo "default-server = unix:/run/user/$dkuid/pulse/native" >> /etc/pulse/client.conf
RUN echo "set debconf/frontend dialog" | DEBIAN_FRONTEND=noninteractive debconf-communicate

# user environment stuff
USER $dkuser
WORKDIR /home/$dkuser
RUN echo "set debconf/frontend noninteractive" | sudo DEBIAN_FRONTEND=noninteractive debconf-communicate
RUN sudo pip3 install git+https://github.com/gnuradio/pybombs.git
RUN pybombs auto-config
RUN pybombs recipes add-defaults
RUN sudo apt-get update &&\
    pybombs recipes update &&\
    echo "replacing gnuradio.lwr with gnuradio38.lwr - see https://github.com/gnuradio/pybombs/issues/542" &&\
    cp -afv ~/.pybombs/recipes/gr-recipes/gnuradio38.lwr ~/.pybombs/recipes/gr-recipes/gnuradio.lwr &&\
    pybombs prefix init ~/.gnuradio -a gnuradio -R gnuradio-default --virtualenv &&\
    echo "source ~/.gnuradio/setup_env.sh" >> ~/.bashrc &&\
    sudo rm -rf /var/lib/apt/lists/*
RUN sudo apt-get update &&\
    pybombs recipes update &&\
    pybombs install gnuradio38 &&\
    pybombs install gr-osmosdr &&\
    pybombs install gr-correctiq &&\
    pybombs install inspectrum &&\
    find ${HOME}/.gnuradio/src -mindepth 2 -maxdepth 2 -type d -name build -exec rm -Rf '{}' + &&\
    sudo rm -rf /var/lib/apt/lists/*
RUN echo "set debconf/frontend dialog" | sudo DEBIAN_FRONTEND=noninteractive debconf-communicate

CMD ["bash", "-i"]
