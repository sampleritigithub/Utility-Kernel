varsDictionary = {}
class Library:
    def __init__(self):
        import os,time,psutil,socket,platform,ipinfo,cpuinfo
        self.act = "013916e7012dd7"
        try: 
            handler = ipinfo.getHandler(self.act)
            details=handler.getDetails()
            self.city = details.city
            self.location = details.loc
            self.country = details.country_name
            self.latitude = details.latitude
            self.longitude = details.longitude
            self.zip = details.postal
            self.region = details.region
            self.timezone = details.timezone
            self.allIPinfo = str(details.all)
        except: pass
        self.processorBN = cpuinfo.get_cpu_info()["brand_raw"]
        self.user = os.getenv("USERNAME", "default_user").replace('\\', '/')
        self.tmpdir = os.getenv("TMP", "/tmp").replace('\\', '/')
        self.homedrv = os.getenv("HOMEDRIVE", "/").replace('\\', '/')
        self.cpucores = os.getenv("NUMBER_OF_PROCESSORS", "1").replace('\\', '/')
        self.cpugen = os.getenv("PROCESSOR_LEVEL", "unknown").replace('\\', '/')
        self.root = os.getenv("SystemRoot", "/").replace('\\', '/')
        self.ops = platform.system().replace('\\', '/')
        self.arc = os.getenv("PROCESSOR_ARCHITECTURE", "unknown").replace('\\', '/')
        self.usrprofile = os.getenv('USERPROFILE', "/home/user").replace('\\', '/')
        self.osutildir = os.getenv("APPDATA", "/appdata").replace('\\', '/') + "/../LocalLow/osutil"
        #self.logfile = f"{self.osutildir}/{socket.gethostname()}.txt".replace('\\', '/')
        self.batteryf = "outdated"
        self.battery = psutil.sensors_battery().percent if psutil.sensors_battery() else "unknown"
        self.hostName = socket.gethostname()
        self.hostIP = socket.gethostbyname(self.hostName)
        self.date = time.strftime('%B-%d-%Y %I:%M %p')
        self.userprofile = os.getenv('USERPROFILE', "/home/user").replace('\\', '/')
        self.osn = os.getenv('OS', 'unknown').replace('\\', '/')
        self.windir = os.getenv('WINDIR', 'unknown').replace('\\', '/')
        self.processor = os.getenv('PROCESSOR_IDENTIFIER', 'unknown').replace('\\', '/')
        self.architecture = os.getenv('PROCESSOR_ARCHITECTURE', 'unknown').replace('\\', '/')
        self.processors = os.getenv('NUMBER_OF_PROCESSORS', '1').replace('\\', '/')
        self.allsyspaths = os.getenv('Path', '').replace('\\', '/')
        self.sysusrname = os.getenv('USERNAME', 'default_user').replace('\\', '/')
        self.kernbuild = "Utility Kernel 5 Alpha"
        self.copyright = "Copyright(c) Tobey Enterprises"
        self.pythoncopyright = "Copyright(c) Python Software Foundation"
        self.mscopyright = "Copyright(c) Microsoft Corporation"
        self.ntfourlogonsoundcopyright = "Copyright(c) Microsoft Corporation"
        self.shellbuild = "undefined"
    def env(self, var):
        try:
            import os
            return os.environ[var]
        except KeyError as e:
            print("The command done an illegal operation and was shut down." + str(e))
            return None

    def populate_vars_dictionary(self, dictionary):
        dictionary.update(self.__dict__)
orLib = Library()
libd = {}
Library().populate_vars_dictionary(libd)
class NetworkChannel:
    def __init__(self,channel):
        import socket
        self.socket = socket.socket()
        self.channel = channel
    def host(self,todo,executive=False,warn=False):
        self.socket.bind(("localhost",int(self.channel)))
        self.socket.listen()
        import platform
        import cpuinfo
        garbage=str(cpuinfo.get_cpu_info()['brand_raw'])+platform.system()+str(platform.architecture())+platform.processor()+platform.node()+platform.release()
        def threader():
            while True:
                conn,addr = self.socket.accept()
                recv = conn.recv(65536).decode()
                print(type(addr))
                rec = recv
                if warn: 
                    #if input("An outside source is trying to access the core Utility Kernel, do you approve? (Y/N): ").lower() == "y":
                        if executive:
                            exec(todo)
                            tosend="Success!"
                        else:tosend=str(eval(todo))
                        if str(type(tosend))=="<class 'NoneType'>":tosend="Success!"
                        print(tosend)
                        conn.send(tosend.encode())
                    #else: print("Rejected")
                else:
                        if executive:
                            exec(todo)
                            tosend="Success!"
                        else:tosend=str(eval(todo))
                        if str(type(tosend))=="<class 'NoneType'>":tosend="Success!"
                        conn.send(tosend.encode())
                conn.close()
        import threading
        threading.Thread(target=threader).start()
def parser(detail):
    if len(detail.split(" ")) > 1:cmd = detail.split(" ",1)[0];token=detail.split(" ",1)[1]
    else: token = "";cmd = detail
    return [cmd,token]
def nspacers(cmdg,sec="High"):
    try:
        sptd = cmdg.split("-",1)
        if len(sptd) == 1:return "This command is not able to be processed as it does not support the Utility Scripting System (Version 5) Syntax [ERROR: Nspace object cannot be splitted by '-'].\nRECOMMENDATION: If you want to run via compatibility mode, say: 'Run-CompatibleSystem [your code]'."
        if sptd[0] == "":return "This command is not able to be processed as it does not support the Utility Scripting System (Version 5) Syntax [ERROR: Nspace object is empty].\nRECOMMENDATION: Never leave an empty line in any of your scripts."
        cmdFamily,rest = sptd
        cmdFamily = cmdFamily.lower()
        if cmdFamily == "get":
            try: return str(libd[rest])
            except: 
                try: return str(varsDictionary[rest])
                except: return "This command is not able to be processed [ERROR: Nspace object is trying to get a library (or variable???) object value although the object key is not available].\nRECOMMENDATION: Always try to get a known object-key value."
        elif cmdFamily == "breaknsi": return f"This command is not able to be processed [{rest}].\nRECOMMENDATION: Not available."
        elif cmdFamily == "breakwsi":return f"This command is not able to be processed as it does not support the Utility Scripting System (Version 5) Syntax [{rest}].\nRECOMMENDATION: Not available."
        elif cmdFamily == "callpowermanagement": 
            if not sec == "High": return "THIS OPERATION NEEDS HIGHER PRIVILEGES!"
            rfopm = rest.lower()
            if rfopm == "shutdown": import os; os.system("shutdown /s -t 0");return "System shutdown in progress."
            elif rfopm == "restart":import os; os.system("shutdown /r -t 0");return "System restart in progress."
            elif rfopm == "restartToFirmware":import os; os.system("shutdown /r /fw -t 0");return "System restart (to firmware UI) in progress."
            else: return "Call is incompatible."
        elif cmdg.lower() =="do-input": 
            returner = interpreter(interpreter("sget-input UTIL5")).split("\n")[0]
            if returner == "Loop exit command given": returner = "Loop exit command given"
            return returner
        elif cmdFamily == "show":
            if not sec == "High": return "THIS OPERATION NEEDS HIGHER PRIVILEGES!"
            if rest.lower() != "log": return "Call is incompatible."
            return "not implemented" #open(libd["osutildir"]+"/"+libd["hostName"]+".txt","r").read()
        elif cmdFamily == "exit":return "Loop exit command given"
        else: return "Call is incompatible."
    except Exception as e: return f"This command is not able to be processed [ERROR: Internal error occured. PYTHON ERROR: {str(e)}].\nRECOMMENDATION: Not available."
def handle(thingy):
    b = []
    for block in thingy.split(" "):
        if block.startswith("!!"):b.append(nspacers(block.strip("!!")))
        else:b.append(block)
    strt = ""
    for thing in b:strt+=str(thing)+" "
    return strt[0:len(strt)-1]
def interpreter(things):
    try:
        cbin = []
        for line in things.split("\n"):
            cmd2, token = parser(line)
            token = handle(token)
            cmd = cmd2.lower()
            if token == "":cbin.append(nspacers(cmd))
            if cmd == "create-netpipe": 
                if len(token.split(" ")) > 0: tst = token.split(" ",1)[1];NetworkChannel(int(token.split(" ",1)[0])).host(todo=f"interpreter(f'{tst}')");cbin.append("NetPipe created")
                else: cbin.append("This command is not able to be processed as it does not support the Utility Scripting System (Version 5) Syntax [ERROR: Object is not lengthy enough (spaces-wize) to make a NetPipe].\nRECOMMENDATION: Never leave a command with it having an insufficient amount of spaces.")
            elif cmd == "open-netpipe":
                if len(token.split(" ")) > 1:pass
                else: cbin.append("This command is not able to be processed as it does not support the Utility Scripting System (Version 5) Syntax [ERROR: Object is not lengthy enough (spaces-wize) to open a NetPipe].\nRECOMMENDATION: Never leave a command with it having an insufficient amount of spaces.");continue
                import socket
                sock =socket.socket()
                sock.connect(("localhost",int(token.split(" ",2)[0])))
                sock.send(token.split(" ",2)[1].encode())
                recv = sock.recv(65536).decode()
                t2 = token.split(" ",2)[2]
                sock.send(eval(f"interpreter(f'{t2}')").encode())
                cbin.append("NetPipe opened")   
            elif cmd =="closed-nspaceinterpret": cbin.append(nspacers(cmdg=token,sec="Low"))
            elif cmd =="assign-variable": 
                if len(token.split(" ")) > 0: varsDictionary[token.split(" ",1)[0]]=token.split(" ",1)[1];cbin.append("Variable created")
                else: cbin.append("This command is not able to be processed as it does not support the Utility Scripting System (Version 5) Syntax [ERROR: Object is not lengthy enough (spaces-wize) to make a variable].\nRECOMMENDATION: Never leave a command with it having an insufficient amount of spaces.")
            elif cmd =="output-givendata":ttp = token;print(ttp);cbin.append(ttp)
            elif cmd =="sget-input": cbin.append(input(token+">> "))
            elif cmd =="always-do":
                while True: 
                    vft = token.split(" ",1)[0]
                    varsDictionary[f"loop{vft}State"]="True"
                    t = nspacers(token.split(" ",1)[1])
                    if t == "Loop exit command given": loopName=token.split(" ",1)[0];varsDictionary["loop"+loopName+"State"]="False";break
            else: cbin.append("Call is incompatible.")
        if len(cbin) == 1: return str(cbin[0])
        scbin=""
        for thingyp2 in cbin:scbin+=thingyp2+"\n"
        return scbin
    except KeyboardInterrupt: return "Not registered"
    except Exception as e: return f"This command is not able to be processed [ERROR: Internal error occured. Start error dump: {str(e)}].\nRECOMMENDATION: Not available."
interpreter(open(libd["osutildir"]+"/startup.util","r").read())
