import json
import zipfile
import glob
import os
import random
from pprint import pprint
import colorama
from colorama import Fore, Style
from section_cut import cut,find_after,find_from_list,search_from_list,find_context
import zh_calculator as cal
from ver_5 import *
import matplotlib.pyplot as plt
import numpy as np
from sd import *
import sys



temp_lst=[]
tempc=0
ct1=0
ct11=0
ct2=0
ct3=0
ct4=0
ct5=0
ct6=0
ct7=0
ct8=0
ct9=0
ct10=0
ct11=0
ct12=0

k_ver=0#學歷,經濟
k_type=type_學歷 if k_ver==0 else type_經濟

otct_lst=[[0,0,0] for i in range(len(k_type))]
#output=[[[] for j in range(len(type_狀態))] for i in range (len(type_學歷))]#[[title,stuff,stuff_type,stuff_value]]
output=[[] for i in range (len(k_type))]
simple_output=[]
small_output=[]
total_price=0
t_=[]

tp_str=""
output_str=""
#"""
#def find_num_part(target,pre_offset):
	
#"""
def fc(title,lst,st,ed,s_char):
	
	
	ward_end=find_after(lst,st,ed)
	end=ward_end+lst[ward_end:].find(s_char)+1
	p_string=lst[lst.find(st):end]
	
	find_stuff(title,p_string,st,ed,int(len(keyward)),0,list(cal.number_int+cal.number_int_full))
	
	if(find_after(lst,st,st)!=-1):
		
		fc(title,lst[find_after(lst,st,st):],st,ed,s_char)
	else:
		return 1

		
def find_value(lst):
	return cal.enter(lst)
def find_stuff_type(lst):
	str_type=""
	if(search_from_list(list_a,lst)!=-1):
		str_type+="a"
	if(search_from_list(list_b,lst)!=-1):
		str_type+="b"
	if(search_from_list(list_c,lst)!=-1):
		str_type+="c"
	if(str_type==""):
		str_type="?"
	return str_type

def find_stuff(title,lst,st,ed,offset_st,offset_ed,num_list):
	global output
	global total_price
	global key_char_list
	global tp_str,output_str
	
	tp_str=str(lst[lst.find(st):lst.find(st)+offset_st])
	output_str+=tp_str
	

	key_char="價值"
	for i in range(1,len(key_char_list),1):
		if(lst[lst.find(st)+offset_st:lst.find(ed)+offset_ed].find(key_char)==-1):
			key_char=key_char_list[i]
		else:
			break
	
	if(lst[lst.find(st)+offset_st:lst.find(ed)+offset_ed].find(key_char)!=-1):
		t=lst[lst.find(st)+offset_st:lst.find(ed)+offset_ed]
		tp_str=str(Fore.WHITE+t[:t.find(key_char)]+Fore.WHITE+key_char+Fore.WHITE+t[t.find(key_char)+len(key_char):])
		output_str+="\n"+tp_str
		
		content=t[t.find(key_char)+1:]
		
		tp_str=str(Style.RESET_ALL)
		output_str+="\n"+tp_str
		
		tp_str="==================＄==================="
		output_str+="\n"+tp_str
		
		a=cal.enter(content.replace(" ",""),"元")
		tp_str=str(Fore.WHITE+str(a))
		output_str+="\n"+tp_str
		
		tp_str=str(Style.RESET_ALL)
		output_str+="\n"+tp_str
		
		tp_str="======================================"
		output_str+="\n"+tp_str
		
		total_price+=(a if a!=-1 else 0)
		
	else:
		tp_str=str(Fore.WHITE+lst[lst.find(st)+offset_st:lst.find(ed)+offset_ed])
		output_str+="\n"+tp_str
		
	
	tp_str=str(Style.RESET_ALL)
	output_str+="\n"+tp_str
	
	tp_str=str(lst[lst.find(ed)+offset_ed:])
	output_str+="\n"+tp_str
	
	return 1
#"""
str_ii=""

for ii in range(1,13,1):
	str_ii="0"+str(ii) if (ii<10) else str(ii)
	dlist=os.popen("ls \"./2011/2011"+str_ii+"\"").readlines()

	for i in range(len(dlist)):

		s=str("./2011/2011"+str_ii+"/"+str(dlist[i][:-1]))
		flist=os.popen("ls \""+s+"\"").readlines()

		for doc in flist:
			
			if (doc[:-1].endswith(".json")):
				file = json.load(open(s+"/"+doc[:-1],"r"))
				if (file['JFULL'].find("犯竊盜罪")!=-1 and file['JFULL'].find("犯罪事實")!=-1 
					and file['JFULL'].find("得手")!=-1
					and not(file['JFULL'].find("報告")==-1 and file['JFULL'].find("偵")==-1 and file['JFULL'].find("辦")==-1)):
					
					tp_str=""
					output_str=""
					ct1+=1
					
					
					file['JFULL']=file['JFULL'].replace("叁","參").replace("十","拾").replace("\r\n    ","")

					

					if(file['JFULL'].find("報告偵辦")!=-1):
						print_str=file['JFULL'][file['JFULL'].find("犯罪事實\r\n"):find_after(file['JFULL'],"犯罪事實\r\n","報告偵辦")+4]
					elif(file['JFULL'].find("偵辦")!=-1):
						print_str=file['JFULL'][file['JFULL'].find("犯罪事實\r\n"):find_after(file['JFULL'],"犯罪事實\r\n","偵辦")+2]
					elif(file['JFULL'].find("報告")!=-1):
						print_str=file['JFULL'][file['JFULL'].find("犯罪事實\r\n"):find_after(file['JFULL'],"犯罪事實\r\n","報告")+2]							
					else:
						print_str=file['JFULL'][file['JFULL'].find("犯罪事實\r\n"):find_after(file['JFULL'],"犯罪事實\r\n","二、")+2]
					
					total_price=0
					
					if(len(print_str)>=20):	
						f_dir=str(s)+"/"+str(doc.replace("\n",""))
						#print(doc)
						#print(str("cp "+f_dir+" ./target_case/"))
						
						os.popen(str("cp \""+f_dir+"\" ./target_case"))
						print(f_dir)
						print(ct3)
						ct3+=1
						if(file['JFULL'].find("科刑")!=-1):
							ct4+=1
						
					
						"""
						p_str=cut(file['JFULL'],"mid",start_point,mid_point,end_point,start_list,mid_list,end_list)
						if(cal.enter(p_str,"元")>0):
							print(file['JID'])
							print(p_str)
							print(cal.enter(p_str,"元"))
						#"""
				
#"""

#"""
print(ct3,ct4)
"""					
f=open('./stuff_list.txt','w')
for i in range(len(output)):
	f.write(str(output[i]).replace(' ','')+str('\n'))
f.close()				
"""
					#print(file['JFULL'])

#"""output

#print(count_學歷,sum(count_學歷),ct7)
#print(count_經濟,sum(count_經濟),ct6)

#print(output)
#print(sum([len(output[i]) for i in range(len(output))]))
#"""
#"""
"""
print("===============")
print(ct11,ct12)
print(otct_lst)
print("===============")
#"""
#os.popen("rm -rf fig")
#os.popen("mkdir fig")

		#plt.savefig("./fig/"+str(k_type[i])+"_ot3.png")
		#plt.clf()
		#plt.show()

#"""