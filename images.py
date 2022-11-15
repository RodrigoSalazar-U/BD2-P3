import face_recognition

def ImageLoader(image_list_file):
    """
    Generador para extraer todos los vectores caracterisitcos
    de una lista de archivos de imagenes
    """
    with open(image_list_file) as f:
        for filename in f:
            imgvec = get_image_vector(filename.strip("\n"))
            if imgvec:
                yield (filename, imgvec)

def get_image_vector(filename):
    """
    Funcion para extraer el vector caracteristico de una imagen
    """
    loaded_image = face_recognition.load_image_file(filename)
    face_encoding = face_recognition.face_encodings(loaded_image)
    if face_encoding:
        return face_encoding[0]
    else:
        return None

def get_image_distance(vec1, vec2):
    """
    Funcion para calcular distancia entre dos vectores caracteristicos
    """
    dist = face_recognition.face_distance(known_face_encodings, face_encoding)
    return dist
