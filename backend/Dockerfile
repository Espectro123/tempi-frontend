# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn pandas openpyxl

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./ /app

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
