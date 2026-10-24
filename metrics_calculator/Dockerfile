#base image
FROM python:3.13-slim

#work dir
WORKDIR /app

#copy {source/destination}
COPY . .

#run
RUN pip install -r requirements.txt

#port
EXPOSE 5000

#cmd
CMD ["python","app.py"]