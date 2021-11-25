"""
list_a=os.popen("cat ./stuff_type/a.txt").readlines()
list_b=os.popen("cat ./stuff_type/b.txt").readlines()
list_c=os.popen("cat ./stuff_type/c.txt").readlines()
list_a=[i.replace("\n","") if i.find("\n")!=-1 else i for i in list_a]
list_b=[i.replace("\n","") if i.find("\n")!=-1 else i for i in list_c]
list_c=[i.replace("\n","") if i.find("\n")!=-1 else i for i in list_c]
#"""

累犯=["竊盜前科","竊盜之前科","竊盜之前案","累犯"]
學歷=["智識程度","學歷","教育"]

經濟=["經濟","家庭狀況","生活狀況"]


start_point="主  文\r\n"
mid_list=["犯 罪 事 實 及 理 由\r\n","犯罪事實","犯 罪 事 實 及 理 由","事實及理由\r\n","    事實及理由\r\n","  理  由\r\n","理    由\r\n","    事實及理由\r\n","    事實理由及證據\r\n","    事 實 理 由 及 證 據\r\n","事實理由及證據\r\n","事實及證據理由\r\n","理      由\r\n","  "]
start_list=["主  文\r\n","主    文\r\n","主　 文\r\n","主      文\r\n","    主　　　文\r\n","    主　　文\r\n","     文\r\n","主  文"]
#end_point="    理  由\r\n"
mid_point="    事實及理由\r\n"
end_point="中    華    民    國"
end_list=["中    華    民    國","中      華      民      國","中　　華　　民　　國"]
#target_keyword=[["所得"]]
key_char_list=["價值","內","之",",","，"]
keyward="徒手竊取"


type_學歷=["碩士","大學","大專","五專","三專","二專","專科","高中","高職","國中","國小","小學"]
count_學歷=[0 for i in range(len(type_學歷))]
type_狀態=["畢業","肄業",""]#假定"畢業"=""
#type_學歷+=["健全","成熟"]


type_經濟=["富裕","小康","勉持","貧寒","貧窮","貧困"]
count_經濟=[0 for i in range(len(type_經濟))]

#"""
count_學歷+=[0,0,0]
count_經濟+=[0,0,0]
type_學歷+=["自述","自陳","兼衡"]
type_經濟+=["自述","自陳","兼衡"]
#"""
