# Web Scraping de Episodios de Game of Thrones

Este proyecto es un script de Python que realiza un web scraping a la página de Wikipedia sobre los episodios de la serie Game of Thrones.
Utiliza la biblioteca requests para obtener el contenido de la página y BeautifulSoup para analizar y extraer los datos de interés, como las temporadas, los títulos de los episodios,
quién dirigió el episodio, quien escribió el episodio y la fecha de emisión.

## Descripción del Proyecto
Este script extrae y muestra los siguientes datos:
- Número de temporada de cada conjunto de episodios.
- Número y título de cada episodio en la temporada correspondiente.
- Nombre de quien dirigió el episodio
- Nombre de quien escribió el episodio
- Fecha de emisión

El objetivo principal de este script es demostrar cómo se pueden extraer datos estructurados de una página web usando Python.

## Requisitos
- Python 3.x
- Las siguientes bibliotecas
    - **requests**
    - **beautifulsoup4**

Puedes instalar las bibliotecas requeridas utilizando pip:
```bash
pip install requests beautifulsoup4
```

## Cómo ejecutar el script

1. Clona este repositorio o copia el código del script en tu entorno de desarrollo.
2. Ejecuta el script:
```bash
python nombre_del_archivo.py
```
3. El script comenzará a extraer y mostrar en la consola el número de temporada, seguido por una lista de episodios con su número, título, quien dirigió el episodio, quien lo escribió y la fecha de emisión

## Explicación del código
- **requests.get(url):** Realiza una solicitud HTTP GET a la URL especificada para obtener el contenido de la página.

- **BeautifulSoup(content, 'html.parser'):** Crea un objeto BeautifulSoup a partir del contenido HTML, permitiendo un análisis fácil de la estructura del DOM.

- **soup.find_all('div', class_='mw-heading mw-heading3'):** Busca todos los elementos <div> que contienen los encabezados de las temporadas.

- **temporada.find('h3').get_text().strip():** Obtiene el texto del encabezado de la temporada y elimina espacios en blanco innecesarios.

- **temporada.find_next_sibling('div'):** Encuentra el siguiente hermano del <div> actual, que es donde se encuentra la tabla con los episodios.

- **tabla.find_all('tr', class_='vevent'):** Encuentra todas las filas de la tabla que contienen los episodios.

- **celdas[0].get_text(strip=True):** Extrae el texto de la primera celda, que corresponde al número del episodio, eliminando espacios en blanco.

- **celdas[2].get_text(strip=True):** Extrae el texto de la tercera celda, que contiene el título del episodio.


## Aplicaciones del Web Scraping
Este tipo de scraping puede aplicarse en muchos modelos de negocio, como:

- **Agregadores de Contenidos:** Empresas que recolectan información de diferentes fuentes para crear un único punto de acceso.
- **Monitoreo de Precios:** Plataformas que rastrean cambios en los precios de productos en sitios web de comercio electrónico.
- **Análisis de Competencia:** Empresas que analizan las ofertas y estrategias de sus competidores a partir de datos en línea.

Este script es un ejemplo básico que puede ser adaptado a otros casos de uso según las necesidades del negocio.

## Licencia
Este proyecto está bajo la Licencia MIT.
