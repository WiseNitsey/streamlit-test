import streamlit as st

st.title('hitung luas persegi panjang')

panjang = st.number_input('nilai p', 0 )
lebar = st.number_input('nilai l', 0 )
hitung = st.button('luas')

if hitung : 
    luas = panjang * lebar
    st.write('luas', luas)
  
