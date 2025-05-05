FROM nvcr.io/nvidia/tritonserver:25.02-py3

WORKDIR /app

# Install Python dependencies
RUN pip install opencv-python numpy

# Copy model configuration if needed
# We don't copy models as they will be mounted from host

# Expose necessary ports for Triton
EXPOSE 8000 8001 8002

# The entrypoint will be provided in the docker run command
