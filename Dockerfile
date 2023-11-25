FROM python:3.9-alpine
WORKDIR /
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
RUN pytest tst/ && pylint app.py
CMD ["flask", "run", "--host=0.0.0.0"]
