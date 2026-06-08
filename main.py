import streamlit as st
import time
st.title("WELCOME IN PYTHON WEB WORLD!!!")
p=st.progress(0,"Wait for Loading ....")
for i in range(1,100):
       time.sleep(0.05)
       p.progress(i,"Loading....")
p.empty()
st.image("p4.jpeg",width=5000)





