FROM python:3
ADD myflask_app.py / 
RUN pip install flask
EXPOSE 5000
CMD ["python3", "./myflask_app.py"]