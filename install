#!/usr/bin/bash
########################################################
########################################################
########### ------------------------------- ############
########### SAYDOG FRAMEWORK V1.2 INSTALLER ############
########### ------------------------------- ############
#################### copyright©2020 ####################
########################################################
########################################################

r="\e[31;1m"
b="\e[36;1m"
w="\e[00m"

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
echo "\e[32m[*] Preparing for installing perl ..."
echo "\e[00m    If u find (y/n) please choose Y or yes"
echo "\e[00m    If u find manual, please type 'manual' and enter"
echo "\e[32m[*] Installing perl ..."
echo "\e[00m    Please wait in 10-15 minutes ..."
pkg install -y perl;pkg install -y clang;pkg install -y make;pkg install -y openssl;pkg install openssl-tool;cpan install Net::SSLeay::Handle;cpan LWP::UserAgent
echo "\e[32m[*] Preparing for installing other packages ..."
echo "\e[00m    Php, python, python2, ruby, nodejs, jp2a"
echo "\e[00m    figlet, toilet, gnupg, zip, unzip,  wget"
pkg install -y php python python2 ruby nodejs;pkg install -y jp2a figlet toilet gnupg zip unzip wget
echo "\e[32m[*] Preparing for installing python requirements ..."
echo "\e[00m    requests, bs4, pyfiglet, urllib"
pip install requests bs4 pyfiglet urllib;pip2 install requests bs4;pip install --upgrade pip
echo "\e[32m[*] All dependencies have been installed"
echo "\e[32m[*] configure console calls"
echo "\e[00m    Please wait"
chmod +x run saydog;mv saydog /data/data/com.termux/files/usr/bin;rm install.sh
echo "\e[32m[*] Saydog framework have been installed !"
echo "\e[00m    thankyou for installing saydog framework version 1.2"
echo "\e[00m    if u have any question, and if u find the bug in this tool"
echo "\e[00m    plese contact to me saydog.official@gmail.com"
echo "\e[00m    Start saydog framework with command: \e[33m./run\e[00m  or \e[33msaydog"
