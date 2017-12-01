FROM ubuntu:artful

ARG dkuser=gnr
ARG dkgroup=gnr
ARG dkuid=1000
ARG dkgid=1000

COPY files/sources.list /etc/apt/sources.list
COPY files/local.conf /etc/fonts/local.conf
COPY files/02nocache /etc/apt/apt.conf.d/02nocache
RUN groupadd -g $dkgid $dkgroup
RUN useradd  -m -N -G dialout,audio,plugdev -g $dkgid -u $dkuid $dkuser
RUN mkdir /etc/sudoers.d
RUN echo "$dkuser ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/misc
RUN chmod 755 /etc/sudoers.d
RUN chmod 400 /etc/sudoers.d/misc
RUN apt-get update &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends apt-utils &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends sudo ca-certificates python-apt python-pip python-setuptools python-wheel git pulseaudio xterm vim-nox

COPY files/client.conf /etc/pulse/client.conf
RUN echo "default-server = unix:/run/user/$dkuid/pulse/native" >> /etc/pulse/client.conf

RUN pip install git+https://github.com/gnuradio/pybombs.git

USER $dkuser
WORKDIR /home/$dkuser
RUN pybombs auto-config
RUN pybombs recipes add-defaults
RUN pybombs prefix init ~/.gnuradio-default -a gnuradio-default -R gnuradio-default
RUN pybombs install gr-osmosdr
RUN pybombs install gr-correctiq
RUN pybombs install inspectrum
RUN echo "source ~/.gnuradio-default/setup_env.sh" >> ~/.bashrc

CMD ["bash", "-i"]
