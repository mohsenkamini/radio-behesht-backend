#!/bin/bash
#
set -x 

TOKEN=$1
curl -X GET http://localhost:8000/api/users/ \
-H "Authorization: Bearer $TOKEN"
