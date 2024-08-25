from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from os import system
from json import dumps, loads

system("cls || clear")

app = QApplication([])

class Edit(QLineEdit):
    def __init__(self, window, x: int, y: int, w: int, h: int):
        super().__init__(window)
        self.setGeometry(x, y, w ,h)
        self.setReadOnly(True)
        self.hide()
        self.setStyleSheet("""
        background-color: #cce6ff;
        border-radius: 8px;
        font-size: 20px;
""")

class Button(QPushButton):
    def __init__(self, window, x, y, w, h, s):
        super().__init__(window)
        self.setGeometry(x, y, w, h)
        self.setText(s)    
        self.hide()
        self.setStyleSheet("""
        font-size: 25px;
        border-radius: 8px;
        background-color: white;
""")
        
fayl = open("Testlar.json", "r", encoding="utf-8")
testlar = loads(fayl.read())
soni = len(testlar)

oyna = QWidget()
oyna.setFixedSize(1000, 800)
oyna.setWindowTitle("Tester")
oyna.setWindowIcon(QIcon("TesterIcon.png"))

mainlabel = QLabel(oyna)
mainlabel.setText("Tester")
mainlabel.move(20, 20)
mainlabel.setStyleSheet("""
    font-size: 35px;
""")

edit1 = QLineEdit(oyna)
edit1.setGeometry(20, 100, 960, 80)
edit1.setReadOnly(True)
edit1.setText("Testlar soni: " + str(soni))
edit1.setStyleSheet("""
        background-color: #b3d9ff;
        border-radius: 8px;
        font-size: 25px;
""")

edit2 = Edit(oyna, 200, 220, 780, 80)
edit3 = Edit(oyna, 200, 320, 780, 80)
edit4 = Edit(oyna, 200, 420, 780, 80)
edit5 = Edit(oyna, 200, 520, 780, 80)

A = Button(oyna, 100, 220, 80, 80, "A")
B = Button(oyna, 100, 320, 80, 80, "B")
C = Button(oyna, 100, 420, 80, 80, "C")
D = Button(oyna, 100, 520, 80, 80, "D")

b1 = QPushButton(oyna)
b1.setGeometry(770, 670, 120, 40)
b1.setText("Start")
b1.setStyleSheet("""
    background-color: #0099cc;
    border-radius: 20px;
    font-size: 20px;
""")

b2 = QPushButton(oyna)
b2.setGeometry(600, 670, 120, 40)
b2.setText("Add")
b2.setStyleSheet("""
    background-color: #0099cc;
    border-radius: 20px;
    font-size: 20px;
""")

ogoxlantirish = QMessageBox(oyna)
ogoxlantirish.setText("Iltimos barcha maydonlarni to'ldiring")
ogoxlantirish.setWindowTitle("Xatolik")
ogoxlantirish.setIcon(QMessageBox.Critical)
ogoxlantirish.setWindowIcon(QIcon("TesterIcon.png"))

#   Global o'zgaruvchilar
javob = ""
togrilar = 0
xatolar = 0
j = 0

def korsatish():    # Variantlarni ko'rsatish
      edit2.show()
      edit3.show()
      edit4.show()
      edit5.show()
      A.show()
      B.show()
      C.show()
      D.show()

def yashirish():    # Variantlarni yashirish
      edit2.hide()
      edit3.hide()
      edit4.hide()
      edit5.hide()
      A.hide()
      B.hide()
      C.hide()
      D.hide()

def boshlangich(self: Button):  # Variantlarni boshlang'ich holatga keltirish
    self.setStyleSheet("""
        font-size: 25px;
        border-radius: 8px;
        background-color: white;
""")

def variant(self: Button):  # Variant tanlash
    global javob
    boshlangich(A)
    boshlangich(B)
    boshlangich(C)
    boshlangich(D)
    self.setStyleSheet("""
    background-color: blue;
    border-radius: 8px;
    font-size: 25px;
    """)
    javob = self.text()
    b1.setEnabled(True)

def testYuklash(i: int):  # Oynaga testni yuklash
    global testlar
    b1.setText("Next")
    b2.setText("Stop")
    korsatish()
    edit1.setText(" Savol " + str(i+1) + ": " + testlar[i]["savol"])
    edit2.setText("  " + testlar[i]["A"])
    edit3.setText("  " + testlar[i]["B"])
    edit4.setText("  " + testlar[i]["C"])
    edit5.setText("  " + testlar[i]["D"])

def tugallash():  # Test ishlashni tugallash
    boshlangich(A)
    boshlangich(B)
    boshlangich(C)
    boshlangich(D)
    global j
    global togrilar
    global xatolar
    yashirish()
    edit1.setText("To'gri javoblar: " + str(togrilar) + " ta\tXato javoblar: " + str(xatolar) + " ta")
    b1.setText("Start")
    b2.setText("Add")
    j = 0
    xatolar = 0
    togrilar = 0

def bosildib1():    # b1 tugma bosilganda
    global javob
    global testlar
    global j
    global togrilar
    global xatolar
    global soni
    boshlangich(A)
    boshlangich(B)
    boshlangich(C)
    boshlangich(D)
    if j < len(testlar):
        if b1.text() == "Start":
            testYuklash(j)
            b1.setEnabled(False)
            j += 1
        elif b1.text() == "Next":
            if javob == testlar[j-1]["javob"]:
                togrilar += 1
            else:
                xatolar += 1
            testYuklash(j)
            b1.setEnabled(False)
            j += 1
    else:
        if javob == testlar[j-1]["javob"]:
            togrilar += 1
        else:
            xatolar += 1
        tugallash()
    if b1.text() == "Add":
        if not edit1.text == "" and not edit2.text == "" and not edit3.text == "" and not edit4.text == "" and not edit5.text == "" and not javob == "":
            testlar.append({
                "savol":edit1.text()[7:],
                "A":edit2.text(),
                "B":edit3.text(),
                "C":edit4.text(),
                "D":edit5.text(),
                "javob": javob
            })
            faylr = open("Testlar.json", "w")
            faylr.write(dumps(testlar, indent=4))
            faylr.close()
            fayl = open("Testlar.json", "r", encoding="utf-8")
            testlar = loads(fayl.read())
            soni = len(testlar)
            testAdd()
        else:
            ogoxlantirish.show()

def testAdd():      # Test qo'shish uchun
    global testlar
    global javob
    korsatish()

    edit1.setText("")
    edit2.setText("")
    edit3.setText("")
    edit4.setText("")
    edit5.setText("")
    javob = ""

    edit1.setReadOnly(False)
    edit2.setReadOnly(False)
    edit3.setReadOnly(False)
    edit4.setReadOnly(False)
    edit5.setReadOnly(False)
    edit1.setText("Savol: ")

def bosildib2():    # b2 tugma bosilganda
    global j
    global testlar
    global soni
    if b2.text() == "Stop":
        b1.setEnabled(True)
        tugallash()
    elif b2.text() == "Add":
        b1.setText("Add")
        b2.setText("Cancel")
        testAdd()
    elif b2.text() == "Cancel":
        b1.setText("Start")
        b2.setText("Add")
        edit1.setText("")
        edit2.setText("")
        edit3.setText("")
        edit4.setText("")
        edit5.setText("")
        edit1.setReadOnly(True)
        edit2.setReadOnly(True)
        edit3.setReadOnly(True)
        edit4.setReadOnly(True)
        edit5.setReadOnly(True)
        yashirish()
        edit1.setText("Testlar soni: " + str(soni))

    
b1.clicked.connect(bosildib1)
b2.clicked.connect(bosildib2)
A.clicked.connect(lambda : variant(A))
B.clicked.connect(lambda : variant(B))
C.clicked.connect(lambda : variant(C))
D.clicked.connect(lambda : variant(D))

oyna.show()
app.exec()