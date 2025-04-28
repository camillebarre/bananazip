import os
import pickle


def decompression(dir_compressed):
    """
    Décodage du fichier compressé.
    Prend en argument le chemin du dossier contenant le fichier compressé et la table d'encodage.
    Ne retourne rien.
    """
    path_file= os.path.basename(dir_compressed)[:-10] + ".bin"
    with open(
        os.path.join(dir_compressed, path_file), "rb"
    ) as f:
        byte_data = f.read()
    with open(os.path.join(dir_compressed, "table.pkl"), "rb") as f:
        table_code = pickle.load(f)
        extention = table_code["EXTENTION"]
        del table_code["EXTENTION"]
        table_code = {
            v: k for k, v in table_code.items()
        }  # inversion des clés et valeurs du dictionnaire

    # Récupération du nombre de zero en complétion
    completion = byte_data[0]

    chaine_binaire = ""
    for byte in byte_data[1:]:
        chaine_binaire += f"{byte:08b}"
        # f"" permet de formater un string avec des variables
        # byte:08b permet de convertir un byte en binaire sur 8 bits ( 0 = remplissage de gauche, 8 = nombre de bits et b = binaire)

    # Suppression de la completion
    if completion > 0:
        chaine_binaire = chaine_binaire[:-completion]

    # Décodage avec la table d'encodage
    byte = bytearray()
    i = 0
    while i < len(chaine_binaire):
        j = i
        while chaine_binaire[i:j] not in table_code:
            j += 1
        byte.append(table_code[chaine_binaire[i:j]])
        i = j
    parent = os.path.dirname(dir_compressed)
    # création du fichier décompressé avec des bytes

    with open(os.path.join(parent, dir_compressed[:-10] + str(extention)), "wb") as f:

        f.write(byte)
