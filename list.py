import os
import subprocess
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


