import requests
from bs4 import BeautifulSoup

# Obtener el contenido de la página
response = requests.get('https://es.wikipedia.org/wiki/Anexo:Episodios_de_Game_of_Thrones')
content = response.text
soup = BeautifulSoup(content, 'html.parser')

# Encontrar todas las temporadas
temporadas = soup.find_all('div', class_='mw-heading mw-heading3')

for temporada in temporadas:
    # Obtener el número de la temporada
    num_temporada = temporada.find('h3').get_text().strip()
    print(f'\n{num_temporada.upper()}\n' + '-'*30)

    # Obtener la tabla correspondiente a la temporada
    siguiente = temporada.find_next_sibling('div')
    if siguiente:
        tabla = siguiente.find('table', class_='wikitable')
        if tabla:
            episodios = tabla.find_all('tr', class_='vevent')
            for episodio in episodios:
                celdas = episodio.find_all('td')
                num_episodio = celdas[0].get_text(strip=True)
                titulo = celdas[1].get_text(strip=True).strip('«»')
                dir_por = celdas[2].get_text(strip=True)
                escrito_por = celdas[3].get_text(strip=True)
                emision = celdas[4].get_text(strip=True)
                print(f'\nEpisodio {num_episodio}')
                print(f'titulado {titulo}')
                print(f'Dirigido por {dir_por}')
                print(f'Escrito por {escrito_por}')
                print(f'Fecha de emisón {emision}')

