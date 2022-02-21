###Finding all numbers from list
import re
f=open("sample.txt","r")
s=f.read()
#phnumber = re.findall("[0-9]+-[0-9]+-[0-9]+",s)
#print(phnumber)
###Email
# email=re.findall("[a-z]+@[a-z]+.[a-z]+",s)
# print(email)
###Name
# name= re.findall("[A-Z][a-z]+ [A-Z][a-z]+\n",s)
# print(name)
###Extracting zip code
# zipcode=re.findall(" [0-9]+\n",s)
# print(zipcode)
###Doornumber
# dno=re.findall(r"\n[0-9]+ ", s)
# print(dno)
###Street
street=re.findall(" [0-9A-Za-z]+ St.",s)
print(street)

#ans = re.match("[a-zA-Z]*",s)

# f = open("SampleAmarnath.txt", "r")
# s = f.read()
  
# lst = re.findall('\S+@\S+', s)     
  
# print(lst)

# import re
# def validateEmail(strEmail):
#     if re.match("(.*)@(.*).(.*)", strEmail):
#         return True
#     return False


