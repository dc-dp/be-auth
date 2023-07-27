FROM python:3.10

RUN pip install --upgrade pip

RUN mkdir /app
COPY . /app

RUN useradd -ms /bin/bash worker
RUN chown -R worker:worker /app

USER worker
WORKDIR /app
ENV PATH="/home/worker/.local/bin:$PATH"

RUN pip install pipenv
RUN pipenv install
RUN pipenv install gunicorn

EXPOSE 8000

RUN chmod +x ./entrypoint.sh
CMD ["sh", "entrypoint.sh"]