import requests
from bs4 import BeautifulSoup
import pandas as pd



response = requests.get('https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx')

soup=BeautifulSoup(response.text,'html.parser')

#테이블에 해당하는 선택자 (selector)
container=soup.select('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody >tr ')

lists=[]
index=0
df=pd.DataFrame()
mylist=[[]for j in range(0,30)]
my_list=[]


#테이블 선택자에서 td 항목 선택 후 0,1,2,3...번째 항목들 가져옴
for con in container:
    for i in range(0,16):
        detail=con.select('td')[i].text
        mylist[index].append(detail)
        
    #print(mylist[index])
    #print('\n')
    my_list.append(mylist[index])
    
    df=pd.DataFrame(my_list,columns=['rank','선수명','팀명','AVG','G','PA','AB','R','H','2B','3B','HR','TB','RBI','SAC','SF'])    
        
    
   
    #print(lists)
    #print('\n')
    index=index+1
#print(my_list)   
print(df)