* You need docker, obviously. Go fetch.
* Review [build.sh](build.sh) and override the user/uid/group/gid arguments if necessary. Out-of-the-box it'll use those of whoever kicks off the build script.
* Run 'build.sh' from alongside the Dockerfile. When all is said and done, you should have a nice and shiny image tagged 'gnr.'
* Run the container! For X11 to work, you *must* use host networking, export DISPLAY, and mount your '.Xauthority' file. For sound to work, you also need to mount your `${XDG_RUNTIME_DIR}/pulse` directory (If you don't use pulseaudio on your host... well, you're on your own.)

Suggested execution:
```
docker run -it --rm --net=host -e DISPLAY \
--user "$(id -u):$(id -g)" \
-v "${HOME}/.Xauthority:/home/$(id -un)/.Xauthority" \
-v "${XDG_RUNTIME_DIR}/pulse:/run/user/$(id -u)/pulse" \
gnr
```

Please note above the id subshells. If you didn't build the image with the same user/uid/group/gid as you are running the container as, take care that these map up correctly (`-v {HOSTSIDE}:{CONTAINERSIDE}`) and note you should tell docker to run the container as yourself, else the '.Xauthority' and pulse rundir will mount inside the container as root, breaking stuff.

**CAUTION**: If you use `--net=host` (as you must, to allow X11 to work container-to-host) the hostname inside the container will match the host. Be aware of this. Your prompt will (probably) look similar, if not identical, to the prompt on your host system.
