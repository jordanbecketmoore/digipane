# curl -X POST http://localhost:3141/api/videos \
#      -H "Content-Type: application/json" \
#      -d '{"url": "https://www.youtube.com/watch?v=2PuFyjAs7JA"}'

curl -X PUT http://localhost:3141/api/display \
     -H "Content-Type: application/json" \
     -d '{"path": "vid.webm"}'