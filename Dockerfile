FROM python:3.8

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "/code/manage.py", "migrate"]
CMD ["python", "/code/manage.py", "runserver", "0.0.0.0:8000"]
