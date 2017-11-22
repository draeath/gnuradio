FROM buildpack-deps:sid

ARG user=gnr
ARG group=gnr
ARG uid=1000
ARG gid=1000

RUN groupadd -g $gid $group && useradd  -m -N -g $gid -u $uid $user
ADD pybombs /home/$user/pybombs

USER $user
WORKDIR /home/$user
CMD ["bash"]
