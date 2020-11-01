#!/bin/bash

alias python3='/usr/bin/python3.7'
python3 -m grpc_tools.protoc -I ./Server/grpc/protos --python_out=. --grpc_python_out=. ./Server/grpc/protos/GameManager.proto