# Build image
docker build -t dfk-email:latest -f Dockerfile .

# Cross-compile project
docker run -it dfk-email:latest
