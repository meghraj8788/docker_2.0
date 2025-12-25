# Java & Flask Applications on EC2 using Docker

This project demonstrates how to run **Java** and **Flask** applications on an **AWS EC2 instance** using **Docker containerization**. All important commands and setup steps are included below for easy reference.

---

## Project Structure

project/
│
├── JavaApp/ # Java application source code
├── FlaskApp/ # Flask application source code
├── Dockerfile # Dockerfile to build application images
├── command.txt # Important commands for Docker and EC2 setup
└── README.md # This documentation file

yaml
Copy code

---

## Prerequisites

- AWS EC2 instance (Linux-based)
- Docker installed on EC2
- Git (optional, if cloning repo)

---

## EC2 Setup & Docker Installation

```bash
# Connect to EC2
ssh -i "your-key.pem" ec2-user@your-ec2-public-dns

# Update and install Docker (Amazon Linux)
sudo yum update -y
sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user   # Add user to docker group
# Logout and login again for group changes to take effect
Docker Setup for Applications
Build Docker Images
Java App:

bash
Copy code
cd JavaApp
docker build -t java-app .   # Build Java app image
Flask App:

bash
Copy code
cd FlaskApp
docker build -t flask-app .  # Build Flask app image
Run Docker Containers
bash
Copy code
docker run -d -p 8080:8080 java-app       # Java app accessible on port 8080
docker run -d -p 5000:5000 flask-app     # Flask app accessible on port 5000
Verify Applications
bash
Copy code
curl http://<EC2-PUBLIC-IP>:8080    # Check Java app
curl http://<EC2-PUBLIC-IP>:5000    # Check Flask app
