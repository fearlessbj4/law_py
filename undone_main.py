import json
import zipfile
import glob
import os
from pprint import pprint
import colorama
from colorama import Fore, Style
from section_cut import cut,find_after
import zh_calculator as cal

start_point="主  文\r\n"
mid_list=["    事實及理由\r\n","  理  由\r\n","理    由\r\n","    事實及理由\r\n","    事實理由及證據\r\n","    事 實 理 由 及 證 據\r\n","事實理由及證據\r\n","事實及證據理由\r\n","理      由\r\n","  "]
start_list=["主  文\r\n","主    文\r\n","主　 文\r\n","主      文\r\n","    主　　　文\r\n","    主　　文\r\n","     文\r\n"]
#end_point="    理  由\r\n"
mid_point="    事實及理由\r\n"
end_point="中    華    民    國"
end_list=["中    華    民    國","中      華      民      國","中　　華　　民　　國"]   
print(Style.RESET_ALL)
#target_keyword=[["所得"]]

tempc=0
ct1=0
ct2=0
ct3=0
ct4=0
dlist=os.popen("ls ../law_py/202011").readlines()
k=0

def fc(lst,a,b,s_char):
	ward_end=find_after(lst,a,b)
	end=ward_end+lst[ward_end:].find(s_char)+1
	p_string=lst[lst.find("徒手竊取"):end]
	find_stuff(p_string,"徒手竊取","得手",int(len("徒手竊取")),int(-len("，")),list(cal.number_int+cal.number_int_full))

	#print(p_string)
def find_stuff(lst,st,ed,offset_st,offset_ed,num_list):
	print(lst[lst.find(st):lst.find(st)+offset_st])
	print(Fore.BLUE+lst[lst.find(st)+offset_st:lst.find(ed)+offset_ed])
	print(Style.RESET_ALL)
	print(lst[lst.find(ed)+offset_ed:])
	return 1
	

for i in range(len(dlist)):

	s=str("../law_py/202011/"+str(dlist[i][:-1]))
	flist=os.popen("ls "+s).readlines()
	#print(flist)
	for doc in flist:
		#if(ct<0):
		#	print(doc)
		#	ct+=1
		if (doc[:-1].endswith(".json")):
			file = json.load(open(s+"/"+doc[:-1],"r"))
			if (file['JCASE'].find("簡")!=-1 and file['JFULL'].find("犯竊盜罪")!=-1 and file['JFULL'].find("犯罪事實")!=-1 and file['JFULL'].find("徒手竊取")!=-1 and file['JFULL'].find("得手")!=-1):
				ct1+=1
				if(file['JFULL'].find("報告偵辦")!=-1):
					k=1
					ct2+=1
				#if(file['JFULL'].find("准予賠償")!=-1):
				#int(len(file['JFULL'])*0.5):]		
				
				#print(file['JID'])
				
				file['JFULL']=file['JFULL'].replace("叁","參").replace("十","拾")

				
				#if(len(cut_full)>=0):
					

				if(tempc<=2000 and k==1):
					k=0
					tempc+=1
					
					#print(cut_full)
					#file['JFULL'][file['JFULL'].find("犯罪事實"):].find("\r\n")
					print_str=file['JFULL'][file['JFULL'].find("犯罪事實\r\n"):file['JFULL'].find("犯罪事實\r\n")+file['JFULL'][file['JFULL'].find("犯罪事實\r\n"):].find("報告偵辦。\r\n")+7]
					
					if(len(print_str)>=20):
						print(file['JID'])
						print(print_str)
						print("-----------------------")
						#print(fc(print_str,"徒手竊取","得手","。"))
						fc(print_str,"徒手竊取","得手","。")
						print("-----------------------")
						ct3+=1
					if(print_str.find("徒手竊取")!=-1):
						ct4+=1
				
					#print(file['JFULL'])

"""
print(ct1)
print(ct2)
print(ct3)
print(ct4)
"""
