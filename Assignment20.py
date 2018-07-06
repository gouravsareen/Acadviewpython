#Q1:-
import pandas as pd
data={'name':['gourav'],'age':[20],'mail_id':['gouravsareen0112@gmail.com'],'phone_no':[8708151150]}
df=pd.DataFrame(data)
print(df)
print(df.append({'name':'akshu','age':20,'mail_id':'akshitasharma01111@gmail.com','phone_no':9813489211},ignore_index=True))

#Q2:-
import pandas as pd
df1=pd.read_csv('Data.csv')
#a.) First 5 rows of Dataframe
print(df1.head(5))
#b.) First 10 rows of Dataframe
print(df1.head(10))
#c.) find basic statistics on the particular dataset.
print(df1.sum(axis=0))   #gives the sum of all columns.
print(df1.sum(axis=1))   #gives the sum of all rows.
print(df1.mean(axis=0))  #gives the mean of all columns.
print(df1.mean(axis=1))  #gives the mean of all rows.
print(df1.describe())    #describe A bunch of different stats for the datafile
print(df1.count())       #get the number of values you have in the column.
#d.) Find the last 5 rows of the dataframe.
print(df1.tail(5))
#e.) Extract the 2nd column and find basic statistics on it.
#The second column is Location.
print(df1['Location'].sum())
print(df1['Location'].describe())
print("Location occurs "+str(df1['Location'].count())+" times")
#CAN'T FINE MEAN OF THE LOCATION COLUMN BECAUSE THE DATATYPE OF THAT COLUMN IS OBJECT,,AND MEAN IS CALCULATED FOR INTEGER TYPE VALUES ONLY.