file=open('C:/Users/Admin/OneDrive/Desktop/test.txt','w')
file.write('''hi 
             my name is himank''')
file.close()
file=open('C:/Users/Admin/OneDrive/Desktop/test.txt','r')
print(file.readline())
file.close()