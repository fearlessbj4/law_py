from section_cut import find_after,search_from_list

element_char="元"#init_

number_zh=["零","壹","貳","參","肆","伍","陸","柒","捌","玖","拾","佰","仟","萬","一","二","三","四","五","六","七","八","九","十"]
number_int=["0","1","2","3","4","5","6","7","8","9"]
number_int_full=["０","１","２","３","４","５","６","７","８","９"]
number_all=number_zh+number_int+number_int_full

def is_number(target):
	global number_all
	if(number_all.count(target)!=0):
		return enter(str(tar)+"元","元")
	else:
		return int(-1)
def number_only(target,the_list):
	for char_i in range(len(target)):
		jd=0
		for ct_i in the_list:
			if(target[char_i]!=ct_i):
				jd+=1
		if(jd==len(the_list)):
			target=target[:char_i]+"r"+target[char_i+1:]

	target=target.replace("r","")
	return int(target)

def pre_calculator(target):
	if(target.find("零")!=-1):
		if(target.find("萬")!=-1):
			target=pre_calculator(target[:target.find("萬")])+"萬"+pre_calculator(target[target.find("萬")+1:])
			return target
		else:#1002,2003
			if((target.find("仟")!=-1 or target.find("千")!=-1) 
				and (target.find("佰")==-1 or target.find("百")==-1)
				and (target.find("拾")==-1 or target.find("十")==-1)):
				target=target[:target.find("零")]+"零"+target[target.find("零"):]
				
				return target
			#0020,0003
			elif((target.find("仟")==-1 or target.find("千")==-1) 
				and (target.find("佰")==-1 or target.find("百")==-1)):
				if(target.find("拾")!=-1 or target.find("十")!=-1):
					target=target[:target.find("零")]+"零"+target[target.find("零"):]
				else:
					target=target[:target.find("零")]+"零零"+target[target.find("零"):]

				return target			
	else:
		return target
def fake_calculator(target,offset):
	sum=0


	if(target.find(element_char)!=-1 or offset>0):
		if(target.find(element_char)!=-1 and (target[target.find(element_char)-1]=="拾" or target[target.find(element_char)-1]=="佰" or target[target.find(element_char)-1]=="仟" or target[target.find(element_char)-1]=="萬")):
			
			t=target[target.find(element_char)-1]
			if(t=="拾"):
				offset+=1
			elif(t=="佰"):
				offset+=2
			elif(t=="仟"):
				offset+=3
			elif(t=="萬"):
				offset+=4
			return fake_calculator(target[:target.find(element_char)-1],offset)
		elif(len(target)==0):
			sum=-1
			return sum
		elif(target[-1]=="拾" or target[-1]=="佰" or target[-1]=="仟" or target[-1]=="萬"):
			
			t=target[-1]
			if(t=="拾"):
				offset+=1
			elif(t=="佰"):
				offset+=2
			elif(t=="仟"):
				offset+=3
			elif(t=="萬"):
				offset+=4

			if(target=="拾"):
				return fake_calculator("壹",offset)
			else:
				return fake_calculator(target[:-1],offset)
		
		else:
			

			f=True
			target=target.replace("拾","").replace("佰","").replace("仟","").replace("萬","")
			str_sum=""
			while f:
				for char in target:
					jd=0
					for char_i in range(0,10,1):
						if(char==number_zh[char_i]):
							jd=1
							str_sum+=str(char_i)
							break

				break				

			str_sum+="0"*offset
			sum=(int(str_sum) if (str_sum!='') else 0)
			return sum


	else:
		sum=-1
	return sum
def number_k_switch(sum):
	s=""
	for i in range(len(str(sum))):
		if((len(str(sum))-i)%3==0 and i!=0):
			s+=","

		s+=str(sum)[i]
	return s

#t1="1009萬0020元"
#t1="壹仟零玖萬零貳拾元"
def enter(t1,e):
	global element_char
	element_char=str(e)#防呆
	sum=0
	t1=t1.replace("千","仟")
	if(find_after(t1,element_char,element_char)!=-1):
		t1_t=t1
		while (t1_t.find(element_char)!=-1):
			t1_h=t1_t[:t1_t.find(element_char)+1]
			t1_t=t1_t[t1_t.find(element_char)+1:]
			if(int(main(t1_h).replace(",",""))==-1):
				sum+=0
			else:
				sum+=int(main(t1_h).replace(",",""))
		return sum
	else:
		if(int(main(t1).replace(",",""))==-1):
			sum+=0
		else:
			sum+=int(main(t1).replace(",",""))
		return sum

def pre(t1):
	t1=t1.replace("\r\n"," ")
	t1=t1.replace(" ","")
	t1=t1.replace("千","仟")
	if(t1.find("拾")!=-1):
		
		if(search_from_list(number_zh,t1[t1.find("拾")-1])==-1):
			t1=t1.replace("拾","壹拾")
	t1=t1.replace(",","")
	anchor_char=element_char
	ed=t1.find(element_char)#should equal to len(t1)-1
	st=ed+1
	for i in range(ed-1,-1,-1):
		if(search_from_list(number_all,t1[i])!=-1):
			st=i
		else:
			break
	return t1[st:ed+1]



def main(t1):
	t1=pre(t1)
	
	if(t1.find("0")!=-1 or t1.find("1")!=-1 or t1.find("2")!=-1 or t1.find("3")!=-1 or t1.find("4")!=-1 
		or t1.find("5")!=-1 or t1.find("6")!=-1 or t1.find("7")!=-1 or t1.find("8")!=-1 or t1.find("9")!=-1):
				#sum_str=number_k_switch(t.replace(",","").replace("萬","").replace("元",""))
		#t1=t1.replace("萬","0000")
		#t1=t1.replace("仟","千").replace("千","000")
		if(t1.find("萬")!=-1 and t1.find("仟")==-1):
			if(len(t1[t1.find("萬"):t1.find(element_char)])>1):
				t1=str(number_only(t1[:t1.find("萬")+1].replace("萬","0000"),number_int)+number_only(t1[t1.find("萬")+1:],number_int))
			else:
				t1=str(number_only(t1.replace("萬","0000"),number_int))
		elif(t1.find("萬")==-1 and t1.find("仟")!=-1):
			if(len(t1[t1.find("仟"):t1.find(element_char)])>1):
				t1=str(number_only(t1[:t1.find("仟")+1].replace("仟","000"),number_int)+number_only(t1[t1.find("仟")+1:],number_int))
			else:
				t1=str(number_only(t1.replace("仟","000"),number_int))
		elif(t1.find("萬")!=-1 and t1.find("仟")!=-1):
			if(len(t1[t1.find("仟"):t1.find(element_char)])>1):
				t1=str(number_only(t1[:t1.find("仟")+1].replace("萬","").replace("仟","000"),number_int)+number_only(t1[t1.find("仟")+1:],number_int))
			else:
				t1=str(number_only(t1.replace("萬","").replace("仟","000"),number_int))
		else:
			t1=number_only(t1,number_int)
		#print(t1)
		#print(number_k_switch(t1))

		return number_k_switch(t1)
	else:
		t1=pre_calculator(t1)
		int_t1=0
		if(t1.find("萬")!=-1):
			if(len(t1[t1.find("萬"):t1.find(element_char)])>1):
				int_t1=fake_calculator(t1[:t1.find("萬")+1]+element_char,0)+fake_calculator(t1[t1.find("萬")+1:],0)
			else:
				int_t1=fake_calculator(t1,0)
		else:
			int_t1=fake_calculator(t1,0)


		#print(t1)
		#print(number_k_switch(int_t1))
		return number_k_switch(int_t1)
