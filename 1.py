import json
import zipfile
import glob
import os
from pprint import pprint
import colorama
from colorama import Fore, Style
from section_cut import cut,find_after,search_from_list,find_from_list
import zh_calculator as cal

list_a=os.popen("cat ./stuff_type/a.txt").readlines()
list_b=os.popen("cat ./stuff_type/b.txt").readlines()
list_c=os.popen("cat ./stuff_type/c.txt").readlines()
list_a=[i.replace("\n","") for i in list_a]
list_b=[i.replace("\n","") for i in list_b]
list_c=[i.replace("\n","") for i in list_c]


def find_value(lst):
	return cal.enter(lst)

def find_stuff_type(lst):
	str_type=""
	if(find_from_list(list_a,lst)!=-1):
		str_type+="a"
	if(find_from_list(list_b,lst)!=-1):
		str_type+="b"
	if(find_from_list(list_c,lst)!=-1):
		str_type+="c"
	if(str_type==""):
		str_type="?"
	return str_type


#"""
str_example="魚丸一包價值新台幣200元"
lst_example=[str_example,find_stuff_type(str_example),find_value(str_example)]
#"""



stuff_list=os.popen("cat 2.txt").readlines()
lst=[]
#for i in range(24,25,1):
for i in range(len(stuff_list)):
	p=stuff_list[i][stuff_list[i].find("',")+2:stuff_list[i].find("]")]
	p=p.replace("\",","',")
	p=p.replace("000多元","000元")
	p=p[:p.find("',")]
	
	#print(p)
	lst.append([stuff_list[i][:stuff_list[i].find("',")].replace("[",""),
		p,find_stuff_type(p),find_value(p)])



f_lst=lst
f_lst.sort(key=lambda e:(int(e[3])-int(find_value(str_example)))**2)
print(int(lst[30][3]))
ct=0
for i in range(len(f_lst)):
	if(f_lst[i][2]==find_stuff_type(str_example) and f_lst[i][3]!=-1 and ct<10):
		print(f_lst[i])
		ct+=1
#print(lst)
#print(lst)

"""

"""
f=open('./2_stuff_list.txt','w')
for i in range(len(lst)):
	f.write(str(lst[i]).replace(' ','')+str('\n'))
f.close()
