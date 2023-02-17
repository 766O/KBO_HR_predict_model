# -*- coding: utf -8 -*-
from flask import Flask,render_template,request

import datetime
import pandas as pd
import numpy as np
import pickle
import joblib
from sklearn.preprocessing import RobustScaler

X = pd.DataFrame(pd.read_csv('./ml/2016-2021_data.csv',engine='python',encoding='CP949'))
Y = pd.DataFrame(pd.read_csv('./ml/2022_data.csv',engine='python',encoding='CP949'))
X=X.drop(['선수명','팀명','Year'],axis=1)
X=X.drop(['AVG','G','PA','AB','H','3B','SAC','SF','AO','GO','BB/K','P/PA'],axis=1)
X_result=np.log1p(X['HR'])
X=X.drop(['HR'],axis=1)
Y_result=np.log1p(Y['HR'])
Y=Y.drop(['  Year','HR','선수명', '팀명', 'AVG', 'G', 'PA', 'AB','3B',
       'HR','SAC', 'SF','GO', 'AO','BB/K', 'P/PA'],axis=1)
Y=Y.drop(['H'],axis=1)
X=X.drop(['GO/AO'],axis=1)
Y=Y.drop(['GO/AO'],axis=1)

X_train=X
X_test=Y

rs=RobustScaler()
rs_Xtrain=rs.fit_transform(X_train) #학습X데이터
print(rs_Xtrain.shape)

app=Flask(__name__)

#model=joblib.load('./model/voting_predict_model.pkl')
#arr=np.array([99,46,338,144,79,9,0.276,136.4,0.372])
#pred=model.predict(arr)
#print(pred)

@app.route("/",methods=['GET','POST'])

def index():
	if request.method=='GET':
		return render_template('index.html')
	if request.method=='POST':
		R=int(request.form['R'])
		secondB =int(request.form['2B'])
		TB = int(request.form['TB'])
		RBI = int(request.form['RBI'])
		XBH=int(request.form['XBH'])
		GWRBI = int(request.form['GWRBI'])
		ISOP = float(request.form['ISOP'])
		XR=float(request.form['XR'])
		GPA=float(request.form['GPA'])
		HR = 0

		testdata=[[R,secondB,TB,RBI,XBH,GWRBI,ISOP,XR,GPA]]
		rs_testdata=rs.transform(testdata)

		predict_HR=pd.Series(model.predict(rs_testdata))
		predict_HR=np.exp(predict_HR)-1


		#print(predict_HR)
		return render_template('index.html',HR=predict_HR[0])






if __name__ =='__main__':
	model = joblib.load('./model/voting_predict_model.pkl')
	app.run(debug=True)
