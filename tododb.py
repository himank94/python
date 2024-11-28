import mysql.connector

#create the database connection
connection = mysql.connector.connect(host = "localhost" , username = "root" , password = "123456789" , database = "todo")

# to check the connection is establish or not
if connection.is_connected():
    print("database is connected")
else:
    print("database is not connected")

#create table for todo app task
task = "create table if not exists task (taskname text , mobile text)"

#create cursor to execute the mysql query
mycursor = connection.cursor()

#to execute the create task table in database todo
mycursor.execute(task)

#to commit or save the mysql query
connection.commit()

#to insert the task in to do database
inserttask = "insert into task values('{}' , '{}')".format(input("enter task name ") , input("enter mobile no "))
#to execute the insert query
mycursor.execute(inserttask)
#to save the operation
connection.commit()

#update the task in todo database
updatetask = "update task set taskname = 'its vam' where mobile ='9489859'"
mycursor.execute(updatetask)
connection.commit()

#to delete the task from database todo
deletetask = "delete from task where mobile ='9489859'"
mycursor.execute(deletetask)
connection.commit()

#to access the data from database
mytask = "select * from task"
mycursor.execute(mytask)
print(mycursor.fetchall())
connection.commit()

#to drop the table
droptask = "drop table task"
mycursor.execute(droptask)
connection.commit()

# press 1 to add new event : eventname , eventdate , venue , eventid
# press 2 to get all event
# press 3 to delete event 
# press 4 to update event 
# press 5 to add student in event : studentname , stuemail , stumobile , studept , stuyear  , eventname
# press 6 to get all student
# press 7 to delete student
# press 8 to update student
# press 9 to add student

#railway reservation
#create hotel mgmt system
#create flight booking system