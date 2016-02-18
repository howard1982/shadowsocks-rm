import logging

#Config
MYSQL_HOST = 'xxxx.com'
MYSQL_PORT = 3306
MYSQL_USER = 'xxxx'
MYSQL_PASS = 'xxxxx'
MYSQL_DB = 'xxxx'

#Server Group
SERVER_GROUP = 1

# any or 0 - free,  1 - vip
ALLOW_USER_TYPE = 'any'

MANAGE_PASS = 'xxxxx'
#if you want manage in other server you should set this value to global ip
MANAGE_BIND_IP = '127.0.0.1'
#make sure this port is idle
MANAGE_PORT = 63333
#BIND IP
#if you want bind ipv4 and ipv6 '[::]'
#if you want bind all of ipv4 if '0.0.0.0'
#if you want bind all of if only '4.4.4.4'
SS_BIND_IP = '0.0.0.0'
SS_METHOD = 'aes-256-cfb'

#LOG CONFIG
LOG_ENABLE = False
LOG_LEVEL = logging.DEBUG
LOG_FILE = '/var/log/shadowsocks.log'

