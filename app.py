



#3: Chargement des librairies. (1 pts)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


df = pd.read_csv('dataset_stats.csv')


# Demander le nom de l’utilisateur et le saluer. (1 pts)
st.set_page_config(page_title="TP2 Streamlit", layout="wide")
st.title("TP2 : Explorateur de données interactif")
user_name = st.text_input("Entrez votre nom :")
if user_name:
    st.write(f"Bonjour, {user_name} !")


# Chargement de vos données avec `st.file_uploader` ou directement. (1 pts)
st.subheader("Chargement des données")
data_file = st.file_uploader("Téléversez votre fichier CSV", type=['csv'])
if data_file:
    try:
        df = pd.read_csv(data_file)
        st.success(f"Données chargées : {df.shape[0]} lignes, {df.shape[1]} colonnes.")
    except Exception as e:
        st.error(f"Erreur lors du chargement : {e}")


 # Afficher un premier graphique des données. (1 pts)
    st.subheader("Histogramme de la première colonne numérique")
    numeric_cols = df.select_dtypes(include=['number']).columns
    if len(numeric_cols) > 0:
        col0 = numeric_cols[0]
        fig, ax = plt.subplots()
        ax.hist(df[col0].dropna(), bins=20)
        ax.set_xlabel(col0)
        ax.set_ylabel("Fréquence")
        st.pyplot(fig)
    else:
        st.info("Aucune colonne numérique pour l'histogramme.")


 # Calculer des corrélations et les afficher. (1 pts)
    st.subheader("Matrice de corrélation")
    corr = df.corr()
    st.dataframe(corr)

# Utiliser `st.selectbox` pour sélectionner une variable x et y et afficher un graphique Plotly.
    st.sidebar.subheader("Bonus : Sélection interactive")
    if len(numeric_cols) >= 2:
        x_axis = st.sidebar.selectbox("Axe X", numeric_cols)
        y_axis = st.sidebar.selectbox("Axe Y", numeric_cols)
        filter_col = st.sidebar.selectbox("Filtrer par", numeric_cols)
        vmin, vmax = float(df[filter_col].min()), float(df[filter_col].max())
        selected_range = st.sidebar.slider(f"Plage pour {filter_col}", vmin, vmax, (vmin, vmax))
        df_filtered = df[(df[filter_col] >= selected_range[0]) & (df[filter_col] <= selected_range[1])]
        st.subheader(f"Scatter Plot : {y_axis} vs {x_axis}")
        fig2 = px.scatter(df_filtered, x=x_axis, y=y_axis)
        st.plotly_chart(fig2)
    else:
        st.info("Bonus requiert au moins deux colonnes numériques.")



    