import argparse

HOST = ''
PATH = ''
def set_val(args):
    global HOST,PATH
    HOST = args.host
    PATH = args.path
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
set_value = subparsers.add_parser('conf')
set_value.add_argument('--host',default='db')
set_value.add_argument('--path')
set_value.set_defaults(func=set_val)
args = parser.parse_args()
args.func(args)
def edit(path,old,new):
    #edit backend tag in netdata main config file to connect it to influxdb
    file = open(path, 'r')
    conf = file.read()
    file.close()
    file = open(path,'w')
    file.write(conf.replace(old,new))
    file.close()
edit('/etc/netdata/netdata.conf','xxx.ip',HOST)
edit('/etc/netdata/python.d/web_log.conf','path.p',PATH)

