FROM resin/raspberry-pi-python:2.7

#RUN export UNAME=$(uname -a)

# Support for x86 via https://resin.io/blog/building-arm-containers-on-any-x86-machine-even-dockerhub/
#RUN [ "cross-build-start" ]

# Enable systemd
ENV INITSYSTEM on

# set working directory
ENV APPDIR /usr/src/app

RUN sudo mkdir -p ${APPDIR}
WORKDIR ${APPDIR}

# install raspian dependencies
RUN apt-get update
RUN apt-get install -t jessie python-smbus

# add requirements (to leverage Docker cache)
ADD ./Pipfile ${APPDIR}/Pipfile
ADD ./Pipfile.lock ${APPDIR}/Pipfile.lock

# install environment
RUN pip install pipenv
ENV PIPENV_TIMEOUT=600
RUN pipenv install

# add app
ADD . ${APPDIR}

# run server
# enable i2c support https://docs.resin.io/hardware/i2c-and-spi/#i2c
CMD modprobe i2c-dev
CMD pipenv run python manage.py runserver -h 0.0.0.0

#RUN [ "cross-build-end" ]