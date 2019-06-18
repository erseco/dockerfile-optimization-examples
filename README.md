# dockerfile-optimization-examples

----------------------------

docker run -it alpine:3.8 sh

ls -l /bin/sh

bash -> ash
apt -> apk
libc -> musl
vim -> vi

# Packages

https://pkgs.alpinelinux.org/packages

apk update

apk search curl

apk add curl

apk add tree

apk add git

git clone https://github.com/exolever/pyaccredible.git

## Build

- docker build -t erseco/whois:debian -f Dockerfile.debian .
- docker build -t erseco/whois:debianslim -f Dockerfile.debianslim .
- docker build -t erseco/whois:python -f Dockerfile.python .
- docker build -t erseco/whois:alpine -f Dockerfile.alpine .

docker images whois



Usa el --cache-from=container

docker pull erseco/

concatena los ENV y demás con \
