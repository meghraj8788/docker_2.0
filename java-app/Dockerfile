#Base Image
FROM eclipse-temurin:21-jdk-alpine

#Create Wroking Dir
WORKDIR /app

#Copy Code to WORKDIR
#Location is same where Docerfile is

COPY src/Main.java /app/Main.java
COPY quotes.txt quotes.txt

#Run command to install some libraries 

RUN javac Main.java

#Enable port 8000 cause our application run on it 

EXPOSE 8000

#CMD command to keep it running container 
CMD ["java","Main"]

