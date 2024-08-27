import numpy as np
import matplotlib.pyplot as plt

# GRAFICO DE LINEAS /////////////////////////////////////////////////////////////////////////

plt.plot([1, 2, 3, 4], [1, 4, 9, 16]) # crea un grafico de lineas
plt.title("Gráfico de líneas") # titulo del grafico
plt.xlabel("Eje X") # etiqueta para eje x
plt.ylabel("Eje Y") # etiqueta para eje y
plt.grid(True) # añade cuadricula
plt.show()  # muestra el grafico

# GRAFICO DE BARRAS /////////////////////////////////////////////////////////////////////////

plt.bar([1, 2, 3, 4], [10, 20, 15, 25]) # crea un grafico de barras
plt.title("Gráfico de barras")
plt.xlabel("Categorías")
plt.ylabel("Valores")
plt.show()

# HISTOGRAMA /////////////////////////////////////////////////////////////////////////

data = np.random.randn(1000)
plt.hist(data, bins=30, alpha=0.75) # crea un histograma
plt.title("Histograma")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()


# GRAFICO DE DISPERSION /////////////////////////////////////////////////////////////////////////

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]
plt.scatter(x, y) # crea un grafico de dispersion
plt.title("Gráfico de dispersión")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# PERZONALIZACION /////////////////////////////////////////////////////////////////////////

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], color='green', marker='^', linestyle='--', linewidth=2)
# color: define el color de la linea
# linestyle: estilo de la linea ( - , -- , -. , : )
# linewidth: grosor de la linea
# marker: marcadores para los puntos ( o , s , ^ ) circulo, cuadrado, triangulo
plt.show()

# etiquetas y legendas
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], label='Línea 1')
plt.plot([1, 2, 3, 4], [1, 2, 4, 8], label='Línea 2')
plt.legend()
plt.show()


# MULTIPLES GRAFICOS /////////////////////////////////////////////////////////////////////////

fig, axs = plt.subplots(2, 2) # crea una figura con subgraficos organizados en una cuadricula
axs[0, 0].plot([1, 2, 3], [1, 4, 9])
axs[0, 1].plot([1, 2, 3], [1, 2, 3])
axs[1, 0].plot([1, 2, 3], [1, 8, 27])
axs[1, 1].plot([1, 2, 3], [1, 1, 1])
plt.show()


# GUARDAS UN GRAFICO

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
#plt.savefig('grafico.png') # guarda el grafico en el formato definido (png, jpg, pdf, etc)

