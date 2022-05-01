"""

--------------------------------------------------------------
Clean and delete the hashtag email link history to csv file.

(C) 2022 Saeed Mirzamohammadi, Qazvin, Iran

Email: saeed1843mirzamohammadi@gmail.com

Id telegram : @e_l_f_5_5_5

2022/5/1
--------------------------------------------------------------


"""




import pandas as pd
import re


path_csv=r"your path file.csv"    #F:\\new\\dataset.csv
data=pd.read_csv(path_csv)


def remove_link():
    for number_tweet in range(12859):
        data_tweet=data.iloc[number_tweet,0] 
        re_remove=re.compile(r"[https://http://a-zA-Z0-9]+[.ir.com.org.net.me]")
        text_is_remove=re_remove.sub("",data_tweet)
        data.iloc[number_tweet,0]=text_is_remove



def remove_time():
    for number_tweet in range(12859):
        data_tweet=data.iloc[number_tweet,0] 
        re_remove=re.compile(r"[0-9]+[/\.,]+[0-9]+[/\.,]+[0-9]")
        text_is_remove=re_remove.sub("",data_tweet)
        data.iloc[number_tweet,0]=text_is_remove



def remove_email():
    for number_tweet in range(12859):
        data_tweet=data.iloc[number_tweet,0] 
        re_remove=re.compile(r"[a-zA-Z0-9_]+@[a-zA-z0-9_]+.com")
        text_is_remove=re_remove.sub("",data_tweet)
        data.iloc[number_tweet,0]=text_is_remove



def remove_hashtag():
    for number_tweet in range(12859):
        data_tweet=data.iloc[number_tweet,0] 
        re_remove=re.compile(r"#[a-zA-Z0-9_آ-ی]+")
        text_is_remove=re_remove.sub("",data_tweet)
        data.iloc[number_tweet,0]=text_is_remove



if __name__=="__main__":
    remove_link()
    remove_time()
    remove_email()
    remove_hashtag()
    print(data)
