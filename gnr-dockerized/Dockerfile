FROM ubuntu:rolling

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
RUN echo "set debconf/frontend Noninteractive" | debconf-communicate &&\
    apt-get update &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends apt-utils &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends sudo ca-certificates curl dialog git less pulseaudio python-apt python-pip python-setuptools python-wheel vim-nox wget xterm &&\
    echo "daemon-binary = /bin/true" > /etc/pulse/client.conf &&\
    echo "enable-shm = false" >> /etc/pulse/client.conf &&\
    echo "autospawn = no" >> /etc/pulse/client.conf &&\
    echo "default-server = unix:/run/user/$dkuid/pulse/native" >> /etc/pulse/client.conf &&\
    pip install git+https://github.com/gnuradio/pybombs.git &&\
    echo "set debconf/frontend Dialog" | debconf-communicate &&\
    rm -rf /var/lib/apt/lists/* &&\
    ldconfig

# user environment stuff
USER $dkuser
WORKDIR /home/$dkuser
RUN echo "set debconf/frontend Noninteractive" | sudo debconf-communicate &&\
    pybombs auto-config &&\
    pybombs recipes add-defaults &&\
    pybombs prefix init ~/.gnuradio-default -a gnuradio-default -R gnuradio-default &&\
    echo "source ~/.gnuradio-default/setup_env.sh" >> ~/.bashrc &&\
    pybombs install gr-osmosdr &&\
    pybombs install gr-correctiq &&\
    pybombs install inspectrum &&\
    find ${HOME}/.gnuradio-default/src -mindepth 2 -maxdepth 2 -type d -name build -exec rm -Rf '{}' + &&\
    echo "set debconf/frontend Dialog" | sudo debconf-communicate &&\
    sudo rm -rf /var/lib/apt/lists/* &&\
    sudo ldconfig

# aaaand go! this container is interactive, contrary to the typical container pattern
CMD ["bash", "-i"]
