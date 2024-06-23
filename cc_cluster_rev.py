import os
import json
import numpy as np
from numpy.linalg import norm
from tqdm import tqdm

import math
#-------global variables-------
_file_ouput=(1==1)
_reduced_data=True
_float_size=4
_target=json.load(open("../2022~2023_sigmoid_all_result.json"))
_index=json.load(open("../2022~2023_sigmoid_result.json"))
#print([i for i in _index])
#------------------------------
#-------helper functions-------
def find_center(_cluster,id_lst):
    global sig_sim_lst
    tp_lst=np.array([sig_sim_lst[id_lst.index(_e)] for _e in _cluster])
    temp=np.average(tp_lst, axis=0)
    cs_lst=[[cos_sim(tp_lst[_e],temp),_cluster[_e]] for _e in range(len(tp_lst))]
    tp=max(cs_lst)[-1]
    return tp
def dist_find_center(_cluster,id_lst):
    global _target#[str(i)+'&'+str(j)]
    m_lst=[[0 for j in _cluster] for i in _cluster]
    for i in range(len(_cluster)):
        for j in range(len(_cluster)):
            if i==j:
                m_lst[i][j]=0
            elif i>j:
                temp=str(id_lst.index(_cluster[i]))+'&'+str(id_lst.index(_cluster[j])) if str(id_lst.index(_cluster[i]))+'&'+str(id_lst.index(_cluster[j])) in _target else str(id_lst.index(_cluster[j]))+'&'+str(id_lst.index(_cluster[i]))
                m_lst[i][j]=1-_target[temp]
                m_lst[j][i]=1-_target[temp]
    tp_lst=min(m_lst,key=lambda x:sum(x))
    tp=_cluster[m_lst.index(tp_lst)]
    return tp
def o_find_center(_cluster,id_lst):
    #print(_cluster)
    global sig_sim_lst
    e=2.718281828459
    import math

    temp=[[0 if i==j else math.log(abs(1-sig_sim_lst[id_lst.index(i)][id_lst.index(j)])+0.000000001,e) for j in _cluster] for i in _cluster]
    _max=-10000000000
    tp=''
    for i in range(len(temp)):
        if sum(temp[i])>_max:
            tp=_cluster[i]
            _max=sum(temp[i])
    return tp
def dict_index(v,d,_all=False):
    return [i for i in d if v in d[i]] if _all else [i for i in d if v in d[i]][0]
def cos_sim(a,b):
    global _reduced_data,_float_size
    return round(float(np.dot(a,b)/(norm(a)*norm(b))),_float_size) if _reduced_data else float(np.dot(a,b)/(norm(a)*norm(b)))
def jl(p):
    with open(p,'r',encoding='utf8') as f:
        lst=list(f)
    return [json.loads(s) for s in lst]

def most_sim():
    global train_test_sim,train_id,test_id
    temp=[]
    temp_max=[]
    ncs_lst=np.array(train_test_sim)
    for e in range(len(test_id)):
        
        _max=-1
        _max_id=0
        mtp=list(ncs_lst[:,e])  
        _max=max(mtp)
        _max_id=train_id[mtp.index(_max)]
        
        #print(_max_id)
        #print(test_id[e])
        temp.append(_max_id)
        temp_max.append(_max)
    return temp,temp_max

def list_set(lst):
    tp=[]
    for i in lst:
        if i not in tp:
            tp.append(i)
    return tp


def clusters(id_lst,v_sim_lst,r,r_r=2):

  sim_lst=[[(id_lst[i],id_lst[j]) for j in range(len(v_sim_lst)) if i!=j and v_sim_lst[i][j]>=r]for i in range(len(v_sim_lst))]
  n_clusters={}
  ct=0
  jd=[]
  rr=r**r_r

  for i in tqdm(range(len(id_lst))):
    if sim_lst[i]==[] and (id_lst[i] not in jd):
      
      ct+=1
      temp=[id_lst[i]]
      jd.append(id_lst[i])
      n_clusters[str(ct)]=temp
    else:
      
      tp=[e[1] for e in sim_lst[i]]
      if id_lst[i] not in jd:

        ct+=1
        jd.append(id_lst[i])
        temp=[id_lst[i]] 
        for e in tp:
          if e not in jd:
            temp.append(e)
            jd.append(e)
        n_clusters[str(ct)]=temp
      else:
        
        ttp=dict_index(id_lst[i],n_clusters)
        id=n_clusters[ttp][0]

        for e in tp:
          if e not in jd:
            if(v_sim_lst[id_lst.index(id)][id_lst.index(e)]>=rr):

              jd.append(e)
              n_clusters[ttp].append(e)
            else:
              
              ct+=1
              temp=[e]
              jd.append(e)
              n_clusters[str(ct)]=temp
  if _file_ouput:
        file= open("../case22~23_clusters_"+str(r)[2:4]+"_"+str(r_r)+".json","w",encoding='utf8')
        json.dump({'clusters':n_clusters},file,ensure_ascii=False)
        file.close()
  return n_clusters 
def cc_clusters(o_id_lst,v_sim_lst,r,r_r=2):
    global _file_ouput
    id_lst=sorted(o_id_lst)
    sim_lst=[[(id_lst[i],id_lst[j]) for j in range(len(v_sim_lst)) if i!=j and v_sim_lst[o_id_lst.index(id_lst[i])][o_id_lst.index(id_lst[j])]>=r]for i in range(len(v_sim_lst))]
    n_clusters={}
    ct=0
    jd=[]
    rr=r**r_r
    jjd=[]
    for i in tqdm(range(len(id_lst))):
        #print(i)
        if sim_lst[i]==[] and (id_lst[i] not in jd):
            
            ct+=1
            temp=[id_lst[i]]
            jd.append(id_lst[i])
            n_clusters[str(ct)]=temp
        else:
            
            tp=[e[1] for e in sim_lst[i]]
            if id_lst[i] not in jd:

                ct+=1
                jd.append(id_lst[i])
                temp=[id_lst[i]] 
                for e in tp:
                    if e not in jd:
                        temp.append(e)
                        jd.append(e)
                        ttp=[ee[1] for ee in sim_lst[id_lst.index(e)]]
                        for ee in ttp:
                            if ee not in jd:
                                if v_sim_lst[o_id_lst.index(ee)][o_id_lst.index(id_lst[i])]>=rr:
                                    temp.append(ee)
                                    jd.append(ee)
                n_clusters[str(ct)]=temp
            else:
                
                ttps=dict_index(id_lst[i],n_clusters,1==1)
                #ttp=dict_index(id_lst[i],n_clusters)
                #id=n_clusters[ttp][0]
                #id=find_center(n_clusters[ttp],id_lst)
                ids=[find_center(n_clusters[e],id_lst) for e in ttps]

                for e in tp:
                    if e not in jd:
                        max_cs=-1
                        max_id=-1
                        for _e in ids:
                            _tp=v_sim_lst[o_id_lst.index(_e)][o_id_lst.index(e)]
                            if _tp>=rr and _tp>max_cs:
                                max_id=_e
                        if max_id!=-1:
                        
                            jd.append(e)
                            n_clusters[ttps[ids.index(max_id)]].append(e)
                        else:                           
                            ct+=1
                            temp=[e]
                            jd.append(e)
                            n_clusters[str(ct)]=temp
    if _file_ouput:
        file= open("../v_case22~23_cc_clusters_"+str(r)[2:4]+"_"+str(r_r)+".json","w",encoding='utf8')
        json.dump({'clusters':n_clusters},file,ensure_ascii=False)
        file.close()
    
    return n_clusters
#------------------------------
#-------processing functions-------

sig_sim_lst=[[-2 if _e!=_ee else 1 for _ee in range(len(_index['id']))] for _e in range(len(_index['id']))]
for i in tqdm(range(len(_index['id']))):
    for j in range(len(_index['id'])):
        if i>j:
            temp=_target[str(i)+'&'+str(j)]
            sig_sim_lst[i][j]=temp
            sig_sim_lst[j][i]=temp
#print(sig_sim_lst[-1])
file= open("./2022~2023_case_sigmoid_sim.json","w",encoding='utf8')
json.dump({'sig_sim':sig_sim_lst,"id":_index['id']},file,ensure_ascii=False)
file.close()
print(len(sig_sim_lst))
sig_sim_lst_np=np.array(sig_sim_lst)
sig_1d_lst=sig_sim_lst_np.reshape((len(sig_sim_lst)*len(sig_sim_lst[0])))
q_lst=np.quantile(sig_1d_lst, [0,0.25,0.5,0.75,1])
th_lower=q_lst[1]-1.5*(q_lst[3]-q_lst[1])
th_upper=q_lst[3]+1.5*(q_lst[3]-q_lst[1])
#print(len(sig_1d_lst))
tp_lst=[_e for _e in sig_1d_lst if _e >= th_lower and _e<=th_upper]
_r=(max(tp_lst)-min(tp_lst))*0.8+min(tp_lst)
r_r=1.2#q_lst[3]/q_lst[2]

_file_ouput=(1==1)
#clusters(_index['id'],sig_sim_lst,_r,r_r)
cc_clusters(_index['id'],sig_sim_lst,_r,r_r)
#print(len(tp_lst))
