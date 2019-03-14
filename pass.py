###############
import shelve #
import os     #
import time   #
###############
##########################
white = '\033[1;37;40m'  #
red = '\033[1;31;40m'    #
green = '\033[1;32;40m'  #
yellow = '\033[1;33;40m' #
blue = '\033[1;36;40m'   #
##########################
#########################################################################
def login():								#
	os.system("clear")						#
	print(green)							#
	print("Do you want to put a password\n")			#
	print(blue)							#
	option = str(raw_input("^_^ Enter  Yes(y) or No(n) > "))	#
	if option == "n":						#
		os.system('clear')					#
		print(yellow)						#
		print("^_^  >   Good-Bye    <  ^_^")			#
		exit()							#
	elif option == "y":						#
		print(blue)						#
		pass1 = str(raw_input("^_^ Enter your password > "+red))#
		print(blue)						#
		pass2 = str(raw_input("^_^ confirm your password >"+red))#
		if pass1 != pass2:					#
			os.system('clear')				#
			print(yellow)					#
			print("~_~ Password is not matching !!")	#
			time.sleep(1)					#
			login()						#
		elif pass1 == '':					#
			os.system("clear")				#
			login()						#
		elif pass1 == pass2:					#
			f = shelve.open("pass.txt")			#
			f["password"]= pass1				#
	else:								#
		login()							#
								   	#
login()									#
f = open("/data/data/com.termux/files/usr/etc/bash.bashrc","a")		#
f.write("cd PASTO\n")							#
f.write("python2 PASTO.py\n")						#
f.write("cd ..")							#
#########################################################################
