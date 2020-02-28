import os,sys,time
from time import *

r='\x1b[00m\x1b[91m'
g='\x1b[00m\x1b[32m'
y='\x1b[00m\x1b[33m'
c='\x1b[00m\x1b[36m'
w='\x1b[00m'
u='\033[4m'
b='\033[5m'

def sprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 100)
  
def exit():
	printr+('[!]'+w+' The user forces it to stop')
	print(r+'[!]'+w+' Exiting tool')
	sys.exit(1)

def dhelp():
		print('')
		print('command                                     example')
		print('-------                                     -------')
		print('set image [path/name]    set image /sdcard/logo.jpg')
		print('set output [path]                set output /sdcard')
		print('run, go, create                              create')
		print('')
def corrupt():
	print(r+'[?]'+w+' Command not found, please type help')

def default_main():
	global name
	global output
	while True:
		try:
			dm = input(w+'saydog('+r+'img2ascii/invert'+w+') > '+w)
			if dm == 'help':
				dhelp()
			elif dm == 'back':
				sys.exit(0)
			elif dm == 'clear':
				os.system('clear')
			elif 'exit' in dm:
				exit()
			elif 'set image' in dm:
				name = dm.split()[(-1)]
				print('image > '+name)
			elif 'set output' in dm:
				output = dm.split()[(-1)]
				print('output > '+output)
			elif dm == 'create' or dm  =='run' or dm == 'go':
				os.system('jp2a -i '+name+' > '+name+'.txt;cat '+name+'.txt > '+output+'/ASCII-IMAGES.txt;rm '+name+'.txt;jp2a -i '+name)
			else:
				corrupt()
		except NameError:
			print(r+'[!] Error:'+w+' [path name] or [output] not found')
		
default_main()