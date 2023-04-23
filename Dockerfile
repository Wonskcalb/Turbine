FROM python:3.11-slim

# Non-root user 
RUN useradd -mr turbine
WORKDIR /home/turbine

USER turbine

COPY requirements.txt ./
RUN pip install -r requirements.txt

ARG GIT_HASH
ENV GIT_HASH=${GIT_HASH:-dev}

COPY . .
