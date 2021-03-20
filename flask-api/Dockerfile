FROM python:3.7
RUN mkdir /code
WORKDIR /code
COPY requirements.txt .
RUN pip install -r /code/requirements.txt -i https://pypi.douban.com/simple
EXPOSE 5000
CMD ["gunicorn", "start:app", "-c", "./gunicorn.conf.py"]
