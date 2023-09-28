# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./ /app

# Run app.py when the container launches
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
