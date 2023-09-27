#pull latest Python image
FROM python:latest

RUN mkdir /document

#install dependencies and libraries
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

#change our workdir to facturx
WORKDIR /document

#copy gunicorn apps and entrypoint

# COPY app.py /test/
#go to app forlder

RUN cd /document

#Expose custom port
# EXPOSE 5000

#Run the webservice and listen in all interfaces using gunicorn

# CMD gunicorn --bind 0.0.0.0:5000 'app'

# CMD ["tail", "-f", "/dev/null"] facile pour tester 
CMD ["python","/document/app.py"] 
