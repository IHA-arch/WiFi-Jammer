import socket

def interface_Name():
    interface_name = socket.if_nameindex()
    try:
        wlan_interface_name = interface_name[2][1]
    except:
        print("\033[1;32mNo wireless interface")
        print("\033[1;32mexiting...")
        exit()
    return wlan_interface_name

def check_jammer():
    try:
        interface_name = socket.if_nameindex()
        jammer = interface_name[3][1]
        if jammer == 'jammer':
            jam = "RwR"
        else:
            jam = "rrr"
    except:
        jam = "RRR"
    return jam

