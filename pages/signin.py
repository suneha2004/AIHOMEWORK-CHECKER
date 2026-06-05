import streamlit as st
import pymongo


conn=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.3")
mydb=conn["experi"]
my=mydb["supriya"]
       
st.header("C V Analysis using AI and Machine Learning")
st.subheader("SignIn")



with st.form("SignIn"):
       t1=st.text_input("👤Username",type="username)
       t2=st.text_input("🔒 Password",type="password")
       if st.form_submit_button("SignIn"):
              if not t1 or not t2:
                     st.error("Fill The Fields!!!")
              else:
                  res=my.find({"username":t1,"password":t2})
                  v=0
                  for data in res:
                         v=v+1
                  st.success(f"Welcome:{"username"}")
                  if v==0:
                        st.error("invalid login") 
                        st.switch_page("pages/profilepage.py")
                    




                        
                     





