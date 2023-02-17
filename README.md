### KBO 홈런개수 예측 머신러닝 모델 ###
타격지표 9개를 이용하여 타자의 홈런갯수를 예측해주는 머신러닝 모델입니다  
  
LGBM,XGboost,Gradient boosting 3가지 기법을 기반으로 Voting 기법을 적용  
  
예측에 활용되는 지표  
* 득점(R) 
* 2루타(2B)  
* 총 루타(TB)   
* 타점(RBI)   
* 장타개수(XBH)   
* 결승타개수(GW RBI)   
* 순장타율(ISOP)   
* 득점생산성(XR)   
* GPA(GPA)   



### 시스템 구성 ###

![img](https://user-images.githubusercontent.com/121467486/219630891-6af956e1-30b7-47be-a849-1a2064fb25a3.png)



### Web site ###
<details>
<summary>자세히보기</summary>
  
  
<div markdown='1'>
  <img src="https://user-images.githubusercontent.com/121467486/219619704-885cfa82-0f3d-48c2-9f50-2149a73c0893.PNG">
  
  <img src="https://user-images.githubusercontent.com/121467486/219619847-6f060b86-f7bf-494a-bbbd-7d3ed444eca7.PNG">
  
  <img src="https://user-images.githubusercontent.com/121467486/219619897-16a8bb5e-ce94-4ebb-ba14-e3bf44198957.PNG">
  
  <img src="https://user-images.githubusercontent.com/121467486/219620012-ad023b74-bbf8-4541-8598-38237ce25aa2.PNG">
  
  <img src="https://user-images.githubusercontent.com/121467486/219620161-e29a6cc2-2443-433f-a5c3-b1a5ee322ded.PNG">
  
  <img src="https://user-images.githubusercontent.com/121467486/219620255-507b78d8-5842-4fe3-a309-3271c523e7fd.PNG">
  
</div>
</details>


### 참고문헌 ###

[- 모델 제작관련](https://minding-deep-learning.tistory.com/category/Minding%27s%20Baseball/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D%EC%9C%BC%EB%A1%9C%20%ED%99%88%EB%9F%B0%EC%99%95%20%EC%98%88%EC%B8%A1%ED%95%98%EA%B8%B0)  
[- 플라스크 서버 제작관련 - 1](https://niceman.tistory.com/192)  
[- 플라스크 서버 제작관련 - 2](https://www.youtube.com/watch?v=gmbkKE-jUUE&list=PL6ip5tgLI7PdRFqrldGQvxB4D4MrMLTEw&index=6)  
[- KBO 타자 데이터](https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx)  


### 개선점 ###
2차기본지표 활용한 모델 업데이트   
학습결과 통해 재학습하는 모델 제작   

