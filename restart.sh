#!/usr/bin/env bash
docker pull joeboyscout/piclockapi:latest
docker stop piclockapi
sleep 10
docker rm piclockapi
docker run --privileged --name piclockapi -d -p 5000:80 joeboyscout/piclockapi:latest