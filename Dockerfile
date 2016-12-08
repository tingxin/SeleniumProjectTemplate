FROM python
RUN pip install selenium
RUN mkdir /opt/cases
RUN mkdir /opt/common
ADD cases /opt/cases
ADD common /opt/common
COPY main.py /opt
COPY setting.cfg /opt

WORKDIR /opt/
CMD ["python", "main.py"]
