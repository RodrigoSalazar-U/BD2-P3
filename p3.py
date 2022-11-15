
import numpy as np
import os
import rtree
import time
import pandas as pd
import heapq
import math
import random
import face_recognition
### KNN LINEAR
# Distancia Euclidiana con Numpy
def ED(Q, P):
	return np.sqrt(((Q-P)**2).sum())

# Linear Heap KNN search
def KNNSearch(data,q,k):
	result = []
	for row in data:
		dist = - ED(q,row) # Dist negativa para convertir min heap a max heap
		if (len(result) < k):
			heapq.heappush(result, (dist, row))
		else:
			current_max = result[0]
		if (current_max[0] < dist):
			heapq.heappop(result)
			heapq.heappush(result, (dist, row))
	result = [(tup[1], - tup[0]) for tup in result]
	result.sort(key=lambda tup : tup[1])
	return result

### RTree Config
# Configurar el indice
prop = rtree.index.Property()
prop.dimension = 128
prop.buffering_capacity = 4 # M, m = M/2
prop.dat_extension = "data"
prop.idx_extension = "index"
### Tiempos
tiempos_rtree = dict()
tiempos_rtree[3] = list()
tiempos_rtree[6] = list()
tiempos_rtree[9] = list()
tiempos_scan = dict()
tiempos_scan[3] = list()
tiempos_scan[6] = list()
tiempos_scan[9] = list()
### VC Functions
# Obtener vector caracteristico
def get_image_vector(filename):
	loaded_image = face_recognition.load_image_file(filename)
	face_encoding = face_recognition.face_encodings(loaded_image)
	return face_encoding[0]
# Cargar lista de imagenes
def load_image_list(filename):
	with open(filename) as f:
		imagels = f.read().splitlines()
	return imagels
# Cargar lista de vc a memoria
def load_train_data(datals):
	result = []
	for imgfile in datals:
		try:
			result.append(get_image_vector(imgfile))
		except:
			# Algunas imagenes estan corrompidas/No se puede generar su vector
			caracteristico
			# De ser el caso, ignorar
			pass
	return result
### TESTS
# Pseudo random
random.seed(1)
# Cargar lista de imagenes
imagels = load_image_list("imagels.txt")
# Ejecutar tests
for i in [2,3,4,]:#5,6] 5 y 6 fuera de rango
	# Eliminar los archivos
	if os.path.exists("puntos.data"):
		os.remove("puntos.data")
	if os.path.exists("puntos.index"):
		os.remove("puntos.index")
	# Generar los datos
	N = pow(10, i)
	print("Starting set for N={}".format(N))
	samplels = random.sample(imagels, N)
	data = load_train_data(samplels)
	# Insertar los vc_imgs
	ind = rtree.index.Index("vc_imgs", properties = prop)
	j = 0
	for vc_img in data:
		ind.insert(j, vc_img)
		j += 1
	print("Generated sample of size {}".format(len(data)))
	query = data[0]
	for k in [3,6,9]:
		print("K={}".format(k))
		print("START rtree ...")
		# RTree
		start_time = time.time_ns()
		ind.nearest(query, num_results=k)
		tiempos_rtree[k].append(time.time_ns() - start_time)
		print("END rtree")
		# Scan
		print("START linear scan ...")
		start_time = time.time_ns()
		KNNSearch(data,query,k)
		tiempos_scan[k].append(time.time_ns() - start_time)
		print("END linear Scan")
	ind.close()
print("RTREE")
print(pd.DataFrame.from_dict(tiempos_rtree))
print("SCAN")
print(pd.DataFrame.from_dict(tiempos_scan))
