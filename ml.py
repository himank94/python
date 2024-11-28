import numpy as np
from scipy import stats as st
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
# # mean = average value
# # median = middle value if data is arranged
# # mode = most repeated value
# # standard deviation
# # variance

# dataset = [50,60,55,80,70,95]
# print(np.mean(dataset))

# salary = [65000 , 85000 , 90000 , 70000 , 80000 , 65000]
# print(np.mean(salary))
# print(np.max(salary))
# print(np.min(salary))
# print(np.median(salary))
# print(st.mode(salary))
# print(np.std(salary))
# print(np.var(salary))

# data = np.random.randint(0,10,1000)
# print(data)

# plt.hist(data)
# plt.show()

# # normal and uniform data distribution

# data1 = np.random.uniform(0,10,1000)
# print(data1)
# data2 = np.random.normal(0,10,1000)
# print(data2)
# plt.hist(data1)
# plt.show()
# plt.hist(data2)
# plt.show()
# kmean model is an unsupervised machine learning data technique model it can help you to built k clusters based on data set 

age=[60,50,40,30,20]
salary = [15000,20000,25000,30000,32000]
data = list(zip(age,salary))
blank_array = []
for mydata in range(1,6):
    kmeans = KMeans(n_clusters=mydata)
    kmeans.fit(data)
    blank_array.append(kmeans.inertia_)
plt.plot(range(1,6) , blank_array , marker = 'o')
plt.show()