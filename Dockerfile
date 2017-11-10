FROM python:2.7.14

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements (to leverage Docker cache)
ADD ./Pipfile /usr/src/app/Pipfile
ADD ./Pipfile.lock /usr/src/app/Pipfile.lock

# install environment
RUN pip install pipenv
ENV PIPENV_TIMEOUT=600
RUN pipenv install

# add app
ADD . /usr/src/app

# run server
CMD pipenv run python manage.py runserver -h 0.0.0.0
