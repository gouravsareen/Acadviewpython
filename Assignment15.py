#Q1:-
import re
email= "zuck26@facebook.com page33@google.com jeff42@amazon.com"
output=re.findall('([\w\d]{1,22}[\w]{1,22}[\w]{1,5})',email)
t1=(output[0:3])
t2=(output[3:6])
t3=(output[6:9])
p1=(tuple(t1))
p2=(tuple(t2))
p3=(tuple(t3))
l1=[]
l1.append(p1)
l1.append(p2)
l1.append(p3)
print(l1)

#Q2:-
import re
text="Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
gg=re.findall('[Bb][\w]{1,20}',text)
print(gg)

#Q3:-
import re
sentence="A, very very; irregular_sentence"
ggg=re.sub("[;_,]","",sentence)
print(ggg)

#Q4:-
import re
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
def clean_tweet(tweet):
    tweet = re.sub('http\S+\s*',' ',tweet)
    tweet = re.sub('RT|cc',' ',tweet)
    tweet = re.sub('#\S+',' ',tweet)
    tweet = re.sub('@\S+',' ',tweet)
    tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""),' ',tweet)
    tweet = re.sub('\s+',' ',tweet)
    return tweet
print(clean_tweet(tweet))
