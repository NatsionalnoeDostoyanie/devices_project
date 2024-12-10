FROM python:3.12

RUN pip install poetry

COPY . /devices_project

WORKDIR /devices_project

CMD ["make", "first-run-container"]