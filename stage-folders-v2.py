import os
import shutil

def main():
    #client_folder = "D:\Tenea\Jenkins\Client\Prueba"  # Actualiza con la ruta correcta
    client_folder = 'Prueba/'

    while verify_folder(client_folder):

    #if verify_folder(client_folder): # Si existe la carpeta notificamos y iniciamos rollback
        print("ERROR: Carpeta cliente existe! Iniciando rollback...")
        print("Iniciando Rollback")
        rollback(client_folder)

    else: # Si no existe copiamos el template
        print("La carpeta del cliente no existe. Copiando el template...")
        copy_template(client_folder)

        if verify_folder(client_folder): # Verifica la plantilla copiada
            print("Carpeta del cliente creada y verificada exitosamente.")
        else:
            print("Error en la verificación de la carpeta del cliente. Iniciando rollback...")
            #rollback(client_folder)

def copy_template(client_folder): # En prueba
    # Crea la carpeta del cliente 
    os.makedirs(client_folder)
    # Ruta completa del nuevo archivo dentro del directorio
    new_file_path = os.path.join(client_folder, 'nombre_del_archivo.txt')

    # Contenido que deseas escribir en el archivo
    file_content = 'Este es el contenido del archivo.'

    # Crear el archivo y escribir el contenido
    with open(new_file_path, 'w') as file:
        file.write(file_content)

def verify_folder(client_folder):
    return os.path.exists(client_folder) # Verificamos si la carpeta existe

def rollback(client_folder): # Eliminamos la carpeta
    print("Eliminando la carpeta del cliente durante el rollback...")
    shutil.rmtree(client_folder)
    print("Carpeta del cliente eliminada exitosamente durante el rollback.")

if __name__ == "__main__":
    main()