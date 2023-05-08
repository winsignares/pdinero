FROM alpine:3.10

RUN apk add --no-cache python3-dev \
&& pip3 install --upgrade pip 
RUN apk update && apk add --no-cache build-base openssl-dev libffi-dev
WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000
ENV PKG_CONFIG_PATH=/usr/lib/x86_64-linux-gnu/pkgconfig/
ENV MYSQL_DATABASE="adso"
ENV MYSQL_USER="root"
ENV MYSQL_PASSWORD="secret"
ENV MYSQL_HOST="adso_mysql"

ENTRYPOINT  ["python3"]

CMD ["/app/src/app.py"]

