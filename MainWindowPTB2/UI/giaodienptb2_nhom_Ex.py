from MainWindowPTB2.UI.function import calc_PTB2
from MainWindowPTB2.UI.giaodienptb2_nhom import Ui_MainWindow

class giaodienptb2_nhom_Ex(Ui_MainWindow):


    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalandSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalandSlot(self):
        #self.pushButtonClose.clicked.connect(self)
        self.pushButtonCalc.clicked.connect(self.slot_calc)
        self.pushButtonClose.clicked.connect(self.slot_close)
        self.pushButtonContinue.clicked.connect(self.slot_continue)
    def slot_continue(self):
        self.lineEditA.setText("")
        self.lineEditB.setText("")
        self.lineEditC.setText("")
        self.lineEditKetQua.setText("")
        self.lineEditA.setFocus()

    def slot_close(self):
        self.MainWindow.close()

    def slot_calc(self):
        a = int(self.lineEditA.text())
        b = int(self.lineEditB.text())
        c = int(self.lineEditC.text())
        kq = calc_PTB2(a, b, c)
        self.lineEditKetQua.setText(f"{kq}")