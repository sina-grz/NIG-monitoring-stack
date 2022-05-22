FROM netdata/netdata

#copy main editable-netdata config file to container

COPY netdata.conf /etc/netdata/

#copy web editablelog collector module config file to containar

COPY web_log.conf /etc/netdata/python.d/

#copy python script gonna edit conf file easily

COPY health_alarm_notify.conf /etc/netdata/

