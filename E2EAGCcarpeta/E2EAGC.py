import requests
import os
import sys
from bs4 import BeautifulSoup as bs
import webbrowser


'''
Eder Antonio García Castillo 1799409

Este script hace la busqueda en la pagina de noticias de la universidad
de la facultad solicitada por sus siglas y con un ciclo busca entre el
rango proporcionado, al encontrar algo abre una pagina web directamente.
Abre una pestaña por cada noticia encontrada.
'''


try: 
    import webbrowser 
except ImportError: 
    os.system('pip install webbrowser') 
    print('Installing webbrowser...') 
    print('Ejecuta de nuevo tu script...') 
    exit()

try: 
    import requests 
except ImportError: 
    os.system('pip install requests') 
    print('Installing requests...') 
    print('Ejecuta de nuevo tu script...') 
    exit()

try: 
    from bs4 import BeautifulSoup as bs 
except ImportError: 
    os.system('pip install BeautifulSoup') 
    print('Installing webbrowser...') 
    print('Ejecuta de nuevo tu script...') 
    exit()


print("Este script navega en las páginas de noticias de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")


if inicioRango > finRango:
    inicioRango,finRango = finRango,inicioRango


for i in range (inicioRango,finRango,1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get (url)
    if pagina.status_code != 200: #el codigo 200 es que cargó bien la pagina
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content,"html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content,"html.parser")
                parrafos = soup2.select("p")    
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo",url2)
                        webbrowser.open(url2)
                        break
    

