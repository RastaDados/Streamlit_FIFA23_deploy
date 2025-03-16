import streamlit as st

st.set_page_config(
    page_title='Players',
    page_icon='🏃',
    layout='wide'
)

df_data = st.session_state['data']

clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox('Clube', clubes)

df_players = df_data[(df_data['Club'] == club)]
players = df_players['Name'].value_counts().index
player = st.sidebar.selectbox('Jogador', players)

player_stats = df_data = df_data[df_data['Name'] == player].iloc[0]

st.image(player_stats['Photo'])
st.title(player_stats['Name'])

st.markdown(f'**Clube:** {player_stats["Club"]}')
st.markdown(f'**Posição:** {player_stats["Position"]}')

col1, col2, col3 = st.columns(3)
with col1:
    col1.markdown = st.markdown(f'**Idade:** {player_stats["Age"]}')
with col2:
    col2.markdown = st.markdown(f'**Altura:** {player_stats["Height(cm.)"] / 100}')
with col3:
    col3.markdown = st.markdown(f'**Peso:** {player_stats["Weight(lbs.)"] * 0.453:.2f}')
st.divider()

st.subheader(f'Overall {player_stats['Overall']}')
st.progress(int(player_stats['Overall']))

col1, col2, col3 = st.columns(3)
with col1:
    col1.metric(label='Valor de Mercado', value=f"£ {player_stats['Value(£)']:,}")
with col2:
    col2.metric(label='Resumeração Semanal', value=f"£ {player_stats['Wage(£)']:,}")
with col3:
    col3.metric(label='Cláusula de Recisão', value=f"£ {player_stats['Release Clause(£)']:,}")
st.divider()
