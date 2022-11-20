
IMG_LIST = "images.txt"
DB_FOLDER = "DB"

SEQUENTIAL_FILE       = f"{DB_FOLDER}/seq.db"
RTREE_FILE            = f"{DB_FOLDER}/rtree"
KDTREE_FILE           = f"{DB_FOLDER}/kdtree"
RTREE_DATA_EXTENSION  = "dat"
RTREE_INDEX_EXTENSION = "ind"

RTREE_DATAFILE        = RTREE_FILE + "." + RTREE_DATA_EXTENSION
RTREE_INDEXFILE       = RTREE_FILE + "." + RTREE_INDEX_EXTENSION
KDTREE_DATAFIILE      = KDTREE_FILE + "." + RTREE_DATA_EXTENSION
KDTREE_INDEXFILE      = KDTREE_FILE + "." + RTREE_INDEX_EXTENSION

import numpy as np
# Distancia Euclidiana con Numpy
def ED(Q, P):
	return np.sqrt(((Q-P)**2).sum())