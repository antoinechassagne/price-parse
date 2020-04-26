FROM ubuntu:16.04
FROM python:3.7
ENV FLASK_APP "api/app.py"
COPY . /api
WORKDIR /api
RUN pip install -r api/requirements.txt
COPY . /cdiscount
WORKDIR /cdiscount
RUN pip install ./cdiscount/
WORKDIR /api
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["api/app.py"]


