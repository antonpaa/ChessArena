FROM python:3.8-buster

LABEL "com.github.actions.name" = "CI Setup"
LABEL "com.github.actions.description" = "Sets up the environment to run the CI"
LABEL "com.github.actions.icon" = "chevron-right"
LABEL "com.github.actions.color" = "green"

# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

RUN alias python3="/usr/bin/python3.7"

# Instantiate a guest user
RUN \
    groupadd -g 999 guest && useradd -u 999 -g guest -G sudo -m -s /bin/bash guest && \
    sed -i /etc/sudoers -re 's/^%sudo.*/%sudo ALL=(ALL:ALL) NOPASSWD: ALL/g' && \
    sed -i /etc/sudoers -re 's/^root.*/root ALL=(ALL:ALL) NOPASSWD: ALL/g' && \
    sed -i /etc/sudoers -re 's/^#includedir.*/## **Removed the include directive** ##"/g' && \
    echo "guest ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
    echo "Customized the sudoers file for passwordless access to the guest user!" && \
    echo "guest user:";  su - guest -c id

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
RUN python3 -m pip install --user grpcio-tools
RUN python3 -m pip install --user protobuf

COPY protobuf-check.sh /protobuf-check.sh
RUN chmod +x /protobuf-check.sh
ENTRYPOINT ["/protobuf-check.sh"]

# Switch back to non privileged user
USER guest
