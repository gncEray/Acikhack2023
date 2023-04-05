from PyQt5.QtWidgets import QApplication
from sim_ana_sayfa import AnaSayfa

app = QApplication([])
window = AnaSayfa()
window.show()
app.exec_()