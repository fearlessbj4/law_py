from random import randint as ri
from random import seed
from math import log,exp
def split(lst,r,s):
	seed(s)
	if len(lst)==0:
		return [[],[]]
	else:
		ct=int(r*len(lst))
		ot=[]
		temp_lst=[i for i in lst]
		while(ct!=0):
			anchor=ri(0,len(temp_lst)-1)
			i=temp_lst[anchor]
			ot.append(i)
			temp_lst.remove(i)
			ct-=1
		#print(ot,temp_lst)
		return ot,temp_lst#train,test
def rev(x,y,features,tick_lower,tick_upper,tick_size):
	if ([len(x),len(y),len(features)].count(len(x))!=3 or len(x)==0):#retard proof
		return []
	else:
		t_r=int((tick_upper-tick_lower)/tick_size)+1
		t_ot=[0 for i in range(len(features[0]))]
		temp_sum=100000000000#initiate with a quite big number or -1
		for i in range(t_r**len(features[0])):#initate test/train range as -1~1 and slice to 0.1 per tick 
			tick=[int(i/(t_r**j))%t_r for j in range(len(features[0]))]
			tick=[tick_lower+(j*tick_size) for j in tick]
			if r_sum(x,y,features,tick)<temp_sum:
				temp_sum=r_sum(x,y,features,tick)
				t_ot=tick
				#print(temp_sum/len(x))

		return temp_sum,t_ot

def r_sum(x,y,features,tick):

	s=0
	for i in range(len(features)):
		temp=1
		for j in range(len(tick)):
			if(features[i][j]==0):
				temp*=1
			else:
				temp*=features[i][j]**tick[j]#initiate relations as features' power multiple
		s+=abs(x[i]*temp-y[i])#initiate |pred_y-true_y| as the score
	return s
def r_sum_reg(x,y,features,tick):

	s=0
	for i in range(len(features)):
		x_l=log(x[i])
		y_l=log(y[i])
		temp=0
		for j in range(len(tick)):
			if(features[i][j]==0):
				temp+=0
			else:
				temp+=(log(features[i][j])*tick[j])
				#temp*=features[i][j]**tick[j]#initiate relations as features' power multiple
		s+=abs(exp(x_l+temp)-exp(y_l))#initiate |pred_y-true_y| as the score
	return s
#l=[[i,i**2] for i in range(10)]
#split(l,0.8,10)
