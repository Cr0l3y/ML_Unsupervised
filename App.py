import streamlit as st
import pandas as pd
import joblib

encoder = joblib.load('encoder.pkl')
scaler = joblib.load('scaler.pkl')
kmeans =joblib.load('kmeans.pkl')



st.title('Grupos de interesse para marketing')
st.write("""
         Aplicando algoritmo de clusterização K-means para identificar e prever agrupamentos de interesses de usuários, com o objetivo de direcionar campanhas de marketing de forma mais eficaz.
         Através dessa análise, conseguimos segmentar o público em bolhas de interesse, permitindo a criação de campanhas personalizadas e mais assertivas, com base nos padrões de comportamento e preferências de cada grupo.
         """)

#button
up_file = st.file_uploader('Escolha um arquivo CSV para realizar a previsão',type='csv')





