FROM alpine:latest

LABEL "com.github.actions.name" = "CI Setup"
LABEL "com.github.actions.description" = "Sets up the environment to run the CI"
LABEL "com.github.actions.icon" = "chevron-right"
LABEL "com.github.actions.color" = "green"

LABEL "repository" = "https://github.com/vergi40/ChessArena"
LABEL "homepage" = "https://github.com/vergi40/ChessArena"

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
