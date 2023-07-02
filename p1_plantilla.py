import time
import asyncio
import random

PRECIO_MINIMO = 20000   #El precio base al que se inicia la subasta
PRECIO_MAXIMO = 100000  #El precio maximo que cualquiera de los participantes está dispuesto a pagar(úselo como tope en random.randint()

async def participante():
    



if __name__ == "__main__":
        
	

	"""    
	El código *(cuenta(i) for i in range(5)) desempaqueta los valores generados por la expresión cuenta(i) for i in range(5). En este caso, cuenta(i) representa una función o expresión que devuelve un valor para cada valor de i en el rango del 0 al 4. La expresión cuenta(i) for i in range(5) crea 
	un generador que produce estos valores.Al utilizar el operador "*", se desempaquetan
	los valores generados por el generador y se pasan como argumentos individuales a la función o constructor que los recibe. En este caso, los valores generados por el generador
	se desempaquetan y se pasan como argumentos individuales a una función o constructor no especificada en el código que has proporcionado.
	En resumen, el código *(cuenta(i) for i in range(5)) toma los valores generados por el generador y los pasa como argumentos
	individuales a una función o constructor específico que no está visible en el código proporcionado."""
	#se genera el main de otra forma con esta sintaxis
async def main():
    await asyncio.gather(*(cuenta(i) for i in range(100000)))


if __name__ == "__main__":
    inicio = time.perf_counter()
    asyncio.run(main())	
    fin = time.perf_counter()

    print(f"El programa ejecuto en {fin-inicio} segundos")

"""