
IMG_LIST = "/home/software2_utec/BD2-P3/images.txt"
DB_FOLDER = "DB"

SEQUENTIAL_FILE       = f"{DB_FOLDER}/seq.db"
RTREE_FILE            = f"{DB_FOLDER}/rtree"
KDTREE_FILE           = f"{DB_FOLDER}/kdtree"
RTREE_DATA_EXTENSION  = "dat"
RTREE_INDEX_EXTENSION = "ind"

MAX_NUMBER_ENTRIES    = 197

RTREE_DATAFILE        = RTREE_FILE + "." + RTREE_DATA_EXTENSION
RTREE_INDEXFILE       = RTREE_FILE + "." + RTREE_INDEX_EXTENSION
KDTREE_DATAFIILE      = KDTREE_FILE + "." + RTREE_DATA_EXTENSION
#KDTREE_INDEXFILE      = KDTREE_FILE + "." + RTREE_INDEX_EXTENSION

import numpy as np
# Distancia Euclidiana con Numpy
def ED(Q, P):
	return np.sqrt(((Q-P)**2).sum())
