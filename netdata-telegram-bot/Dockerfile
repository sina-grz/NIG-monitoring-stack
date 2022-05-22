FROM python:3

WORKDIR /usr/src/app

COPY bot.py ./

RUN pip3 install python-telegram-bot get-docker-secret

WORKDIR /usr/src/app/


CMD ["python","/usr/src/app/bot.py","/etc/netdata/health_alarm_notify.conf"]
