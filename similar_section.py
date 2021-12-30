from zh_calculator import number_only,number_k_switch

def find_similar_part(full,the_section,hard):
	int_t=0
	if(hard==-1):
		return False
	else:
		
		if(full.find("按月")!=-1):
			full=full[full.find("按月"):]
		if(full.find("給付")!=-1):
			full=full[full.find("給付"):]
		full=full[full.find("幣")+1:]
		t=full[:full.find("元")+1]
		if(t.find("0")!=-1 or t.find("1")!=-1 or t.find("2")!=-1 or t.find("3")!=-1 or t.find("4")!=-1 
			or t.find("5")!=-1 or t.find("6")!=-1 or t.find("7")!=-1 or t.find("8")!=-1 or t.find("9")!=-1):
			#sum_str=number_k_switch(t.replace(",","").replace("萬","").replace("元",""))
			t=t.replace("萬","").replace("元","")
			#print(t)
			t=number_only(t,number_int)
			#print(t)
			sum_str=number_k_switch(t)
		else:
			t=pre_calculator(t)
			#print(t)
			
			if(t.find("萬")!=-1):
				if(len(t[t.find("萬"):t.find("元")])>0):
					int_t=fake_calculator(t[:t.find("萬")]+"元",0)*10000+fake_calculator(t[t.find("萬")+1:],0)
				else:
					int_t=fake_calculator(t,0)			
			else:
				int_t=fake_calculator(t,0)

			sum_str=number_k_switch(int_t)
		if(hard==1):
			print(Fore.YELLOW+sum_str)
			print(Style.RESET_ALL)
		#"""
		sum_str_2="r"
		if(int_t>=10000):
			sum_str_2=number_k_switch(int(int_t/10000))+"萬"+number_k_switch(int(int_t%10000))
		#"""

		if(the_section.find(sum_str)!=-1):
			return the_section.find(sum_str)
		elif(sum_str_2!="r" and the_section.find(sum_str_2)!=-1):
			return the_section.find(sum_str_2)
		else:
			return the_section.find(sum_str)


#"""
def find_keyward_target(full,target,k_list):
	f=True
	ct=0
	shallow_target=target
	find_ed=0
	while f:
		if(shallow_target.find("扶養費")!=-1 or shallow_target.find("給付")!=-1):
			if(shallow_target.find("扶養費")!=-1):
				ct+=1
				print("---------"+str(ct)+"---------")
				find_ed=print_section(full,shallow_target,shallow_target.find("扶養費"),True)
				shallow_target=shallow_target[find_ed:]
			"""
			if(shallow_target.find("其後十二期之給付視為")!=-1):
				ct+=1
				print("---------"+str(ct)+"---------")
				find_ed=print_section(shallow_target,shallow_target.find("其後十二期之給付視為"),True)
				shallow_target=shallow_target[find_ed:]
			"""
			if(shallow_target.find("給付")!=-1):
				ct+=1
				print("---------"+str(ct)+"---------")
				find_ed=print_section(full,shallow_target,shallow_target.find("給付"),True)
				shallow_target=shallow_target[find_ed:]
		else:
			break
