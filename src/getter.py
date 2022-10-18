from pathlib import Path



def get_all(path): # Retornar todo del directorio;
    all = { # Diccionario con las claves tipo listas vacias para llenar osea declaro un diccionario con listas
        'subdir' : [],
        'files' : [],
        'suffixes' : []
    }
    path = Path(path)
    if path.is_dir(): # Verifica que la ruta es correcta retorna true;
        for i in path.iterdir(): # recorre todos los objetos del directorio archivos y carpeta;
            # los sufijos vacios o llenos son determinantes
            # ya que los vacios serian tipo Downloads no lleva sufijo, entonces por descarte es una carpeta
            # los sufijos llenos serian tipo los Downloads.py que llevan sufijo, por descarte es un archivo
            if i.is_file(): # si el sufijo es diferente al vacio se ejecutara, en este caso es un archivo
                all['files'].append(i) # agregar valores al diccionario all, en la parte de files
                if i.suffix not in all['suffixes']: # si el sufijo no esta en la lista, se agrega
                    all['suffixes'].append(i.suffix) # agregar valores al diccionario all, en la parte de suffixes
            elif i.is_dir(): # si el sufijo es diferente al lleno se ejecutara, en este caso es una carpeta
                all['subdir'].append(i) # agregar valores al diccionario all, en la parte de subdir
            
    return all['subdir'], all['files'], all['suffixes']

def exist(obj, path,  mode):
    suffix = obj.split('.') # lo divide en partes 
    num = len(suffix) # cuenta cuantas partes tiene 
    
    if num == 3: # en caso de archivos como ejemplo.tar.gz
        suffix = (suffix[1] + '.' + suffix[2]) # Declaras el sufijo con su partes correspondientes
    elif num == 2: # en caso de archivos como ejemplo.py
        suffix = ('.' + suffix[1]) # Declaras el sufijo con su partes correspondientes

    if mode == 'parent': # Directorio Superficial
        parent = sorted(path.glob(f'*{suffix}'))
    elif mode == 'sub': # Directorio Superficial Y Subdirectorio
        parent = sorted(path.glob(f'*/*{suffix}'))
    elif mode == 'tree': # Revisa toda la raiz desde el directorio dado
        parent = sorted(path.glob(f'**/*{suffix}'))
        
    if any(parent) == False: # Si esta la lista vacia retorna false
        return False
    
    for i in parent: # Itinera los valores de la lista
        if obj in i.name: # si el archivo o carpeta que ingresamos coincide, existe devuelve true y la direccion
            return True, i
        elif obj not in i.name: # y si no coincide continua la itineracion
            continue
        
    return False

