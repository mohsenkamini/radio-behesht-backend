curl -X POST http://localhost:8000/auth/users/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "V4q57giibABXzx2S"}'


curl -X POST http://localhost:8000/auth/jwt/create/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "V4q57giibABXzx2S"}'

curl -X POST http://localhost:8000/auth/jwt/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "your_refresh_token"}'

curl -X POST http://localhost:8000/auth/jwt/verify/ \
  -H "Content-Type: application/json" \
  -d '{"token": "your_access_token"}'

