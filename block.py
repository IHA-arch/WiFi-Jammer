import sys
import os
import getpass
import socket
import subprocess
from interface import interface_Name
from time import time, sleep

def root():
    user = getpass.getuser()
    if ( user != 'root'):
        print("\033[1;32mPlease run as root")
        exit()

def connection():
    try:
        socket.create_connection(("1.1.1.1", 53))
        print("\r \033[1;31m!!Connected!!")
    except OSError:
        print("\r \033[1;33mconnecting...", end='')
    except KeyboardInterrupt:
        pass

def update_pass_list():
    path = '/etc/NetworkManager/system-connections'
    psk_key = open("pass.key", "w")
    files = os.listdir(path)
    for file_name in files:
        if "Wired connection" in file_name:
            pass
        else:
            command = "cat " + path + "/" + "'" + file_name + "'" + " | grep psk="
            try:
                ap_psk = subprocess.check_output(command, shell=True)
            except:
                ap_psk = b'=no password'
            psk_key.write(file_name)
            psk_key.write(str(ap_psk, 'utf-8'))
    psk_key.close()

def one_time_connection():
    try:
        socket.create_connection(("1.1.1.1", 53))
        connect_ap = "iwconfig {} | grep 'ESSID'".format(interface_Name())
        connect_ap_name=subprocess.check_output(connect_ap, shell=True)
        cc = str(connect_ap_name, 'utf-8').split(':')
        cc = cc[1].replace('\n', '')
        cc = cc.replace('" ', '')
        cc = cc.replace('"', '')
        print("\033[1;31m!!You Connected with '\033[1;36m{}\033[1;31m' Access Point".format(cc))
    except OSError:
        print("\033[1;31mYou Don't Have Any Wireless connection")
        pass

def mac_changer():
    name = interface_Name()
    print("\033[1;35m*=======>\033[1;31mMac Address\033[1;35m<=======*\033[1;34m")
    sleep(0.1)
    command = 'macchanger -s ' + name
    os.system(command)
    command1 = 'ifconfig ' + name + ' down'
    os.system(command1)
    print("\n\033[1;35m*=======>\033[1;31mNew Mac Address\033[1;35m<=======*\033[1;34m")
    sleep(0.1)
    command2 = 'macchanger -r ' + name
    try:
        rr = subprocess.check_output(command2, shell=True)
    except:
        pass

    os.system(command)
    command3 = 'ifconfig ' + name + ' up'
    os.system(command3)

def get_block():
    try:
        essid = input("\033[1;34mEnter Target Access point ESSID(Who BLOCK You):")
        read_essid = open('scan.txt', 'r')
        ressid = read_essid.read()
        if essid in ressid:
            pass
            connect_ap = "iwconfig {} | grep 'ESSID'".format(interface_Name())
            connect_ap_name=subprocess.check_output(connect_ap, shell=True)
            cc = str(connect_ap_name, 'utf-8').split(':')
            cc = cc[1].replace('\n', '')
        else:
            print("\033[1;34mEntered Access Point '\033[1;37m{}\033[1;34m' Not in Range...".format(essid))
        if essid in cc:
            print("\033[1;31m You Already connect with '\033[1;36m{}\033[1;31m' Access Point".format(essid))
        else:
            pass

        k = open('pass.key', 'r')
        l = k.read()
        if essid in l:
            cmd = "cat pass.key | grep '{}'".format(essid)
            password = subprocess.check_output(cmd, shell=True)
            pas = str(password, 'utf-8')
            pas1 = pas.split('=')
            pas1 = pas1[1].split('\n')
            cmd = "nmcli d wifi connect '{}' password {} > /dev/null 2>&1 &".format(essid, pas1[0])
            os.system(cmd)
        
        else:
            print("Own Machine has't connected to '{}' even once".format(essid))
    except KeyboardInterrupt:
        pass
        


def main():
    root()
    update_pass_list()
    condition=True
    one_time_connection()
    start_time = time()
    interface_Name()
    get_block()
    mac_changer()
    while condition:
        try:
            socket.create_connection(("1.1.1.1", 53))
            print("\r \033[1;31m!!Connected!!")
            condition=False
        except OSError:
            print("\r\033[1;33mConnecting...", end='')
        except KeyboardInterrupt:
            condition=False
        end_time = time()
        time_diff = end_time-start_time
        if(time_diff > 15):
            print("\n")
            mac_changer()
            start_time=time()


