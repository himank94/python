import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from scipy import stats as st
years = [2019 , 2020 , 2021 , 2022 , 2023]
revenue = [280 , 386 , 469 , 510 , 514]
profit = [11.5 , 21.3 , 33.4 , 3.2 , 7.7]
slope,intercept,r,p,std_err=st.linregress(years , revenue)
print("slope",slope , "intercept",intercept , "r",r , "p",p , "std_err",std_err)
def futurerevpro(years):
    return slope*years+intercept
print(futurerevpro(2025))

# futurerevprof = np.poly1d(np.polyfit(years , revenue , 2))
# print(futurerevprof(2025))
