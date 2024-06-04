def WriteASCII(data,file):
	fs = eval(open("filesystem.fs","r").read())
	try:
		fs.update({file: data})
	except:
		fs[file] = data
	with open("filesystem.fs","w") as f:
		f.write(str(fs.copy()))
def WriteBINARY(bin,file):
	fs = eval(open("filesystem.fs","r").read())
	fs.update({file: bin})
	with open("filesystem.fs","wb") as f:
		f.write(fs.copy())
def AppendASCII(data,file):
	fs = eval(open("filesystem.fs","r").read())
	try:
		fs.update({file: str(fs.get(file)+data)})
	except:
		fs[file] = data
	with open("filesystem.fs","w") as f:
		f.write(str(fs.copy()))
def AppendBINARY(bin,file):
	fs = eval(open("filesystem.fs","r").read())
	fs.update({file: str(fs.get(file)+bin)})
	with open("filesystem.fs","w") as f:
		f.write(fs.copy())
