import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# years = np.array([2020 , 2021 , 2022 , 2023])
# grades = np.array([81 , 85 , 90 , 75])

# # show data in graph  -  line(x.y) , pie(x) , bar(x,y) , scatters(x,y)
# plt.plot(years , grades , marker = 'o')

# #give the graph title
# plt.title("academic growth")

# # set the name for x and y axis
# plt.xlabel("passing years")
# plt.ylabel("student marks")
# plt.show()

# trendinglangname = np.array(["python" , "java" , "java script" , "c++"])
# trendinglang = np.array([45 , 30 , 20 , 5])
# plt.title("TRENDING LANGUAGE MARKET PLACE")
# plt.pie(trendinglang)
# plt.legend(trendinglangname)
# plt.show()

# jio 5 years sell growth , 2020 - 2024

# year = np.array([2020 , 2021 , 2022 , 2023 , 2024])
# sellgr = np.array([25 , 28 , 20 , 22 , 21 ])
# plt.title("SELL GROWTH OF JIO")
# plt.bar(year , sellgr)
# plt.xlabel("YEARS")
# plt.ylabel("TURNOVER(in cr.)")
# plt.grid()
# plt.show()

#create an array start from 1 to 49
no = np.arange(50)
# 1*50
# 50*1
# 2*25
# 25*2
# 5*10
# 10*5
#find the min , max , mean form no
print(no.max())
print(no.mean())
print(no.min())
mydata = no.reshape(5,10)
mydata = mydata+500
print(mydata.shape)
print(mydata >505)
print(no.shape)
print(no)
#array slicing
print(no[:])
print(no[4:8])
emp = np.array([5,6,3,2,1,9,10.4,7])
print(emp[-5:-1])

# pandas will represent the data set in dataframes
mydataframe = pd.DataFrame(data= np.arange(0,50).reshape(10,5))
print(mydataframe)
print("mean ",mydataframe.mean())
print("median ",mydataframe.median())
print("mode ",mydataframe.mode())
print(mydataframe.head(1))
print(mydataframe.tail(1))
print(mydataframe.loc[[2,5]])
