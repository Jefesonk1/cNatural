import numpy as np
import random as rd
import matplotlib.pyplot as plt
def zakh(n):
	index=b=c=0
	a=sum([(x**2) for x in n])
	size=len(n)
	while index<size:

		b+=0.5*(index+1)*n[index]
		c+=0.5*(index+1)*n[index]
		index+=1	
	return a+(b**2)+(c**4)		
	
def demonio(old,new,CR):
	dim=np.shape(old)
	U=np.zeros(shape=[dim[0],dim[1]])
	for i in range(dim[0]):
		for j in range(dim[1]):
			if rd.uniform(0,1)<=CR or j== rd.randint(0,dim[1]-1):
				U[i][j]=new[i][j]
			else:
				U[i][j]=old[i][j]
	return U

def DE(NP,CR,F,n,gen):
	contador=0
	x=np.zeros(shape=[NP,n])
	fitx=[]
	fitu=[]
	for i in range(NP):
		for j in range(n):
			x[i][j]=rd.uniform(-5, 10)

	

	while contador<gen:
		fitx.clear()
		for i in range(NP):
			fitx.append(zakh(x[i]))
		v=muta(x,F)
		u=demonio(x,v,CR)

		for i in range(NP):
			fitu.append(zakh(u[i]))
		for i in range(NP):
			if fitu[i]<fitx[i]:
				x[i]=u[i]
		fitu.clear()
		contador+=1
	
	for i in range(NP):
		print(zakh(x[i]))

	print('\n')

	for i in range(NP):
		print(x[i])		

def muta(pop,F):
	dim=np.shape(pop)
	newpop=np.zeros(shape=[dim[0],dim[1]])
	for x in range (dim[0]):
		result = rd.sample(range(0,dim[0]-1),3)
		newpop[x]=pop[result[0]]+F*(pop[result[1]]-pop[result[2]])
	return newpop



def main():
	CR=0.3
	NP=40
	F=0.5
	n=5
	gen=200

	DE(NP,CR,F,n,gen)


if __name__ == '__main__':
	main()