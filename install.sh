#!/bin/bash
root() {
user=`whoami`
if [[ $user != 'root' ]]; then
	echo "Please run as root\n"
	exit
fi
}

check_pakage() {
pakage=`which $pakage_name`
if [[ $pakage == '' ]]; then
	printf "pakage $pakage_name not install\n"
	sleep 0.2
	printf "pakage '$pakage_name' installing...\n"
	apt-get install $pakage_name
else
	sleep 0.5
	printf "pakage installed at '$pakage'\n"
fi
}

root
pakage_name="aircrack-ng"
check_pakage
pakage_name="xterm"
check_pakage
pakage_name="mdk4"
check_pakage
pakage_name="python3"
check_pakage
pakage_name="macchanger"
check_pakage

printf "installing pip3...."
pakage=`which pip3`
if [[ $pakage == '' ]]; then
	printf "installing pip3..."
	apt-get install python3-pip
else
	sleep 0.5
	printf "\npip3 installed at '$pakage'"
fi

sleep 0.5

printf "install random2...."
pip3 install random2

cp -r jammer_IHA /usr/share

access() {
cat > /usr/local/bin/wifijammer <<EOF
#!/bin/bash
cd /usr/share/jammer_IHA
python3 jammer.py
EOF

chmod +x /usr/local/bin/wifijammer

printf "\n\ntype 'wifijammer' anywhere on the terminal\n"
}
access

