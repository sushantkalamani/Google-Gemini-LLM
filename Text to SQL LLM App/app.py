import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import os
import sqlite3


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = ['''You are an expert in converting English questions to SQL query!
The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION and MARKS \n\nFor example, \nExample 1 - How many entries of records are present the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
\nExample 2 - Tell me all the students studying in Data Science class?,
the SQL command will be something like this SELECT * FROM STUDENT
where CLASS="Data Science";
also the sql code should not have in beginning or end and sql word in output''']

db = "student.db"

def generate_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

def read_sql(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

st.set_page_config(page_title= "I can Retrive any SQL query")
st.header("Gemini App to Retrive SQL Data")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

if submit:
    response = generate_gemini_response(question, prompt)
    print(response)
    data = read_sql(response, db)
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)

