FROM python:3.12.3

WORKDIR /Space Shooter Pygame

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "./starter.py"]