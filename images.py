import face_recognition

def ImageLoader(image_list_file, num_entries):
    """
    Generador para extraer todos los vectores caracterisitcos
    de una lista de archivos de imagenes
    """
    with open(image_list_file) as f:
        for num in range(num_entries):
            filename = next(f).strip("\n")
            imgvec = get_image_vector(filename)
            if imgvec is not None:
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
    dist = face_recognition.face_distance((vec1,), vec2)
    return dist

if __name__=="__main__":
    for i in ImageLoader("images.txt",5):
        print(i)