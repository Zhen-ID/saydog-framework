#!/usr/bin/bash
########################################################
########################################################
########### ------------------------------- ############
########### SAYDOG FRAMEWORK V1.2 INSTALLER ############
########### ------------------------------- ############
#################### copyright©2020 ####################
########################################################
########################################################

r="\x1b[31;1m"
b="\x1b[36;1m"
w="\x1b[00m"

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
      echo -ne "\r[ $i ]$w saydog framework version 1.2";
      sleep 0.1;
    done;
  done
}

count
echo "\x1b[32m[*] Preparing for installing perl ..."
echo "\x1b[00m    If u find (y/n) please choose Y or yes"
echo "\x1b[00m    If u find manual, please type 'manual' and enter"
echo "\x1b[32m[*] Installing perl ..."
echo "\x1b[00m    Please wait in 10-15 minutes ..."
pkg install -y perl;pkg install -y clang;pkg install -y make;pkg install -y openssl;pkg install openssl-tool;cpan install Net::SSLeay::Handle;cpan LWP::UserAgent
echo "\x1b[32m[*] Preparing for installing other packages ..."
echo "\x1b[00m    Php, python, python2, ruby, nodejs, jp2a"
echo "\x1b[00m    figlet, toilet, gnupg, zip, unzip,  wget"
pkg install -y php python python2 ruby nodejs;pkg install -y jp2a figlet toilet gnupg zip unzip wget
echo "\x1b[32m[*] Preparing for installing python requirements ..."
echo "\x1b[00m    requests, bs4, pyfiglet, urllib"
pip install requests bs4 pyfiglet urllib;pip2 install requests bs4;pip install --upgrade pip
echo "\x1b[32m[*] All dependencies have been installed"
echo "\x1b[32m[*] configure console calls"
echo "\x1b[00m    Please wait"
chmod +x run saydog;mv saydog /data/data/com.termux/files/usr/bin;rm install.sh
echo "\x1b[32m[*] Saydog framework have been installed !"
echo "\x1b[00m    thankyou for installing saydog framework version 1.2"
echo "\x1b[00m    if u have any question, and if u find the bug in this tool"
echo "\x1b[00m    plese contact to me saydog.official@gmail.com"
echo "\x1b[00m    Start saydog framework with command: \x1b[33m./run\x1b[00m  or \x1b[33msaydog"
