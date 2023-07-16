#! /bin/bash

docker run --name postgres-light -d -e POSTGRES_PASSWORD=password -p 5432:5432 postgres:alpine
