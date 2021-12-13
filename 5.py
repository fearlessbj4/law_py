import json
import zipfile
import glob
import os
import random
from pprint import pprint
import colorama
from colorama import Fore, Style
from section_cut import *
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

r_var=0
t_var=0#geometric_mean,mean
title="g_mean" if t_var==0 else "mean"
title+="" if r_var==0 else "_r"
k_var=0#學歷,經濟
k_type=type_學歷 if k_var==0 else type_經濟

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
		tp_str=str(Fore.WHITE+t[:t.find(key_char)]+Fore.RED+key_char+Fore.BLUE+t[t.find(key_char)+len(key_char):])
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
s=str("./target_case")

flist=os.popen("ls "+s).readlines()
富裕=os.popen("cat ./富裕.txt").readlines()
富裕=[i.replace("\n","")for i in 富裕]
ct_富裕=0
for doc in flist:
	
	if (doc[:-1].endswith(".json")):
		file = json.load(open(s+"/"+doc[:-1],"r"))
		
		if (file['JTITLE'].find("擄人勒贖")==-1):
			file['JFULL']=file['JFULL'].replace("叁","參").replace("十","拾").replace("\r\n    ","")
			ct9_=False
			
			if(file['JFULL'].find("富裕")!=-1 ):
				file['JFULL']=file['JFULL'].replace("花蓮市富裕","花蓮市富_裕").replace("江富裕","江富_裕").replace("陳富裕","陳富_裕").replace("富裕二街","富_裕二街").replace("富裕彩券行","富_裕彩券行").replace("富裕一街","富_裕一街").replace("鄭富裕","鄭富_裕").replace("翔富裕","翔富_裕").replace("佯稱為家境富裕","佯稱為家境富_裕")
				file['JFULL']=file['JFULL'].replace("富裕旅店","富_裕旅店").replace("富裕門市","富_裕門市")
			#file['JFULL']=revise(file['JFULL'],富裕_revise)
			if(file['JFULL'].find("富裕")!=-1 ):
				
				
				if(file['JFULL'].find("不富裕")==-1):
					ct9_=True
					
					#print(file['JID'])
					ct9+=1
				else:
					file['JFULL']=file['JFULL'].replace("不富裕","勉持").replace("不是很富裕","勉持")#<-------revise-------


			tp_str=""
			output_str=""
			ct1+=1
			
			
			

			

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
				#print(ct3)
				total_price=0
				p_str=cut(file['JFULL'],"short",start_point,mid_point,end_point,start_list,mid_list,end_list)
				p_str=p_str.replace(" ","")
				print_str=print_str.replace("      ","").replace(" ","").replace("\r\n","").replace("(下同)","").replace("（下同）","").replace("【下同】","").replace("餘萬元","萬元")
				fc(file['JID'],print_str,keyward,"得手","。")
				tp_output_str=output_str

				p_str=p_str.replace(" ","").replace("\r\n","").replace("(下同)","").replace("（下同）","").replace("【下同】","").replace("餘萬元","萬元")
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
				if([y,m,d].count(0)==3):
					temp_f=file['JFULL'][:file['JFULL'].find("犯罪事實\r\n")]
					"""
					if(find_after(temp_f,"易科罰金","易科罰金")!=-1 and temp_f.find("應執行")!=-1):
						temp_f=temp_f[temp_f.find("應執行"):find_after(temp_f,"應執行","，")]
						y=cal.enter(temp_f[:temp_f.find("易科罰金")],"年")
						m=cal.enter(temp_f[:temp_f.find("易科罰金")],"月")
						d=cal.enter(temp_f[:temp_f.find("易科罰金")],"日")
					el
					"""
					if(temp_f.find("應執行")!=-1):
						y=cal.enter(temp_f[temp_f.find("應執行"):find_after(temp_f,"應執行","，")],"年")
						m=cal.enter(temp_f[temp_f.find("應執行"):find_after(temp_f,"應執行","，")],"月")
						d=cal.enter(temp_f[temp_f.find("應執行"):find_after(temp_f,"應執行","，")],"日")
					if([y,m,d].count(0)==3 and temp_f.find("有期徒刑")!=-1):
						y=cal.enter(temp_f[temp_f.find("有期徒刑"):find_after(temp_f,"有期徒刑","，")],"年")
						m=cal.enter(temp_f[temp_f.find("有期徒刑"):find_after(temp_f,"有期徒刑","，")],"月")
						d=cal.enter(temp_f[temp_f.find("有期徒刑"):find_after(temp_f,"有期徒刑","，")],"日")
					if([y,m,d].count(0)==3 and temp_f.find("拘役")!=-1):
						y=cal.enter(temp_f[temp_f.find("拘役"):find_after(temp_f,"拘役","，")],"年")
						m=cal.enter(temp_f[temp_f.find("拘役"):find_after(temp_f,"拘役","，")],"月")
						d=cal.enter(temp_f[temp_f.find("拘役"):find_after(temp_f,"拘役","，")],"日")
					
				if(j2!=-1):
					
					if(p_str.find("易服勞役")!=-1):
						
						
						f_p_str=p_str[:p_str.find("易服勞役")]
						
						fine=cal.enter(f_p_str[find_after(f_p_str,"罰金","應執行"):],"元")
						if(fine==0):
							fine=cal.enter(f_p_str[f_p_str.find("罰金"):],"元")
						
						
					else:
						fine=cal.enter(p_str,"元")
						
				
				ct3+=1
				p1=total_price
				if(p1==0):
					p1=cal.enter(print_str,"元")
					if(p1==0 and (file['JFULL'].find("犯罪所得")!=-1 or file['JFULL'].find("不法所得")!=-1)):
						temp_f=file['JFULL']
						p1=cal.enter(temp_f[temp_f.find("犯罪所得"):find_after(temp_f,"犯罪所得","，")],"元")
						if(p1==0 and file['JFULL'].find("不法所得")!=-1):
							p1=cal.enter(temp_f[temp_f.find("不法所得"):find_after(temp_f,"不法所得","，")],"元")
				p2=(m if m!=-1 else 0)*30*1000+(d if d!=-1 else 0)*1000+(fine if fine!=-1 else 0)
				
				total_price=0

				"""
				if(ct_富裕<len(富裕) and file['JID']==富裕[ct_富裕]):
					print(file['JID'])
					print("--------------------------------------")
					print(print_str)
					print(p1)
					print(p2)
					#print(print_str)
					print("--------------------------------------")
					ct_富裕+=1
				#"""

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
					
					#if(ct3<100):
					#	print(small_str)
					
					if(find_after(file['JFULL'],"坦承","所示之刑")!=-1):
						t_=[]
						ct8+=1
					

					temp_lst=[]#============!
					ver=find_from_list(file['JFULL'],學歷)
					if(ver!=-1):
						
						type_=[]
						
						tempc=100

						for i in range(len(type_學歷)):
							a=[]
							temp_f=file['JFULL'].replace(" ","").replace("\r\n","")
							a.append(find_after(temp_f,type_學歷[i],學歷[ver]))
							a.append(find_after(temp_f,學歷[ver],type_學歷[i]))
							type_+=a
							if((a[0]!=-1 or a[1]!=-1) and i<tempc):
								tempc=i
						if(tempc!=100):
							count_學歷[tempc]+=1
							temp_lst.append(type_學歷[tempc])#============!
						

						t_.append(type_)
						ct7+=1
					ver=find_from_list(file['JFULL'],經濟)
					
					if(ver!=-1):

						type_=[]
						
						tempc=100
						for i in range(len(type_經濟)):
							a=[]

							
							temp_f=file['JFULL'].replace(" ","").replace("\r\n","")
							a.append(find_context(file['JFULL'].replace(" ",""),type_經濟[i],經濟[ver],20))
							a.append(find_context(file['JFULL'].replace(" ",""),經濟[ver],type_經濟[i],20))
							#a.append(find_after(temp_f,type_經濟[i],經濟[ver]))
							#a.append(find_after(temp_f,經濟[ver],type_經濟[i]))
							type_+=a
							if((a[0]!=-1 or a[1]!=-1) and i<tempc):
								tempc=i
						
						if(tempc!=100):
							count_經濟[tempc]+=1
							temp_lst.append(type_經濟[tempc])#============!
							
						

						"""
						if(type_.count(-1)!=len(type_)):
							ct9+=1
						else:
							print(file['JID'])
						#"""

						ct6+=1
						t_.append(type_)
					

					
					if(len(temp_lst)==2 and len(t_)==2 and (t_[0].count(-1)!=len(t_[0]) and t_[1].count(-1)!=len(t_[1]))):
						ct10+=1
						"""#=========!
						print(file['JID'])
						print("涉案金額",p1)
						print("換算罰金",p2)
						#print(t_)
						print(temp_lst)
						#"""#============!
						
						if(search_from_list(k_type,temp_lst[k_var])!=-1):
							if(1):
							#if(find_from_list(file['JFULL'].replace("\r\n      ",""),type_狀態)!=-1):
								ff=file['JFULL'].replace(" ","")
								tct=find_from_list(ff,type_狀態)
								
								#print(type_狀態[find_from_list(file['JFULL'],type_狀態)])
								for i in range(len(k_type)):
						#<jd------------------>
									if(r_var==0):
										jd=True
									else:
										jd=(file['JFULL'].find("累犯")!=-1 and file['JFULL'].find("未構成累犯")==-1 
										and file['JFULL'].find("不構成累犯")==-1 and file['JFULL'].find("加重其刑")!=-1)
									if(temp_lst[k_var]==k_type[i] and jd!= False):
										output[i].append([p1,p2])
										
										if(k_type[i]=="富裕"):
											#print(file['JID'])
											os.popen("cp \"./target_case/"+file['JID']+".json\" ./富裕")

										#if(file['JFULL'].find("累犯")!=-1 and file['JFULL'].find("未構成累犯")==-1 
										#	and file['JFULL'].find("不構成累犯")==-1 and file['JFULL'].find("加重其刑")!=-1):
										#	otct_lst[i][2]+=1
										if(tct==1):
											otct_lst[i][1]+=1
										elif(tct==0 or tct==2):
											otct_lst[i][0]+=1
										else:
											...
										

								#if(temp_lst[0]=="大學"):
								#	ct11+=1
								#	output.append([p1,p2])
								

							else:
								...
								#print("?")

						#=========!

					#if(file['JFULL'].find("身心障礙")!=-1):
						#	ct10+=1
					
					t_=[]

					#print(small_str)
					if(file['JFULL'].find("累犯")!=-1 and file['JFULL'].find("未構成累犯")==-1 and file['JFULL'].find("不構成累犯")==-1):
						ct11+=1
						if(file['JFULL'].find("加重其刑")!=-1 and len(temp_lst)!=0):
							#print(file['JID'])
							ct12+=1
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

#"""output
print(ct3,ct4,ct5,ct6,ct7,ct8,ct9,ct10)
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

#os.popen("mkdir fig")
jd=1

color_lst=["red","orange","yellow","green","blue","purple","black"]
color_ct=0
for i in range(len(output)):
	
	if(jd==1 and len(output[i])>0):
		#output=outlier_2D(output,sd_2D(output)[0][0],sd_2D(output)[0][1],sd_2D(output)[1][0],sd_2D(output)[1][1])
		print(k_type[i])	
		temp_ot=output[i]
		
		#"""經濟
		if(k_var==1):
			if(i==type_經濟.index("貧寒")):
				temp_ot+=output[type_經濟.index("貧窮")]
				temp_ot+=output[type_經濟.index("貧困")]
			elif(i==type_經濟.index("自述")):
				temp_ot+=output[type_經濟.index("自陳")]
				temp_ot+=output[type_經濟.index("兼衡")]
			elif(i==type_經濟.index("貧窮") or i==type_經濟.index("貧困") 
				or i==type_經濟.index("自陳") or i==type_經濟.index("兼衡")):
				continue
		#"""

		#"""學歷
		if(k_var==0):
			if(i==type_學歷.index("研究所")):
				temp_ot+=output[type_學歷.index("博士")]
				temp_ot+=output[type_學歷.index("碩士")]
			elif(i==type_學歷.index("大學")):
				temp_ot+=output[type_學歷.index("大專")]
			elif(i==type_學歷.index("五專")):
				temp_ot+=output[type_學歷.index("二專")]
				temp_ot+=output[type_學歷.index("三專")]
				temp_ot+=output[type_學歷.index("專科")]
			elif(i==type_學歷.index("高中")):
				temp_ot+=output[type_學歷.index("高職")]
			elif(i==type_學歷.index("國小")):
				temp_ot+=output[type_學歷.index("小學")]
			elif(i==type_學歷.index("自述")):
				temp_ot+=output[type_學歷.index("自陳")]
				temp_ot+=output[type_學歷.index("兼衡")]
			elif(i==type_學歷.index("博士") or i==type_學歷.index("碩士")
				or i==type_學歷.index("大專") or i==type_學歷.index("二專") 
				or i==type_學歷.index("三專") or i==type_學歷.index("專科") 
				or i==type_學歷.index("高職") or i==type_學歷.index("小學") 
				or i==type_學歷.index("自陳") or i==type_學歷.index("兼衡")):
				continue
		#"""

		a=len(temp_ot)#

		temp_ot=outlier_2D_3(temp_ot)
		simple_np=np.array(temp_ot)

		print("%.2f%s %d%s%d"%(len(temp_ot)/a*100,"%",len(temp_ot),"/",a))#
		#print(len(simple_np))
		x=[e[0] for e in simple_np]
		y=[e[1] for e in simple_np]


		plt.xlabel("value")
		plt.ylabel("fine")

		plt.xlim(0,110000)
		plt.ylim(0,200000)
		mean_ot=1
		mean_ot_lst=[1 for i in range(100)]
		mct=0

		if(t_var!=0):
			mean_ot=sum([temp_ot[i][1]/temp_ot[i][0] for i in range(len(temp_ot))])/len(temp_ot)
		else:
			mean_ot_ct=1
			for ij in range(len(temp_ot)):
				mean_ot_ct*=(temp_ot[ij][1]/temp_ot[ij][0])
				if(mean_ot_ct>=sys.maxsize/200):
					mean_ot*=mean_ot_ct**(1/len(temp_ot))
					mean_ot_ct=1
			mean_ot*=mean_ot_ct**(1/len(temp_ot))
			"""
				mean_ot_lst[mct]*=(temp_ot[ij][1]/temp_ot[ij][0])
				if(mean_ot_lst[mct]>=sys.maxsize/100):
					mean_ot*=mean_ot_lst[mct]**(1/len(temp_ot))
					mct+=1
			mean_ot*=mean_ot_lst[mct]**(1/len(temp_ot))
			"""
			print("g_mean: "+str(mean_ot))
			print("mean: "+str(sum([temp_ot[i][1]/temp_ot[i][0] for i in range(len(temp_ot))])/len(temp_ot)))
			#print("--------")
			#print(mct)

		plt.title(title)
		plt.scatter(simple_np[:,0],simple_np[:,1],1,color=color_lst[color_ct])	
		plt.plot([0,200000/mean_ot],[0,200000],color=color_lst[color_ct])
		color_ct+=1
		#plt.plot(x,y)
		
		#"""#<--------------[on,off]=[1,2]
		if(k_var==0):
			plt.savefig("./fig/學歷_ot3_"+title+".png")
		elif(k_var==1):
			plt.savefig("./fig/經濟_ot3_"+title+".png")
		else:
			plt.savefig("./fig/經濟_ot3_"+title+".png")#undone
		"""
		plt.savefig("./fig/"+("學歷" if k_var==0 else "經濟")+"/"+str(k_type[i])+"_ot3_"+title+".png")
		plt.clf()
		#"""
		#plt.show()

#"""