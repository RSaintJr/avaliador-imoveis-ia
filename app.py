import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Avaliador de Imóveis IA", page_icon="🏡", layout="wide")

st.title("🏡 Avaliador de Imóveis Inteligente")
st.markdown("---")

# Criando um menu lateral para os inputs do usuário
st.sidebar.header("📊 Características do Imóvel")

# Campos para o usuário digitar
renda_media = st.sidebar.number_input("Renda Média da Vizinhança (em dezenas de milhares de $)", min_value=0.0, max_value=15.0, value=5.0, step=0.5)
idade_casa = st.sidebar.slider("Idade da Casa (anos)", min_value=1, max_value=100, value=20)
total_quartos = st.sidebar.number_input("Total de Cômodos", min_value=1, value=5)
total_quartos_dormir = st.sidebar.number_input("Total de Quartos de Dormir", min_value=1, value=3)
populacao = st.sidebar.number_input("População do Bairro", min_value=10, value=1000)
familias = st.sidebar.number_input("Número de Famílias no Bairro", min_value=1, value=300)

# Localização e Proximidade do Oceano
st.sidebar.markdown("---")
st.sidebar.subheader("📍 Localização")
ocean_proximity = st.sidebar.selectbox(
    "Proximidade do Oceano",
    ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"]
)

# Coordenadas (Colocando valores padrão da Califórnia)
latitude = st.sidebar.number_input("Latitude", value=35.0)
longitude = st.sidebar.number_input("Longitude", value=-119.0)

botao_avaliar = st.button("Calcular Preço Justo 🚀")

if botao_avaliar:
    with st.spinner("A Inteligência Artificial está analisando o imóvel..."):
        modelo = joblib.load('modelo_imobiliario_v1.pkl')
        
        inland = 1 if ocean_proximity == "INLAND" else 0
        island = 1 if ocean_proximity == "ISLAND" else 0
        near_bay = 1 if ocean_proximity == "NEAR BAY" else 0
        near_ocean = 1 if ocean_proximity == "NEAR OCEAN" else 0
        
        dados_entrada = pd.DataFrame({
            "longitude": [longitude],
            "latitude": [latitude],
            "housing_median_age": [idade_casa],
            "total_rooms": [total_quartos],
            "total_bedrooms": [total_quartos_dormir],
            "population": [populacao],
            "households": [familias],
            "median_income": [renda_media],
            "ocean_proximity_INLAND": [inland],
            "ocean_proximity_ISLAND": [island],
            "ocean_proximity_NEAR BAY": [near_bay],
            "ocean_proximity_NEAR OCEAN": [near_ocean]
        })
        
        preco_estimado = modelo.predict(dados_entrada)[0]
        
        st.success(f"🏡 O valor estimado deste imóvel é de **${preco_estimado:,.2f}**")
        st.caption(f"Aviso: Este modelo possui uma margem de erro média de $31.330")
