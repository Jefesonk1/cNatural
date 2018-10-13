import numpy as np
import random as rd
import matplotlib.pyplot as plt
def zakh(n):
	beg=0
	a=sum([(x**2) for x in n])
	c=0
	b=0
	size=len(n)
	while beg<size:
		b+=0.5*(beg+1)*n[beg]
		c+=0.5*(beg+1)*n[beg]
		beg+=1	
	return a+(b**2)+(c**4)	

def cruzamento(old,NP,n,new):
	U=np.zeros(shape=[NP,n])
	print(U)			


def DE(NP,CR,F,n,gen):
	pop=np.zeros(shape=[NP,n])
	for x in range(NP):
		for y in range(n):
			pop[x][y]=rd.uniform(-5, 10)
	newpop=muta(pop,NP,n,F)
	cruzamento(pop,NP,n,newpop)
			

def muta(pop,NP,n,F):
	newpop=np.zeros(shape=[NP,n])
	for x in range (NP):
		result = rd.sample(range(0,NP-1),3)
		newpop[x]=pop[result[0]]+F*(pop[result[1]]+pop[result[2]])
	return newpop



def main():
	DE(40,0.3,0.2,2,50)


if __name__ == '__main__':
	main()