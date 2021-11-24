import subprocess
import interface
from time import sleep

cmd = "iwlist {} scan | grep -e 'ESSID' -e 'Address' -e 'Channel:' -e 'Frequency:' -e 'Encryption'".format(interface.interface_Name())
print("Scanning...")

def scanning():
    try:
        j = subprocess.check_output(cmd, shell=True)
    except:
        j = b'cld'
    j = str(j, 'utf-8')
    subprocess.call("clear", shell=True)
    if 'cld' in j:
        print("\033[1;31mNo Device found nearby you")
    else:
        ff = open('scan.txt', 'w')
        print("\033[1;31mS.No\t\tBSSID\t  Channel\t Frequency\t   Encryption \t     ESSID\033[1;32m", end='')
        j = j.replace('ESSID:','')
        j = j.replace('Address:', '')
        j = j.replace('Channel:', '')
        j = j.replace('Encryption','')
        j = j.replace('Frequency:', '')
        j = j.replace('"', '')
        j = j.replace('\n', ' ')
        j = j.replace('   Cell','\n')
        j = j.replace('                 ', '')
        print(j)
        ff.write(j)
        ff.write("\n")
        ff.close()
        sleep(10)
        print("\033[1;31mrescan...")

while True:
    scanning()




