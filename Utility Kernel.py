from Functions import printingSystem, Logger, mathHandler, readFiles, writeFiles, inputtingSystem
import threading, os
def echo(line,programName):
        argonly = line.split('print ', 1)[-1]
        try: printingSystem.Print(varsDictionary[argonly.split('$', 1)[1]],programName=programName)
        except: printingSystem.Print(argonly,programName=programName)
def exec2(line,programName):
    exec(line)
    Logger.LOG(text="Executed Line: "+line, user=programName)
varsDictionary = {}

print=printingSystem.Print

class Process:
    def __init__(self, name, execCode, version, priority=1):
        self.name = name
        self.execCode = execCode
        self.priority = priority
        self.version = version

    def printIdentity(self):
        printingSystem.Print(f"\n----------------------------------------------\n Name: {self.name}\n Priority: {self.priority}\n Version: {self.version}\n----------------------------------------------")

class System:
    def __init__(self, name, version):
        self.name = name
        self.version = version
    def run(self, processes):
        process_queue = sorted(processes, key=lambda p: (p.priority == "System", p.priority))
        for process in process_queue:
            if process.priority == "System":
                process.printIdentity()
                threading.Thread(target=RunCode, args=(process,)).start()
            else:
                process.printIdentity()
                RunCode(process)
def RunCode(process):
        for line in process.execCode:
            line = line.lower()
            try:
                result = mathHandler.safe_eval(line)
                if result is not "None":
                    printingSystem.Print(result, programName=process.name)
                    continue
            except: pass
            if "=" in line:
                key, value = line.split("=", 1)
                varsDictionary[key.strip()] = value.strip()
                printingSystem.Print(f"{key.strip()} = {value.strip()}", programName=process.name)
            elif line.startswith("print"): echo(line,process.name)
            elif line.startswith("promptuser"):
                inputted = inputtingSystem.__init__("")
                try: exec2(inputted,process.name+"[USER INPUT]")
                except: printingSystem.Print(f"The command [{inputted}] done an illegal operation and was shut down.\n Reinstalling this feature may help.", programName=process.name)
            elif line.startswith("writefile"): writeFiles.WriteASCII(line.split(" ",2)[2],line.split(" ",2)[1])
            elif line.startswith("readfile"): readFiles.readfile(line.split(" ",1)[1])
            elif line.startswith("sayvars"): printingSystem.Print(str(varsDictionary), programName=process.name)
            else: printingSystem.Print(f"The command [{line}] done an illegal operation and was shut down.\n Reinstalling this feature may help.", programName=process.name)

kernelStart = System("Utility Kernel", "3dv")
box = []
for file in os.listdir("Programs"):
    processcube=Process(file,open("Programs"+os.sep+file).read().split("\n"),1,1)
    box.append(processcube)
    printingSystem.Print(file)
kernelStart.run(processes=box)
