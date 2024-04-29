# Base Image with Python
FROM python:3.9 

# Install necessary dependencies 
RUN pip install pyvisa pyserial  # Install R&S VISA (if necessary)

# Copy your Python script 
COPY ./etl_script.py /app/  

# Set working directory
WORKDIR /app

# Specify the command to run when the container starts
CMD ["python", "etl_script.py"] 
