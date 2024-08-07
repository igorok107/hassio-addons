ARG BUILD_FROM
FROM $BUILD_FROM

WORKDIR /app

# Define environment variables
# Use this variable when creating a container to specify the MQTT broker host.
ENV MQTT_HOST="homeassistant" \
    MQTT_PORT=1883 \
    MQTT_USERNAME="mqtt_user" \
    MQTT_PASSWORD="mqtt_pass"

LABEL Maintainer="Igorok107" \
Description="This image publishes MQTT topic via HTTP request on local server."

# Copy Python requirements file
COPY requeiment.txt /tmp/

RUN apk add --no-cache \
	curl=8.5.0-r0 \
	python3=3.10.14-r1 \
	py3-pip=22.1.1-r0 \
    && pip3 install --no-cache-dir -r /tmp/requeiment.txt \
    && rm -f -r /tmp/* \
    && find /usr \( -type d -a -name test -o -name tests -o -name '__pycache__' \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' +

COPY rootfs/ /
RUN chmod +x /app/run.sh

HEALTHCHECK CMD curl --fail http://localhost:2883/health || exit 1 

ENTRYPOINT ["bashio", "/app/run.sh"]
