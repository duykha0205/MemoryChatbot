FROM python:3.9

# Set the working directory in the container
WORKDIR /langchain

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project code to the working directory
COPY . .

# Expose any necessary ports
# EXPOSE 2000

# docker build -t langchain:1.0