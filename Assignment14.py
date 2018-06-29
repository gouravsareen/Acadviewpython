#Q1:-
file=open("myfile.txt","r")
print(file)
for line in reversed(list(open("myfile.txt"))):
    print(line.rstrip())
print(file.readlines())
n=int(input("enter lines to be read:- "))
file=open('myfile.txt')
lines=file.readlines()
print(lines[0:n-1])


#Q2:-
import re
import string

frequency = {}
document_text = open('myfile.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    print(words, frequency[words])


#Q3:-
with open("file1.txt","w") as f:
    with open("file2.txt", "r") as f1:
        for line in f1:
            f.write(line)


#Q4:-
with open('abc.txt','r') as fh1, open('def.txt','r') as fh2:
    for line1,line2 in zip(fh1,fh2):
        line1=line1[:3]
        line2=line2[:3]
        file3 = open("ghi.txt", "a")
        file3.write(line1+line2+"\n")
        file3.close()
    file4 = open("ghi.txt", "r")
    print(file4.readlines())
    file4.close()


#Q5:-
import random
l=[]
with open("randomno1.txt.py","a+",encoding="utf-8") as gh1, open("randomno2.txt.py","a+",encoding="utf8") as gh2:
    for i in range(0,9):
        l.append(random.randint(0,9))
    for i in l:
        gh1.writelines(str(i))
    l.sort()
    print(l)
    for k in l:
        gh2.write(str(l)+"\n")
        print(gh2.read)
