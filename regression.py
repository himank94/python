# prediction:- regression:- it is a relaiton between variables or dataset
# linear regression:- y=mx+c
import matplotlib.pyplot as plt
from scipy import stats as st
from sklearn.metrics import r2_score
import numpy as np
age = [40,20,35,50,60,30,70,80]
salary = [20000,40000,18000,15000,12000,25000,35000,50000]
# plt.scatter(age,salary,marker = 'o')
# slope,intercept,r,p,std_err=st.linregress(age,salary)
# print("slope",slope , "intercept",intercept , "r",r , "p",p , "std_err",std_err)
# # note:- if r is near to 1 , so best case
# # note:- if r is near to 0 , so bad case
# def futuresalary(age):
#     return slope*age+intercept
# print(futuresalary(35))
# # when we apply linear regression
# # apply : r=~1
# # not apply : r=~0
# plt.show()

# polynomial regression
futuredata = np.poly1d(np.polyfit(age,salary,3))
print(futuredata(55))
print(r2_score(salary,futuredata(age)))
