import requests
from bs4 import BeautifulSoup
import pandas as pd
#2022 타자 데이터 크롤링

#2022 기본기록 1페이지 타자들 30명 
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
        
    
    my_list.append(mylist[index])
    df=pd.DataFrame(my_list,columns=['rank','선수명','팀명','AVG','G','PA','AB','R','H','2B','3B','HR','TB','RBI','SAC','SF'])    
    index=index+1

#print(df)

#2022 기본기록 2페이지 타자들 30명 
response =requests.get('https://www.koreabaseball.com/Record/Player/HitterBasic/Basic2.aspx') 
soup=BeautifulSoup(response.text,'html.parser')
container=soup.select('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody >tr ')

lists=[]
index=0
mylist_2=[[]for j in range(0,30)]
my_list_2=[]

#테이블 선택자에서 td 항목 선택 후 0,1,2,3...번째 항목들 가져옴
for con in container:
    for i in range(4,15):
        detail=con.select('td')[i].text
        #print(detail)
        mylist_2[index].append(detail)
        
    #print(detail)
    #print('\n')
    my_list_2.append(mylist_2[index])
    df_2=pd.DataFrame(my_list_2,columns=['BB','IBB','HBP','SO','GDP','SLG','OBP','OPS','MH','RISP','PH-BA'])    
    index=index+1

#print(df_2)

df=pd.concat([df,df_2],axis=1)
#print(df)

#2022 세부기록 1페이지 타자들 30명
response =requests.get('https://www.koreabaseball.com/Record/Player/HitterBasic/Detail1.aspx') 
soup=BeautifulSoup(response.text,'html.parser')
container=soup.select('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody >tr ')

lists=[]
index=0
mylist_3=[[]for j in range(0,30)]
my_list_3=[]

#테이블 선택자에서 td 항목 선택 후 0,1,2,3...번째 항목들 가져옴
for con in container:
    for i in range(4,14):
        detail=con.select('td')[i].text
        #print(detail)
        mylist_3[index].append(detail)
        
    
    my_list_3.append(mylist_3[index])
    df_3=pd.DataFrame(my_list_3,columns=['XBH','GO','AO','GO/AO','GWRBI','BB/K','P/PA','ISOP','XR','GPA'])    
    index=index+1

df=pd.concat([df,df_3],axis=1)
print(df)
#절대경로 설정시 \\ 두개씩 쳐줘야함
df.to_excel('C:\\Users\\asd\\Desktop\\KBO_HR_predict\\2022_KBO_DATA_crwaling.xlsx',sheet_name='2022_KBO_DATA_crawling_ver',index=False)
