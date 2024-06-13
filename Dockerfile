FROM python:3.10.12-slim as base

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt


COPY . .

CMD gunicorn 'app:app' --bind=0.0.0.0:8000
