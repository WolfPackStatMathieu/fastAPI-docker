FROM ubuntu:22.04
WORKDIR ${HOME}/fastAPI-docker
# Install Python
RUN apt-get -y update && \
    apt-get install -y python3-pip

# Install project dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]