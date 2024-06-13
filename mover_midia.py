import os
import shutil

"""
Move todas as imagens e videos que contêm uma palavra-chave específica no nome para um diretório de destino.
    
"""
def mover_midia(base_dir, destino_dir, palavra_chave):

    os.makedirs(destino_dir, exist_ok=True)
    
    for dirpath, dirnames, filenames in os.walk(base_dir):
        for file in filenames:
            if file.endswith(('.jpg', '.png', '.mp4')) and palavra_chave in file:
                full_file_path = os.path.join(dirpath, file)
                
                destino_file_path = os.path.join(destino_dir, file)
                
                shutil.move(full_file_path, destino_file_path)
                print(f'Arquivo {full_file_path} movido para {destino_file_path}')

base_dir = r''

destino_dir = r''
palavra_chave = ''

mover_midia(base_dir, destino_dir, palavra_chave)