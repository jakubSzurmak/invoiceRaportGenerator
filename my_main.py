from PyQt5 import QtWidgets as Qtw
from PyQt5 import QtCore as Qtc
from PyQt5 import QtGui as Qtg


class Main(Qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kreator Zestawień Fakturowych")
        self.resize(516, 470)
        self.setFont(Qtg.QFont("Arial", 10))
        self.tab1info, self.tab2info, self.tab3info = [], [], []
        self.layout = Qtw.QVBoxLayout()
        self.setLayout(self.layout)
        self.tabmenu()
        self.stillbuttons()

    def tabmenu(self):
        self.tabs = Qtw.QTabWidget()
        self.addtab1()
        self.addtab2()
        self.addtab3()
        self.addtab4()
        self.layout.addWidget(self.tabs)

    def insidetab1(self):
        self.label12 = Qtw.QLabel("Podmiot: ")
        self.label22 = Qtw.QLabel("Nr Faktury: ")
        self.label32 = Qtw.QLabel("Kwota: zł ")

        self.textedit1 = Qtw.QLineEdit()
        self.textedit2 = Qtw.QLineEdit()
        self.textedit3 = Qtw.QLineEdit()

    def addtab1(self):
        self.tab1 = Qtw.QWidget()
        self.tab1.layout = Qtw.QGridLayout(self.tab1)
        self.tabs.addTab(self.tab1, "Opłacono")
        self.insidetab1()

        self.tab1.layout.addWidget(self.label12)
        self.tab1.layout.addWidget(self.textedit1)
        self.tab1.layout.addWidget(self.label22)
        self.tab1.layout.addWidget(self.textedit2)
        self.tab1.layout.addWidget(self.label32)
        self.tab1.layout.addWidget(self.textedit3)
        self.tab1.setLayout(self.tab1.layout)

    def insidetab2(self):
        self.label4 = Qtw.QLabel("Nr Faktury: ")
        self.label5 = Qtw.QLabel("Podmiot: ")
        self.label6 = Qtw.QLabel("Kwota: zł ")

        self.textedit4 = Qtw.QLineEdit()
        self.textedit5 = Qtw.QLineEdit()
        self.textedit6 = Qtw.QLineEdit()

    def addtab2(self):
        self.tab2 = Qtw.QWidget()
        self.tab2.layout = Qtw.QGridLayout(self.tab2)
        self.tabs.addTab(self.tab2, "Wystawiono")
        self.insidetab2()

        self.tab2.layout.addWidget(self.label4)
        self.tab2.layout.addWidget(self.textedit4)
        self.tab2.layout.addWidget(self.label5)
        self.tab2.layout.addWidget(self.textedit5)
        self.tab2.layout.addWidget(self.label6)
        self.tab2.layout.addWidget(self.textedit6)
        self.tab2.setLayout(self.tab2.layout)

    def insidetab3(self):
        self.label7 = Qtw.QLabel("Imię i Nazwisko Pracownika: ")
        self.label8 = Qtw.QLabel("Liczba określająca wysokość etatu: ")
        self.label9 = Qtw.QLabel("Wynagrodzenie w Zł: ")

        self.textedit7 = Qtw.QLineEdit()
        self.textedit8 = Qtw.QLineEdit()
        self.textedit9 = Qtw.QLineEdit()

    def addtab3(self):
        self.tab3 = Qtw.QWidget()
        self.tab3.layout = Qtw.QGridLayout(self.tab3)
        self.tabs.addTab(self.tab3, "Wynagrodzenia")
        self.insidetab3()

        self.tab3.layout.addWidget(self.label7)
        self.tab3.layout.addWidget(self.textedit7)
        self.tab3.layout.addWidget(self.label8)
        self.tab3.layout.addWidget(self.textedit8)
        self.tab3.layout.addWidget(self.label9)
        self.tab3.layout.addWidget(self.textedit9)
        self.tab3.setLayout(self.tab3.layout)

    def addbuttaction(self):
        self.addtab1info()
        self.addtab2info()
        self.addtab3info()
        self.clearlines()

    def addtab4(self):
        self.tab4 = Qtw.QWidget()
        self.tab4.layout = Qtw.QGridLayout(self.tab4)
        self.tabs.addTab(self.tab4, "Podsumowanie")
        self.insidetab4()

        self.tab4.layout.addWidget(self.scrollArea)
        self.tab4.setLayout(self.tab4.layout)

    def insidetab4(self):
        self.scrollArea = Qtw.QScrollArea(parent=self.tab4)
        self.scrollAreaWidgetContents = Qtw.QWidget(parent=self.scrollArea)
        self.scrollAreaWidgetContents.layout = Qtw.QVBoxLayout(self.scrollAreaWidgetContents)

        self.paidlabel = Qtw.QLabel("Opłacono", parent=self.scrollAreaWidgetContents)
        self.paidlabel.setAlignment(Qtc.Qt.AlignCenter)
        self.paidlabel.setStyleSheet('border: 1px solid black;')
        self.scrollAreaWidgetContents.layout.addWidget(self.paidlabel)
        self.paidlines = Qtw.QListWidget(parent=self.paidlabel)
        self.scrollAreaWidgetContents.layout.addWidget(self.paidlines)

        self.issuedlabel = Qtw.QLabel("Wystawiono", parent=self.scrollAreaWidgetContents)
        self.issuedlabel.setAlignment(Qtc.Qt.AlignCenter)
        self.issuedlabel.setStyleSheet('border: 1px solid black;')
        self.scrollAreaWidgetContents.layout.addWidget(self.issuedlabel)
        self.issuedlines = Qtw.QListWidget(parent=self.issuedlabel)
        self.scrollAreaWidgetContents.layout.addWidget(self.issuedlines)

        self.cashsumlabel = Qtw.QLabel("Wynagrodzenia", parent=self.scrollAreaWidgetContents)
        self.cashsumlabel.setAlignment(Qtc.Qt.AlignCenter)
        self.cashsumlabel.setStyleSheet('border: 1px solid black;')
        self.scrollAreaWidgetContents.layout.addWidget(self.cashsumlabel)
        self.cashsumlines = Qtw.QListWidget(parent=self.cashsumlabel)
        self.cashsumlines.setStyleSheet('text-align: justify; ')
        self.scrollAreaWidgetContents.layout.addWidget(self.cashsumlines)

        self.scrollArea.setLayoutDirection(Qtc.Qt.LeftToRight)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setFrameShape(Qtw.QFrame.StyledPanel)
        self.scrollArea.setFrameShadow(Qtw.QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(Qtc.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(Qtw.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

    def addtab1info(self):
        subject = self.textedit1.text()
        theirnumber = self.textedit2.text()
        theirsum = self.textedit3.text()
        if len(subject) > 2 and len(theirsum) > 1 and len(theirnumber) > 3:
            curr_line = f'- {subject}\t{theirnumber}\t{theirsum}'
            self.tab1info.append(curr_line)
            self.paidlines.addItem(curr_line)
            self.clearlines()
        else:
            pass

    def addtab2info(self):
        mynumber = self.textedit4.text()
        myname = self.textedit5.text()
        mysum = self.textedit6.text()
        if len(mynumber) > 3:
            curr_line = f'- {mynumber}\t{myname}\t{mysum}'
            self.tab2info.append(curr_line)
            self.issuedlines.addItem(curr_line)
            self.clearlines()
        else:
            pass

    def addtab3info(self):
        workersinfo = self.textedit7.text()
        timenum = self.textedit8.text()
        pay = self.textedit9.text()
        if len(workersinfo) > 2:
            curr_line = f'- {workersinfo}\t{timenum}\t{pay}'
            self.tab3info.append(curr_line)
            self.cashsumlines.addItem(curr_line)
            self.clearlines()
        else:
            pass

    def finbuttaction(self):
        from create_docx import load_data

        if len(self.tab1info) > 0 and len(self.tab2info) > 0:
            load_data(self.tab1info, self.tab2info, self.tab3info)
            sys.exit()

    def endbuttaction(self):
        self.msgbox = Qtw.QMessageBox()
        self.msgbox.setWindowTitle("Kreator Zestawień Fakturowych")
        self.msgbox.setText("Czy na pewno chcesz zakończyć pracę z Kreatorem ?")
        self.msgbox.setIcon(Qtw.QMessageBox.Question)
        self.msgbox.setStandardButtons(Qtw.QMessageBox.Yes | Qtw.QMessageBox.No)
        self.msgbox.setDefaultButton(Qtw.QMessageBox.No)
        self.msgbox.buttonClicked.connect(self.msgboxbutts)
        self.msgbox.exec_()

    def deletebuttaction(self):
        clicked_paid = self.paidlines.currentRow()
        clicked_issued = self.issuedlines.currentRow()
        clicked_cashsum = self.cashsumlines.currentRow()

        if clicked_paid >= 0:
            self.tab1info.remove(self.paidlines.item(clicked_paid).text())
            self.paidlines.takeItem(clicked_paid)
            self.clicked_paid = None

        if clicked_issued >= 0:
            self.tab2info.remove(self.issuedlines.item(clicked_issued).text())
            self.issuedlines.takeItem(clicked_issued)
            self.clicked_issued = None

        if clicked_cashsum >= 0:
            self.tab3info.remove(self.cashsumlines.item(clicked_cashsum).text())
            self.cashsumlines.takeItem(clicked_cashsum)
            self.clicked_cashsum = None

    def clearlines(self):
        self.textedit1.clear()
        self.textedit2.clear()
        self.textedit3.clear()
        self.textedit4.clear()
        self.textedit5.clear()
        self.textedit6.clear()
        self.textedit7.clear()
        self.textedit8.clear()
        self.textedit9.clear()

    def msgboxbutts(self, i):
        signal = list(i.text())
        if signal[1] == 'Y':
            sys.exit()

    def stillbuttons(self):
        self.addbutt = Qtw.QPushButton('Dodaj')
        self.finbutt = Qtw.QPushButton('Finalizuj pracę')
        self.endbutt = Qtw.QPushButton('Wyłącz')
        self.deletebutt = Qtw.QPushButton('Usuń z Listy')

        self.addbutt.clicked.connect(self.addbuttaction)
        self.finbutt.clicked.connect(self.finbuttaction)
        self.endbutt.clicked.connect(self.endbuttaction)
        self.deletebutt.clicked.connect(self.deletebuttaction)

        self.layout.addWidget(self.addbutt)
        self.layout.addWidget(self.finbutt)
        self.layout.addWidget(self.endbutt)
        self.layout.addWidget(self.deletebutt)


if __name__ == '__main__':
    import sys

    app = Qtw.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
