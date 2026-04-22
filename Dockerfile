FROM python:3.12.3

WORKDIR /Space Shooter Pygame

COPY . .

ENV DISPLAY=:0

RUN pip install -r requirements.txt

CMD ["python", "./starter.py"]