# Import is not working for me *
import pymongo
from pymongo import MongoClient
client = MongoClient ("mongodb+srv://admin:admin@cluster0.2i2k0ee.mongodb.net/?retryWrites=true&w=majority")

#Obtaining data from MongoDb
db = client ["pytech"]

#Retrieving collection of students
students =db.students

#Now, we are asked to use the find() function to retrieve all students in said collection:
student_Collection = students.find("{Input student data}")

#Print collection / database of students *required format match (i.e borrowed verbatim)
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#Loop (haven't done this in a while...)
for students in student_Collection:
 print (student_Collection)
 
#Updating last name of Student to Oaks...sounds...simpler LOL
result = db.collection.update_one({“student_id”: 1007}, {“$set”: {“last_name”: “Oaks”}})

#Update student 
Thorin = students.find_one({"student_id": "1007"}) 
 
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

#End message via program...
input("\n\n  End of program, press any key to continue...")