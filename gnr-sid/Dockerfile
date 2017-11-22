FROM buildpack-deps:sid

ENV DEBIAN_FRONTEND noninteractive

ARG dkuser=gnr
ARG dkgroup=gnr
ARG dkuid=1000
ARG dkgid=1000

ADD sources.list /etc/apt/sources.list
ADD sources.list /etc/apt/sources.list
RUN groupadd -g $dkgid $dkgroup && useradd  -m -N -g $dkgid -u $dkuid $dkuser &&\
    apt-get update &&\
    apt-get install -y apt-utils &&\
    apt-get install -y gnuradio hackrf soapysdr-module-hackrf &&\
    apt-get clean

USER $dkuser
WORKDIR /home/$dkuser
CMD ["bash"]
