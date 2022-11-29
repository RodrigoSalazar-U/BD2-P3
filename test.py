import time
from rt import *
from seq import * 
from kdtree import *

TEST_K = 8

print(f"""Testing Config:
    -N:{MAX_NUMBER_ENTRIES}
    -K:{TEST_K}
""")

# TESTING QUERY
imgf = "data/lfw/Zydrunas_Ilgauskas/Zydrunas_Ilgauskas_0001.jpg"
q = get_image_vector(imgf)

print("--- TEST SEQUENTIAL ---")
db_seq = SequentialFile(force=True)
tmp_time = time.time()
result = db_seq.KNNSearch(q,TEST_K)
seq_time = time.time()-tmp_time

print(f"--- PARTIAL RESULTS ---")
print(f"Sequential: Time {seq_time}")
print()

print("--- TEST RTREE ---")
db_rt = RtreeStruct()
tmp_time = time.time()
result = db_rt.KNNSearch(q,TEST_K)
rt_time = time.time()-tmp_time


print(f"--- PARTIAL RESULTS ---")
print(f"Sequential: Time {seq_time}")
print(f"RTree: Time {rt_time}")
print()

print("--- TEST KDTREE ---")
arbolito = KDTree()
tmp_time = time.time()
result, nombres = arbolito.KNN_search_arbolito(q,TEST_K)
kdtree_time = time.time()-tmp_time


print(f"--- FINAL RESULTS ---")
print(f"Sequential: {seq_time}")
print(f"RTree: {rt_time}")
print(f"KDTree: {kdtree_time}")
print()
