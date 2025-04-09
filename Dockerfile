FROM python:3.11-slim

WORKDIR /src

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:create_app", "--host", "0.0.0.0", "--port", "80"]