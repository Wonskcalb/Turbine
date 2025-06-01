FROM python:3.13-slim

# Non-root user 
RUN useradd -mr turbine
WORKDIR /home/turbine

USER turbine

COPY --chown=turbine:turbine requirements.txt ./

RUN cat requirements.txt
RUN pip install --user -r requirements.txt --no-deps

ARG GIT_HASH
ENV GIT_HASH=${GIT_HASH:-dev}

COPY . .
