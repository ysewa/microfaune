FROM python:3.7

ADD application /app

RUN pip install -r /app/requirements.txt

# Generate PB2 files
# RUN python -m  grpc_tools.protoc -I /protos --python_out=/helloworld/. --grpc_python_out=/helloworld/. /protos/helloworld.proto

EXPOSE 50051

# CMD [ "python", "/application/server.py" ]
