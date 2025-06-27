FROM registry.access.redhat.com/ubi9/python-312
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
