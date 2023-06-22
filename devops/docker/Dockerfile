# Using the official Python 3 base image from Docker Hub
FROM python:3

# Copies the 'application' directory from the local file system into the image's file system at '/application'
COPY application /application

# Changes the working directory for any following instructions in the Dockerfile (also for when the container is running) to '/application'
WORKDIR /application

# Installs the Python dependencies that are defined in the 'requirements.txt' file
# Gunicorn is also added here
RUN pip3 install -r requirements.txt gunicorn

# Sets an environment variable called 'MY_ENV' with the value 'dev'
ENV MY_ENV dev

# Exposes port 8080 from inside the Docker container to the Docker host
EXPOSE 8080

# The command that is run when the Docker container starts
# Here we run Gunicorn, bind it to 0.0.0.0:8080, and tell it to serve 'script:app'
CMD ["gunicorn", "-b", "0.0.0.0:8080", "script:app"]
