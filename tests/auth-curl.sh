curl -X POST http://localhost:8000/api/auth/users/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "V4q57giibABXzx2S"}'


curl -X POST http://localhost:8000/api/auth/jwt/create/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "V4q57giibABXzx2S"}'

curl -X POST http://localhost:8000/api/auth/jwt/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "your_refresh_token"}'

curl -X POST http://localhost:8000/api/auth/jwt/verify/ \
  -H "Content-Type: application/json" \
  -d '{"token": "your_access_token"}'

