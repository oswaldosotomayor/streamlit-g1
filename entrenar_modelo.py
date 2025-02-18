# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 21:06:17 2025

@author: osotomayor
"""

import streamlit as st
import joblib
import numpy as np 

model_filename = 'arnes.pkl'
# Cargamos el modelo desde el archivo
loaded_model = joblib.load(model_filename)
 
st.title('Compra de Arneses y Botas para perros')
st.header("Tienda RED")
st.subheader("Ingrese los datos de su perro")

with st.form(key='perritos-pred-form'):
    col1, col2 = st.columns(2)
    
    arnes = col1.slider(label='Tamaño del arnés:', min_value=1, max_value=100)
    botas = col2.text_input(label='Tamaño de la Bota:')
    submit = st.form_submit_button(label='Check')
    
    if submit:
        # Convertir el valor de la bota a entero
        try:
            botas = int(botas)  # Transformar el valor de texto a entero
        except ValueError:
            st.error("Por favor, ingresa un número válido para el tamaño de la bota.")
            st.stop()  # Detener la ejecución si no es un número válido
        
        # Predecir el tamaño de bota recomendado
        inputs = np.array(arnes).reshape(-1, 1)
        predicted_boot_size = loaded_model.predict(inputs)[0]
        predicted_boot_size = round(predicted_boot_size)  # Redondear el valor predicho
        
        # Mostrar el tamaño de bota recomendado
        st.write(f"El tamaño de bota recomendado es: {predicted_boot_size}")
        
        # Validaciones
        if botas < predicted_boot_size:
            st.warning(f"El tamaño de la bota es muy pequeño. Te sugiero el tamaño {predicted_boot_size}.")
        elif botas > predicted_boot_size:
            st.warning(f"El tamaño de la bota es muy grande. Te sugiero el tamaño {predicted_boot_size}.")
        else:
            st.success("¡Felicitaciones! Parece que el tamaño de la bota es el correcto.")