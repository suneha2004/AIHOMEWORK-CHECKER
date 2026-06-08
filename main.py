import streamlit as st
import pandas as pd
import time
st.title("WELCOME IN PYTHON WEB WORLD!!!")
p=st.progress(0,"Wait for Loading ...")
for i in range(1,100):
       time.sleep(0.05)
       p.progress(i,"Loading....")
p.empty()
st.image("p4.jpeg",width=5000)
st.title("WELCOME IN PYTHON WEB WORLD!!! ")
st.write("""
The AI Homework Checker is a web-based application developed using Python,
Streamlit, and MongoDB. This system helps students and teachers evaluate
homework automatically using Artificial Intelligence.
### Features:
* Upload homework files

* Automatic answer checking

* Instant result generation

* Student profile management

* Performance tracking

* Report generation

* Secure login and signup system.""")
st.success("project loaded successfully!")
# Dashboard Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Uploads", "120")
col2.metric("Checked", "98")
col3.metric("Average Score", "85%")
col4.metric("Accuracy", "92%")

st.divider()

# Recent Activity
st.header("📋 Recent Homework Checks")

data = pd.DataFrame({
    "File Name": [
        "Math.pdf",
        "Science.pdf",
        "English.docx"
    ],
    "Subject": [
        "Math",
        "Science",
        "English"
    ],
    "Score": [
        "88%",
        "92%",
        "85%"
    ]
})

st.dataframe(data, use_container_width=True)

# Chart
st.header("📊 Performance Overview")

chart_data = pd.DataFrame({
    "Scores": [60, 75, 85, 90, 95]
})




