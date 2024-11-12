from MainWindowPTB2.UI.giaodienptb2_nhom import Ui_MainWindow

class MainWindowEX(Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.MainWindow = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def showWindow(self):
        self.MainWindow.show()