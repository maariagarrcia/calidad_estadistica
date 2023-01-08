# diagrama de cajas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
from colorama import Fore
valores = [1.15, 1.20, 1.17, 1.16, 1.16, 1.20, 1.14, 1.19, 1.13, 1.19, 1.20, 1.18, 1.15, 1.13, 1.20, 1.23, 1.22, 1.19, 1.13, 1.15, 1.17, 1.13, 1.22, 1.19, 1.21, 1.19, 1.20, 1.20, 1.17, 1.25, 1.15, 1.20, 1.12, 1.11, 1.18, 1.15, 1.17, 1.20, 1.16, 1.19, 1.17, 1.13, 1.15, 1.20, 1.18, 1.17, 1.16, 1.20, 1.17, 1.17, 1.16, 1.18, 1.16, 1.17, 1.15, 1.21, 1.15, 1.20, 1.18, 1.17, 1.17, 1.13,
           1.16, 1.16, 1.17, 1.17, 1.19, 1.23, 1.20, 1.24, 1.17, 1.17, 1.17, 1.17, 1.18, 1.24, 1.16, 1.18, 1.16, 1.22, 1.15, 1.22, 1.19, 1.18, 1.19, 1.17, 1.16, 1.17, 1.18, 1.19, 1.23, 1.19, 1.16, 1.19, 1.20, 1.20, 1.19, 1.17, 1.19, 1.22, 1.19, 1.18, 1.11, 1.19, 1.19, 1.17, 1.19, 1.17, 1.20, 1.16, 1.16, 1.16, 1.20, 1.20, 1.16, 1.18, 1.21, 1.20, 1.22, 1.19, 1.14, 1.19, 1.17, 1.20, 1.16]

# ordenarlos de menor a mayor
valores.sort()
# calcular de cada numero cuantos hay
valores_unicos = np.unique(valores, return_counts=True)
print("Cuantos valores hay de cada uno:",Fore.YELLOW,valores_unicos,Fore.WHITE)
print()

# calcular la media
media = np.mean(valores)
print()

print("La media es: ",Fore.YELLOW, media,Fore.WHITE)

#calcula la moda
moda = stats.mode(valores)
print()

print("La moda es: ",Fore.YELLOW, moda,Fore.WHITE)

# calcular la mediana
mediana = np.median(valores)
print()

print("La mediana es: ",Fore.YELLOW, mediana,Fore.WHITE)

# calcular los cuartiles
cuartiles = np.quantile(valores, [ 0.25, 0.5, 0.75])
print()

print("Los cuartiles son: ",Fore.YELLOW, cuartiles,Fore.WHITE)

# carlculae el  coeficiente de variacion
coeficiente_variacion = stats.variation(valores)
print()

print("El coeficiente de variacion es: ", Fore.YELLOW,coeficiente_variacion,Fore.WHITE)

# calcular la desviacion tipica estandar
desviacion_tipica = np.std(valores)
print()

print("La desviacion tipica es: ", Fore.YELLOW,desviacion_tipica,Fore.WHITE)

# diagrama de  cajas
plt.boxplot(valores)
plt.title("Diagrama de cajas")
plt.show()

# histograma de frecuencias de struggle
plt.hist(valores, bins=10)
plt.title("Histograma de frecuencias")
plt.show()

# sesgo y curtosis estandar
sesgo = stats.skew(valores)
curtosis = stats.kurtosis(valores)
print("El sesgo es: ", Fore.YELLOW,sesgo,Fore.WHITE)
print()

print("La curtosis es: ",Fore.YELLOW, curtosis,Fore.WHITE)
print()

# desviacion  estandar muestral
desviacion_estandar_muestral = np.std(valores, ddof=1)
print("La desviacion estandar muestral es: ", Fore.YELLOW,desviacion_estandar_muestral,Fore.WHITE)
print()

EI=1.10
ES=1.30
# cp,cps
cp = (ES-EI)/(6*desviacion_estandar_muestral)

print("cp: ",Fore.YELLOW, cp,Fore.WHITE)
print()

cps = (ES-media)/(3*desviacion_estandar_muestral)
print("cps: ", Fore.YELLOW,cps,Fore.WHITE)
print()

# cpk
cpk = min(abs((media-EI)/(3*desviacion_estandar_muestral)), abs((ES-media)/(3*desviacion_estandar_muestral)))
print("cpk: ", Fore.YELLOW,cpk,Fore.WHITE)
print()


#cpi
cpi = abs((media-EI)/(3*desviacion_estandar_muestral))
print("cpi: ",Fore.YELLOW, cpi,Fore.WHITE)
print()

#k
k = (media-1.2)/((ES-EI)/2)*100
print("k: ",Fore.YELLOW, k,Fore.WHITE)
print()





