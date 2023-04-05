from PyQt5.QtWidgets import *
from ui_ana_sayfa import Ui_MainWindow
from sim_e_mail import Email
from sim_sosyal_medya import Sosyal
from sim_canli_destek import Operator
import subprocess

class AnaSayfa(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ana_sayfa = Ui_MainWindow()
        self.ana_sayfa.setupUi(self)

        self.git_e_mail = Email()
        self.git_sosyal_medya = Sosyal()
        self.git_canli_destek = Operator()

        # iletme fonksiyonlarının tanımlanması
        self.ana_sayfa.btn_email.mousePressEvent = self.go_e_mail
        self.ana_sayfa.btn_musteri.mousePressEvent = self.go_musteri_hizmetleri
        self.ana_sayfa.btn_sosyal.mousePressEvent = self.go_sosyal_medya

    # fonksiyon kullanarak farklı pencerelere iletme
    def go_e_mail(self, checked):
        print('email clicked')
        self.git_e_mail.show()

    def go_sosyal_medya(self, checked):
        print('sosyal medya clicked')
        self.git_sosyal_medya.show()

    def go_musteri_hizmetleri(self, checked):
        print('musteri hizmetleri clicked')
        self.git_canli_destek.show()

