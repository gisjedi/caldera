FROM python:2.7-slim

RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    libpq-dev \
    binutils \
    libproj-dev \
    gdal-bin

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

ENV CALDERA_DB_SERVER postgis

RUN echo $CALDERA_DB_SERVER:5432:*:postgres:postgres > ~/.pgpass
RUN chmod 0600 ~/.pgpass

COPY . /opt/caldera/

# Execute the 'erupt' command on container start with 1000 features being generated every 30 seconds
WORKDIR /opt/caldera
CMD ["sh", "docker/caldera/init-app.sh"]
