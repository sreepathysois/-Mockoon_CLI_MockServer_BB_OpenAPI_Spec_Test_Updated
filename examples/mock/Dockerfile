FROM node:14-alpine

ARG version=latest

RUN npm install -g @mockoon/cli@$version

# Do not run as root.
RUN adduser --shell /bin/sh --disabled-password --gecos "" mockoon
USER mockoon


ENTRYPOINT ["mockoon-cli", "start", "--data data","--hostname", "0.0.0.0", "--daemon-off"]
