FROM python:3.8-buster

LABEL "com.github.actions.name" = "CI Setup"
LABEL "com.github.actions.description" = "Sets up the environment to run the CI"
LABEL "com.github.actions.icon" = "chevron-right"
LABEL "com.github.actions.color" = "green"

RUN mkdir /workdir
WORKDIR /workdir

LABEL "repository" = "https://github.com/vergi40/ChessArena"
LABEL "homepage" = "https://github.com/vergi40/ChessArena"

# Add pip
USER root
RUN \
	apt-get update && \
	pip install -U pip && \
    rm -rf /var/lib/apt/lists/*

# Install protobuf checker requirements
RUN pip install --user grpcio-tools
RUN pip install --user protobuf

COPY protobuf-check.sh /protobuf-check.sh
RUN chmod +x /protobuf-check.sh
ENTRYPOINT ["/protobuf-check.sh"]

# Switch back to non privileged user
USER guest
