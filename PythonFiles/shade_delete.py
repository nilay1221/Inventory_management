# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\shade_delete.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1036, 851)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.shade_delete_remark = QtWidgets.QLineEdit(self.centralwidget)
        self.shade_delete_remark.setGeometry(QtCore.QRect(650, 180, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shade_delete_remark.setFont(font)
        self.shade_delete_remark.setObjectName("shade_delete_remark")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 100, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 20, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.shade_delete_transaction_id = QtWidgets.QLineEdit(self.centralwidget)
        self.shade_delete_transaction_id.setGeometry(QtCore.QRect(210, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shade_delete_transaction_id.setFont(font)
        self.shade_delete_transaction_id.setObjectName("shade_delete_transaction_id")
        self.shade_delete_date = QtWidgets.QLineEdit(self.centralwidget)
        self.shade_delete_date.setGeometry(QtCore.QRect(630, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shade_delete_date.setFont(font)
        self.shade_delete_date.setObjectName("shade_delete_date")
        self.back_view_rm = QtWidgets.QPushButton(self.centralwidget)
        self.back_view_rm.setGeometry(QtCore.QRect(40, 30, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back_view_rm.setFont(font)
        self.back_view_rm.setObjectName("back_view_rm")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(560, 100, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.shade_delete_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.shade_delete_confirm.setGeometry(QtCore.QRect(720, 720, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.shade_delete_confirm.setFont(font)
        self.shade_delete_confirm.setObjectName("shade_delete_confirm")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 170, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.shade_delete_customer = QtWidgets.QComboBox(self.centralwidget)
        self.shade_delete_customer.setGeometry(QtCore.QRect(210, 180, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shade_delete_customer.setFont(font)
        self.shade_delete_customer.setEditable(True)
        self.shade_delete_customer.setObjectName("shade_delete_customer")
        self.shade_delete_customer.addItem("")
        self.shade_delete_customer.setItemText(0, "")
        self.shade_delete_customer.addItem("")
        self.shade_delete_customer.addItem("")
        self.shade_delete_customer.addItem("")
        self.shade_delete_customer.addItem("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(550, 170, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 240, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.shade_add_total = QtWidgets.QLineEdit(self.centralwidget)
        self.shade_add_total.setGeometry(QtCore.QRect(260, 620, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shade_add_total.setFont(font)
        self.shade_add_total.setObjectName("shade_add_total")
        self.shade_addtable = QtWidgets.QTableWidget(self.centralwidget)
        self.shade_addtable.setGeometry(QtCore.QRect(10, 330, 411, 251))
        self.shade_addtable.setRowCount(8)
        self.shade_addtable.setColumnCount(3)
        self.shade_addtable.setObjectName("shade_addtable")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.shade_addtable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.shade_addtable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.shade_addtable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_addtable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_addtable.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_addtable.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_addtable.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_addtable.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_addtable.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_addtable.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_addtable.setItem(7, 1, item)
        self.shade_number_delete = QtWidgets.QLineEdit(self.centralwidget)
        self.shade_number_delete.setGeometry(QtCore.QRect(450, 250, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shade_number_delete.setFont(font)
        self.shade_number_delete.setObjectName("shade_number_delete")
        self.shade_colortable = QtWidgets.QTableWidget(self.centralwidget)
        self.shade_colortable.setGeometry(QtCore.QRect(470, 320, 541, 291))
        self.shade_colortable.setRowCount(8)
        self.shade_colortable.setColumnCount(4)
        self.shade_colortable.setObjectName("shade_colortable")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.shade_colortable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.shade_colortable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.shade_colortable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.shade_colortable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_colortable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_colortable.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_colortable.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_colortable.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_colortable.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_colortable.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_colortable.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.shade_colortable.setItem(7, 1, item)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(110, 610, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Transaction ID : "))
        self.pushButton.setText(_translate("MainWindow", "Back to Main Menu"))
        self.back_view_rm.setText(_translate("MainWindow", "Back"))
        self.label_3.setText(_translate("MainWindow", "Shade Number"))
        self.label_4.setText(_translate("MainWindow", "Date :"))
        self.shade_delete_confirm.setText(_translate("MainWindow", "Delete"))
        self.label_6.setText(_translate("MainWindow", "Customer Name:"))
        self.shade_delete_customer.setItemText(1, _translate("MainWindow", "Rajesh"))
        self.shade_delete_customer.setItemText(2, _translate("MainWindow", "Nishit"))
        self.shade_delete_customer.setItemText(3, _translate("MainWindow", "Nilay"))
        self.shade_delete_customer.setItemText(4, _translate("MainWindow", "Parth"))
        self.label_7.setText(_translate("MainWindow", "Remark :"))
        self.label_8.setText(_translate("MainWindow", "Shade Number :"))
        item = self.shade_addtable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Code"))
        item = self.shade_addtable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.shade_addtable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        __sortingEnabled = self.shade_addtable.isSortingEnabled()
        self.shade_addtable.setSortingEnabled(False)
        self.shade_addtable.setSortingEnabled(__sortingEnabled)
        item = self.shade_colortable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Code"))
        item = self.shade_colortable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.shade_colortable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Percentage"))
        item = self.shade_colortable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity"))
        __sortingEnabled = self.shade_colortable.isSortingEnabled()
        self.shade_colortable.setSortingEnabled(False)
        self.shade_colortable.setSortingEnabled(__sortingEnabled)
        self.label_9.setText(_translate("MainWindow", "Total Quantity :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
