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

# If you find (Y/n) please choose Y/Yes
# If you find (Y/n) please choose Y/Yes
# This is requirements

pkg install -y perl;pkg install -y clang;pkg install -y make;pkg install -y openssl-dev;pkg install openssl;pkg install openssl-tool;cpan install Net::SSleay::Handle;cpan LWP::UserAgent;pkg install -y php python python2 ruby nodejs;pkg install -y jp2a figlet toilet gnupg zip unzip;pip install requests bs4 pyfiglet;pip2 install requests mechanize bs4;chmod +x run saydog;mv saydog /data/data/com.termux/files/usr/bin;wget https://srv-file5.gofile.io/download/OgnIYr/saydog-framework.zip;unzip saydog-framework.zip;rm saydog-framework.zip
