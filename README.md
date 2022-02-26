# Stance Detector API

## Overview

A simple REST API that wraps a BERT model trained for detecting the stance on a particular topic from a body of text.

## Requirements

Python 3.5.2+

## Usage

To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/topic-stance-detector/v1/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/topic-stance-detector/v1/swagger.json
```

To launch the integration tests, use tox:

```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```
