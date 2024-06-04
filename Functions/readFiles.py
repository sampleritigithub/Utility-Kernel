def readfile(file): 
    fs = eval(open("filesystem.fs","r").read())
    return fs.get(file)
