number_zh=["零","壹","貳","參","肆","伍","陸","柒","捌","玖","拾","佰","仟","萬","一","二","三","四","五","六","七","八","九","十"]
number_int=["0","1","2","3","4","5","6","7","8","9"]
def number_only(target,the_list):
	for char_i in range(len(target)):
		jd=0
		for ct_i in the_list:
			if(target[char_i]!=ct_i):
				jd+=1
		if(jd==len(the_list)):
			target=target[:char_i]+"r"+target[char_i+1:]

	target=target.replace("r","")
	return target

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
	
	if(target.find("元")!=-1 or offset>0):
		if(target.find("元")!=-1 and (target[target.find("元")-1]=="拾" or target[target.find("元")-1]=="佰" or target[target.find("元")-1]=="仟" or target[target.find("元")-1]=="萬")):
			
			t=target[target.find("元")-1]
			if(t=="拾"):
				offset+=1
			elif(t=="佰"):
				offset+=2
			elif(t=="仟"):
				offset+=3
			elif(t=="萬"):
				offset+=4
			return fake_calculator(target[:target.find("元")-1],offset)
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
			sum=int(str_sum)
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
def enter(t1):
	if(t1.find("0")!=-1 or t1.find("1")!=-1 or t1.find("2")!=-1 or t1.find("3")!=-1 or t1.find("4")!=-1 
		or t1.find("5")!=-1 or t1.find("6")!=-1 or t1.find("7")!=-1 or t1.find("8")!=-1 or t1.find("9")!=-1):
				#sum_str=number_k_switch(t.replace(",","").replace("萬","").replace("元",""))
		t1=number_only(t1,number_int)
		#print(t1)
		#print(number_k_switch(t1))
		return number_k_switch(t1)
	else:
		t1=pre_calculator(t1)
		int_t1=0
		if(t1.find("萬")!=-1):
			if(len(t1[t1.find("萬"):t1.find("元")])>1):
				int_t1=fake_calculator(t1[:t1.find("萬")+1]+"元",0)+fake_calculator(t1[t1.find("萬")+1:],0)
			else:
				int_t1=fake_calculator(t1,0)
		else:
			int_t1=fake_calculator(t1,0)


		#print(t1)
		#print(number_k_switch(int_t1))
		return number_k_switch(int_t1)