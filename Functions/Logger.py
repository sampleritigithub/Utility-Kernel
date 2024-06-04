from Functions import printingSystem
from Functions import writeFiles
from Functions import timeSignature
def LOG(level="INFO", text="logger called",user="defaultKernelBody"):
    printingSystem.Print(f"Logger Called [by {user}] -- Data: {text} -- {level} level",color="GREEN",programName="kernel.Logger")
    writeFiles.AppendASCII(f"[{user} {timeSignature.Signature()}] {level}: {text} | end |      ",f"{user}.log")
