import random
def name(len,seed):
	sa=[]
	for i in range(len):
		sa.append(random.choice(seed))
	salt="".join(sa)
	return salt

def randdel(x):
	x=str(x)
	len_x=len(x)
	pos=random.randint(0,len_x-1)
	x=x[0:pos]+x[pos+1:len_x]
	return x

seed = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sex=['F','f','female','male','M','m']
seed2='1234567890'
seed3=['086','010','110','22','33','44','55','66','77','88']
seed4="1234567890"+seed
N=20000
R=5
data=[["" for x in range(10)] for x in range(N)]
data_rep=[[""] for x in range((R-1)*N)]
for i in range(N):
	data[i][0]=name(8,seed)
	data[i][1]=random.randint(18,28)
	data[i][2]=random.choice(sex)
	data[i][3]=name(10,seed2)
	data[i][4]="("+random.choice(seed3)+")"+name(11,seed2)
	data[i][5]=name(5,seed)
	data[i][6]=name(15,seed4)
	data[i][7]=name(30,seed)
	data[i][8]=name(30,seed)
	data[i][9]=random.randint(0,1)
	for j in range(R-1):
		data_rep[4*i+j]=list(data[i])
		data_rep[4*i+j][0]+=random.choice(seed)
		for x in range(5,10):
			data_rep[4*i+j][x]=randdel(data_rep[4*i+j][x])
data_all=data+data_rep

f=open('data_large.csv','w')
f.write("name,age,sex,id,phone,city,e-mail,like,dislike,state\n")
for i in range(len(data_all)):
	f.write(",".join([str(item) for item in data_all[i]])+"\n")
f.close()
