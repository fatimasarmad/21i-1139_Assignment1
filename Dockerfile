# Use official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the application files
COPY . /app

# Install required dependencies
RUN pip install --no-cache-dir flask

# Expose the port Flask runs on
EXPOSE 5000

# Set the entry point for the container
CMD ["python", "main.py"]
