from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key
api_key=os.getenv("api_key")
genai.configure(api_key=api_key)

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

# Create SQLite Database and Insert Records

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows



## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name COSTA_EMPLOYEE and has the following columns - NAME, DESIGNATION, 
    DEPARTMENT,SALARY \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM COSTA_EMPLOYEE ;
    \nExample 2 - Tell me all the employee whose designations is software engineer?, 
    the SQL command will be something like this SELECT * FROM COSTA_EMPLOYEE 
    where DESIGNATION="SOFTWARE ENGINEER"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]


st.set_page_config(
        page_title="SQL Query App",
        page_icon=":bar_chart:",
        layout="centered",
        initial_sidebar_state="expanded"
    )

    # Apply some styling
st.markdown(
        """
        <style>
        .stApp {
            background-color: #f0f2f6;
            color: #333333;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        .stTextInput>div>div>div>input {
            background-color: #ffffff;
            color: #333333;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stTextArea>div>div>textarea {
            background-color: #ffffff;
            color: #333333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )



## Streamlit App


st.header("App To Retrieve Data From Database")

question=st.text_area('Enter Your Query:', '')

submit=st.button("Question To Me")

# if submit is clicked
if submit:
    if question.strip() != '':

        response=get_gemini_response(question,prompt)
        st.subheader('SQL Query:')
        st.code(response)
        try:
            response1=read_sql_query(response,"COSTA_EMPLOYEE.db")
            if response1:
                        st.subheader('Response:')
                        st.dataframe(response1)
            else:
                st.write('No results found.')
        except Exception as e:
             st.error(f"An error occurred: {e}")
    
    else:
         st.warning('Please enter an SQL query.')


