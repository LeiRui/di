#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

class Levenshtein:
	def edit_distance(x,y):
		rows=len(x)+1
		cols=len(y)+1
		dist=[[0 for x in range(cols)] for x in range(rows)]
		for i in range(cols):
			dist[0][i]=i
		for i in range(rows):
			dist[i][0]=i
		for i in range(1,rows):
			for j in range(1,cols):
				if(x[i-1]==y[j-1]):
					cost=0
				else:
					cost=1
				dist[i][j]=min(dist[i-1][j-1]+cost, dist[i][j-1]+1, dist[i-1][j]+1)
#		for i in range(rows):
#			print(dist[i])
		return dist[rows-1][cols-1]
	
	def edit_sim(x,y):
		if len(x)==0 and len(y)==0:
			return 1
		else:
			return 1-Levenshtein.edit_distance(x,y)/max(len(x),len(y))

	def Jaro(x,y):
		len_x=len(x)
		len_y=len(y)
		if len_x==0 and len_y==0:
			return 1

		margin=min(len_x,len_y)//2
		march_x=[False for x in range(len_x)]
		march_y=[False for x in range(len_y)]
		march=0
		for i in range(len_x):
			low=max(0,i-margin)
			high=min(len_y,i+margin+1)
			for j in range(low,high):
				if(march_y[j]!=True and (x[i]==y[j])):
					march_y[j]=True
					march_x[i]=True
					march += 1
					break	
		if(march==0):
			return 0

		transposition=0
		k=0
		for i in range(len_x):
			if(not march_x[i]):
				continue #good
			while(not march_y[k]):
				k+=1
			if(x[i]!=y[k]):
				transposition+=1
			k+=1

		return (march/len_x+march/len_y+(march-transposition/2)/march)/3

	def Jaro_Winkler(x,y):
		PW=0.1
		PL=0
		Len=min(len(x),len(y))
		for i in range(Len):
			if(PL==4):
				break
			if(x[i]!=y[i]):
				break
			PL+=1
		return PL*PW+(1-PL*PW)*Levenshtein.Jaro(x,y)

	def Affine_gap(x,y):
		"suppose gap opening pushnishment -1 continuing -0.5, mismatch -1, match +2"
		co=-1
		cr=-0.5
		cmatch=1
		cmis=-1

		rows=len(x)+1
		cols=len(y)+1
		M=[[0 for x in range(cols)] for x in range(rows)]
		Ix=[[0 for x in range(cols)] for x in range(rows)]
		Iy=[[0 for x in range(cols)] for x in range(rows)]
		for i in range(cols):
			M[0][i]=-i
			Ix[0][i]=-i
			Iy[0][i]=-i
		for i in range(rows):
			M[i][0]=-i
			Ix[i][0]=-i
			Iy[i][0]=-i
		for i in range(1,rows):
			for j in range(1,cols):
				if x[i-1]==y[j-1]:
					c=cmatch
				else:
					c=cmis
				M[i][j]=max(M[i-1][j-1], Ix[i-1][j-1],Iy[i-1][j-1])+c
				Ix[i][j]=max(M[i-1][j]+co,Ix[i-1][j]+cr,Iy[i-1][j]+co)
				Iy[i][j]=max(M[i][j-1]+co, Ix[i][j-1]+co, Iy[i][j-1]+cr)
		for i in range(rows):
			for j in range(cols):
				print("%5.1f " %M[i][j],end="")
			print("")
		print("")
		for i in range(rows):
			for j in range(cols):
				print("%5.1f " %Ix[i][j],end="")
			print("")
		print("")
		for i in range(rows):
			for j in range(cols):
				print("%5.1f " %Iy[i][j],end="")
			print("")
		print("")
		return max(M[rows-1][cols-1],Ix[rows-1][cols-1],Iy[rows-1][cols-1]) 
