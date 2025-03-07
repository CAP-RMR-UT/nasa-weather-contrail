# syntax=docker/dockerfile:1

# Use the official slim Python 3.12 image
FROM python:alpine

ARG VERSION
ARG REVISION

# Label the image with values that will not change often
# https://github.com/opencontainers/image-spec/blob/main/annotations.md
LABEL org.opencontainers.image.title="cap-nasa-weather"
LABEL org.opencontainers.image.description="Data conversion and validation of tabular data files to JSON for upload to WMIRS"
LABEL org.opencontainers.image.url="https://github.com/CAP-RMR-UT/cap-nasa-weather"
LABEL org.opencontainers.image.documentation="https://github.com/CAP-RMR-UT/nasa-weather-contrail.git/apps/wmirsdata"
LABEL org.opencontainers.image.source="https://github.com/CAP-RMR-UT/nasa-weather-contrail.git/apps/wmirsdata"

RUN <<EOF
    apk add curl
    wget -q -O - https://taskfile.dev/install.sh | sh
EOF

# Build and install the application
LABEL org.opencontainers.image.version=${VERSION}
LABEL org.opencontainers.image.revision=${REVISION}
COPY . /src/wmirsdata/
WORKDIR /src/wmirsdata
RUN task install


# Set the working directory
WORKDIR /var/lib/wmirsdata
ENTRYPOINT [
    "/usr/local/bin/wmirsdata",
    "spool",
    "--input=var/lib/wmirsdata/in",
    "--output=var/lib/wmirsdata/out",
    "--error=var/lib/wmirsdata/err"
]
