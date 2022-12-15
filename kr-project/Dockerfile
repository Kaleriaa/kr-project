# Dockerfile

FROM python:3.9
COPY kr-project/requirements.txt requirements.txt 
RUN pip install --no-cache-dir -r requirements.txt
RUN ls
COPY . app 
WORKDIR /app 
# RUN python ./manage.py migrate 
# RUN python ./manage.py collectstatic
# EXPOSE 8000