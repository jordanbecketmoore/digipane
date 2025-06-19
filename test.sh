# download test video
curl -X POST http://localhost:3141/api/videos \
     -H "Content-Type: application/json" \
     -d '{"url": "https://www.youtube.com/watch?v=2PuFyjAs7JA"}'

# download longer video
curl -X POST http://localhost:3141/api/videos \
     -H "Content-Type: application/json" \
     -d '{"url": "https://www.youtube.com/watch?v=Q4sS1Wv-1GE"}'


curl -X PUT http://localhost:3141/api/display \
     -H "Content-Type: application/json" \
     -d '{"path": "library/test.mp4"}'

curl -X PUT http://localhost:3141/api/display \
     -H "Content-Type: application/json" \
     -d '{"path": "library/drone.mp4"}'