FROM python:3
ENV FLASK_APP=/ego.py
RUN pip install flask && \
    apt-get update && \
    apt-get install -y cowsay
COPY ego.py /ego.py
CMD ["flask", "run", "--host=0.0.0.0"]
