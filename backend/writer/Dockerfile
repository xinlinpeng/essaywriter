FROM python:3.7.0
RUN mkdir /data/prj/essaywriter -p
COPY . /data/prj/essaywriter
WORKDIR /data/prj/essaywriter
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -r requirements.txt -i  https://mirrors.aliyun.com/pypi/simple/
WORKDIR /data/prj/essaywriter
CMD python manage.py runserver 0.0.0.0:8000

