sudo docker build -t ai-videos .
sudo docker run -dp 127.0.0.1:3000:3000 ai-videos

sudo docker run --attach stdout ai-avideos