* You need docker, obviously. Go fetch.
* Edit [build.sh](build.sh) and supply your username/groupname. Also, if your UID/GID isn't 1000, specify those as well (`dkuid` and `dkgid` respectively)
* Run `build.sh` from alongside the `Dockerfile`. When all is said and done, you should have a nice and shiny image tagged `gnr-sid` - assuming the current dockerhub `debian:sid` image isn't broken.
* Run the container! You'll need some arguments to support X11 clients on your host X11, use the following as guidance. Note the username/uid in th volumes arguments, this should match what you put in `build.sh`. Note this assumes you use pulseaudio. If you don't... well, you're on your own!

```
docker run -it --net=host -e DISPLAY \
-v $HOME/.Xauthority:/home/draeath/.Xauthority \
-v $XDG_RUNTIME_DIR/pulse:/run/user/1000/pulse \
gnr-sid
```
