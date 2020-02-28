#!/usr/bin/bash
########################################################
########################################################
########### ------------------------------- ############
########### SAYDOG FRAMEWORK V1.2 INSTALLER ############
########### ------------------------------- ############
#################### copyright©2020 ####################
########################################################
########################################################

# Just animation
cat << EOF
EOF

spinner=('Installing iNstalling inStalling insTalling instAlling instaLling instalLing installIng installiNg installinG installing')

count(){
  spin &
  pid=$!

  for i in `seq 1 10`
  do
    sleep 1;
  done

  kill $pid
}

spin(){
  while [ 1 ]
  do
    for i in ${spinner[@]};
    do
      echo -ne "\r[ $i ] saydog framework version 1.2";
      sleep 0.1;
    done;
  done
}

count
echo "[*] Preparing for installing perl ..."
echo "    If u find (y/n) please choose Y or yes"
echo "    If u find What approach do you want? local::lib, please type 'manual' and enter"
echo ""
sleep 2
echo "[*] Installing perl ..."
echo "    Please wait in 10-15 minutes ..."
echo ""
pkg install -y perl;pkg install -y clang;pkg install -y make;pkg install -y openssl;pkg install openssl-tool;cpan install Net::SSLeay::Handle;cpan LWP::UserAgent
echo ""
echo "[*] Preparing for installing other packages ..."
echo "    Php, python, python2, ruby, nodejs, jp2a"
echo "    figlet, toilet, gnupg, zip, unzip,  wget"
echo ""
pkg install -y php python python2 ruby nodejs;pkg install -y jp2a figlet toilet gnupg zip unzip wget
echo ""
echo "[*] Preparing for installing python requirements ..."
echo "    requests, bs4, pyfiglet, urllib"
echo ""
pip install requests bs4 pyfiglet urllib;pip2 install requests bs4;pip install --upgrade pip
echo ""
echo "[*] All dependencies have been installed"
echo "[*] configure console calls"
echo "    Please wait"
echo ""
chmod +x run saydog;mv saydog /data/data/com.termux/files/usr/bin;rm install.sh
echo "[*] Saydog framework have been installed !"
echo "    thankyou for installing saydog framework version 1.2"
echo "    if u have any question, and if u find the bug in this tool"
echo "    plese contact to me saydog.official@gmail.com"
echo "    Start saydog framework with command: ./run  or saydog"
