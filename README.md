# pi-cam
raspberry pi live feed camera using flask and redis

## Running the Service

- Clone this repo on your pi.
- You'll probably need these dependencies
  - `sudo apt-get install -y libffi-dev libssl-dev`
  - `sudo apt-get install -y python3 python3-pip`
  - `sudo apt-get remove python-configparser`
- Install docker and docker-compose on your pi.
  - Docker
    - `curl -fsSL https://get.docker.com -o get-docker.sh`
    - `sudo sh get-docker.sh`
  - docker-compose
    - `sudo pip3 -v install docker-compose`
- Run the setup script to make the picamera accessible by docker (must be `sudo`!!!)
  - `sudo ./setup.sh`
- Run the service!
  - `docker-compose up`
- This will start 3 services:
  - `redis`: this is used for in-memory video frame stream
  - `recorder`: this captures a continuous feed from the raspberry pi camera, and publishes frames to redis (keeps 1000 most recent frames on the redis stream)
  - `webserver`: this reads off of the redis video feed and sends continuous frames to your browser
  - anything else: you can hang any other services that you want off of the redis feed -- i.e. for image recognition, motion sensing, save the video off somewhere
- How to access the camera:
  - http://raspberrypi.local (or whatever your pi's IP/hostname is)
