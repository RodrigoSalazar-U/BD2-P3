import json
import heapq
from .images import get_image_distance

### SEQUENTIAL
class SequentialFile():
	def __init__(self):
		self.init_seqfile()

	# ------------------------------------------------
	#                WRITE AND READ
	# ------------------------------------------------
	def init_seqfile():
		### Create Sequential File
		for filename, imgvec in ImageLoader(IMG_LIST):
			with open(SEQUENTIAL_FILE, 'w') as f:
				data = {filename:imgvec}
				jsondata = json.dumps(data) + "\n"
				f.write(data)

	def read_seqfile():
		### Read Sequential File
		with open(SEQUENTIAL_FILE, 'r') as f:
			for jsondata in f:
				data = json.loads(jsondata)
				for filename, imgvec in data.iteritems():
					yield (filename, imgvec)
			
	# ------------------------------------------------
	#                  OPERATIONS
	# ------------------------------------------------
	def KNNSearch(q,k):
		result = []
		for (filename, imgvec) in self.read_seqfile():
			dist = - get_image_distance(q,imgvec) # Dist negativa para convertir min heap a max heap
			if (len(result) < k):
				heapq.heappush(result, (dist, (filename, imgvec)))
			else:
				current_max = result[0]
				if (current_max[0] < dist):
					heapq.heappop(result)
					heapq.heappush(result, (dist, (filename, imgvec)))
		result = [(tup[1], - tup[0]) for tup in result]
		result.sort(key=lambda tup : tup[1])
		return result

	def RangeSearch(q,radius):
		result = []
		for (filename, imgvec) in self.read_seqfile():
			dist = get_image_distance(q,imgvec) # Dist negativa para convertir min heap a max heap
			if (dist <= radius):
				result.append( ((filename, imgvec), dist) )
		result.sort(key=lambda tup : tup[1])
		return result


