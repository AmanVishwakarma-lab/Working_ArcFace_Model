# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=7860

# Install system dependencies for OpenCV and InsightFace
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Create the uploads folder as defined in your app
RUN mkdir -p uploads && chmod 777 uploads

# Expose the port Hugging Face expects
EXPOSE 7860

# Start the application using Gunicorn (as listed in your requirements)
# Your app.py uses 'app' as the Flask instance
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]