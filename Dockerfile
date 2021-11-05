FROM python:3.8
 
# RUN apt-get update
# COPY requirements.txt requirements.txt  
# RUN pip install -U pip
# RUN pip install fastapi uvicorn
# RUN pip install -r requirements.txt 
# Update pip
RUN apt-get update 
# Copy application dependency manifests to the container image.
# Copying this separately prevents re-running pip install on every code change.
COPY requirements.txt ./ 

# Install production dependencies.
RUN set -ex; \
    pip install -r requirements.txt; \
    pip install gunicorn

 
COPY ./app /app    
ENV PYTHONPATH "${PYTHONPATH}:/app"   
ENV APP_HOME /app  

CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 app.main:app