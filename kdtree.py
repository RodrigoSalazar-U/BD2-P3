import math
import json
import subprocess
import argparse
import os
import numpy as np
from config import *
from images import get_image_vector, get_image_distance, ImageLoader
from scipy import spatial

class KDTree():
    def __init__(self):
        #Defino la cantidad de dimensiones
        self.n = 128
        #Elimino los archivos, si existen
        if os.path.exists(KDTREE_DATAFIILE):
            os.remove(KDTREE_DATAFIILE)
        #if os.path.exists(KDTREE_INDEXFILE):
        #    os.remove(KDTREE_INDEXFILE)
        #Creo el KD Tree con la data
        self.kd_tree, self.arreglo_datos, self.arreglo_nombres = self.load_data()

    def load_data(self):
        arreglo = []
        arreglo_name = []
        for nombre, imgvec in ImageLoader(IMG_LIST, MAX_NUMBER_ENTRIES):
            arreglo_name.append(str(nombre))
            arreglo.append(imgvec)
        arbolito = spatial.KDTree(arreglo)
        return arbolito, arreglo, arreglo_name

    def print_arreglo_datos(self):
        print(self.arreglo_datos)
    
    def KNN_search_arbolito(self,point,k_n):
        distance, index = self.kd_tree.query(point,k=k_n) #Devuelve dos resultados, un arreglo de distancias y una arreglo de indices
        arreglo_resultados = {}
        arreglo_nombre_resultado = []
        for indice in index:
            arreglo_resultados[self.arreglo_nombres[indice]] = self.arreglo_datos[indice]
            arreglo_nombre_resultado.append(self.arreglo_nombres[indice])
            #arreglo_resultados.append(self.arreglo_datos[indice])
        return arreglo_resultados, arreglo_nombre_resultado
            
    def range_search_arbolito(self,point,r):
        result = sorted(self.kd_tree.query_ball_point(point,r)) #Devuelve un arreglo de indices con los resultados
        resultado_puntos = {} #Si point es un arreglo de un unico punto, entonces devuelve un arreglo de indices
        resultado_nombres = []
        for indice in result: #Si point es un arreglo de varios puntos, entonces devuelve varios puntos con respecto al radio
            resultado_puntos[self.arreglo_nombres[indice]] = self.arreglo_datos[indice]
            resultado_nombres.append(self.arreglo_nombres[indice])
        return resultado_puntos, resultado_nombres
        
if __name__ == '__main__':
    arbolito = KDTree()
    #q = get_image_vector('data/lfw/Azra_Akin/Azra_Akin_0001.jpg')
    parser = argparse.ArgumentParser()
    parser.add_argument("-n","--number",help="Number")
    parser.add_argument("-f","--filename",help="Filename")
    args = vars(parser.parse_args())

    q = get_image_vector(args['filename'])


    #print('-----------')
    #print('TEST KNN')
    result, nombres = arbolito.KNN_search_arbolito(q,int(args['number']))
    print(nombres)

    #print('------------')
    #print('RANGE SEARCH')
    #result2, nombres2 = arbolito.range_search_arbolito(q,0.7)
    #print(nombres2)
    
