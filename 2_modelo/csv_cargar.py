#
# Entrada / salida de archivos CSV
#

import csv
import numpy as np

arch = '/home/yoviajo/Documentos/lab/tesis/p11/extraido/opiniones/s01/790r/ta_resenia_sitio.csv'

# Leer archivo CSV e imprimir cada fila como un arreglo de elementos
#with open(arch) as csvDataFile:
#    csvReader = csv.reader(csvDataFile)
#    for row in csvReader:
#        print(row)

# Leer archivo CSV e imprimir las reseñas que se cargaron a un vector
resenias = []

with open(arch) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        resenias.append(row[4])

#print(resenias)

with open(r'/home/yoviajo/Documentos/lab/tesis/p12/resenias.csv', 'w') as f: 
    write = csv.writer(f) 
    #write.writerow(Details) 
    write.writerows(resenias)
