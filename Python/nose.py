import xml.etree.ElementTree as ET
import csv

# Cargar el archivo XML
tree = ET.parse('movies.xml')
root = tree.getroot()

# Crear un archivo CSV
with open('movies.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Director', 'Year'])  # Escribir la cabecera

    # Iterar sobre cada elemento en el archivo XML
    for movie in root.findall('movie'):
        title = movie.find('title').text
        director = movie.find('director').text
        year = movie.find('year').text
        writer.writerow([title, director, year])  # Escribir los datos de cada película