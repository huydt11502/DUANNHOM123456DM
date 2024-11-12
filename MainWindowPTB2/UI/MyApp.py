from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindowPTB2.UI.giaodienptb2_nhom_Ex import giaodienptb2_nhom_Ex

app=QApplication([])
window=QMainWindow()
myUI=giaodienptb2_nhom_Ex()
myUI.setupUi(window)
myUI.showWindow()
app.exec()