import streamlit as st

st.title("IMC app")
height = st.number_input(label= "Taille(cm)",min_value=1, max_value=500, placeholder="Entrer votre taille (en cm)")
weight = st.number_input(label="Poids(kg)", min_value=1, placeholder="Enter votre poids (en kg)")
imc = weight / (height/100)**2
category = ["Maigre", "Poids idéal", "Surpoids", "Obesité modérée", "Obesité sévère", "Obésité morbide"]
limit = [18.5, 24.9, 29.9, 34.9, 39.9, float('inf')]
color = ["yellow", "green", "yellow","orange","red", "red"]

f_cat, f_col = next((cat,col) for cat, lim, col in zip(category, limit,color) if imc < lim)
st.markdown(f":{f_col}[**{f_cat}**]")
