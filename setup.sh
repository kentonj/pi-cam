#!/bin/bash

# make the camera rules file if it doesn't exist yet
if [ ! -f /etc/udev/rules.d/99-camera.rules ]; then
    touch /etc/udev/rules.d/99-camera.rules
fi

# allow other users (docker) to access the picamera
if [ ! grep -Fxq 'SUBSYSTEM=="vchiq",MODE="0666"' /etc/udev/rules.d/99-camera.rules]; then
    echo 'SUBSYSTEM=="vchiq",MODE="0666"' >> /etc/udev/rules.d/99-camera.rules
fi
