import rtree
import os
import numpy as np
from config import *
from images import ImageLoader, get_image_distance, get_image_vector

class RtreeStruct():
    def __init__(self):
        ### RTree Config
        # Configurar el indice
        prop = rtree.index.Property()
        prop.dimension = 128
        prop.buffering_capacity = 4 # M, m = M/2
        prop.dat_extension = RTREE_DATA_EXTENSION 
        prop.idx_extension = RTREE_INDEX_EXTENSION
        # Eliminar los archivos
        if os.path.exists(RTREE_DATAFILE):
            os.remove(RTREE_DATAFILE)
        if os.path.exists(RTREE_INDEXFILE):
            os.remove(RTREE_INDEXFILE)
        # Crear indice
        self.ind = rtree.index.Index(RTREE_FILE, properties = prop)
        # load data
        self.load_data()


    # ------------------------------------------------
    #                   LOAD DATA
    # ------------------------------------------------
    def load_data(self):
        # Load img vectors to rtree
        count = 0
        for filename, imgvec in ImageLoader(IMG_LIST):
            count += 1
            self.ind.insert(count, imgvec, obj=filename)


    # ------------------------------------------------
    #                   OPERATIONS
    # ------------------------------------------------
    def KNNSearch(self,q,k):
        result = self.ind.nearest(q, num_results=k, objects=True)
        result = [((item.object, item.bbox[0:128]),ED(np.array(q), np.array(item.bbox[0:128]))) for item in result]
        result.sort(key=lambda tup : tup[1])
        return result
    
    def RangeSearch(self,q,radius):
        result = []
        bottom = [i - radius for i in q]
        top    = [i + radius for i in q]
        MBB    = bottom+top

        upperbound = self.ind.intersection( tuple(MBB), objects=True )
        for item in upperbound:
            mbb = item.bbox[0:128]
            dist = ED(np.array(q), np.array(mbb))
            if ( dist <= radius):
                result.append(((item.object, mbb), dist))

        result.sort(key=lambda tup : tup[1])
        return result

if __name__=="__main__":
    db = RtreeStruct()
    q = get_image_vector('data/lfw/Aaron_Eckhart/Aaron_Eckhart_0001.jpg')
    #q = get_image_vector('https://storage.cloud.google.com/bd3-proyecto/ROSTROS/Aaron_Eckhart/Aaron_Eckhart_0001.jpg')

    print("----------")
    print("TEST KNN")
    result = db.KNNSearch(q,3)
    for i in result:
        print(i[0][0])

    print("----------")
    print("TEST RANGE")
    result = db.RangeSearch(q,0.7)
    for i in result:
        print(i[0][0])

