* You need docker, obviously. Go fetch.
* Edit [build.sh](build.sh) and supply your username/groupname. Also, if your UID/GID isn't 1000, specify those as well (`dkuid` and `dkgid` respectively)
* Run `build.sh` from alongside the `Dockerfile`. When all is said and done, you should have a nice and shiny image tagged `gnr-sid` - assuming the current dockerhub `debian:sid` image isn't broken.
* Run the container! You'll need some arguments to support X11 clients on your host X11, use the following as guidance. Note the username/uid in the volumes argument, this should match what you put in `build.sh`.

```
docker run -it --net=host -e DISPLAY \
-v $HOME/.Xauthority:/home/draeath/.Xauthority \
gnr-sid
```

**CAUTION**: If you use `--net=host` (as you must, to allow X11 to work container-to-host) the hostname inside the container will match the host. Be aware of this.
