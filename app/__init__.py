##Importar, utilizar
# una dependencia en python

from flask import Flask, render_template


#crear la aplicacion de flask

app = Flask(__name__)

# Utiizar app para crear una ruta

@app.route('/prueba')
def prueba():
    #defino la lista de paises
    paises = [
        {
            "nombre":"Argentina", 
            "capital":"Buenos aires",
            "moneda": "peso argentino",
            "poblacion": "17 km2",
            "superficie": "2.780.400 km2",
            "ciudades_principales": [
                                        "Mendoza",
                                        "Cordoba",
                                        "Rosario"
                                    ]
        },
        {
            "nombre":"Brasil",
            "capital":"Brazilia",
            "moneda": "real brasileño",
            "poblacion": "25 km2",
            "superficie": "8.515.767 km2",
            "ciudades_principales": [
                                        "Mendoza",
                                        "Cordoba",
                                        "Rosario"
                                    ]
        },
        {
            "nombre":"Mexico",
            "capital":"ciudad de mexico",
            "moneda": "peso mexicano",
            "poblacion": "66 km2",
            "superficie": "1.964.375 km2",
            "ciudades_principales": [
                                        "Guadalajara",
                                        "Moterrey",
                                        "Puebla"
                                    ]
        },
        {
            "nombre":"Colombia",
            "capital":"Bogotá",
            "moneda": "peso colombiano",
            "poblacion": "47 km2",
            "superficie": "1.141.748 km2",
            "ciudades_principales": [
                                        "Medellin",
                                        "cali",
                                        "Cartegena"
                                    ]
        },
        {
            "nombre":"Italia",
            "capital":"Roma",
            "moneda": "euro",
            "poblacion": "200 km2",
            "superficie": "301.340 km2",
            "ciudades_principales": [
                                        "Milan",
                                        "Napoles",
                                        "Turin"
                                    ]
        }
    
    ]

    #Enviar la lista de paises a la vista

    return render_template("paises.html", paises=paises, usuario="Cristian")

