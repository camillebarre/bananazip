class FilePriorite:
    def __init__(self):

        self.file = []

    def enfiler(self, e, p: int):
        """
        Ajoute un élément e à la file avec la priorité p.
        Prend en argument l'élément e et sa priorité p."""
        self.file.append((e, p))
        self.file = sorted(self.file, key=lambda x: x[1], reverse=True)

    def defiler(self):
        """Retourne l'élément de la file avec la plus petite priorité."""
        e = self.file.pop()
        return e[0], e[1]

    def __str__(self):
        return str(self.file)

    def __len__(self):
        return len(self.file)


if __name__ == "__main__":
    f = FilePriorite()
    f.enfiler("toto", 6)
    f.enfiler("toto2", 5)

    print(f.defiler())
