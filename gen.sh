#!/bin/bash

ls

python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. rides.proto