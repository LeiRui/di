from preloader import precluster

from sim import sim,logistic_sim,sim_only_name,sim_simple

from sklearn import cluster

from output import output

data_large=precluster('data_large.csv')

cluster_number={ x:2000 for x in data_large}

labels_all=[]

pre_n=0

for loc in data_large:

	data=data_large[loc]

	num_size=len(data)

	#num_attr=len(data[0])

	matrix=[[0 for x in range(num_size)] for x in range(num_size)]

	for i in range(num_size):

		for j in range(num_size):

			matrix[i][j]=1-sim_simple(data[i],data[j])

#		print(matrix[i])

	sk=cluster.AgglomerativeClustering(cluster_number[loc],affinity='precomputed',linkage='single')

	labels=sk.fit_predict(matrix)

	#print(labels)

	labels_all += [pre_n+k for k in labels]

	pre_n=cluster_number[loc]

output(labels_all,sum(cluster_number.values()))
