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
# Seis imagens serão exibidas, aleatoriamente

import streamlit as st
import requests
from bs4 import BeautifulSoup
import random
import sys

# Configurando a página (Favicon e título da página)
st.set_page_config(page_title="Buscador de imagens",page_icon=":globe_with_meridians:", layout="wide")

# Criando o H1
st.markdown("<h1 style='text-align: center;'>À procura de imagens</h1>", unsafe_allow_html=True)

# Criando o formulário
with st.form("Busca"):
  keyword=st.text_input("Digite uma palavra")
  busca=st.form_submit_button("Busca")
  surpresa=st.form_submit_button("Surpreenda-me")
  
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
    if "/premium_photo-" not in url:
      list_images.append(url)
  
  # Escolhendo aleatoriamente seis imagens (a lista contém 92)
  try:
      list_images_random=random.sample(list_images,6)
  except:
      st.error("Digite uma palavra, ou tente outra")
      sys.exit()
  
  # Exibindo as imagens
  for i in range(0,6):
    if (i%2) == 1:
      col1.image(list_images_random[i])
    else:
      col2.image(list_images_random[i])


# Ao clicar em "Surpreenda-me"
if surpresa:
  list_images=[]
  words=['bear', 'bee', 'bird', 'camel', 'cat', 'chicken', 'cow', 'crocodile', 'dog', 'dolphin', 'elephant', 'fish', 'fox', 'frog', 'giraffe', 'goat', 'horse', 'kangaroo', 'leopard', 'lion', 'lizard', 'monkey', 'mouse', 'octopus', 'otter', 'panda', 'penguin', 'pig', 'rabbit', 'rat', 'rhinoceros', 'seal', 'snake', 'spider', 'squirrel', 'tiger', 'turtle', 'whale', 'wolf', 'zebra', 'daffodil', 'hyacinth', 'lilac', 'lily', 'orchid', 'rose', 'sunflower', 'tulip', 'violet', 'azalea', 'begonia', 'camellia', 'carnation', 'chamomile', 'daisy', 'dandelion', 'delphinium', 'gardenia', 'geranium', 'hibiscus', 'hollyhock', 'iris', 'jasmine', 'lavender', 'lily of the valley', 'lotus', 'marigold', 'morning glory', 'narcissus', 'pansy', 'peony', 'primrose', 'rosemary', 'saffron', 'sage', 'snapdragon', 'sunflower', 'violet', 'wisteria', 'zinnia', 'Chevrolet Corvette', 'Ford Mustang', 'Dodge Challenger', 'Chevrolet Camaro', 'Ford F-150', 'Chevrolet Silverado', 'Ram 1500', 'Toyota Camry', 'Honda Accord', 'Honda Civic', 'Toyota Corolla', 'Nissan Sentra', 'Mazda3', 'Hyundai Elantra', 'Kia Forte', 'Volkswagen Jetta', 'Nissan Altima', 'Toyota RAV4', 'Honda CR-V', 'Ford Explorer', 'Chevrolet Tahoe', 'Chevrolet Suburban', 'Ford Expedition', 'GMC Yukon', 'Toyota Highlander', 'Honda Pilot', 'Nissan Pathfinder', 'Hyundai Santa Fe', 'Kia Telluride', 'Volkswagen Atlas', 'Mercedes-Benz C-Class', 'BMW 3 Series', 'Audi A4', 'Lexus IS', 'Acura TLX', 'Infiniti Q50', 'Lincoln MKZ', 'Tesla Model 3', 'Tesla Model Y', 'Porsche 911', 'BMW M3', 'Audi R8', 'Mercedes-AMG C 63', 'Lexus LC 500', 'Boeing 747', 'Boeing 737', 'Boeing 787', 'Airbus A320', 'Airbus A330', 'Airbus A380', 'Cessna 172', 'Piper Cherokee', 'Diamond DA40', 'Gulfstream G650', 'Bombardier Global 7500', 'Embraer Legacy 650', 'Cessna Citation X', 'Dassault Falcon 7x', 'Beechcraft King Air 350', 'Piper M600', 'Cessna Citation Latitude', 'Embraer Praetor 600', 'Dassault Falcon 8x', 'Boeing 777', 'Airbus A350', 'Boeing 767', 'Airbus A340', 'Boeing 757', 'Airbus A319', 'Boeing 737 MAX', 'Airbus A321neo', 'Cessna Citation CJ3+', 'Piper Meridian', 'Diamond DA50', 'Gulfstream G550', 'Bombardier Global 6500', 'Embraer Legacy 500', 'Cessna Citation XLS+', 'Dassault Falcon 900LX', 'Beechcraft King Air 200', 'Piper M500', 'Cessna Citation Sovereign', 'Embraer Praetor 500', 'diamond', 'ruby', 'emerald', 'sapphire', 'topaz', 'amethyst', 'peridot', 'tourmaline', 'garnet', 'aquamarine', 'tanzanite', 'tsavorite', 'kunzite', 'heliodor', 'citrine', 'smoky quartz', 'rose quartz', 'agate', 'onyx', 'jade', 'malachite', 'jasper', 'lapis lazuli', 'turquoise', 'moonstone', 'opal', 'pearl']

  keyword=random.sample(words,1)
  page = requests.get(f"https://unsplash.com/pt-br/s/fotografias/{keyword}")
  soup = BeautifulSoup(page.content, "html.parser")
  images = soup.find_all("div", class_="MorZF")
  # Criando as colunas abaixo do formulário
  col1,col2=st.columns(2)
  # Abastecendo a lista com todas urls
  for image in images:
    url=image.find("img").get("src")
    if "/premium_photo-" not in url:
      list_images.append(url)
  
  # Escolhendo aleatoriamente seis imagens (a lista contém 92)
  try:
      list_images_random=random.sample(list_images,6)
  except:
      st.error("Digite uma palavra, ou tente outra")
      sys.exit()
  
  # Exibindo as imagens
  for i in range(0,6):
    if (i%2) == 1:
      col1.image(list_images_random[i])
    else:
      col2.image(list_images_random[i])

# st.markdown(f"### {keyword}")