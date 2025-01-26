FROM registry.red-soft.ru/ubi7/python-38-minimal

USER root

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8050

CMD ["python", "app/main.py"]