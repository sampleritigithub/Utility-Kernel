varsDictionary={}
class Logger:
    import sys
    def __init__(self,file=False,output=sys.stdout):
        self.file=file
        self.output = output
        import colorama as s
        self.s           = s
        self.MAGENTA     = s.Fore.MAGENTA
        self.RESET       = s.Fore.RESET
        self.YELLOW      = s.Fore.YELLOW
    def Log(self,data="Logger Called",user="sys.kernel",level="INFO"):
        if self.file:
            try:
                import time
                with open(self.file,"a") as file:file.write("\n"+time.strftime("%Y-%m-%d %I:%M:%S %p")+f" {user} | [{level}]: {data}")
            except Exception as e: print(RED+f"ERROR WHILE WRITING A LOG LINE! [{str(e)}]"+RESET)
        import time
        YELLOW = self.YELLOW
        MAGENTA = self.MAGENTA
        RESET = self.RESET
        RED = self.s.Fore.RED
        print(YELLOW+time.strftime("%Y-%m-%d %I:%M:%S %p")+f" {MAGENTA}{user} {RESET}| {MAGENTA}[{level}]: {data}{RESET}",file=self.output)
    def initLog(self):
        import socket,os
        hostName = socket.gethostname()
        Logger(file=os.path.join(os.getenv("APPDATA", "/appdata") + "\\..\\LocalLow\\osutil",hostName+".log")).Log("Starting System...")
        Logger(file=os.path.join(os.getenv("APPDATA", "/appdata") + "\\..\\LocalLow\\osutil",hostName+".log")).Log("Logger Initiated!")
class Library:
    def __init__(self):
        import platform
        self.user = self.getenv("USERNAME", "default_user")
        self.tmpdir = self.getenv("TMP", "/tmp")
        self.homedrv = self.getenv("HOMEDRIVE", "/")
        self.cpucores = self.getenv("NUMBER_OF_PROCESSORS", "1")
        self.cpugen = self.getenv("PROCESSOR_LEVEL", "unknown")
        self.root = self.getenv("SystemRoot", "/")
        self.ops = platform.system()
        self.arc = self.getenv("PROCESSOR_ARCHITECTURE", "unknown")
        self.usrprofile = self.getenv('USERPROFILE', "/home/user")
        self.osutildir = self.getenv("APPDATA", "/appdata") + "\\..\\LocalLow\\osutil"
        import socket;self.logfile = f"{self.osutildir}\\{socket.gethostname()}.txt"
        import psutil;self.batteryf = psutil.sensors_battery()
        self.battery = self.batteryf.percent if self.batteryf else "unknown"
        import socket;self.hostName = socket.gethostname()
        self.hostIP = socket.gethostbyname(self.hostName)
        import time;self.date = time.strftime('%B-%d-%Y %I:%M %p')
        self.userprofile = self.getenv('USERPROFILE', "/home/user")
        self.osn = self.getenv('OS', 'unknown')
        self.windir = self.getenv('WINDIR', 'unknown')
        self.processor = self.getenv('PROCESSOR_IDENTIFIER', 'unknown')
        self.architecture = self.getenv('PROCESSOR_ARCHITECTURE', 'unknown')
        self.processors = self.getenv('NUMBER_OF_PROCESSORS', '1')
        self.allsyspaths = self.getenv('Path', '')
        self.sysusrname = self.getenv('USERNAME', 'default_user')
        self.kernbuild = "Utility Kernel 0.4.0(2024.6 Kernel)"
        self.copyright = "Copyright(c) Tobey Enterprises 2024"
        self.pythoncopyright = "Copyright(c) Python Software Foundation"
        self.mscopyright = "Copyright(c) Microsoft Corporation 2006-2024"
        self.ntfourlogonsoundcopyright = "Copyright(c) Microsoft Corporation"
        import os;self.logger = Logger(file=os.path.join(self.osutildir,self.hostName+".log")).Log
        import sys;self.emergencyLogger = Logger(file=os.path.join(self.osutildir,self.hostName+".log"),output=sys.stderr).Log
    def getenv(self, *vars):
        bin = []
        for var in vars:
            try:import subprocess;bin.append(subprocess.getoutput("set "+var).split("=",1)[1])
            except: pass
        return bin[0]
    def populate_vars_dictionary(self, dictionary):dictionary.update(self.__dict__)
Library().populate_vars_dictionary(varsDictionary)
class System:
    def __init__(self):pass
    def Start(self):
        try:
            import threading,os,keyboard
            keyboard.send("F11")
            threading.Thread(target=self.LoggerPipeStart)              .start()
            threading.Thread(target=self.SystemPipeStart)              .start()
            threading.Thread(target=self._3dvHandle)                   .start()
            threading.Thread(target=self.LaunchAnything)               .start()
            threading.Thread(target=self.CyberTerminal1)               .start()
            threading.Thread(target=os.system,args=("commission.exe",)).start()
        except:self.LockDown()
    def SystemPipeStart(self):
        import socket
        s = socket.socket()
        s.bind(("localhost",9150))
        s.listen()
        while True:
            import subprocess
            conn,addr = s.accept()
            todo = conn.recv(1024).decode()
            toSend = subprocess.getoutput(todo).encode()
            conn.send(toSend)
            conn.close()
    def LoggerPipeStart(self):
        import socket
        s = socket.socket()
        s.bind(("localhost",9200))
        s.listen()
        while True:
            import subprocess
            conn,addr = s.accept()
            todo = conn.recv(1024).decode()
            varsDictionary["logger"](data = todo,user = str(addr))
            toSend = "1".encode()
            conn.send(toSend)
            conn.close()
    def WriteASCII(self,data,file):
        fs = eval(open("filesystem.fs","r").read())
        try:
            fs.update({file: data})
        except:
            fs[file] = data
        with open("filesystem.fs","w") as f:
            f.write(str(fs.copy()))
    def WriteBINARY(self,bin,file):
        fs = eval(open("filesystem.fs","r").read())
        fs.update({file: bin})
        with open("filesystem.fs","wb") as f:
            f.write(fs.copy())
    def AppendASCII(self,data,file):
        fs = eval(open("filesystem.fs","r").read())
        try:
            fs.update({file: str(fs.get(file)+data)})
        except:
            fs[file] = data
        with open("filesystem.fs","w") as f:
            f.write(str(fs.copy()))
    def AppendBINARY(self,bin,file):
        fs = eval(open("filesystem.fs","r").read())
        fs.update({file: str(fs.get(file)+bin)})
        with open("filesystem.fs","w") as f:
            f.write(fs.copy())
    def echo(self,line):
                try:
                    argonly = line.split('print ', 1)[-1]
                    try: return varsDictionary[argonly.split('$', 1)[1]]
                    except: return argonly
                except:
                    try:
                        argonly = line.split('echo ', 1)[-1]
                        try: return varsDictionary[argonly.split('$', 1)[1]]
                        except: return argonly
                    except:pass
    def CyberTerminal1(self):
        import socket
        s = socket.socket()
        s.bind(("localhost",9000))
        s.listen()
        while True:
            try:
                conn,addr=s.accept()
                code = conn.recv(1024).decode()
                message = []
                import os,platform,subprocess,time
                if code == 'ping':
                    host = code.split(" ",2)[1]
                    number = code.split(" ",2)[2]
                    def ping(host):
                        param = '-n' if platform.system().lower() == 'windows' else '-c'
                        command = ['ping', param, number, host]
                        return subprocess.call(command)
                    message.append(ping(host))
                if code == 'local':
                    message.append("Your Local IPS Is: " + varsDictionary["hostIP"])
                    message.append("Your Desktop Name Is: " + varsDictionary["hostName"])
                if code == 'date':message.append("The Local Date Is: " + time.strftime("%m/%d/%Y"))
                if code == 'list':
                    dir_list = os.listdir()
                    message.append("Files and Directories in '", os.getcwd(), "' :")
                    message.append(dir_list)
                if code == 'list -a':
                    file = code.split(" ")[1]
                    dir_list2 = os.listdir(file)
                    message.append("Files and directories in '", file, "':")
                    message.append(dir_list2)
                if code == 'echo_me':message.append(code.split(" ",1)[1])
                bin = ""
                for object in message:bin+=object+" _ "
                sendto = bin.encode()
                conn.send(sendto)
                conn.close
            except:pass
    def LaunchAnything(self):
        import socket
        s = socket.socket()
        s.bind(("localhost",9050))
        s.listen()
        while True:
            try:
                conn,addr = s.accept()
                message = []
                opt = conn.recv(1024).decode()
                import os
                if opt == "27":import os;os.system("cls");return True
                if opt == "31":
                    import socket;message.append(socket.gethostname()+ " " + socket.gethostbyname(socket.gethostname()))          
                if opt == "1":
                        try:
                            run = opt.split(" ")[1]
                            os.startfile(run)
                        except FileNotFoundError:
                            message.append("Invalid File!")
                        except OSError:
                            message.append("Invalid win32 user mode executable!")
                if opt == "29":
                    import webbrowser
                    webbrowser.open("youtube.com")
                    return True
                if opt == "30":
                    import webbrowser
                    webbrowser.open("bing.com")
                    return True      
                
                if opt == "2":
                        filew = opt.split(" ")[1]
                        os.system("python3 " + filew)

                if opt == "3":
                        filewa = opt.split(" ")[1]
                        os.system("python" + filewa)

                if opt == "4":
                        filewan = opt.split(" ")[1]
                        os.system("python" + filewan)      

                if opt == "9":
                        os.system("pip install pyinstaller")
                if opt == "14":
                        out = opt.split(" ")[1]
                        os.system("color " + out + "0")
                if opt == "24":
                        ping = opt.split(" ")[1]
                        os.system("ping " + ping)

                if opt == "25":
                        import webbrowser
                        web = opt.split(" ")[1]
                        webbrowser.open(web)

                if opt == "26":
                    import requests
                    try:
                        ip = opt.split(" ")[1]
                        url = f"https://ipinfo.io/{ip}?token=89eb984d917dd5"
                        response = requests.get(url).json()
                        message.append("IP:", response['ip'])
                        message.append("\n")
                        message.append("ADDRESS:")
                        message.append("Country Code:", response['country'])
                        message.append("Region Name:", response['region'])
                        message.append("City:", response['city'])
                        message.append("\n")
                        message.append("POSTAL/TIMEZONE:")
                        message.append("Postal Code:", response['postal'])
                        message.append("Timezone:", response['timezone'])
                        message.append("\n")
                        message.append("LAT/LONG")
                        message.append("Location:", response['loc'])
                    except KeyError:
                        message.append("Invalid IP Address")
                if opt == "13":
                        os.system("cmd")
                if opt == "16":
                        title = opt.split(" ")[1]
                        os.system("title " + title)
                if opt == "15":
                        coc = opt.split(" ")[1]
                        os.system("color " + coc)

                if opt == "17":
                        os.startfile("Notepad")

                if opt == "18":
                        os.startfile("explorer")

                if opt == "19":
                        os.startfile("write")

                if opt == "20":
                        os.startfile("winver")

                if opt == "21":
                        os.startfile("REGEDIT")

                if opt == "22":
                        os.startfile("taskmgr")
                if opt == "23":
                        kill = opt.split(" ")[1]
                        os.system("taskkill /IM " + kill)
                bin = ""
                for object in message:bin+=object+" _ "
                sendto = bin.encode()
                conn.send(sendto)
                conn.close
            except:pass
    def exec(self,command):
        command = command.split("\n")[0]
        do = True
        formerDict = varsDictionary
        if do: exec(command)
        varsDictionary = formerDict
    def _3dvHandle(self):
            import socket
            s = socket.socket()
            s.bind(("localhost",9100))
            s.listen()
            while True:
                conn,addr = s.accept()
                command = conn.recv(1024).decode()
                line=command
                message = []
                try:
                    result = eval(line)
                    if result is not None:
                        message.append(result)
                        pass
                        return True
                except: pass
                if "=" in line:
                    key, value = line.split("=", 1)
                    libDic = {}
                    Library().populate_vars_dictionary(libDic)
                    if key not in libDic:
                        varsDictionary[key.strip()] = value.strip()
                        message.append(f"{key.strip()} = {value.strip()}")
                    #elif key in libDic and priority.lower()=="system":
                    #    varsDictionary[key.strip()] = value.strip()
                    #    message.append(f"{key.strip()} = {value.strip()}")                       
                    else:message.append(f"Authority is not justified for editing {key.strip()}")

                elif line.startswith("print"): message.append(self.echo(line))
                elif line.startswith("prompt"):
                    try:
                        inputted = line.split(" ",1)[1]
                        try: message.append(eval(inputted))
                        except: message.append(f"The command [{inputted}] done an illegal operation and was shut down.\n Reinstalling this feature may help.")
                    except:pass
                elif line.startswith("writefile"): 
                   try:self.WriteASCII(line.split(" ",2)[2],line.split(" ",2)[1])
                   except:pass
                elif line.startswith("readfile"): 
                    try:message.append(self.readfile(line.split(" ",1)[1]))
                    except:pass
                    
                elif line.startswith("sayvars"): message.append(str(varsDictionary))
                else: pass
                bin = ""
                for object in message:bin+=str(object)+" _ "
                sendto = bin.encode()
                conn.send(sendto)
                conn.close
                
    def LockDown(self):
        while True: 
            try:self._3dvHandle(input(" >> "),1)
            except:continue
system = System()
system.Start()