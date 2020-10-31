FROM alpine:latest

LABEL "com.github.actions.name" = "CI Setup"
LABEL "com.github.actions.description" = "Sets up the environment to run the CI"
LABEL "com.github.actions.icon" = "chevron-right"
LABEL "com.github.actions.color" = "green"

LABEL "repository" = "https://github.com/vergi40/ChessArena"
LABEL "homepage" = "https://github.com/vergi40/ChessArena"

# Add pip
USER root
RUN apt-get update
RUN apt-get install -y python3-pip

# Install protobuf checker requirements
RUN pip3 install --user grpcio-tools
RUN pip3 install --user protobuf
RUN pip3 install invoke

ADD protobuf-check.sh /protobuf-check.sh
RUN chmod +x /protobuf-check.sh
ENTRYPOINT ["/protobuf-check.sh"]
