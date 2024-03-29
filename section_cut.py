def cut(lst,mode,start_point,mid_point,end_point,start_list,mid_list,end_list):
	shallow_stp=start_point
	shallow_mdp=mid_point
	shallow_edp=end_point
	for sti in range(len(start_list)):
		if(lst.find(start_list[sti])!=-1):
			shallow_stp=start_list[sti]
			break
		else:
			continue
	for mdi in range(len(mid_list)):
		if(lst.find(mid_list[mdi])!=-1):
			shallow_mdp=mid_list[mdi]
			break
		else:
			continue
	for edi in range(len(end_list)):
		if(lst.find(end_list[edi])!=-1):
			shallow_edp=end_list[edi]
			break
		else:
			continue

	r_lst=lst[lst.find(shallow_stp)+len(shallow_stp):lst.find(shallow_edp)]
	

	if(mode=="short"):
		
		return r_lst[:r_lst.find(shallow_mdp)]
	elif(mode=="mid"):
		return r_lst[r_lst.find(shallow_mdp):]
	else:
		return r_lst

def find_after(lst,anchor_keyward,the_keyward):
	if(lst.find(anchor_keyward)==-1 or lst.find(the_keyward)==-1):
		return int(-1)
	elif(lst[lst.find(anchor_keyward)+len(anchor_keyward):].find(the_keyward)<=-1):
		return int(-1)

	else:
		return int(lst.find(anchor_keyward)+len(anchor_keyward)+lst[lst.find(anchor_keyward)+len(anchor_keyward):].find(the_keyward))

def find_context(lst,anchor_keyward,the_keyward,offset):
	if(lst.find(anchor_keyward)!=-1 and lst.find(the_keyward)!=-1):
		st=(lst.find(anchor_keyward)-offset)
		ed=(lst.find(anchor_keyward)+offset)+len(anchor_keyward)
		st=st if st>=0 else 0
		ed=ed if ed<=(len(lst)-1) else len(lst)-1
		if(lst[st:ed].find(the_keyward)!=-1):
			return int(st+lst[st:ed].find(the_keyward))
		else:
			return int(-1)

	else:
		return int(-1)

def search_from_list(lst,target):
	flag=-1
	for i in range(len(lst)):
		if(target==lst[i]):
			flag=i
			break
	return int(flag)
def find_from_list(target,lst):
	flag=-1
	for i in range(len(lst)):
		if(target.find(lst[i])!=-1):
			flag=i
			break
	return int(flag)
	
def find_all_from_list(lst,target):
	flag=[]
	for i in range(len(lst)):
		if(target.find(lst[i])!=-1):
			flag.append(i)
	return flag
def revise(lst,revise_lst):
	revised_lst=lst
	for i in revised_lst:
		revised_lst=revised_lst.replace(i,"-")
	return revised_lst

