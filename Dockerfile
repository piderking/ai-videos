# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.12-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1


# Configuration Tool
ENV CONFIG_URL=0
ENV ELEVEN_LABS_TOKEN=!

# Install FFMPEG
RUN apt-get install ffmpeg


# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Enviroment
ENV URLS="https://www.reddit.com/r/AmItheAsshole/comments/1bzneq5/aita_for_selling_the_gift_my_exgirlfriend_bought/;https://www.reddit.com/r/AmItheAsshole/comments/1bzneq5/aita_for_selling_the_gift_my_exgirlfriend_bought/"

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "main.py"]
