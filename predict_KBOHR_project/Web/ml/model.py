import pandas as pd
import numpy as np
import pickle
import joblib

X = pd.DataFrame(pd.read_csv('2016-2021_data.csv',engine='python',encoding='CP949'))
Y = pd.DataFrame(pd.read_csv('2022_data.csv',engine='python',encoding='CP949'))

X=X.drop(['선수명','팀명','Year'],axis=1)

player_id=Y['선수명']

#분석 컬럼 결정
X=X.drop(['AVG','G','PA','AB','H','3B','SAC','SF','AO','GO','BB/K','P/PA'],axis=1)

#훈련시 타겟데이터는 X_result 에 따로 저장후
X_result=np.log1p(X['HR'])

#X에서 HR데이터 삭제
X=X.drop(['HR'],axis=1)

Y_result=np.log1p(Y['HR'])
Y=Y.drop(['  Year','HR','선수명', '팀명', 'AVG', 'G', 'PA', 'AB','3B',
       'HR','SAC', 'SF','GO', 'AO','BB/K', 'P/PA'],axis=1)

Y=Y.drop(['H'],axis=1)

X=X.drop(['GO/AO'],axis=1)
Y=Y.drop(['GO/AO'],axis=1)

X_train=X
X_test=Y



from sklearn.model_selection import KFold, cross_val_score, GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.linear_model import ElasticNet, Lasso, LinearRegression

from sklearn.preprocessing import RobustScaler


rs=RobustScaler()
rs_Xtrain=rs.fit_transform(X_train) #학습X데이터
rs_Xtest=rs.transform(X_test) #학습 검증 X데이터

#KFold test

kfold=KFold(n_splits=5)

random_state=42

##################################################
GBC=GradientBoostingRegressor()


params={
    'n_estimators':[30,50,100],
    'learning_rate':[0.1,0.01,0.2],
    'max_depth':[3,4,5],
    'min_samples_leaf':[1,5,10],
    'max_features':[0.3,0.2,0.15]
}

grid_GBC=GridSearchCV(GBC,param_grid=params,scoring='neg_mean_squared_error',cv=kfold,n_jobs=-1,verbose=1)
#GBC.get_params().keys()
#하이퍼 파라미터 튜닝하는 값을 잘못 넣은줄 알았는데 올바르지않은 파라미터 이름(오타)였음
grid_GBC.fit(rs_Xtrain,X_result)

print(grid_GBC.best_estimator_)
print(grid_GBC.best_score_)

best_GBC=grid_GBC.best_estimator_
##################################################

XGB=XGBRegressor()

params={
     'n_estimators':[30,50,100],
     'max_depth':[3,4,5],
     'learning_rate':[0.1,0.01,0.2], #학습 단계별로 이전 결과를 얼마나 반영할지 설정한다. 일반적으로는 0.01 ~ 0.2 사이의 값
     'subsample': [0.6, 0.7, 1.0],# 각 트리마다 데이터 샘플링 비율 over-fitting방지 일반적으로 0.5 ~ 1을 사용
     'colsample_bytree' : [0.3,0.5,0.7],#각 트리마다 feature 샘플링 비율 일반적으로 0.5 ~ 1을 사용한다.
     'scale_pos_weight' : [0.5,1], #데이터가 불균형 할때 사용 보통은 음성 데이터 수 / 양성 데이터 수 값으로 한다.
     'reg_alpha': [0,0.05,0.0005] #규제(Lasso)

}

grid_XGB=GridSearchCV(XGB,param_grid=params,scoring='neg_mean_squared_error',cv=kfold,n_jobs=-1,verbose=1)
grid_XGB.fit(rs_Xtrain,X_result)

print(grid_XGB.best_params_)
print(grid_XGB.best_estimator_)
print(grid_XGB.best_score_)

best_XGB=grid_XGB.best_estimator_

##################################################

LGBM=LGBMRegressor()

params={
    'n_estimators':[30,50,100],
     'max_depth':[3,4,5,10,15],
     'learning_rate':[0.1,0.01,0.2],
     'num_leaves': [10, 30, 50],
     'min_split_gain': [0.1, 0.2, 0.3],

}

grid_LGBM=GridSearchCV(LGBM,param_grid=params,scoring='neg_mean_squared_error',cv=kfold,n_jobs=-1,verbose=1)
grid_LGBM.fit(rs_Xtrain,X_result)

print(grid_LGBM.best_params_)
print(grid_LGBM.best_estimator_)
print(grid_LGBM.best_score_)

best_LGBM=grid_LGBM.best_estimator_

##################################################


from sklearn.ensemble import VotingRegressor
voting=VotingRegressor(estimators=[('XGB',best_XGB),('LGBM',best_LGBM),('GBC',best_GBC)],n_jobs=-1)
voting.fit(rs_Xtrain,X_result)

joblib.dump(voting, '../model/voting_predict_model.pkl')

