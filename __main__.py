# DISCLAIMER
# This is an open source for everyone
# you may redistribute, modify, use patents and use privately without any obligation to redistribute
# but it should be noted to include the source code of the library that was modified (not the source code of the entire program)
# include the license, include the original copyright of the author (iqbalmh18)
# and include any changes made (if modified)
# Users do not have the right to sue the creator when there is damage to the software or even demand if there is a problem
# caused by the makers of this tool. because every risk is caused by the user risk it self
# copyright©saydog2020
# https://instagram.com/saydog.official

# Author : iqbalmh18
# Team   : I dont have a team dude

import os,sys
from time import *
from __logo__ import *

u='\033[4m'
w='\x1b[00m'
r='\x1b[91m'
b='\x1b[36;1m'
y='\x1b[33m'

def exit():
        print(r+'[!]'+w+' The user forces it to stop')
        print(r+'[!]'+w+' Exiting program')
        sys.exit(1)
        
def corrupt():
        print(r+'[?]'+w+' Command not found, please type help')
        
def help():
  print('')
  print('HELP NAVIGATION')
  print('---------------')
  print('Welcome to the help navigation page')
  print('the following is collection of command')
  print('for using this tool')
  print('')
  print('command                                        description')
  print('-------                                        -----------')
  print('use pytoolkit                       python hacking toolkit')
  print('use webtoolkit                     website hacking toolkit')
  print('use socialbrute                     bruteforce socialmedia')
  print('use malware                              malware generator')
  print('use installer                               just installer')
  print('others                                         other tools')
  print('')
  print('other command                                  description')
  print('-------------                                  -----------')
  print('banner                                 change image banner')
  print('clear                                         clear screen')
  print('exit                                             exit tool')
  print('?                                       author information')

######################### OTHERS ######################
def other():
        while True:
                try:
                        ot = input(w+'saydog('+r+'other'+w+') > ')
                        if ot == 'help':
                                print('')
                                print('OTHER TOOLS')
                                print('-----------')
                                print('other tool, just for fun')
                                print('')
                                print('command                       description')
                                print('-------                       -----------')
                                print('use img2ascii        convert img to ascii')
                                print('use text2ascii      convert text to ascii')
                                print('')
                        elif ot == 'back':
                                main()
                        elif ot == 'clear':
                                os.system('clear')
                        elif ot == 'exit':
                                exit()
                        elif 'use img2ascii' in ot:
                                while True:
                                        try:
                                                df = input(w+'saydog('+r+'img2ascii'+w+') > ')
                                                if df == 'help':
                                                        print('')
                                                        print('IMAGE TO ASCII')
                                                        print('--------------')
                                                        print('jpg & jpeg converter')
                                                        print('')
                                                        print('command                       description')
                                                        print('-------                       -----------')
                                                        print('use convert/default     default converter')
                                                        print('use convert/invert      invert background')
                                                        print('')
                                                elif df == 'back':
                                                        main()
                                                elif df == 'exit':
                                                        exit()
                                                elif df == 'clear':
                                                        os.system('clear')
                                                elif 'use convert/default' in df:
                                                        print('convert > default')
                                                        os.system('cd module;python img_converter.py')
                                                elif 'use convert/invert' in df:
                                                        print('convert > invert')
                                                        os.system('cd module;python img_converter2.py')
                                                else:
                                                        corrupt()
                                        except KeyboardInterrupt:
                                                exit()
                        elif 'use text2ascii' in ot:
                                while True:
                                        try:
                                                ta = input(w+'saydog('+r+'text2ascii'+w+') > ')
                                                if ta == 'help':
                                                        print('')
                                                        print('TEXT TO ASCII')
                                                        print('-------------')
                                                        print('Text converter')
                                                        print('')
                                                        print('command                       description')
                                                        print('-------                       -----------')
                                                        print('use convert/all             all converter')
                                                        print('')
                                                elif ta == 'clear':
                                                        os.system('clear')
                                                elif ta == 'back':
                                                        main()
                                                elif ta  == 'exit':
                                                        exit()
                                                elif 'use convert/all' in ta:
                                                        print('convert > all')
                                                        os.system('cd module;python text_converter.py')
                                                else:
                                                        corrupt()
                                        except KeyboardInterrupt:
                                                exit()
                        else:
                                corrupt()
                except KeyboardInterrupt:
                        exit()

######################### INSTALLER ######################
def installer():
        while True:
                try:
                        ir = input(w+'saydog('+r+'installer'+w+') > ')
                        if ir == 'help':
                                print('')
                                print('INSTALLER TOOLKIT')
                                print('-----------------')
                                print('Auto installer tool')
                                print('')
                                print('command                            sources')
                                print('-------                            -------')
                                print('install ngrok                www.ngrok.com')
                                print('install shodan               www.shodan.io')
                                print('install debian                     Anlinux')
                                print('install opensuse-leap              Anlinux')
                                print('install centos                     Anlinux')
                                print('install blackbox                   Anlinux')
                                print('install kali                       Anlinux')
                                print('install ubuntu                     Anlinux')
                                print('install fedora                    Nmilosev')
                                print('install parrot                     Anlinux')
                                print('install nethunter             www.kali.org')
                                print('')
                        elif ir == 'back':
                                main()
                        elif ir == 'clear':
                                os.system('clear')
                        elif ir == 'exit':
                                exit()
                        elif 'install ngrok' in ir:
                                print(b+'[+]'+w+' Downloading ngrok in https://bin.equinox.io/')
                                print(b+'[+]'+w+' please wait for a few minutes')
                                os.system('cd;wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip;unzip ngrok-stable-linux-arm.zip;chmod +x ngrok;cp ngrok ../usr/bin;rm ngrok;rm ngrok-stable-linux-arm.zip')
                                print(b+'[+]'+w+' please take your authtoken in https://ngrok.com')
                                print(b+'[+]'+w+' login or register, and copy your authtoken')
                                print(b+'[+]'+w+' trying to open your browser')
                                time.sleep(2)
                                os.system('xdg-open https://ngrok.com')
                                ng = input('    paste your authtoken here: '+y)
                                if './ngrok authtoken' in ng:
                                        token = ng.split()[(-1)]
                                        os.system('ngrok authtoken '+token)
                                        print(b+'[+]'+w+' successfully installing ngrok')
                                        print(b+'[+]'+w+' now you can use ngrok')
                                        print('')
                                        os.system('ngrok -h')
                                else:
                                        os.system('ngrok authtoken '+ng)
                                        print(b+'[+]'+w+' successfully installing ngrok')
                                        print(b+'[+]'+w+' now you can use ngrok')
                                        print('')
                                        os.system('ngrok -h')
                        elif 'install shodan' in ir:
                                print(b+'[+]'+w+' Downloading shodan package')
                                print(b+'[+]'+w+' please wait for a few minutes')
                                os.system('cd;apt update;apt upgrade;easy_install shodan;pip install shodan request')
                                print(b+'[+]'+w+' plese take your API token in https://shodan.io')
                                print(b+'[+]'+w+' login or register and take your API token')
                                print(b+'[+]'+w+' tying to open your browser')
                                time.sleep(2)
                                os.system('xdg-open https://account.shodan.io/login')
                                sn = input('    paste your API token here: '+y)
                                if 'shodan init' in sn:
                                        api = sn.split()[(-1)]
                                        os.system('shodan init '+api)
                                        print(b+'[+]'+w+' successfully installing shodan')
                                        print(b+'[+]'+w+' now you can use shodan')
                                        print('')
                                        os.system('shodan -h')
                                else:
                                        os.system('shodan init '+sn)
                                        print(b+'[+]'+w+' successfully installing shodan')
                                        print(b+'[+]'+w+' now you can use shodan')
                                        print('')
                                        os.system('shodan -h')
                        elif 'install kali' in ir:
                                print(b+'[+]'+w+' Downloading package for kali linux')
                                print(b+'[+]'+w+' please wait for a few minutes')
                                os.system('cd;pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh')
                                print(b+'[+]'+w+' successfully installing kali linux')
                                print(b+'[+]'+w+' now you can start kali linux')
                                print(b+'[+]'+w+' command: ./start-kali.sh')
                        elif 'install ubuntu' in ir:
                                print(b+'[+]'+w+' Downloading package for ubuntu')
                                print(b+'[+]'+w+' please wait for a few minutes')
                                os.system('cd;pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh')
                                print(b+'[+]'+w+' successfully installing ubuntu')
                                print(b+'[+]'+w+' now you can start ubuntu')
                                print(b+'[+]'+w+' command: ./start-ubuntu.sh')
                        elif 'install debian' in ir:
                                print(b+'[+]'+w+' Downloading package for debian')
                                print(b+'[+]'+w+' please wait for a few minutes')
                                os.system('cd;pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh')
                                print(b+'[+]'+w+' successfully installing ubuntu')
                                print(b+'[+]'+w+' now you can start debian')
                                print(b+'[+]'+w+' command: ./start-debian.sh')
                        elif 'install parrot' in ir:
                                print(b+'[+]'+w+' Downloading package for parrot security')
                                print(b+'[+]'+w+' please wait for a few minutes')
                                os.system('cd;pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Parrot/parrot.sh && bash parrot.sh')
                                print(b+'[+]'+w+' successfully installing parrot security')
                                print(b+'[+]'+w+' now you can start parrot')
                                print(b+'[+]'+w+' command: ./start-parrot.sh')
                        elif 'install centos' in ir:
                                print(b+'[+]'+w+' Downloading package for centos')
                                print(b+'[+]'+w+' please wait for a few minutes')
                                os.system('cd;pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && bash centos.sh')
                                print(b+'[+]'+w+' successfully installing centos')
                                print(b+'[+]'+w+' now you can start centos')
                                print(b+'[+]'+w+' command: ./start-centos.sh')
                        elif 'install fedora' in ir:
                                print(b+'[+]'+w+' Downloading package for fedora')
                                print(b+'[+]'+w+' please wait for a few minutes')
                                os.system('cd;apt update && apt install wget -y && /data/data/com.termux/files/usr/bin/wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh && sh termux-fedora.sh;')
                                print(b+'[+]'+w+' successfully installing fedora')
                                print(b+'[+]'+w+' now you can start fedora')
                                print(b+'[+]'+w+' command: fedora')
                        elif 'install opensuse-leap' in ir:
                                print(b+'[+]'+w+' Downloading package for opensuse-leap')
                                print(b+'[+]'+w+' please wait for a few minutes')
                                os.system('cd;pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Leap/opensuse-leap.sh && bash opensuse-leap.sh')
                                print(b+'[+]'+w+' successfully installing opensuse-leap')
                                print(b+'[+]'+w+' now you can start opensuse-leap')
                                print(b+'[+]'+w+' command: ./start-leap.sh')
                        elif 'install blackbox' in ir:
                                print(b+'[+]'+w+' Downloading package for blackbox')
                                print(b+'[+]'+w+' please wait for a few minutes')
                                os.system('cd;pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/BackBox/backbox.sh && bash backbox.sh')
                                print(b+'[+]'+w+' successfully installing blackbox')
                                print(b+'[+]'+w+' now you can start blackbox')
                                print(b+'[+]'+w+' command: ./start-blackbox.sh')
                        elif 'install nethunter' in ir:
                                print(b+'[+]'+w+' Downloading package for nethunter')
                                print(b+'[+]'+w+' please wait for a few minutes')
                                os.system('cd;pkg install wget;wget -O install-nethunter-termux https://offs.ec/2MceZWr;chmod +x install-nethunter-termux;./install-nethunter-termux')
                                print(b+'[+]'+w+' successfully installing nethunter')
                                print(b+'[+]'+w+' now you can start nethunter')
                                print(b+'[+]'+w+' command: nethunter')
                                
                                
                        else:
                                corrupt()
                except KeyboardInterrupt:
                        exit()

##################### MALWARE GENERATOR #################
def malware():
        name = ''
        output = ''
        while True:
                try:
                        mg = input(w+'saydog('+r+'malware'+w+') > ')
                        if mg == 'help':
                                print('')
                                print('MALWARE GENERATOR')
                                print('-----------------')
                                print('Malware generator toolkit')
                                print('')
                                print('command')
                                print('-------')
                                print('use module/AndroRat_6Dec2013')
                                print('use module/Android.PegasusB')
                                print('use module/Android.Skygofree')
                                print('use module/Android.Spy.49_iBanking_Feb2014')
                                print('use module/Android.VikingHorde')
                                print('use module/AntiExe.A')
                                print('use module/Artemis')
                                print('use module/BAT.Drop')
                                print('use module/BAT.Pot.A')
                                print('use module/BAT.Skul')
                                print('use module/Backdoor.MSIL.Tyupkin')
                                print('use module/BlackEnergy2.1')
                                print('use module/Brain.A')
                                print('use module/Careto_Feb2014')
                                print('use module/Cascade.1701.W')
                                print('use module/Catapillar.E')
                                print('use module/Civil_War.282')
                                print('use module/Coll.CozyBear')
                                print('use module/Coll.DarkHydrus')
                                print('use module/CryptoLocker_10Sep2013')
                                print('use module/CryptoLocker_20Nov2013')
                                print('use module/CryptoLocker_22Jan2014')
                                print('use module/DOS.Yesmile')
                                print('use module/Dino')
                                print('use module/Dropper.Taleret')
                                print('use module/Duqu2')
                                print('use module/Dyre')
                                print('use module/EquationGroup.Fanny')
                                print('use module/EquationGroup.GROK')
                                print('use module/Form.A')
                                print('use module/Friday_the_13th.408')
                                print('use module/Friday_the_13th.416.A')
                                print('use module/Friday_the_13th.416.B')
                                print('use module/Green_Caterpillar.1575.A')
                                print('use module/INTC.A')
                                print('use module/IllusionBot_May2007')
                                print('use module/JS.JScript.A')
                                print('use module/JS.Lame')
                                print('use module/Jumper.B')
                                print('use module/Junkie')
                                print('use module/KRBanker')
                                print('use module/Kampana.A')
                                print('use module/Kelihos')
                                print('use module/Keylogger.Ardamax')
                                print('')
                        elif mg == 'clear':
                                os.system('clear')
                        elif mg == 'back':
                                main()
                        elif mg == 'exit':
                                exit()
                        elif mg == 'use module/AndroRat_6Dec2013':
                                os.system('cd module;cd malware;python 1.py')
                        elif mg == 'use module/Android.PegasusB':
                                os.system('cd module;cd malware;python 2.py')
                        elif mg == 'use module/Android.Skygofree':
                                os.system('cd module;cd malware;python 3.py')
                        elif mg == 'use module/Android.Spy.49_iBanking_Feb2014':
                                os.system('cd module;cd malware;python 4.py')
                        elif mg == 'use module/Android.VikingHorde':
                                os.system('cd module;cd malware;python 5.py')
                        elif mg == 'use module/AntiExe.A':
                                os.system('cd module;cd malware;python 6.py')
                        elif mg == 'use module/Artemis':
                                os.system('cd module;cd malware;python 7.py')
                        elif mg == 'use module/BAT.Drop':
                                os.system('cd module;cd malware;python 8.py')
                        elif mg == 'use module/BAT.Pot.A':
                                os.system('cd module;cd malware;python 9.py')
                        elif mg == 'use module/BOT.Skul':
                                os.system('cd module;cd malware;python 10.py')
                        elif mg == 'use module/Backdoor.MSIL.Tyupkin':
                                os.system('cd module;cd malware;python 11.py')
                        elif mg == 'use module/BlackEnergy2.1':
                                os.system('cd module;cd malware;python 12.py')
                        elif mg == 'use module/Brain.A':
                                os.system('cd module;cd malware;python 13.py')
                        elif mg == 'use module/Careto_Feb2014':
                                os.system('cd module;cd malware;python 14.py')
                        elif mg == 'use module/Cascade.1701.W':
                                os.system('cd module;cd malware;python 15.py')
                        elif mg == 'use module/Catapillar.E':
                                os.system('cd module;cd malware;python 16.py')
                        elif mg == 'use module/Civil_War.282':
                                os.system('cd module;cd malware;python 17.py')
                        elif mg == 'use module/Coll.CozyBear':
                                os.system('cd module;cd malware;python 18.py')
                        elif mg == 'use module/Coll.DarkHydrus':
                                os.system('cd module;cd malware;python 19.py')
                        elif mg == 'use module/CryptoLocker_10Sep2013':
                                os.system('cd module;cd malware;python 20.py')
                        elif mg == 'use module/CryptoLocker_20Nov2013':
                                os.system('cd module;cd malware;python 21.py')
                        elif mg == 'use module/CryptoLocker_22Jan2014':
                                os.system('cd module;cd malware;python 22.py')
                        elif mg == 'use module/DOS.Yesmile':
                                os.system('cd module;cd malware;python 23.py')
                        elif mg == 'use module/Dino':
                                os.system('cd module;cd malware;python 24.py')
                        elif mg == 'use module/Dropper.Taleret':
                                os.system('cd module;cd malware;python 25.py')
                        elif mg == 'use module/Duqu2':
                                os.system('cd module;cd malware;python 26.py')
                        elif mg == 'use module/Dyre':
                                os.system('cd module;cd malware;python 27.py')
                        elif mg == 'use module/EquationGroup.Fanny':
                                os.system('cd module;cd malware;python 28.py')
                        elif mg == 'use module/EquationGroup.GROK':
                                os.system('cd module;cd malware;python 29.py')
                        elif mg == 'use module/EquationGroup':
                                os.system('cd module;cd malware;python 30.py')
                        elif mg == 'use module/Form.A':
                                os.system('cd module;cd malware;python 31.py')
                        elif mg == 'use module/Friday_the_13th.408':
                                os.system('cd module;cd malware;python 32.py')
                        elif mg == 'use module/Friday_the_13th.416.A':
                                os.system('cd module;cd malware;python 33.py')
                        elif mg == 'use module/Friday_the_13th.416.B':
                                os.system('cd module;cd malware;python 34.py')
                        elif mg == 'use module/Green_Caterpillar.1575.A':
                                os.system('cd module;cd malware;python 35.py')
                        elif mg == 'use module/INTC.A':
                                os.system('cd module;cd malware;python 36.py')
                        elif mg == 'use module/IllusionBot_May2007':
                                os.system('cd module;cd malware;python 37.py')
                        elif mg == 'use module/JS.JScript.A':
                                os.system('cd module;cd malware;python 38.py')
                        elif mg == 'use module/JS.Lame':
                                os.system('cd module;cd malware;python 39.py')
                        elif mg == 'use module/Jumper.B':
                                os.system('cd module;cd malware;python 40.py')
                        elif mg == 'use module/Junkie':
                                os.system('cd module;cd malware;python 41.py')
                        elif mg == 'use module/KRBanker':
                                os.system('cd module;cd malware;python 42.py')
                        elif mg == 'use module/Kampana.A':
                                os.system('cd module;cd malware;python 43.py')
                        elif mg == 'use module/Kelihos':
                                os.system('cd module;cd malware;python 44.py')
                        elif mg == 'use module/Keylogger.Ardamax':
                                os.system('cd module;cd malware;python 45.py')
                        else:
                                corrupt()
                except KeyboardInterrupt:
                        corrupt()

###################### WEBTOOLKIT ####################
def webtoolkit():
	while True:
		try:
			wt = input(w+'saydog('+r+'webtoolkit'+w+') > ')
			if wt == 'help':
				print('')
				print('WEB TOOLKIT')
				print('------------')
				print('Website exploiting toolkit')
				print('')
				print('command                                        description')
				print('-------                                        -----------')
				print('use exploit/adminfinder              find admin login page')
				print('use exploit/traceroute                       route tracker')
				print('use exploit/reverse_dns        determinate the domain name')
				print('use exploit/findhost_dns                  finding dns host')
				print('use exploit/findshare_dns               finding shared dns')
				print('use exploit/dnslookup             checking dns all records')
				print('use exploit/whoislookup                      who is lookup')
				print('use exploit/iploclookup                 ip location lookup')
				print('use exploit/reiplookup                   reverse ip lookup')
				print('use exploit/sublookup                        subnet lookup')
				print('use exploit/tcpscan                       tcp port scanner')
				print('use exploit/headercheck                http header checker')
				print('')
			elif wt == 'back':
				main()
			elif wt == 'exit':
				exit()
			elif wt == 'clear':
				os.system('clear')
			elif 'use exploit/adminfinder' in wt:
				print('exploit > adminfinder')
				os.system('cd exploit;cd webtoolkit;php adminfinder.php')
			elif 'use exploit/traceroute' in wt:
				print('exploit > traceroute')
				os.system('cd exploit;cd webtoolkit;python traceroute.py')
			elif 'use exploit/reverse_dns' in wt:
				print('exploit > reverse_dns')
				os.system('cd exploit;cd webtoolkit;python reversedns.py')
			elif 'use exploit/findhost_dns' in wt:
				print('exploit > findhost_dns')
				os.system('cd exploit;cd webtoolkit;python findhostdns.py')
			elif 'use exploit/findshare_dns' in wt:
				print('exploit > findshare_dns')
				os.system('cd exploit;cd webtoolkit;python findsharedns.py')
			elif 'use exploit/dnslookup' in wt:
				print('exploit > dnslookup')
				os.system('cd exploit;cd webtoolkit;python dnslookup.py')
			elif 'use exploit/whoislookup' in wt:
				print('exploit > whoislookup')
				os.system('cd exploit;cd webtoolkit;python whoislookup.py')
			elif 'use exploit/iploclookup' in wt:
				print('exploit > iploclookup')
				os.system('cd exploit;cd webtoolkit;python iploclookup.py')
			elif 'use exploit/reiplookup' in wt:
				print('exploit > reiplookup')
				os.system('cd exploit;cd webtoolkit;python reiplookup.py')
			elif 'use exploit/sublookup' in wt:
				print('exploit > sublookup')
				os.system('cd exploit;cd webtoolkit;python sublookup.py')
			elif 'use exploit/tcpscan' in wt:
				print('exploit > tcpscan')
				os.system('cd exploit;cd webtoolkit;python tcpscan.py')
			elif 'use exploit/headercheck' in wt:
				print('exploit > headercheck')
				os.system('cd exploit;cd webtoolkit;python headercheck.py')
			else:
				corrupt()
		except KeyboardInterrupt:
			exit()

###################### SOCIAL BRUTE #####################
def socialbrute():
        while True:
                try:
                        sbm = input(w+'saydog('+r+'socialbrute'+w+') > ')
                        if sbm == 'help' in sbm:
                                print('')
                                print('SOCIAL BRUTE')
                                print('------------')
                                print('social media brute force')
                                print('')
                                print('command                                         description')
                                print('-------                                         -----------')
                                print('use exploit/instagram          bruteforce instagram account')
                                print('use exploit/facebook            bruteforce facebook account')
                                print('use exploit/gmail                  bruteforce gmail account')
                                print('create wordlist           wordlist generator for bruteforce')
                                print('')
                        elif  'clear' in sbm:
                                os.system('clear')
                        elif 'back' in sbm:
                                main()
                        elif 'use exploit/instagram' in sbm:
                                print('exploit > instagram')
                                os.system('cd exploit;cd socialbrute;python instabrute.py')
                        elif 'use exploit/facebook' in sbm:
                                print('exploit > facebook')
                                os.system('cd exploit;cd socialbrute;python facebrute.py')
                        elif 'create wordlist' in sbm:
                                os.system('cd exploit;cd socialbrute;python wordlist.py')
                        elif 'use exploit/gmail' in sbm:
                                print('exploit > gmail')
                                os.system('cd exploit;cd socialbrute;python gmailbrute.py')
                        elif 'exit' in sbm:
                                exit()
                        else:
                                corrupt()
                except KeyboardInterrupt:
                        exit()
      
######################## PYTOOLKIT ######################
def pytoolkit():
        while True:
                try:
                        pyt = input(w+'saydog('+r+'pytoolkit'+w+') > ')
                        if pyt == 'help' in pyt:
                                print('')
                                print('PYTOOLKIT')
                                print('---------')
                                print('Python hacking toolkit')
                                print('')
                                print('command                                         description')
                                print('-------                                         -----------')
                                print('use exploit/portscanner                        port scanner')
                                print('use exploit/bannergrabber                   grabbing banner')
                                print('use exploit/filegrabber               grabbing victim files')
                                print('use exploit/minicrypto                    mini cryptolocker')
                                print('use exploit/terabyte                 auto copying files 1TB')
                                print('')
                        elif  'clear' in pyt:
                                os.system('clear')
                        elif 'back' in pyt:
                                main()
                        elif 'use exploit/portscanner' in pyt:
                                print('exploit > portscanner')
                                os.system('cd exploit;cd pytoolkit;python PortScanner.py')
                        elif 'use exploit/bannergrabber' in pyt:
                                print('exploit > bannergrabber')
                                os.system('cd exploit;cd pytoolkit;python BannerGrabber.py')
                        elif 'use exploit/filegrabber' in pyt:
                                print('exploit > filegrabber')
                                os.system('cd exploit;cd pytoolkit;python filegrabber.py')
                        elif 'use exploit/minicrypto' in pyt:
                                print('exploit > minicrypto')
                                os.system('cd exploit;cd pytoolkit;python mini-crypto.py')
                        elif 'use exploit/terabyte' in pyt:
                                print('exploit > terabyte')
                                os.system('cd exploit;cd pytoolkit;python terabyte.py')
                        elif 'exit' in pyt:
                                exit()
                        else:
                                corrupt()
                except KeyboardInterrupt:
                        exit()

######################## MAIN MENU ######################

def mainmenu():
        randomlogo()
        sprint(banner)
        print('')
        main()

def main():
        while True:
                try:
                        dog = input( w+u+'saydog'+w+' > ')
                        if dog == 'help':
                                help()
                        elif dog == 'clear':
                                os.system('clear')
                        elif dog == 'banner':
                                mainmenu()
                        elif dog == 'exit' or dog == 'Exit':
                                exit()
                        elif dog == '?' or dog == 'auth' or dog == 'author':
                                gitlogo()
                        elif dog == 'use img2ascii':
                                img2ascii()
                        elif dog == 'use text2ascii':
                                text2ascii()
                        elif dog == 'use socialbrute':
                                socialbrute()
                        elif dog == 'use webtoolkit':
                                webtoolkit()
                        elif dog == 'use pytoolkit':
                                pytoolkit()
                        elif dog == 'use malware':
                                malware()
                        elif dog == 'use installer':
                                installer()
                        elif dog == 'other' or dog == 'others':
                                other()
                except KeyboardInterrupt:
                        exit()
if __name__ == "__main__":
        mainmenu()
