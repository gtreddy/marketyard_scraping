import pandas as  pd
import json

#df_list=pd.read_html("http://www.puneapmc.org/history.aspx?id=Rates3144")
#k=df_list[2]
#data=k[0:2][1:4]
#print(data)
def url_parse(u):
    df_list=pd.read_html(u)
    k=df_list[2]
    data=k[0:2][1:4]
    return data
#url_parse("http://www.puneapmc.org/history.aspx?id=Rates3144")
ds=[]
for i in range(1,45):
    x=url_parse("http://www.puneapmc.org/history.aspx?id=Rates"+str(3061+i))
    ds.append(x)

#print(ds)
f=open('test.txt','wb')
for item in ds:
    f.write(("%s\n" % str(item)).encode("UTF-8"))

f.close()
