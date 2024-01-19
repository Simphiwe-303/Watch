FROM pypy:latest
WORKDIR /app
COPY . /app
RUN python -m pip install -r requirements.txt
CMD watch_next.py