#FROM buildpack-deps:sid
FROM debian:sid

ENV DEBIAN_FRONTEND noninteractive

ARG dkuser=gnr
ARG dkgroup=gnr
ARG dkuid=1000
ARG dkgid=1000

COPY files/sources.list /etc/apt/sources.list
COPY files/local.conf /etc/fonts/local.conf
RUN groupadd -g $dkgid $dkgroup && useradd  -m -N -g $dkgid -u $dkuid $dkuser &&\
    apt-get update &&\
    apt-get install -y apt-utils &&\
    apt-get install -y ca-certificates gnuradio hackrf soapysdr-module-hackrf pulseaudio &&\
    apt-mark auto ca-certificates &&\
    apt-get clean

USER $dkuser
WORKDIR /home/$dkuser
CMD ["bash"]
