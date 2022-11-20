import math
import os
import numpy as np
from config import *
from images import get_image_vector, get_image_distance, ImageLoader
from scipy import spatial

class KDTree():
    def __init__(self, k):
        #Defino la cantidad de dimensiones
        self.n = 128
        #Elimino los archivos, si existen
        if os.path.exists(KDTREE_DATAFIILE):
            os.remove(KDTREE_DATAFIILE)
        if os.path.exists(KDTREE_INDEXFILE):
            os.remove(KDTREE_INDEXFILE)
        #Creo el KD Tree con la data
        self.kd_tree, self.arreglo_datos = self.load_data()

    def load_data(self):
        arreglo = []
        for _, imgvec in ImageLoader(IMG_LIST):
            arreglo.append(imgvec)
        arbolito = spatial.KDTree(arreglo)
        return arbolito, arreglo
    
    def KNN_search_arbolito(self,point,k_n):
        distance, index = self.kd_tree.query(point,k=k_n) #Devuelve dos resultados, un arreglo de distancias y una arreglo de indices
        arreglo_resultados = []
        for indice in index:
            arreglo_resultados.append(self.arreglo_datos[indice])
        return arreglo_resultados
            
    def range_search_arbolito(self,point,r):
        result = sorted(self.kd_tree.query_ball_point(point,r)) #Devuelve un arreglo de indices con los resultados
        resultado_puntos = [] #Si point es un arreglo de un unico punto, entonces devuelve un arreglo de indices
        for indice in result: #Si point es un arreglo de varios puntos, entonces devuelve varios puntos con respecto al radio
            resultado_puntos.append(self.arreglo_datos[indice])
        return resultado_puntos
        
if __name__ == '__main__':
    x = 0
    
    
'''
    def build_kdtree(self, points, depth=0):
        n = len(points)
        
        if n <= 0:
            return None
        
        axis = depth % self.k
        
        sorted_points = sorted(points, key=lambda point: point[axis])
        
        return {
            "point" : sorted_points[n / 2],
            "left" : self.build_kdtree(sorted_points[:n / 2], depth + 1),
            "left" : self.build_kdtree(sorted_points[n/2 + 1:], depth + 1)
        }
    
    def kdtree_closest_point(self, root, point, depth=0, best=None):
        if root == None:
            return best
        
        axis = depth % self.k
        
        next_best = None #El mejor punto con menor distancia respecto a uno en especifico hasta ahora
        next_branch = None #A cual rama me voy, si la derecha o izquierda
        
        if best is None or ED(point, best) > ED(point, root['point']):
            next_best = root['point']
        else:
            next_best = best
            
        if point[axis] < root['point'][axis]:
            next_branch = root['left']
        else:
            next_branch = root['right']
        
        return self.kdtree_closest_point(next_branch, point, depth + 1, next_best)
    '''