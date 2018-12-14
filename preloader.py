import csv
def csvloader(path):
	f=open(path,'r')
	csvreader=csv.reader(f)
	return list(csvreader)[1:] #leave out header

def precluster(path):
	data=csvloader(path)
	res={}
	for i in range(len(data)):
		code=data[i][4][data[i][4].find("("):data[i][4].find(")")]
		if code not in res:
			res[code]=[]
		res[code].append(data[i])
	return res
