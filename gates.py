# gates.py

from PyQt6.QtWidgets import QGraphicsRectItem, QGraphicsTextItem, QGraphicsEllipseItem
from PyQt6.QtGui import QBrush, QColor, QPen, QFont
from PyQt6.QtCore import Qt

class BaseGate(QGraphicsRectItem):
    """
    Tüm mantık kapılarının miras alacağı temel sınıf.
    Ortak özellikleri (sürüklenme, renk, isim, pinler) burada tanımlarız.
    """
    def __init__(self, name, num_inputs, color_hex, parent=None):
        # Kapının ana gövdesini oluştur (Dikdörtgen)
        # Genişlik: 100, Yükseklik: giriş sayısına göre ayarlanır
        super().__init__(0, 0, 100, (num_inputs * 20) + 30, parent)
        
        # Kapıyı fare ile hareket ettirilebilir yap
        self.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable)
        self.setBrush(QBrush(QColor(color_hex)))
        self.setPen(QPen(Qt.GlobalColor.black, 2)) # Kenarlık ekle

        # Kapının adını yazdır (örn: "AND")
        self.text = QGraphicsTextItem(name, self)
        self.text.setDefaultTextColor(Qt.GlobalColor.white)
        self.text.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        text_width = self.text.boundingRect().width()
        self.text.setPos((self.rect().width() - text_width) / 2, 5)

        self.inputs = []
        self.output = None

        # Kapının giriş pinlerini (küçük daireler) oluştur
        for i in range(num_inputs):
            # Pin'lerin Y pozisyonunu hesapla
            pin_y = 35 + i * 20
            pin = Pin(self, is_output=False)
            pin.setPos(0, pin_y) # Kapının sol kenarına yerleştir
            self.inputs.append(pin)

        # Kapının çıkış pinini oluştur
        pin_y = (self.rect().height()) / 2
        pin = Pin(self, is_output=True)
        pin.setPos(self.rect().width(), pin_y) # Kapının sağ kenarına yerleştir
        self.output = pin

class Pin(QGraphicsEllipseItem):
    """
    Kapıların giriş/çıkışlarını temsil eden küçük daireler.
    """
    def __init__(self, parent, is_output=False):
        # Daireyi merkezden başlatmak için x ve y'ye yarıçapın eksisini ver
        super().__init__(-6, -6, 12, 12, parent) 
        self.is_output = is_output
        color = "#ff4d4d" if is_output else "#4d94ff" # Çıkış kırmızı, giriş mavi
        self.setBrush(QBrush(QColor(color)))
        self.setPen(QPen(QColor("#2c3e50"), 2))

# --- Spesifik Kapı Sınıfları ---
# Her sınıf BaseGate'ten miras alır ve sadece kendi adını, giriş sayısını ve rengini belirtir.

class AndGate(BaseGate):
    def __init__(self):
        super().__init__("AND", 2, "#4A90E2")

class OrGate(BaseGate):
    def __init__(self):
        super().__init__("OR", 2, "#50E3C2")

class NotGate(BaseGate):
    def __init__(self):
        super().__init__("NOT", 1, "#F5A623")

class NandGate(BaseGate):
    def __init__(self):
        super().__init__("NAND", 2, "#9013FE")

class NorGate(BaseGate):
    def __init__(self):
        super().__init__("NOR", 2, "#BD10E0")

class XorGate(BaseGate):
    def __init__(self):
        super().__init__("XOR", 2, "#7ED321")