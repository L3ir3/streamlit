
#  PROYECTO CONSOLIDACION STREAMLIT: FUNCION app.py

# Importaciones

import streamlit as st
import streamlit.components.v1 as stc
from eda_app import run_eda_app
from ml_app import run_ml_app


# Función main()
def main():
	
	menu=["Home", "EDA", "ML", "Info"]

	opcion = st.sidebar.selectbox("Menú", menu)

	if(opcion=="Home"):
		
		html_temp = """
		<div style="background:linear-gradient(to right, #0a0ef7, #3dd0e0);padding:2.5px;border-radius:10px">
		<h1 style="color:white;text-align:center;font-size:36px;">App para la detección temprana de DM</h1>
		<h1 style="color:white;text-align:center;font-size:16px;">(Diabetes Mellitus)</h1>
		</div><br>"""
		st.markdown(html_temp,unsafe_allow_html=True)

		st.subheader("Home")
		st.subheader("App para la detección temprana de DM")
		st.text('Dataset que contiene señales y síntomas que pueden indicar diabetes o posibilidad de diabetes.')
		st.subheader("Fuente de datos")
		st.code("https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.")
		st.subheader("Contenidos de la App")
		st.info('''
		- EDA Section: Análisis exploratorio de los datos  
		- ML Section: Predicción de Diabetes basada en ML (Machine Learning)
		''')

	elif(opcion=="EDA"):
		run_eda_app()
	elif(opcion=="ML"):
		run_ml_app()

	elif(opcion=="Info"):
		st.header("MBIT, proyecto de consolidación, librería Streamlit")
		st.text('This is some text.')
		st.iframe('https://idal.uv.es/', height=800, width=600, scrolling=True)

if __name__ == '__main__':
	main()