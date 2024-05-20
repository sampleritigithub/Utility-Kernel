import os
import string
import customtkinter
from tkinter import PhotoImage, Label, Tk,StringVar
from newsapi import NewsApiClient
import requests
import psutil
import socket
import platform
from time import strftime, sleep
#------------------------------------------------------------#
# Variables                                                  #
#------------------------------------------------------------#
window = customtkinter.CTk()                                                                                                                                                      # Start the GUI
clock = strftime("%H:%M")                                                                                                                                                         # Clock (start)
aprint=print                                                                                                                                                                      # Saving the TUI Print system
def error(error="unknown"):                                                                                                                                                       # Error System
	ErrorWindow = Tk()                                                                                                                                                            # Error Box
	ErrorWindow.title("Error")                                                                                                                                                    # Error Box title
	Label(ErrorWindow, text="The command done an illegal operation and was shut down\nError: "+error, foreground="red", background="white").pack()                                # Error Text
customtkinter.set_appearance_mode("system")                                                                                                                                       # Appearance Mode
customtkinter.set_default_color_theme("dark-blue")                                                                                                                                # Default Color Theme
window.title("Utility Kernel version 3i")                                                                                                                                         # Program Title
tabManager = customtkinter.CTkTabview(master=window)                                                                                                                              # Tab system
newsapi = NewsApiClient(api_key='abe659631e574a9398be163a77cb3e89')                                                                                                               # News API Client
osn = os.environ['OS']                                                                                                                                                            # Type of OS (DOS, [NT] , or POSIX)
windir = os.environ['WINDIR']                                                                                                                                                     # Windows Directory
processor = os.environ['PROCESSOR_IDENTIFIER']                                                                                                                                    # Processor Type (Intel, AMD, or ARM)
architecture = os.environ['PROCESSOR_ARCHITECTURE']                                                                                                                               # Processor Bits (amd64, x86, ARM or arm64)
processors = os.environ['NUMBER_OF_PROCESSORS']                                                                                                                                   # Processor Cores
allsyspaths = os.environ['Path']                                                                                                                                                  # Default Windows Folders
sysusrname = os.environ['USERNAME']                                                                                                                                               # Current Windows Username
userprofile = os.environ ['USERPROFILE']                                                                                                                                          # Current Windows User Profile
tmpdir = os.environ["TMP"]                                                                                                                                                        # Windows Temporary Directory
homedrv = os.environ["HOMEDRIVE"]                                                                                                                                                 # Windows 'Main' Drive
cpugen = os.environ["PROCESSOR_LEVEL"]                                                                                                                                            # Processor Level
root = os.environ["SystemRoot"]                                                                                                                                                   # System Folder or Drive
ops = platform.system()                                                                                                                                                           # Operating System                                                                                                                                                 
kernbuild = "UTIL Kernel 3i (2024 Kernel)"                                                                                                                                        # Utility Kernel Build
copyright = "Copyright(c) Tobey Enterprises"                                                                                                                                      # Utility Kernel Copyright                                                                                                                                              
battery = psutil.sensors_battery().percent                                                                                                                                        # Battery Percentage
hostName = socket.gethostname()                                                                                                                                                   # Computer Name
hostIP = socket.gethostbyname(hostName)                                                                                                                                           # Computer IP Address
all_info = [sysusrname + "|" + hostName + '|' + hostIP + " " + userprofile + "|" + osn + "|" + windir + "|" + processor + "|" +  architecture + "|" + processors]                 # Important System Info
shellbuild = "?"                                                                                                                                                                  # Shellbuild (insert your own)
def print(text, master=window):
	label = customtkinter.CTkLabel(master=master, text=text)
	if master is window: label.pack(padx=20, pady=20, side=customtkinter.TOP)
	else: label.pack(padx=20, pady=20, side=customtkinter.LEFT)
def writeBINARY(bin, file):
  os.system(f'echo "">"{file}"')
  with open(file, "wb")as f: f.write(bin)
def writeASCII(cont, file):
  os.system(f'echo "">"{file}"')
  with open(file, "w")as f: f.write(cont) 
def log(logfile, info):
  try:
    with open(logfile, "a")as f: f.write("\n"+strftime("%H:%M")+"|"+info)
  except UnicodeError:
    with open(logfile, "ab")as f: f.write(bytes("\n", encoding = "ansi")+bytes(strftime("%H:%M"), encoding = "utf8")+bytes("|", encoding="utf8")+bytes(info, encoding = "utf8"))
  except UnicodeEncodeError:
    with open(logfile, "ab")as f: f.write(bytes("\n", encoding = "ansi")+bytes(strftime("%H:%M"), encoding = "utf8")+bytes("|", encoding="utf8")+bytes(info, encoding = "utf8"))
  except OSError:
  	print("--LOGFILE ERROR--\nOSError")
  except:
  	error(error="logfile error")
def TabInit(): tabManager.pack(padx=10,pady=10)
def Title(title): window.title("Utility Kernel version 3i -- "+title)
def AddTab(name): tabManager.add(name)
def SetTab(tab):  tabManager.set(tab)
def BackGround(pic, master):
	bg_image = PhotoImage(file=pic)
	background_label = CTkLabel(master=master, image=bg_image)
	background_label.pack(x=0, y=0, relwidth=1, relheight=1)
def cf(text): 
	bin = ""
	for char in text:
		if char in bin: continue
		else: bin+=char 
	return bin
def enCipher(text, password="Official Utility Kernel1773"):
	bin = ""
	for char in text: bin+=cf(password+string.ascii_letters)[string.ascii_letters.find(char)]
	return bin
def deCipher(text, password="Official Utility Kernel1773"):
	bin = ""
	for char in text: bin+=string.ascii_letters[cf(password+string.ascii_letters).find(char)]
	return bin
def TopHeadLines(query, sources):
    try:
        headlines = newsapi.get_top_headlines(
            q=query,
            sources=sources
        )
        return headlines
    except:
        error()
def env(var):
  try:
    vari = os.system(f'set "{var}"')
    return vari
  except OSError: error("OSError","env()")

window.mainloop()