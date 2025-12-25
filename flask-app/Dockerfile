#BASE IMAGE of python
FROM python:3.11.14-alpine3.23

#make working dir
WORKDIR /app


#copy to working dir
COPY . .

#install require libraries
RUN pip install -r requirements.txt

#Enable port 80
EXPOSE 80

#CMD command to keep running
CMD ["python", "run.py"]
