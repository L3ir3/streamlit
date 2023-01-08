
# PROYECTO DE CONSOLIDACION STREAMLIT: FUNCION eda_app.py

# Importaciones: streamlit, pandas, matplotlib, seaborn
import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

# Función principal que emplearemos en la APP
def run_eda_app():
	st.header("Sección EDA")
		
	submenu=["Descriptivo", "Gráfico"]

	dm_data_path='data/diabetes_data_upload.csv'
	dm_clean_data_path='data/diabetes_data_upload_clean.csv'
	freqdist_path='data/freqdist_of_age_data.csv'

	dm_data=pd.read_csv(dm_data_path)
	dm_clean_data=pd.read_csv(dm_clean_data_path)
	freqdist_data=pd.read_csv(freqdist_path)

	opcion = st.sidebar.selectbox("Submenú", submenu)

	if(opcion=="Descriptivo"):
		st.subheader("Análisis descriptivo")
		st.dataframe(dm_data)

		with st.expander("Tipos de datos"):
			st.write(dm_data.dtypes)
			
		with st.expander("Resumen descriptivo"):
			st.dataframe(dm_clean_data)

		with st.expander("Distribución por género (Gender)"):
			chart_data_dm=dm_data['Gender'].value_counts()
			st.write(chart_data_dm)

		with st.expander("Distribución por clase/label (Class)"):
			chart_data_dm=dm_data['class'].value_counts()
			st.write(chart_data_dm)

	elif(opcion=="Gráfico"):
		st.subheader("Análisis gráfico")
		st.write(dm_clean_data)
		col1,col2=st.columns([2,1]) #bi zutabe, bakoitzean bi expander
		with col1:
			with st.expander("Grafico de distribución de género (Gender)"):
				chart_data_dm=dm_data['Gender'].value_counts()
				st.bar_chart(chart_data_dm)

			with st.expander("Grafico de distribución por clase (Class)"):
				chart_data_dm=dm_data['class'].value_counts()
				st.bar_chart(chart_data_dm)		

		with col2:
			with st.expander("Distribución por Gender"):
				chart_data_dm=dm_data['Gender'].value_counts()
				st.table(chart_data_dm)

			with st.expander("Distribución por Class"):
				chart_data_dm=dm_data['class'].value_counts()
				st.table(chart_data_dm)

		with st.expander("Distribución por edades"):
			#sns.set_style('darkgrid')
			fig = plt.figure(figsize=(10, 4))
			plt.title("Conteo de frecuencia por Edad", fontsize=14)
			sns.barplot(data=freqdist_data, x='Age', y='count')
			plt.xlabel("Age", fontsize=12)
			plt.ylabel("Counts", fontsize=12)
			st.pyplot(fig)

		with st.expander("Detección de outliers"):
			fig = plt.figure(figsize=(10, 4))
			#plt.title("", fontsize=14)
			sns.boxplot(data=dm_data, x='Gender', y='Age')
			plt.xlabel("Gender", fontsize=12)
			plt.ylabel("Age", fontsize=12)
			st.pyplot(fig)

		with st.expander("Gráfico de correlación"):
			fig = plt.figure(figsize=(10, 4))
			#plt.title("", fontsize=14)
			sns.heatmap(data=dm_clean_data.corr())
			plt.xlabel("Gender", fontsize=12)
			plt.ylabel("Age", fontsize=12)
			st.pyplot(fig)
# Fin de la FUNCION







