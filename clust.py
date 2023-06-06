import json
vec_sim_lst=json.load(open('../clause/pre/ex_corpus_3837_vecs_sim_f3.json','r'))['corpus_vecs_sim']
#vec_lst=json.load(open('../clause/pre/corpus_3837_vec.json','r'))
id_lst=json.load(open('../clause/ex_corpus_id.json','r'))['id']
str_lst=json.load(open('../clause/pre/corpus_3837_str.json','r'))
print(len(id_lst))
#vec_lst=vec_lst
#id_lst=id_lst[:100]

r=0.96
#sim_lst=[[(id_lst[i],id_lst[j]) for j in range(len(v_sim_lst)) if i!=j and v_sim_lst[i][j]>=r]for i in range(len(v_sim_lst))]

import numpy as np
from numpy.linalg import norm
def cos_sim(a,b):
  return np.dot(a,b)/(norm(a)*norm(b))
def dict_index(v,d,_all=False):
  return [i for i in d if v in d[i]] if _all else [i for i in d if v in d[i]][0]
def find_center(_cluster,id_lst):
  global vec_sim_lst
  e=2.718281828459
  import math

  temp=[[0 if vec_sim_lst[id_lst.index(i)][id_lst.index(j)]>=1 else math.log((1-vec_sim_lst[id_lst.index(i)][id_lst.index(j)]),e) for j in _cluster] for i in _cluster]
  _max=-10000000000
  tp=''
  for i in range(len(temp)):
    if sum(temp[i])>_max:
      tp=_cluster[i]
      _max=sum(temp[i])
  return tp

def clusters(id_lst,v_sim_lst,r,r_r=2):

  sim_lst=[[(id_lst[i],id_lst[j]) for j in range(len(v_sim_lst)) if i!=j and v_sim_lst[i][j]>=r]for i in range(len(v_sim_lst))]
  n_clusters={}
  ct=0
  jd=[]
  rr=r**r_r

  for i in range(len(id_lst)):
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
  return n_clusters 
def cc_clusters(id_lst,v_sim_lst,r,r_r=2):

  sim_lst=[[(id_lst[i],id_lst[j]) for j in range(len(v_sim_lst)) if i!=j and v_sim_lst[i][j]>=r]for i in range(len(v_sim_lst))]
  n_clusters={}
  ct=0
  jd=[]
  rr=r**r_r
  jjd=[]
  for i in range(len(id_lst)):
    print(i)
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
                if v_sim_lst[id_lst.index(ee)][i]>=rr:
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
              _tp=v_sim_lst[id_lst.index(_e)][id_lst.index(e)]
              if _tp>=rr and _tp>max_cs:
                max_id=_e
            if max_id!=-1:
            #if(v_sim_lst[id_lst.index(id)][id_lst.index(e)]>=rr):

              jd.append(e)
              n_clusters[ttps[ids.index(max_id)]].append(e)
            else:
              
              ct+=1
              temp=[e]
              jd.append(e)
              n_clusters[str(ct)]=temp
        


  return n_clusters    
#--------------------------------------
def vec_to_cs(id_lst,vec_lst):
  cs_lst=[[0 for j in range(len(id_lst))]for i in range(len(id_lst))]
  for i in range(len(id_lst)):
    print(i)
    for j in range(len(id_lst)):
      if i==j:
        cs_lst[i][j]=1
      elif i>j and cs_lst[i][j]==0:
        tp_lst=id_lst[i].split('@')
        f_0=tp_lst[0]
        s_0=int(tp_lst[1])
        ttp_lst=id_lst[j].split('@')
        f_1=ttp_lst[0]
        s_1=int(ttp_lst[1])
        tp=cos_sim(vec_lst[f_0][s_0],vec_lst[f_1][s_1])
        tp=round(tp,3)
        cs_lst[i][j]=tp
        cs_lst[j][i]=tp
  return cs_lst
def non_cs_clusters(id_lst,vec_lst,r,r_r=2):
  cs_lst=[[0 for j in range(len(id_lst))]for i in range(len(id_lst))]
  for i in range(len(id_lst)):
    print(i)
    for j in range(len(id_lst)):
      if i==j:
        cs_lst[i][j]=1
      elif i>j and cs_lst[i][j]==0:
        tp_lst=id_lst[i].split('@')
        f_0=tp_lst[0]
        s_0=int(tp_lst[1])
        ttp_lst=id_lst[j].split('@')
        f_1=ttp_lst[0]
        s_1=int(ttp_lst[1])
        tp=cos_sim(vec_lst[f_0][s_0],vec_lst[f_1][s_1])
        tp=round(tp,3)
        cs_lst[i][j]=tp
        cs_lst[j][i]=tp
  sim_lst=[]
  #=[[(id_lst[i],id_lst[j]) for j in range(len(id_lst)) if i!=j and cos_sim(id_lst[i],)>=r] for i in range(len(id_lst))]
  print('---')
  for i in range(len(id_lst)):
    print(i)
    temp=[]
    for j in range(len(id_lst)):
      if i!=j:
        
        if cs_lst[i][j]>=r:
          temp.append((id_lst[i],id_lst[j]))
    sim_lst.append(temp)

  n_clusters={}
  ct=0
  jd=[]
  rr=r**r_r

  for i in range(len(id_lst)):
    print('--'+str(i))
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
            #if(v_sim_lst[id_lst.index(id)][id_lst.index(e)]>=rr):
            tp_lst=id.split('@')
            f_0=tp_lst[0]
            s_0=int(tp_lst[1])
            ttp_lst=e.split('@')
            f_1=ttp_lst[0]
            s_1=int(ttp_lst[1])
            if(cos_sim(vec_lst[f_0][s_0],vec_lst[f_1][s_1])>=rr):
              jd.append(e)
              n_clusters[ttp].append(e)
            else:
              
              ct+=1
              temp=[e]
              jd.append(e)
              n_clusters[str(ct)]=temp
  return n_clusters

#v_cs=vec_to_cs(id_lst,vec_lst)
#file= open("../clause/pre/ex_corpus_3837_vecs_sim.json","w",encoding='utf8')
#json.dump({'corpus_vecs_sim':v_cs},file,ensure_ascii=False)
#file.close()
#"""
#n_clusters=clusters(id_lst,v_sim_lst,r,1.2)
n_clusters=cc_clusters(id_lst,vec_sim_lst,r,1.2)
print(sum([len(n_clusters[i]) for i in n_clusters]))
print(len(n_clusters))

file= open("../clause/cc_ex_clusters_str_"+str(r)[2:]+".json","w",encoding='utf8')
json.dump({'clusters_str':n_clusters},file,ensure_ascii=False)
file.close()
str_c={}

for i in n_clusters:
  temp=[]
  for e in n_clusters[i]:
    print(e)
    si=e.split('@')
    
    temp.append(str_lst[si[0]][int(si[1])])
  str_c[i]=temp

file= open("../clause/cc_ex_clusters_"+str(r)[2:]+".json","w",encoding='utf8')
json.dump({'clusters':str_c},file,ensure_ascii=False)
file.close()
#"""

#print(str_c)
#print(n_clusters)