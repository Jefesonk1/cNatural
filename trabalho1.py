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




def DE(n,popSiz,geracoes):
	#rangee=np.arange(5,11)
	#gera pop
	pop=np.zeros(shape=[popSiz,n])
	for x in range(popSiz):
		for y in range(n):
			pop[x][y]=rd.uniform(-5, 10)
	print(pop)
	muta(pop,popSiz,n,0.2)
	##end gera pop

def gerarDnv(maxValue):
	return rd.randint(0,maxValue)
def verificarExist(lista,element):
	for x in lista:
		if x == element:
			return 1
	else:
		return 0		
	

def muta(pop,popSiz,n,F):
	newpop=np.zeros(shape=[popSiz,n])
	for x in range (popSiz):
		result = rd.sample(range(0,popSiz-1),3)
		newpop[x]=pop[result[0]]+F*(pop[result[1]]+pop[result[2]])
	print('\n')
	print(newpop)
	teste=pop[0]+pop[1]
	print(teste)
	#print(newpop)



def main():
	a=np.arange(-5,11)
	b=[-3,5]
	print(a)
	var=zakh(b)
	print(var)
	DE(2,40,50)
	#b=zakharov(a)
	#plt.plot(a)
	#plt.show()	
	#print(a)
	#n=zakharov()
	#print('teste')


if __name__ == '__main__':
	main()