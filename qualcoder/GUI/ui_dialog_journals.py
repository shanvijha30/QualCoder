# Form implementation generated from reading ui file 'ui_dialog_journals.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_journals(object):
    def setupUi(self, Dialog_journals):
        Dialog_journals.setObjectName("Dialog_journals")
        Dialog_journals.resize(900, 680)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_journals)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(parent=Dialog_journals)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 70))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 70))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_create = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_create.setGeometry(QtCore.QRect(10, 8, 28, 28))
        self.pushButton_create.setText("")
        self.pushButton_create.setObjectName("pushButton_create")
        self.pushButton_export = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_export.setGeometry(QtCore.QRect(40, 8, 28, 28))
        self.pushButton_export.setText("")
        self.pushButton_export.setObjectName("pushButton_export")
        self.pushButton_delete = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_delete.setGeometry(QtCore.QRect(650, 8, 28, 28))
        self.pushButton_delete.setText("")
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.label_jname = QtWidgets.QLabel(parent=self.groupBox)
        self.label_jname.setGeometry(QtCore.QRect(210, 47, 491, 24))
        self.label_jname.setObjectName("label_jname")
        self.label_jcount = QtWidgets.QLabel(parent=self.groupBox)
        self.label_jcount.setGeometry(QtCore.QRect(13, 47, 181, 24))
        self.label_jcount.setObjectName("label_jcount")
        self.pushButton_export_all = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_export_all.setGeometry(QtCore.QRect(70, 8, 28, 28))
        self.pushButton_export_all.setText("")
        self.pushButton_export_all.setObjectName("pushButton_export_all")
        self.label_search_regex = QtWidgets.QLabel(parent=self.groupBox)
        self.label_search_regex.setGeometry(QtCore.QRect(190, 12, 24, 24))
        self.label_search_regex.setAutoFillBackground(False)
        self.label_search_regex.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_search_regex.setLineWidth(0)
        self.label_search_regex.setText("")
        self.label_search_regex.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_search_regex.setWordWrap(True)
        self.label_search_regex.setObjectName("label_search_regex")
        self.pushButton_next = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_next.setGeometry(QtCore.QRect(520, 8, 28, 28))
        self.pushButton_next.setText("")
        self.pushButton_next.setObjectName("pushButton_next")
        self.label_search_totals = QtWidgets.QLabel(parent=self.groupBox)
        self.label_search_totals.setGeometry(QtCore.QRect(560, 9, 81, 24))
        self.label_search_totals.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_search_totals.setObjectName("label_search_totals")
        self.lineEdit_search = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_search.setGeometry(QtCore.QRect(220, 8, 191, 30))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.checkBox_search_all_journals = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox_search_all_journals.setGeometry(QtCore.QRect(420, 8, 21, 36))
        self.checkBox_search_all_journals.setText("")
        self.checkBox_search_all_journals.setObjectName("checkBox_search_all_journals")
        self.pushButton_previous = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_previous.setGeometry(QtCore.QRect(480, 8, 28, 28))
        self.pushButton_previous.setText("")
        self.pushButton_previous.setObjectName("pushButton_previous")
        self.label_search_all_journals = QtWidgets.QLabel(parent=self.groupBox)
        self.label_search_all_journals.setGeometry(QtCore.QRect(440, 12, 24, 24))
        self.label_search_all_journals.setAutoFillBackground(False)
        self.label_search_all_journals.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_search_all_journals.setLineWidth(0)
        self.label_search_all_journals.setText("")
        self.label_search_all_journals.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_search_all_journals.setWordWrap(True)
        self.label_search_all_journals.setObjectName("label_search_all_journals")
        self.pushButton_help = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_help.setGeometry(QtCore.QRect(700, 8, 28, 28))
        self.pushButton_help.setText("")
        self.pushButton_help.setObjectName("pushButton_help")
        self.pushButton_add_attribute = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_add_attribute.setGeometry(QtCore.QRect(100, 8, 28, 28))
        self.pushButton_add_attribute.setText("")
        self.pushButton_add_attribute.setObjectName("pushButton_add_attribute")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(parent=Dialog_journals)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.splitter)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.textEdit = QtWidgets.QTextEdit(parent=self.splitter)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)

        self.retranslateUi(Dialog_journals)
        QtCore.QMetaObject.connectSlotsByName(Dialog_journals)
        Dialog_journals.setTabOrder(self.pushButton_create, self.pushButton_export)
        Dialog_journals.setTabOrder(self.pushButton_export, self.pushButton_export_all)
        Dialog_journals.setTabOrder(self.pushButton_export_all, self.pushButton_delete)
        Dialog_journals.setTabOrder(self.pushButton_delete, self.lineEdit_search)
        Dialog_journals.setTabOrder(self.lineEdit_search, self.pushButton_previous)
        Dialog_journals.setTabOrder(self.pushButton_previous, self.pushButton_next)
        Dialog_journals.setTabOrder(self.pushButton_next, self.tableWidget)
        Dialog_journals.setTabOrder(self.tableWidget, self.textEdit)
        Dialog_journals.setTabOrder(self.textEdit, self.checkBox_search_all_journals)
        Dialog_journals.setTabOrder(self.checkBox_search_all_journals, self.pushButton_help)

    def retranslateUi(self, Dialog_journals):
        _translate = QtCore.QCoreApplication.translate
        Dialog_journals.setWindowTitle(_translate("Dialog_journals", "Journals"))
        self.pushButton_create.setToolTip(_translate("Dialog_journals", "<html><head/><body><p>Create</p></body></html>"))
        self.pushButton_export.setToolTip(_translate("Dialog_journals", "<html><head/><body><p>Export</p></body></html>"))
        self.pushButton_delete.setToolTip(_translate("Dialog_journals", "<html><head/><body><p>Delete</p></body></html>"))
        self.label_jname.setText(_translate("Dialog_journals", "Journal:"))
        self.label_jcount.setText(_translate("Dialog_journals", "Journals: "))
        self.pushButton_export_all.setToolTip(_translate("Dialog_journals", "<html><head/><body><p>Export all journals as single text file.</p></body></html>"))
        self.label_search_regex.setToolTip(_translate("Dialog_journals", "<html><head/><body><p>Search uses Regex functions. </p><p>A dot ‘.’ is used as a wild card, e.g. ‘.ears’ will match ‘bears’ and ‘years’. </p><p>A ‘?’ after a character will match one or none times that character, e.g. ‘bears?’ will match ‘bear’ and ‘bears’ </p><p><span style=\" background-color:transparent;\">A ‘*’ after a character will match zero or more times. </span></p><p><span style=\" background-color:transparent;\">‘</span>\\. will match the dot symbol, ‘\\?’ will match the question mark. ‘\\n’ will match the line ending symbol. </p><p>Regex cheatsheet: <a href=\"http://www.rexegg.com/regex-quickstart.html\"><span style=\" text-decoration: underline; color:#000080;\">www.rexegg.com/regex-quickstart.html</span></a></p></body></html>"))
        self.pushButton_next.setToolTip(_translate("Dialog_journals", "<html><head/><body><p>Next</p></body></html>"))
        self.label_search_totals.setText(_translate("Dialog_journals", "0 / 0"))
        self.lineEdit_search.setToolTip(_translate("Dialog_journals", "<html><head/><body><p>Search for text.</p><p>check <span style=\" font-weight:600;\">All journals</span> for searching all journals</p></body></html>"))
        self.checkBox_search_all_journals.setToolTip(_translate("Dialog_journals", "<html><head/><body><p>search all journals</p></body></html>"))
        self.pushButton_previous.setToolTip(_translate("Dialog_journals", "<html><head/><body><p>Previous</p></body></html>"))
        self.label_search_all_journals.setToolTip(_translate("Dialog_journals", "<html><head/><body><p>Search all journals</p></body></html>"))
        self.pushButton_help.setToolTip(_translate("Dialog_journals", "Help"))
        self.pushButton_add_attribute.setToolTip(_translate("Dialog_journals", "<html><head/><body><p>Add Attribute</p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog_journals", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog_journals", "Modified"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog_journals", "Coder"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog_journals", "jid"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_journals = QtWidgets.QDialog()
    ui = Ui_Dialog_journals()
    ui.setupUi(Dialog_journals)
    Dialog_journals.show()
    sys.exit(app.exec())
