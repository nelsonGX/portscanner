#!/usr/bin/env python 
#  -*- coding: utf-8 -*-

##########################################################################################
#                                 PyThon Port Scanner                                    #
#                                 PyThon 端口掃描腳本                                     #
#                                                                                        #
# credit: Nelson (https://www.nelsongx.com)                                              #
#                                                                                        #
##########################################################################################


#import
import socket
import sys
import requests
import re
import time
from time import perf_counter
#start
print('\n'*2)
print('  _____           _    _____                                 ')
print(' |  __ \         | |  / ____|                                ')
print(' | |__) |__  _ __| |_| (___   ___ __ _ _ __  _ __   ___ _ __ ')
print(" |  ___/ _ \| '__| __|\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|")
print(' | |  | (_) | |  | |_ ____) | (_| (_| | | | | | | |  __/ |   ')
print(' |_|   \___/|_|   \__|_____/ \___\__,_|_| |_|_| |_|\___|_|   ')
print('                                                             ')
print('                          credit: https://github.com/nelsonGX')
print('\n\n')
print('# Please enter 1 for English, 請輸入 2 以使用中文')
lan = str(input())
if lan == '1':
    print('# Enter IP:')
    ip = str(input())
    while '.' not in ip or len(str(ip)) == 0:
        print('# Invald IP. Please try again.')
        ip = str(input())
    print('# Enter Start Port:')
    aport = int(input())
    while aport < 1:
        print('# Who tf have negative port...Please try again.')
        aport = int(input())
    print('# Enter End Port:')
    eport = int(input())
    while eport < 1:
        print('# Who tf have negative port...Please try again.')
        eport = int(input())
    while eport < aport:
        print('# End port cannot be smaller than Start port.')
        eport = int(input())
    print('# Request Speed [fast(10RPS), normal(5RPS), slow(1RPS), custom(?RPS)]')
    timeout = str(input())
    if timeout == 'fast':
        timeoutd = 0.1
    elif timeout == 'normal':
        timeoutd = 0.2
    elif timeout == 'slow':
        timeoutd = 1
    elif timeout == 'custom':
        print('# Please enter RPS:')
        timeoutd = 1/int(input())
    elif timeout == 'sfast':
        timeoutd = 0.01
    else:
        print('# Request speed was set to normal.')
        timeoutd = 0.2
    sys.stdout.write('\r# Processing...Checking settings')
    sys.stdout.flush()
    sys.stdout.write('\r\n\n# Enter finished. Make sure information down below are correct, and enter Y to start/accept the policy:\nIP: ' +    ip + '\nPort Range: ' + str(aport) + '~' + str(eport) + '\nRequester: ' + re.sub("b","",re.sub("'", "", str(requests.get(url="https://api.ipify.org/").content))) + '\n\n# Enter(y/N):')
    sys.stdout.flush()
    print('')
    confirm = str(input())
    if confirm == 'y' or confirm == 'Y' or confirm == 'Yes' or confirm == 'yes' or confirm == 'YES':
        #counter
        total = eport-aport
        startp = aport
        portresult = ' '
        #start scanning
        start = perf_counter()
        while aport < eport:
            port = aport
            portleft = eport-aport
            nowport = aport-startp
            percent = (nowport*100)//total
            timeleft = time.strftime('%Hh, %Mm, %Ss', time.gmtime((portleft*timeoutd)//1))
            sys.stdout.write('\rProcessing... | Port: ' + str(port) + ' | ' + str(percent) + '% | ' + str(nowport) + '/' + str(total) +     ' | ' + str(portleft) + ' port(s) left | eta. ' + str((timeleft)) + ' | Scanned Ports: ' + str(portresult))
            sys.stdout.flush()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(float(timeoutd))
            result = sock.connect_ex((ip, aport))
            if result == 0:
                portresult = portresult + str(port) + ", "
            sock.close()
            aport += 1

        end = perf_counter()
        print('\n# Finished scan.' + ' (' + str((end-start)//1) + 's)')
        print('# Scanned port(s): ' + str(portresult))
    else:
        print('# Not accepting privacy. Quitting now.')


#chinese
elif lan == '2':
    print('# 輸入 IP:')
    ip = str(input())
    while '.' not in ip or len(str(ip)) == 0:
        print('# 無效的IP地址。請再試一遍。')
        ip = str(input())
    print('# 輸入開始的端口:')
    aport = int(input())
    while aport < 1:
        print('# 你可以跟我講誰端口是負數嗎...請再輸一遍:')
        aport = int(input())
    print('# 輸入結束的端口:')
    eport = int(input())
    while eport < 1:
        print('# 你可以跟我講誰端口是負數嗎...請再輸一遍:')
        eport = int(input())
    while eport < aport:
        print('# 結束的端口不可比開始的端口小。')
        eport = int(input())
    print('# 請求速率: [fast(10RPS), normal(5RPS), slow(1RPS), custom(?RPS)]')
    timeout = str(input())
    if timeout == 'fast':
        timeoutd = 0.1
    elif timeout == 'normal':
        timeoutd = 0.2
    elif timeout == 'slow':
        timeoutd = 1
    elif timeout == 'custom':
        print('# 請輸入 RPS(Requests Per Second):')
        timeoutd = 1/int(input())
    elif timeout == 'sfast':
        timeoutd = 0.01
    else:
        print('# 請求速率已被設置為normal(5RPS)。')
        timeoutd = 0.2
    sys.stdout.write('\r# 請稍等，正在確定設定中...')
    sys.stdout.flush()
    sys.stdout.write('\r\n\n# 輸入完成。請確保下面的數據是正確的，並輸入y來確定開始以及同意條款。\nIP: ' + ip + '\n端口範圍: ' + str(aport) + '~' + str(eport) + '\n請求IP: ' + re.sub("b","",re.sub("'", "", str(requests.get(url="https://api.ipify.org/").content))) + '\n\n# 輸入(y/N):')
    sys.stdout.flush()
    print('')
    confirm = str(input())
    if confirm == 'y' or confirm == 'Y' or confirm == 'Yes' or confirm == 'yes' or confirm == 'YES':
        #counter
        total = eport-aport
        startp = aport
        portresult = ' '
        #start scanning
        start = perf_counter()
        while aport < eport:
            port = aport
            portleft = eport-aport
            nowport = aport-startp
            percent = (nowport*100)//total
            timeleft = time.strftime('%H小時, %M分鐘, %S秒', time.gmtime((portleft*timeoutd)//1))
            sys.stdout.write('\r處理中... | 端口: ' + str(port) + ' | ' + str(percent) + '% | ' + str(nowport) + '/' + str(total) +     ' | 剩下' + str(portleft) + '個端口  | eta. ' + str((timeleft)) + ' | 已掃描端口: ' + str(portresult))
            sys.stdout.flush()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(float(timeoutd))
            result = sock.connect_ex((ip, aport))
            if result == 0:
                portresult = portresult + str(port) + ", "
            sock.close()
            aport += 1

        end = perf_counter()
        print('\n# 掃描完成。' + ' (花費' + str((end-start)//1) + '秒)')
        print('# 已掃描端口: ' + str(portresult))
    else:
        print('# 不接受條款/退出程式。')
else:
    print('# unknown language. quitting now.')