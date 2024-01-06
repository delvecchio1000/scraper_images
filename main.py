### Este código executa um Web Scrapper no site da unsplash.com
### Escolha as fotos que desejar

# Crie uma pasta em seu sistema com o nome que preferir. Ex.: "modulos";
# Abra a pasta no VScode
# Abra um terminal
# digite "python -m venv modulos_venv"
# Baixe streamlit ==> "pip install streamlit"
# Baixe requests ==> "pip install requests"
# Baixe BeautifulSoup4 ==> "pip install BeautifulSoup4"
# Copie o código abaixo em, por exemplo: "main.py", e salve
# Execute digitando no terminal "streamlit run main.py"
# Será aberto uma janela de navegador
# Digite uma palavra (recomenda-se em ingles) no formulário
# Dez imagens serão exibidas, aleatoriamente

import streamlit as st
import requests
from bs4 import BeautifulSoup
import random
import sys

# Criando o Título
st.markdown("<h1 style='text-align: center;'>Web Scraper</h1>", unsafe_allow_html=True)

# Criando o formulário
with st.form("Busca"):
  keyword=st.text_input("Digite uma palavra")
  busca=st.form_submit_button("Busca")
  
# Criando a lógica

# Ao clicar em "Busca"
if busca:
  list_images=[]
  page = requests.get(f"https://unsplash.com/pt-br/s/fotografias/{keyword}")
  soup = BeautifulSoup(page.content, "html.parser")
  images = soup.find_all("div", class_="MorZF")
  # Criando as colunas abaixo do formulário
  col1,col2=st.columns(2)
  # Abastecendo a lista com todas urls
  for image in images:
    url=image.find("img").get("src")
    list_images.append(url)
  
  # Escolhendo aleatoriamente dez imagens (a lista contém 92)
  try:
      list_images_random=random.sample(list_images,7)
  except:
      st.error("Digite uma palavra, ou tente outra")
      sys.exit()
  
  # Exibindo as imagens
  for i in range(0,7):
    if (i%2) == 1:
      col1.image(list_images_random[i])
    else:
      col2.image(list_images_random[i])
