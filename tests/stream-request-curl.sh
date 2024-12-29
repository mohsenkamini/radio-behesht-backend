#!/bin/bash
set -x
TOKEN=$1

curl -X POST http://127.0.0.1:8000/api/stream/request \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $TOKEN" \
-d "{
  \"program_name\": \"My Program\",
  \"description\": \"This is a test program.\",
  \"schedule\": \"Every Thursday\",
  \"start_date\": \"2024-01-01\",
  \"episodes\": 10,
  \"contact\": \"example@example.com\"
}
"
