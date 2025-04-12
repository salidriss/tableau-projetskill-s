import streamlit as st
import plotly.express as px
import pandas as pd 
st.title("""
Tableau de bord projet skill's (Salsabil Idrss )
""")
# Charger les données Excel
df = pd.read_excel("cybersecuritédata.xlsx")


st.title("Tableau de bord interactif - Analyse des participants cybersecurité")

# 1. Effectif total
total = len(df)
st.metric(label="👥 Effectif total des participants", value=total)

st.markdown("---")

# 2. Répartition par genre
st.subheader("Répartition par genre")
genre_count = df['Genre'].value_counts().reset_index()
genre_count.columns = ['Genre', 'N']

fig_genre = px.pie(genre_count, names='Genre', values='N',
                   color='Genre',
                   color_discrete_map={'Homme': 'blue', 'Femme': 'pink'},
                   hole=0.3)

st.plotly_chart(fig_genre, use_container_width=True)

# 3. Répartition des adresses
st.subheader("Répartition des adresses")
adresse_count = df['Adresse'].value_counts().reset_index()
adresse_count.columns = ['Adresse', 'N']
fig_adresse = px.bar(adresse_count, x='Adresse', y='N', color='Adresse')
st.plotly_chart(fig_adresse, use_container_width=True)

# 4. Répartition des certificats
st.subheader("Répartition des certificats")
certif_count = df['certificat_status'].value_counts().reset_index()
certif_count.columns = ['Certificat_status', 'N']
fig_certif = px.bar(certif_count, x='Certificat_status', y='N', color='Certificat_status')
st.plotly_chart(fig_certif, use_container_width=True)

# 5. Certificat par genre et adresse (Barres groupées)
st.subheader("Répartition des certificats par genre et région")
grouped_df = df.groupby(['certificat_status', 'Genre', 'Adresse']).size().reset_index(name='N')
fig_certif_genre_adresse = px.bar(
    grouped_df,
    x='certificat_status',
    y='N',
    color='Genre',
    barmode='group',
    facet_col='Adresse',
    labels={'certificat_status': 'Certificat', 'Genre': 'Genre', 'Adresse': 'Région'}
)
fig_certif_genre_adresse.update_layout(height=700)
st.plotly_chart(fig_certif_genre_adresse, use_container_width=True)

# 6. Affichage des données sous forme de tableau
st.subheader("Données détaillées par certificat, genre et région")
st.dataframe(grouped_df)

df = pd.read_excel("data_hotrellerie.xlsx")
st.write("Aperçu des données :")
st.dataframe(df)




st.title("Tableau de bord interactif - Analyse des participants")

# 1. Effectif total
total = len(df)
st.metric(label="👥 Effectif total des participants", value=total)

st.markdown("---")
df['Adresse'] = df['Adresse'].replace({'arta': 'Arta'})

# 2. Répartition par genre
st.subheader("Répartition par genre")
genre_count = df['Genre'].value_counts().reset_index()
genre_count.columns = ['Genre', 'N']

fig_genre = px.pie(genre_count, names='Genre', values='N',
                   color='Genre',
                   color_discrete_map={'Homme': 'blue', 'Femme': 'pink'},
                   hole=0.3)

st.plotly_chart(fig_genre, use_container_width=True)

# 3. Répartition des adresses
st.subheader("Répartition des adresses")
adresse_count = df['Adresse'].value_counts().reset_index()
adresse_count.columns = ['Adresse', 'N']
fig_adresse = px.bar(adresse_count, x='Adresse', y='N', color='Adresse')
st.plotly_chart(fig_adresse, use_container_width=True)

# 4. Répartition des certificats
st.subheader("Répartition des certificats")
certif_count = df['certificat_status'].value_counts().reset_index()
certif_count.columns = ['certificat_status', 'N']
fig_certif = px.bar(certif_count, x='certificat_status', y='N', color='certificat_status')
st.plotly_chart(fig_certif, use_container_width=True)

# 5. Certificat par genre et adresse
"""st.subheader("Répartition des certificats par genre et région")
fig_certif_genre_adresse = px.sunburst(
    df,
    path=['certificat_status', 'Genre', 'Adresse'],
    values=None,
    color='certificat_status'
)
st.plotly_chart(fig_certif_genre_adresse, use_container_width=True)
"""
"""# 5. Certificat par genre et adresse (Barres groupées)
st.subheader("Répartition des certificats par genre et région")
grouped_df = df.groupby(['certificat_status', 'Genre', 'Adresse']).size().reset_index(name='N')
fig_certif_genre_adresse = px.bar(
    grouped_df,
    x='certificat_status',
    y='N',
    color='Genre',
    barmode='group',
    facet_col='Adresse',
    labels={'certificat_status': 'Certificat', 'Genre': 'Genre', 'Adresse': 'Région'}
)
fig_certif_genre_adresse.update_layout(height=700)
st.plotly_chart(fig_certif_genre_adresse, use_container_width=True)
"""
# 5. Certificat par genre et adresse (Barres groupées)
st.subheader("Répartition des certificats par genre et région")
grouped_df = df.groupby(['certificat_status', 'Genre', 'Adresse']).size().reset_index(name='N')
fig_certif_genre_adresse = px.bar(
    grouped_df,
    x='certificat_status',
    y='N',
    color='Genre',
    barmode='group',
    facet_col='Adresse',
    labels={'certificat_status': 'Certificat', 'Genre': 'Genre', 'adresse': 'Région'}
)
fig_certif_genre_adresse.update_layout(height=700)
st.plotly_chart(fig_certif_genre_adresse, use_container_width=True)

# 6. Affichage des données sous forme de tableau
st.subheader("Données détaillées par certificat, genre et région")
st.dataframe(grouped_df)

