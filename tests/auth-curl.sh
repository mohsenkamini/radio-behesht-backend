#!/bin/bash
#
set -x 

curl -X POST http://localhost:8000/api/auth/users/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "V4q57giibABXzx2S"}'

echo 

export TOKEN=`curl -X POST http://localhost:8000/api/auth/jwt/create/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "V4q57giibABXzx2S"}' | jq -r '.access'`


echo 
export REFRESH_TOKEN=`curl -X POST http://localhost:8000/api/auth/jwt/create/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "V4q57giibABXzx2S"}' | jq -r '.refresh'`

echo 

curl -X POST http://localhost:8000/api/auth/jwt/verify/ \
  -H "Content-Type: application/json" \
  -d "{\"token\": \"${TOKEN}\"}"

echo 
curl -X POST http://localhost:8000/api/auth/jwt/refresh/ \
  -H "Content-Type: application/json" \
  -d "{\"refresh\": \"${REFRESH_TOKEN}\"}"

echo 
