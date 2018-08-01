# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /NqueensChallenge
WORKDIR /NqueensChallenge

# Copy the current directory contents into the container at /NqueensChallenge
ADD . /NqueensChallenge

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV NAME env

# Run generatequeens.py when the container launches
EXPOSE 32771
CMD ["createdb", "-h", "localhost", "-p", "32771", "-U", "postgres", "nqueen"]
CMD ["psql", "-h", "localhost" , "-p", "32771", "-U", "postgres", "nqueen"]
CMD ["python", "generatequeens.py"]
