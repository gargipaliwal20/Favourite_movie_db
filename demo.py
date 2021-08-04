import sqlite3
db=sqlite3.connect('movdb.db')
print ("Opened database successfully")
cr=db.cursor()
cr.execute("create table movies(movie text,actor text, actress text, director text, year_of_release text)")
print("Table created successfully")
cr.execute("insert into movies values('Ramleela','Ranvir Singh','Deepika padukone','Sanjay Leela Bhansali','2013')")
cr.execute("insert into movies values('MiMi','Pankaj Tripathi','Kriti Sanon','Laxman Utekar','2021')")
cr.execute("insert into movies values('3-Idiots','Amir Khan','Kareena Kapoor','Rajkumar Hirani','2009')")
cr.execute("insert into movies values('Twilight','Robert Pattinson','Kristen stewart','Catherine Hardwicke','2008')")
cr.execute("insert into movies values('Titanic','Leonardo DiCaprio','Kate Winslet','James Cameron','1997')")
db.commit()
print("Records created successfully")


cursor = db.execute("SELECT actor,actress,director,year_of_release from movies")
for row in cursor:
   print("Actor = ", row[0])
   print("Actress = ", row[1])
   print("Director = ", row[2])
   print("Year_of_release = ", row[3], "\n")

a= input("Enter Parameter: ")
j=cr.execute("select * from movies where actor='"+a+"'")
for data in j:
    print(data[0])
db.close()

