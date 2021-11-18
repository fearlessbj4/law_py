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



#"""
list_a=os.popen("cat ./stuff_type/a.txt").readlines()
list_b=os.popen("cat ./stuff_type/b.txt").readlines()
list_c=os.popen("cat ./stuff_type/c.txt").readlines()
list_a=[i.replace("\n","") if i.find("\n")!=-1 else i for i in list_a]
list_b=[i.replace("\n","") if i.find("\n")!=-1 else i for i in list_c]
list_c=[i.replace("\n","") if i.find("\n")!=-1 else i for i in list_c]
#"""

#"""
累犯=["竊盜前科","竊盜之前科","竊盜之前案","累犯"]
學歷=["智識程度","學歷","教育"]
經濟=["經濟","家庭狀況","生活狀況"]
#"""
start_point="主  文\r\n"
mid_list=["犯 罪 事 實 及 理 由\r\n","犯罪事實","犯 罪 事 實 及 理 由","事實及理由\r\n","    事實及理由\r\n","  理  由\r\n","理    由\r\n","    事實及理由\r\n","    事實理由及證據\r\n","    事 實 理 由 及 證 據\r\n","事實理由及證據\r\n","事實及證據理由\r\n","理      由\r\n","  "]
start_list=["主  文\r\n","主    文\r\n","主　 文\r\n","主      文\r\n","    主　　　文\r\n","    主　　文\r\n","     文\r\n","主  文"]
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
ct6=0
ct7=0
ct8=0
ct9=0
ct10=0


k=0
output=[]#[[title,stuff,stuff_type,stuff_value]]
simple_output=[]
small_output=[]
total_price=0
t_=[]

tp_str=""
output_str=""

#def find_num_part(target,pre_offset):
	

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
	
str_ii=""
s=str("./target_case")
flist=os.popen("ls "+s).readlines()

for doc in flist:
	
	if (doc[:-1].endswith(".json")):
		file = json.load(open(s+"/"+doc[:-1],"r"))
		if (file['JCASE'].find("簡")!=-1 and file['JFULL'].find("犯竊盜罪")!=-1 and file['JFULL'].find("犯罪事實")!=-1 
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
					
					if(p_str.find("易科罰金")!=-1):
						y=cal.enter(p_str[:p_str.find("易科罰金")],"年")
						m=cal.enter(p_str[:p_str.find("易科罰金")],"月")
						d=cal.enter(p_str[:p_str.find("易科罰金")],"日")
					else:
						y=cal.enter(p_str,"年")
						m=cal.enter(p_str,"月")
						d=cal.enter(p_str,"日")
					
				if(j2!=-1):
					
					if(p_str.find("易服勞役")!=-1):
						
						
						f_p_str=p_str[:p_str.find("易服勞役")]
						
						fine=cal.enter(f_p_str[find_after(f_p_str,"罰金","應執行"):],"元")
						
						
					else:
						fine=cal.enter(p_str,"元")
						
					
					
				
				ct3+=1
				p1=total_price
				p2=(m if m!=-1 else 0)*30*1000+(d if d!=-1 else 0)*1000+(fine if fine!=-1 else 0)
				
				total_price=0
				if(file['JFULL'].find("爰")!=-1 and find_after(file['JFULL'],"爰","被告")!=-1):
					ct5+=1
				#"""
				if(p1!=0 and p2!=0):
					small_str=""
					small_str+=str(Fore.BLUE)+"-----------"+str(ct4)+"------------\n"+str(Style.RESET_ALL)

					
					small_str+=str(file['JID'])+"\n"
					
					small_str+="-----------------------\n"
					
					small_str+="=================事實理由=================\n"
					
					small_str+=p_str+"\n"
					
					tp_str=""
					output_str=""
					

					tp_str=""
					output_str=""
					
					small_str+="==================細節==================\n"
					small_str+=tp_output_str+"\n"

					small_str+="涉案金額:"+str(Fore.WHITE)+str(p1)+"\n"
					
					small_str+=str(Style.RESET_ALL)+"\n"
					
					
					
					if(find_after(file['JFULL'],"坦承","所示之刑")!=-1):
						t_=[]
						ct8+=1
					
					ver=find_from_list(file['JFULL'],學歷)
					if(ver!=-1):
						
						type_=[]
						type_學歷=["大學","高職","高中","國中","國小","小學","未受教育","高等","五專","健全","成熟"]
						#type_學歷+=["自述","自陳","兼衡"]

						for i in range(len(type_學歷)):
							
							type_.append(find_after(file['JFULL'],type_學歷[i],學歷[ver]))
							type_.append(find_after(file['JFULL'],學歷[ver],type_學歷[i]))
						
						
						"""
						if(type_.count(-1)!=len(type_)):
							ct9+=1
						else:
							print(file['JID'])
						#"""

						t_.append(type_)
						ct7+=1
					ver=find_from_list(file['JFULL'],經濟)
					
					if(ver!=-1):

						type_=[]
						type_經濟=["富裕","小康","一般","普通","勉持","貧寒","清寒","貧窮","貧困"]
						type_經濟+=["自述","自陳","兼衡"]

						for i in range(len(type_經濟)):
							type_.append(find_after(file['JFULL'],type_經濟[i],經濟[ver]))
							type_.append(find_after(file['JFULL'],經濟[ver],type_經濟[i]))
						

						#"""
						if(type_.count(-1)!=len(type_)):
							ct9+=1
						else:
							print(file['JID'])
						#"""

						ct6+=1
						t_.append(type_)
					

					
					if(len(t_)==2 and (t_[0].count(-1)!=len(t_[0]) and t_[1].count(-1)!=len(t_[1]))):
						ct10+=1
						#=========!
						#print(file['JID'])
						#print(t_)
						#=========!

					#if(file['JFULL'].find("身心障礙")!=-1):
						#	ct10+=1
					
					t_=[]

					#print(small_str)
					small_output.append(small_str)
					small_str=""
					

					ct4+=1

				#"""
			
				"""
				p_str=cut(file['JFULL'],"mid",start_point,mid_point,end_point,start_list,mid_list,end_list)
				if(cal.enter(p_str,"元")>0):
					print(file['JID'])
					print(p_str)
					print(cal.enter(p_str,"元"))
				#"""
				
#"""

#"""

"""					
f=open('./stuff_list.txt','w')
for i in range(len(output)):
	f.write(str(output[i]).replace(' ','')+str('\n'))
f.close()				
"""
					#print(file['JFULL'])


print(ct3,ct4,ct5,ct6,ct7,ct8,ct9,ct10)

