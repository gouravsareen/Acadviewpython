#Q1:-
import sqlite3
conn=sqlite3.connect("Database1.db")
print("Opened Database1 successfully")
conn.execute('''CREATE TABLE BOOKS(BOOK_ID INT PRIMARY KEY NOT NULL,TITLE_ID INT NOT NULL,LOCATION CHAR NOT NULL,GENRE CHAR(50))''')
conn.execute('''CREATE TABLE TITLES(TITLE_ID INT PRIMARY KEY NOT NULL,TITLE TEXT NOT NULL,ISBN INT NOT NULL,PUBLISHER_ID INT NOT NULL,PUBLICATION_YEAR INT NOT NULL)''')
conn.execute('''CREATE TABLE PUBLISHERS(PUBLISHER_ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,STREET_ADDRESS CHAR(50) NOT NULL,SUITE_NUMBER INT NOT NULL,ZIP_CODE_ID INT NOT NULL)''')
conn.execute('''CREATE TABLE ZIP_CODE(ZIP_CODE_ID INT PRIMARY KEY NOT NULL,CITY TEXT NOT NULL,STATE TEXT NOT NULL,ZIP_CODE INT NOT NULL)''')
conn.execute('''CREATE TABLE AUTHORS_TITLES(AUTHOR_TITLE_ID INT PRIMARY KEY NOT NULL,AUTHOR_ID INT NOT NULL,TITLE_ID INT NOT NULL)''')
conn.execute('''CREATE TABLE AUTHORS(AUTHOR_ID INT PRIMARY KEY NOT NULL,FIRST_NAME TEXT NOT NULL,MIDDLE_NAME TEXT NOT NULL,LAST_NAME TEXT NOT NULL)''')
print("TABLE CREATED SUCCESSFULLY")
#Q2:-
conn.execute("INSERT INTO BOOKS(BOOK_ID,TITLE_ID,LOCATION,GENRE) VALUES(1,100,'India','BIOLOGY')")
conn.execute("INSERT INTO BOOKS(BOOK_ID,TITLE_ID,LOCATION,GENRE) VALUES(2,200,'USA','MATHS')")
conn.execute("INSERT INTO TITLES(TITLE_ID,TITLE,ISBN,PUBLISHER_ID,PUBLICATION_YEAR) VALUES(101,'LIVE VS DEATH',2000,12,2012)")
conn.execute("INSERT INTO TITLES(TITLE_ID,TITLE,ISBN,PUBLISHER_ID,PUBLICATION_YEAR) VALUES(102,'WAY TO SUCCESS',2001,13,2013)")
conn.execute("INSERT INTO PUBLISHERS(PUBLISHER_ID,NAME,STREET_ADDRESS,SUITE_NUMBER,ZIP_CODE_ID) VALUES(12,'GOURAV','YNR',20,1000)")
conn.execute("INSERT INTO PUBLISHERS(PUBLISHER_ID,NAME,STREET_ADDRESS,SUITE_NUMBER,ZIP_CODE_ID) VALUES(13,'AKSHU','YNR',21,1001)")
conn.execute("INSERT INTO ZIP_CODE(ZIP_CODE_ID,CITY,STATE,ZIP_CODE) VALUES(1000,'YNR','HARYANA',300)")
conn.execute("INSERT INTO ZIP_CODE(ZIP_CODE_ID,CITY,STATE,ZIP_CODE) VALUES(1001,'JAGADHRI','HARYANA',301)")
conn.execute("INSERT INTO AUTHORS_TITLES(AUTHOR_TITLE_ID,AUTHOR_ID,TITLE_ID) VALUES(147,456,101)")
conn.execute("INSERT INTO AUTHORS_TITLES(AUTHOR_TITLE_ID,AUTHOR_ID,TITLE_ID) VALUES(148,457,102)")
conn.execute("INSERT INTO AUTHORS(AUTHOR_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME) VALUES(456,'RAM','NARAYAN','MURTI')")
conn.execute("INSERT INTO AUTHORS(AUTHOR_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME) VALUES(457,'RAMA','KRISHNA','MURTI')")
print("VALUES INSERTED SUCCESSFULLY")
conn.commit()
cursor=conn.execute("SELECT BOOK_ID,TITLE_ID,LOCATION,GENRE from BOOKS WHERE BOOK_ID=2")
for row in cursor:
    print("BOOK_ID= ",row[0])
    print("TITLE_ID= ",row[1])
    print("LOCATION= ",row[2])
    print("GENRE= ",row[3], "\n")
print("RECORDS CREATED SUCCESSFULLY")
#Q3:-
conn.execute("UPDATE BOOKS set GENRE='SCIENCE' where BOOK_ID=2")
conn.commit()
cursor=conn.execute("SELECT BOOK_ID,TITLE_ID,LOCATION,GENRE from BOOKS WHERE BOOK_ID=2")
for row in cursor:
    print("BOOK_ID= ",row[0])
    print("TITLE_ID= ",row[1])
    print("LOCATION= ",row[2])
    print("GENRE= ",row[3], "\n")
print("Total no. of rows updated :",conn.total_changes)
conn.close()