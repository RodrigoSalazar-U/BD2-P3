import rtree
import .config

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
		for filename, imgvec in ImageLoader(IMG_LIST):
			self.ind.insert(filename, imgvec)

    # ------------------------------------------------
	#                   OPERATIONS
	# ------------------------------------------------
	def KNNSearch(q,k):
        return self.ind.nearest(q, num_results=k)
    
    def RangeSearch(q,radius):
        result = []
        bottom = [i - radius for i in q]
        top    = [i + radius for i in q]
        MBB    = bottom+top

        upperbound = self.ind.intersection( tuple(MBB), objects=True )
        for item in upperbound:
            dist = ED(np.array(q), np.array(item.mbb))
            if ( dist <= radius):
                result.append(((item.id, item.bbox), dist))

        result.sort(key=lambda tup : tup[1])
        return result
