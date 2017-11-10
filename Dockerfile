FROM resin/raspberry-pi-python:latest

# Support for x86 via https://resin.io/blog/building-arm-containers-on-any-x86-machine-even-dockerhub/
#RUN [ "cross-build-start" ]

# Enable systemd
ENV INITSYSTEM on

# set working directory
ENV APPDIR /usr/src/app
RUN sudo mkdir -p ${APPDIR}
WORKDIR ${APPDIR}

# install raspian dependencies
#RUN apt-get update
#RUN sudo apt-get upgrade
#RUN apt-get install python-pip
RUN apt-get install python-smbus

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
CMD pipenv run python manage.py runserver -h 0.0.0.0

#RUN [ "cross-build-end" ]
