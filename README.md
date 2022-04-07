# Build image
docker build -t dfk-email:latest -f Dockerfile .

# Start project
docker run -it dfk-email:latest
