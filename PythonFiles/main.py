from PythonFiles.stacked import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QMainWindow

pagesDict = {
        'Home': 0,
        'new_rm_entry': 1,
        'new_shade_entry': 2,
        'rm_add': 3,
        'rm_delete': 4,
        'rm_modify': 5,
        'rm_operations': 6,
        'rm_stock_view': 7,
        'rm_view': 8,
        'rm_view_custom': 9,
        'rm_view_by_id': 10,
        'rm_view_by_today': 11,
        'shade_add': 12,
        'shade_delete': 13,
        'shade_modify': 14,
        'shade_operations': 15,
        'shade_view': 16,
        'shade_view_by_custom': 17,
        'shade_view_by_id': 18,
        'shade_view_by_today': 19,

    }

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.uiWindow = Ui_MainWindow()
        self.startUIWindow()



    def startUIWindow(self):
        self.uiWindow.setupUi(self)
        self.uiWindow.EP.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_operations']))
        self.uiWindow.RM.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_operations']))
        self.uiWindow.RM_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_rm_entry']))
        self.uiWindow.RM_3.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['new_shade_entry']))
        self.uiWindow.back_add_rm.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_add_rm_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_add_rm_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_operations']))
        self.uiWindow.back_add_rm_3.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_operations']))
        self.uiWindow.pushButton_3.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_view_rm.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_operations']))
        self.uiWindow.back_add_rm_4.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_operations']))
        self.uiWindow.pushButton_4.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_add_rm_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_view_rm_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_operations']))
        self.uiWindow.pushButton_5.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.rm_add_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_add']))
        self.uiWindow.rm_modify_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_modify']))
        self.uiWindow.rm_delete_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_delete']))
        self.uiWindow.rm_view.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_view']))
        self.uiWindow.pushButton_6.clicked.connect(lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_view_rm_3.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_view']))
        self.uiWindow.op_back.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_operations']))
        self.uiWindow.view_trans.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_view_by_id']))
        self.uiWindow.view_today.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_view_by_today']))
        self.uiWindow.view_custom.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_view_custom']))
        self.uiWindow.back_view_rm_4.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_view']))
        self.uiWindow.pushButton_7.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_view_rm_5.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_view']))
        self.uiWindow.pushButton_8.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_add_rm_5.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_view']))
        self.uiWindow.pushButton_9.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_view_rm_6.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['rm_view']))
        self.uiWindow.pushButton_10.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        #self.uiWindow.back_view_rm_4.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_operations']))
        self.uiWindow.back_view_rm_7.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_operations']))
        self.uiWindow.pushButton_11.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_12.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_view_rm_8.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_operations']))
        self.uiWindow.back_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.shade_add_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_add']))
        self.uiWindow.shade_modify_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_modify']))
        self.uiWindow.shade_delete_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_delete']))
        self.uiWindow.shade_view.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_view']))
        self.uiWindow.op_back_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_operations']))
        self.uiWindow.view_trans_2.clicked.connect(lambda: self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_view_by_id']))
        self.uiWindow.view_today_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_view_by_today']))
        self.uiWindow.view_custom_2.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_view_by_custom']))
        self.uiWindow.pushButton_13.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_view_rm_9.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_view']))
        self.uiWindow.back_add_rm_5.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_view']))
        self.uiWindow.pushButton_14.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.pushButton_15.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home']))
        self.uiWindow.back_view_rm_10.clicked.connect(lambda : self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['shade_view']))


        self.uiWindow.stackedWidget.setCurrentIndex(pagesDict['Home'])
        self.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())






# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
