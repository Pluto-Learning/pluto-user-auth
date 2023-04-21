FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /pluto-user-auth

COPY ./requirements.txt /pluto-user-auth/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /pluto-user-auth/requirements.txt

COPY ./src /pluto-user-auth/src


CMD ["gunicorn", "src.main:app", "-c", "./src/infastructure/config/runtime/gunicorn.conf.py"]
