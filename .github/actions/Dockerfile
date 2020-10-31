FROM alpine:latest

LABEL "com.github.actions.name" = "CI Setup"
LABEL "com.github.actions.description" = "Sets up the environment to run the CI"
LABEL "com.github.actions.icon" = "chevron-right"
LABEL "com.github.actions.color" = "green"

LABEL "repository" = "https://github.com/vergi40/ChessArena"
LABEL "homepage" = "https://github.com/vergi40/ChessArena"

ADD protobuf-check.sh /protobuf-check.sh
RUN chmod +x /protobuf-check.sh
ENTRYPOINT ["/protobuf-check.sh"]
