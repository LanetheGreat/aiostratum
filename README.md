## Description:
This is a reimplementation of the Stratum protocol for use with server and client side
asynchronous networking and Python's asyncio library.

Homepage: http://stratum.bitcoin.cz

## Contact to current maintainer:
Email lshaw.tech at gmail.com  
Nickname LanetheGreat at bitcointalk.org forum.

## Contact to original developer:
Email info at bitcoin.cz  
Nickname slush at bitcointalk.org forum.

## Installation
Requirements:
* python 3.6+
* OS Independent (should work on *nix/Windows/Mac OSX)

### Following instructions will work on Ubuntu & Debian*:
1. ) For developers, using git:
  * git clone git://github.com/LanetheGreat/aiostratum.git
  * sudo python setup.py develop
2. ) From package, permanent install for production use:
  * sudo apt-get install python-dev
  * sudo apt-get install python-setuptools
  * sudo python setup.py install

Note: If Debian doesn't have a 'sudo' command, please do the installation process as a root user.

## Configuration
1. ) Basic configuration:
  * Copy settings.py to config.py
  * (Remove everything from line 155 and below)
  * Edit at least these values: HOSTNAME, BITCOIN_TRUSTED_*
2. ) Message signatures (for enabling message signatures):
  * Generate server's ECDSA key by: `python signature.py > signing_key.pem`
  * Fill correct values to `SIGNING_KEY` and `SIGNING_ID` (config.py).
3. ) Creating keys for SSL-based transports:
  * For all SSL-based transports (HTTPS, WSS, ...) you'll need private key and certificate file. You can use certificates from any authority or you can generate self-signed certificates, which is helpful at least for testing.
  * Following script will generate self-signed SSL certificate:
```bash
#!/bin/bash
openssl genrsa -des3 -out server.key 1024
openssl req -new -key server.key -out server.csr
cp server.key server.key.org
openssl rsa -in server.key.org -out server.key
openssl x509 -req -in server.csr -signkey server.key -out server.crt
```
  * Then you have to fill `SSL_PRIVKEY` and `SSL_CACERT` in config.py file with values 'server.key' and 'server.crt'.

## Startup
* Start devel server:
  * `twistd -ny launcher.tac`
* Devel server *without* lowlevel messages of Twisted:
  * `twistd -ny launcher.tac -l log/twistd.log`
 
## Running in production
* TODO: Guide for running twistd as a daemon, init scripts
* TODO: Loadbalancing and port redirecting using haproxy
* TODO: Tunelling on 80/443 using stunnel
  * (Any volunteer(s) for these ^ ?)