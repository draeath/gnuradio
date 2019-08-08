FROM debian:buster

# sane defaults, but should be overridden in your docker build command to match your host-side user
ARG dkuser=gnr
ARG dkgroup=gnr
ARG dkuid=1000
ARG dkgid=1000

# system setup stuff
RUN groupadd -g $dkgid $dkgroup &&\
    useradd -m -N -G dialout,audio,plugdev -g $dkgid -u $dkuid $dkuser &&\
    mkdir /etc/sudoers.d &&\
    echo "$dkuser ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/misc &&\
    chmod 755 /etc/sudoers.d &&\
    chmod 400 /etc/sudoers.d/misc
RUN echo "set debconf/frontend noninteractive" | DEBIAN_FRONTEND=noninteractive debconf-communicate &&\
    apt-get update &&\
    apt-get dist-upgrade -y &&\
    apt-get install -y --no-install-recommends apt-utils &&\
    apt-get install -y --no-install-recommends sudo ca-certificates curl dialog git less pulseaudio vim-nox wget xterm libxml2 libxml2-dev &&\
    apt-get install -y --no-install-recommends python-apt python-pip python-setuptools python-wheel python-mako python-requests python-numpy python-six python-lxml &&\
    apt-get install -y --no-install-recommends python3-apt python3-pip python3-setuptools python3-wheel python3-mako python3-requests python3-numpy python3-six python3-lxml &&\
    echo "daemon-binary = /bin/true" > /etc/pulse/client.conf &&\
    echo "enable-shm = false" >> /etc/pulse/client.conf &&\
    echo "autospawn = no" >> /etc/pulse/client.conf &&\
    echo "default-server = unix:/run/user/$dkuid/pulse/native" >> /etc/pulse/client.conf &&\
    pip3 install git+https://github.com/gnuradio/pybombs.git &&\
    echo "set debconf/frontend dialog" | DEBIAN_FRONTEND=noninteractive debconf-communicate &&\
    rm -rf /var/lib/apt/lists/* &&\
    ldconfig

# user environment stuff
USER $dkuser
WORKDIR /home/$dkuser
RUN echo "set debconf/frontend noninteractive" | sudo DEBIAN_FRONTEND=noninteractive debconf-communicate &&\
    sudo apt-get update &&\
    pybombs auto-config &&\
    pybombs recipes add-defaults &&\
    pybombs prefix init ~/.gnuradio-default -a gnuradio-default -R gnuradio-default &&\
    echo "source ~/.gnuradio-default/setup_env.sh" >> ~/.bashrc &&\
    pybombs install gr-osmosdr &&\
    pybombs install gr-correctiq &&\
    pybombs install inspectrum &&\
    find ${HOME}/.gnuradio-default/src -mindepth 2 -maxdepth 2 -type d -name build -exec rm -Rf '{}' + &&\
    echo "set debconf/frontend dialog" | sudo DEBIAN_FRONTEND=noninteractive debconf-communicate &&\
    sudo rm -rf /var/lib/apt/lists/* &&\
    sudo ldconfig

# aaaand go! this container is interactive, contrary to the typical container pattern
CMD ["bash", "-i"]
