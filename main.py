# main.py

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene
from PyQt6.QtGui import QAction, QColor
from PyQt6.QtCore import Qt

# Diğer dosyadan (gates.py) kapı sınıflarını içe aktar
from gates import AndGate, OrGate, NotGate, NandGate, NorGate, XorGate

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dijital Mantık Simülatörü v1.0")
        self.setGeometry(100, 100, 1200, 800) # Pencere boyutu

        # Görsel nesnelerin (kapılar vb.) ekleneceği sanal tuval
        self.scene = QGraphicsScene()
        # Sahne arkaplanını koyu bir renkle daha profesyonel göster
        self.scene.setBackgroundBrush(QColor("#34495e"))

        # Bu tuvale baktığımız pencere (view)
        self.view = QGraphicsView(self.scene, self)
        self.view.setRenderHint(QAction.RenderHint.Antialiasing) # Görüntüyü yumuşat
        self.setCentralWidget(self.view)

        # Menüleri oluştur
        self.create_menus()

    def create_menus(self):
        menu_bar = self.menuBar()
        
        # "Kapı Ekle" menüsü
        add_gate_menu = menu_bar.addMenu("Kapı Ekle")

        # Eklenebilecek kapıların listesi
        # Sözlük yapısı (dictionary) kullanarak menü metni ve sınıfı eşleştiriyoruz
        gate_types = {
            "AND Kapısı": AndGate,
            "OR Kapısı": OrGate,
            "NOT Kapısı": NotGate,
            "NAND Kapısı": NandGate,
            "NOR Kapısı": NorGate,
            "XOR Kapısı": XorGate,
        }

        # Sözlükteki her kapı için bir menü öğesi oluştur
        for name, gate_class in gate_types.items():
            action = QAction(name, self)
            # Bir menü öğesine tıklandığında hangi fonksiyonun çalışacağını belirtiyoruz.
            # Lambda fonksiyonu, doğru kapı sınıfını add_gate fonksiyonuna göndermemizi sağlar.
            action.triggered.connect(lambda checked=False, gc=gate_class: self.add_gate_to_scene(gc))
            add_gate_menu.addAction(action)

    def add_gate_to_scene(self, gate_class):
        """Verilen sınıftan bir kapı nesnesi oluşturur ve sahneye ekler."""
        gate = gate_class()
        # Yeni kapıyı görünümün merkezine yerleştir
        view_center = self.view.mapToScene(self.view.viewport().rect().center())
        gate.setPos(view_center)
        
        self.scene.addItem(gate)
        print(f"Sahneye bir '{gate_class.__name__}' eklendi.")


# Uygulamayı başlatan ana blok
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
