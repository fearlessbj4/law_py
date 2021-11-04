import json
import zipfile
import glob
import os
import random
from pprint import pprint
import colorama
from colorama import Fore, Style
from section_cut import cut,find_after,search_from_list
import zh_calculator as cal



#"""
list_a=os.popen("cat ./stuff_type/a.txt").readlines()
list_b=os.popen("cat ./stuff_type/b.txt").readlines()
list_c=os.popen("cat ./stuff_type/c.txt").readlines()
list_a=[i.replace("\n","") if i.find("\n")!=-1 else i for i in list_a]
list_b=[i.replace("\n","") if i.find("\n")!=-1 else i for i in list_c]
list_c=[i.replace("\n","") if i.find("\n")!=-1 else i for i in list_c]
#"""



start_point="主  文\r\n"
mid_list=["犯 罪 事 實 及 理 由\r\n","事實及理由\r\n","    事實及理由\r\n","  理  由\r\n","理    由\r\n","    事實及理由\r\n","    事實理由及證據\r\n","    事 實 理 由 及 證 據\r\n","事實理由及證據\r\n","事實及證據理由\r\n","理      由\r\n","  "]
start_list=["主  文\r\n","主    文\r\n","主　 文\r\n","主      文\r\n","    主　　　文\r\n","    主　　文\r\n","     文\r\n"]
#end_point="    理  由\r\n"
mid_point="    事實及理由\r\n"
end_point="中    華    民    國"
end_list=["中    華    民    國","中      華      民      國","中　　華　　民　　國"]   
print(Style.RESET_ALL)
#target_keyword=[["所得"]]
key_char_list=["價值","內","之",",","，"]
keyward="徒手竊取"

tempc=0
ct1=0
ct11=0
ct2=0
ct3=0
ct4=0
ct5=0

#dlist=os.popen("ls ../law_py/202011").readlines()
k=0
output=[]#[[title,stuff,stuff_type,stuff_value]]
simple_output=[]
small_output=[]
total_price=0

tp_str=""
output_str=""

#def find_num_part(target,pre_offset):
	

def fc(title,lst,st,ed,s_char):
	
	
	ward_end=find_after(lst,st,ed)
	end=ward_end+lst[ward_end:].find(s_char)+1
	p_string=lst[lst.find(st):end]
	
	find_stuff(title,p_string,st,ed,int(len(keyward)),0,list(cal.number_int+cal.number_int_full))
	
	if(find_after(lst,st,st)!=-1):
		#print("!#!")
		fc(title,lst[find_after(lst,st,st):],st,ed,s_char)
	else:
		return 1

	#print(p_string)	
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
	print(tp_str)

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
		print(tp_str)
		content=t[t.find(key_char)+1:]
		#output.append([title,content,0,0])
		tp_str=str(Style.RESET_ALL)
		output_str+="\n"+tp_str
		print(tp_str)
		tp_str="==================＄==================="
		output_str+="\n"+tp_str
		print(tp_str)
		a=cal.enter(content.replace(" ",""),"元")
		tp_str=str(Fore.WHITE+str(a))
		output_str+="\n"+tp_str
		print(tp_str)
		tp_str=str(Style.RESET_ALL)
		output_str+="\n"+tp_str
		print(tp_str)
		tp_str="======================================"
		output_str+="\n"+tp_str
		print(tp_str)
		total_price+=(a if a!=-1 else 0)
		#output.append([title,content,find_stuff_type(content),find_value(content)])
	else:
		tp_str=str(Fore.WHITE+lst[lst.find(st)+offset_st:lst.find(ed)+offset_ed])
		output_str+="\n"+tp_str
		print(tp_str)
	
	tp_str=str(Style.RESET_ALL)
	output_str+="\n"+tp_str
	print(tp_str)
	tp_str=str(lst[lst.find(ed)+offset_ed:])
	output_str+="\n"+tp_str
	print(tp_str)
	return 1
	
str_ii=""
s=str("./target_case")
flist=os.popen("ls "+s).readlines()
#print(flist)
for doc in flist:
	#if(ct<0):
	#	print(doc)
	#	ct+=1
	if (doc[:-1].endswith(".json")):
		file = json.load(open(s+"/"+doc[:-1],"r"))
		if (file['JCASE'].find("簡")!=-1 and file['JFULL'].find("犯竊盜罪")!=-1 and file['JFULL'].find("犯罪事實")!=-1 
			and file['JFULL'].find("得手")!=-1
			and not(file['JFULL'].find("報告")==-1 and file['JFULL'].find("偵")==-1 and file['JFULL'].find("辦")==-1)):
			
			tp_str=""
			output_str=""
			ct1+=1
			
			#if(file['JFULL'].find("准予賠償")!=-1):
			#int(len(file['JFULL'])*0.5):]		
			
			#print(file['JID'])
			
			file['JFULL']=file['JFULL'].replace("叁","參").replace("十","拾").replace("\r\n    ","")


			
			#if(len(cut_full)>=0):
				

			
				#print(cut_full)
				#file['JFULL'][file['JFULL'].find("犯罪事實"):].find("\r\n")
			

			if(file['JFULL'].find("報告偵辦")!=-1):
				print_str=file['JFULL'][file['JFULL'].find("犯罪事實\r\n"):find_after(file['JFULL'],"犯罪事實\r\n","報告偵辦")+4]
			elif(file['JFULL'].find("偵辦")!=-1):
				print_str=file['JFULL'][file['JFULL'].find("犯罪事實\r\n"):find_after(file['JFULL'],"犯罪事實\r\n","偵辦")+2]
			elif(file['JFULL'].find("報告")!=-1):
				print_str=file['JFULL'][file['JFULL'].find("犯罪事實\r\n"):find_after(file['JFULL'],"犯罪事實\r\n","報告")+2]							
			else:
				print_str=file['JFULL'][file['JFULL'].find("犯罪事實\r\n"):find_after(file['JFULL'],"犯罪事實\r\n","二、")+2]
			
			total_price=0
			#and random.randint(0,99)%100==17
			if(len(print_str)>=20):	
				total_price=0
				p_str=cut(file['JFULL'],"short",start_point,mid_point,end_point,start_list,mid_list,end_list)
				p_str=p_str.replace(" ","")
				fc(file['JID'],print_str,keyward,"得手","。")
				tp_output_str=output_str

				p_str=p_str.replace(" ","")
				j1=p_str.find("易科罰金")
				j2=p_str.find("易服勞役")
				y=0
				m=0
				d=0
				fine=0
				if(find_after(p_str,"易科罰金","易科罰金")!=-1 and p_str.find("應執行")!=-1):
					p_str=p_str[p_str.find("應執行"):find_after(p_str,"應執行","，")]
				if(j1!=-1):
					#print(p_str[:p_str.find("易科罰金")])
					if(p_str.find("易科罰金")!=-1):
						y=cal.enter(p_str[:p_str.find("易科罰金")],"年")
						m=cal.enter(p_str[:p_str.find("易科罰金")],"月")
						d=cal.enter(p_str[:p_str.find("易科罰金")],"日")
					else:
						y=cal.enter(p_str,"年")
						m=cal.enter(p_str,"月")
						d=cal.enter(p_str,"日")
					#
					
					#
				if(j2!=-1):
					print("罰金")
					if(p_str.find("易服勞役")!=-1):
						
						
						f_p_str=p_str[:p_str.find("易服勞役")]
						
						fine=cal.enter(f_p_str[find_after(f_p_str,"罰金","應執行"):],"元")
						#print(f_p_str[find_after(f_p_str,"罰金","應執行"):])
						
					else:
						fine=cal.enter(p_str,"元")
						
					
					#print(fine)
				
				ct3+=1
				p1=total_price
				p2=(m if m!=-1 else 0)*30*1000+(d if d!=-1 else 0)*1000+(fine if fine!=-1 else 0)
				#print("涉案金額:",p1)
				#print("換算罰金:",p2)
				total_price=0
				if(file['JFULL'].find("爰")!=-1 and find_after(file['JFULL'],"爰","被告")!=-1):
					ct5+=1
				if(p1!=0 and p2!=0):
					small_str=""
					small_str+=str(Fore.BLUE)+"-----------"+str(ct4)+"------------\n"+str(Style.RESET_ALL)

					print("-----------"+str(ct4)+"------------")
					small_str+=str(file['JID'])+"\n"
					print(file['JID'])
					small_str+="-----------------------\n"
					print("-----------------------\n")
					small_str+="=================事實理由=================\n"
					print("=================事實理由=================")
					small_str+=p_str+"\n"
					print(p_str)				
					#print("----------------------------------------")
					
					tp_str=""
					output_str=""
					print(fc(file['JID'],print_str,keyward,"得手","。"))

					tp_str=""
					output_str=""
					#print("===================科刑==================")
					#print(file['JFULL'].find("爰"))
					#print("====================刑===================")
					
					#print("年")
					#print(y)
					#print("月")
					#print(m)
					#print("日")
					#print(d)
					#print("罰金")
					#if(p_str.find("易服勞役")!=-1):
					#	print(f_p_str[find_after(f_p_str,"罰金","應執行"):])

					#print(fine)
					small_str+="==================細節==================\n"
					small_str+=tp_output_str+"\n"

					small_str+="涉案金額:"+str(Fore.WHITE)+str(p1)+"\n"
					print("涉案金額:"+Fore.WHITE+str(p1))
					small_str+=str(Style.RESET_ALL)+"\n"
					print(Style.RESET_ALL)
					
					small_output.append(small_str)
					small_str=""
					#print("換算罰金:",p2)

					ct4+=1

#"""
f=open('./small.txt','w')
for i in range(len(small_output)):
	f.write(str(small_output[i]).replace(' ','')+str('\n'))
f.close()
#"""

"""					
f=open('./stuff_list.txt','w')
for i in range(len(output)):
	f.write(str(output[i]).replace(' ','')+str('\n'))
f.close()				
"""
					#print(file['JFULL'])


print(ct3,ct4,ct5)

