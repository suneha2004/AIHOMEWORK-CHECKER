import streamlit as st
st.header("SIGNUP PAGE!!!")
import pymongo
from datetime import date
conn=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.3")
mydb=conn["experi"]
my=mydb["supriya"]
n=st.text_input("username 👨‍💼")
pd=st.text_input("Password 👨‍💼")
r=st.slider("Roll",1,100)
c=st.selectbox("Course",["BCA","IT","CS","AI & ML"])
d=st.date_input("DOB",value=date.today(),min_value=date(1900,1,1),max_value=date(2100,12,31))
p=st.file_uploader("Upload Your Picture 📩") 
m=st.text_input("Mobile Number 📞")     
if st.button("SIGNUP"):
       my.insert_one({"name":n,"password":pd,"roll":r,"course":c,"dob":str(d)})
       st.success("DATA SAVE!!!")
       st.switch_page("pages/signin.py")
        




