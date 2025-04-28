import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Bananacompresse import *
from Bananarelaxe import *
import os


class Fenetre(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.path_fichier = None
        self.path_dossier = None
        self.title = "Bananazip"
        self.left = 300
        self.top = 300
        self.width = 620
        self.height = 400
        self.creer_interface()

    def creer_interface(self):
        """
        Creer la fenêtre
        """
        X_label = 20
        Y_label = 48
        X_button = 160
        Y_button1 = 40

        height_button = 25
        width_button = 160

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button1 = QPushButton("Fichier à compresser", self)
        button1.setGeometry(X_button, Y_button1, width_button, height_button)
        button1.clicked.connect(self.ouvrirfichier)

        button2 = QPushButton("Compresser le fichier", self)
        button2.setGeometry(X_button, Y_button1 + 80, width_button, height_button)
        button2.clicked.connect(self.compresser)

        button3 = QPushButton("Fichier à décompresser", self)
        button3.setGeometry(X_button, Y_button1 + 160, width_button, height_button)
        button3.clicked.connect(self.ouvrirdossier)

        button4 = QPushButton("Décompresser le fichier", self)
        button4.setGeometry(X_button, Y_button1 + 240, width_button, height_button)
        button4.clicked.connect(self.decompresser)

        self.label_1 = QLabel(self)
        self.label_1.move(X_label, Y_label)
        self.label_1.setText("1. Choisir un fichier")

        self.label_2 = QLabel(self)
        self.label_2.move(X_label, Y_label + 80)
        self.label_2.setText("2. Compresser le fichier")

        self.label_3 = QLabel(self)
        self.label_3.move(X_label, Y_label + 160)
        self.label_3.setText("1. Choisir un fichier")

        self.label_4 = QLabel(self)
        self.label_4.move(X_label, Y_label + 240)
        self.label_4.setText("2. Décompresser le fichier")

    def ouvrirfichier(self):

        self.path_fichier = QFileDialog.getOpenFileName(
            self,
            "choisir un fichier à compresser ou décompresser",
            "c:\\",
        )[0]
        # QFileDialog.getOpenFileName renvoie un tuple avec le path du fichier et son type
        # or nous n'avons besoins que du path

    def ouvrirdossier(self):

        self.path_dossier = QFileDialog.getExistingDirectory(
            self,
            "Choisir un fichier à compresser ou décompresser",
            "c:\\",
        )

    def compresser(self):
        """
        Ouvre le fichier selectionné s'il a été séléctioné (ou affiche une erreur) et appel la fonction main
        chargée de compresser le fichier, et affiche le méssage de réussite.
        """
 
        if self.path_fichier is None:
            QMessageBox.about(self, "Error", "Veuillez choisir un fichier")
            return
        with open(self.path_fichier, "rb") as f:
            fichier = f.read()
        path_dir = os.path.dirname(self.path_fichier) #path_dir est l'anglicisme de "chemain d'acces"
        nom_fichier, extention = os.path.splitext(os.path.basename(self.path_fichier))

        # récupère le nom du fichier sans son extension

        main(fichier, nom_fichier, path_dir, extention)
        QMessageBox.about(self, "Done", "Compression réussie")

    def decompresser(self):
        """
        Ouvre le dossier selectionné s'il a été séléctioné (ou affiche une erreur) et appel la fonction decompression
        chargée de décompresser le fichier, et affiche le méssage de réussite.
        """

        if self.path_dossier is None:
            QMessageBox.about(self, "Error", "Veuillez choisir un dossier")
            return
        decompression(self.path_dossier)

        QMessageBox.about(self, "Done", "Décompression réussie")


if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)  # empêche de lancer plusieurs applications

    fen = Fenetre()
    fen.show()
    app.exec_()
