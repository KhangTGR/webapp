FROM 240936149117.dkr.ecr.ap-southeast-1.amazonaws.com/python

WORKDIR  /app

COPY requirements.txt requirements.txt
# COPY .aws .

RUN pip install -r requirements.txt

COPY . /app

# EXPOSE 5000

ENTRYPOINT FLASK_APP=/app/app.py flask run --host=0.0.0.0 --port=8080
# CMD ["python3","app.py"]