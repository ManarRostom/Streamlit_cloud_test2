import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

df = pd.read_csv('StudentsPerformance.csv')
numeric_col = ['math score','reading score','writing score']
categorical_col = ['gender','race/ethnicity','parental level of education','lunch','test preparation course']

def Data_Description():
    st.title('Data Description Page')
    st.markdown('### Head of Data')
    st.write(df.head())
    
    st.markdown('### Description of Data')
    st.write(df.describe())
    
    st.markdown('### Missing values')
    st.write(df.isnull().sum())
    
    st.markdown('### Columns Data Types')
    st.write(df.dtypes)
def Numerical_Charts():
    st.title('Numerical Charts Page')
    st.sidebar.header("Histogram Columns")
    hist_col = st.sidebar.selectbox('Choose Hist Column : ',numeric_col)
    st.plotly_chart(px.histogram(data_frame=df,x=hist_col,color_discrete_sequence=['Green']))
    
    st.sidebar.header('Scatter Plot Columns')
    scatter_x = st.sidebar.selectbox('Choose scatter X :',numeric_col)
    scatter_y = st.sidebar.selectbox('Choose scatter Y:',numeric_col)
    scatter_color = st.sidebar.checkbox('Add color')
    if scatter_color:
        color_var = st.sidebar.selectbox('Choose color Column : ',categorical_col)
        fig = px.scatter(data_frame=df,x=scatter_x,y=scatter_y,color=color_var,color_discrete_sequence=px.colors.qualitative.Dark2)
        st.plotly_chart(fig)
    else:
        fig = px.scatter(data_frame=df,x=scatter_x,y=scatter_y,color_discrete_sequence=px.colors.qualitative.Dark2)
        st.plotly_chart(fig)
        
def Categorical_Charts():
    st.title('Categorical Charts Page')
    st.sidebar.header("Count Plot Columns")
    count_col = st.sidebar.selectbox('Choose count Column : ',categorical_col)
    st.plotly_chart(px.histogram(data_frame=df,x=count_col,color_discrete_sequence=['Green']))
    
    st.sidebar.header('Bar Plot Columns')
    bar_x = st.sidebar.selectbox('Choose Bar X :',categorical_col)
    bar_y = st.sidebar.selectbox('Choose Bar Y:',numeric_col)
    bar_color = st.sidebar.checkbox('Add color')
    if bar_color:
        color_var = st.sidebar.selectbox('Choose color Column : ',categorical_col)
        fig = px.bar(data_frame=df,x=bar_x,y=bar_y,color=color_var,text_auto=True,color_discrete_sequence=px.colors.qualitative.Dark2)
        st.plotly_chart(fig)
    else:
        fig = px.bar(data_frame=df,x=bar_x,y=bar_y,color_discrete_sequence=px.colors.qualitative.Dark2)
        st.plotly_chart(fig)
        
        
        
dic = {
    "Data Description":Data_Description,
    "Numerical Charts":Numerical_Charts,
    "Categorical Charts":Categorical_Charts
}
user_choice = st.sidebar.selectbox("Choose Page : ",dic.keys())
dic[user_choice]()
