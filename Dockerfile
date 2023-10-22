##################
##docker-compose##
##################

FROM python:3.9
LABEL authors="arsen"
ENV PYTHONWRITEBYTECODE 1
RUN mkdir /project55
WORKDIR /project55
COPY req.txt .
RUN pip install -r /project55/req.txt
COPY . /project55