import streamlit as st
import pymongo
from datetime import date
conn=pymongo.MangoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.3")
mydb=conn["experi"]
my=mydb["student1"]
n=st.text_input("Username")
r=st.slider("Roll",1,100)
c=st.selectbox("Course",["BCA","IT","CS","AI & ML"])
d=st.date_input("DOB",value=date.today(),min_value=date(1900,1,1),max_value=date(2100,12,31))
       
if st.button("SIGNUP"):
       my.insert_one({"name":n,"roll":r,"course":c,"dob":str(d)})
       st.success("DATA SAVE!!!")
        
