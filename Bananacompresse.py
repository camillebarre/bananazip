from FileAPriorite import *
from Arbre_bin import *
import os
import pickle


def occurence(contenu):
    """
    Compte le nombre d'occurence de chaque caractère dans le texte.
    Prend en argument le texte.
    Retourne un dictionnaire avec les caractères en clé et le nombre d'occurence en valeur.
    """
    a = {}
    for i in contenu:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
    return a


def arbre_huff(dic):
    """
    Crée l'arbre de huffman à partir du dictionnaire des occurences.
    Prend en argument le dictionnaire des occurences.
    Retourne l'arbre de huffman.
    """
    file = FilePriorite()
    for i in dic:
        file.enfiler(ArbreBin(eti=i), dic[i])
    while len(file) > 1:
        e1, p1 = file.defiler()
        e2, p2 = file.defiler()
        file.enfiler(ArbreBin(fg=e1, fd=e2), p1 + p2)
    return file.defiler()[0]


def reecriture(contenu, table_code):
    """
    Converti le texte en binaire grace à la table d'encodage.
    Prend en argument le texte et la table d'encodage.
    Retourne le texte converti en binaire.
    """
    # utilise la  table pour convertir l'integralité du texte en 0 et 1
    chaine_binaire = ""
    for i in contenu:
        chaine_binaire += table_code[i]

    # modifie la chaine pour que sa taille soit un multiple de 8
    completion = 8 - len(chaine_binaire) % 8
    chaine_binaire += "0" * completion

    contenuEnBinaire = bytearray()
    contenuEnBinaire.append(completion)  # renseigne le nombre de zero ajouté
    for i in range(0, len(chaine_binaire), 8):
        contenuEnBinaire.append(
            int(chaine_binaire[i : i + 8], 2)
        )  # converti des tranches des 8 bits en base 10 pour les ajouter au bytearray

    return contenuEnBinaire


def main(contenu, nom_fichier, dir_fichier, extention):
    """
    Fonction principale qui compresse le texte.
    Prend en argument le texte, le nom du fichier compressé et le dossier de sauvegarde.
    """

    dic = occurence(contenu)

    arbre = arbre_huff(dic)
    tab_code = arbre.creer_table()

    contenu = reecriture(contenu, tab_code)

    path_dir = os.path.join(dir_fichier, nom_fichier)+".bananazip"
    tab_code["EXTENTION"] = extention
    os.makedirs(
        path_dir, exist_ok=True
    )  # créer un dossier qui va contenir le fichier compressé et la table d'encodage
    # écriture du fichier .bin
    with open(os.path.join(path_dir, nom_fichier + ".bin"), "wb") as f:
        f.write(contenu)
    # sauvegarde de la table d'encodage avec pickle
    with open(os.path.join(path_dir, "table.pkl"), "wb") as fp:
        pickle.dump(tab_code, fp)


if __name__ == "__main__":
    txt = "BananaMogus flirted with BananaMagus and Bananafell in Bananalove the Bananathird of Bananamarch"
    main(txt, "test", "./")
