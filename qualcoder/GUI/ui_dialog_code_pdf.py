# Form implementation generated from reading ui file 'ui_dialog_code_pdf.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_code_pdf(object):
    def setupUi(self, Dialog_code_pdf):
        Dialog_code_pdf.setObjectName("Dialog_code_pdf")
        Dialog_code_pdf.resize(1054, 699)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog_code_pdf)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(parent=Dialog_code_pdf)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 80))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_coder = QtWidgets.QLabel(parent=self.groupBox)
        self.label_coder.setGeometry(QtCore.QRect(10, 0, 191, 28))
        self.label_coder.setObjectName("label_coder")
        self.lineEdit_search = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_search.setGeometry(QtCore.QRect(40, 38, 171, 30))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.checkBox_search_case = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox_search_case.setGeometry(QtCore.QRect(230, 38, 21, 36))
        self.checkBox_search_case.setText("")
        self.checkBox_search_case.setObjectName("checkBox_search_case")
        self.checkBox_search_all_files = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox_search_all_files.setGeometry(QtCore.QRect(290, 38, 21, 36))
        self.checkBox_search_all_files.setText("")
        self.checkBox_search_all_files.setObjectName("checkBox_search_all_files")
        self.label_search_totals = QtWidgets.QLabel(parent=self.groupBox)
        self.label_search_totals.setGeometry(QtCore.QRect(430, 44, 81, 22))
        self.label_search_totals.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_search_totals.setObjectName("label_search_totals")
        self.label_codes_count = QtWidgets.QLabel(parent=self.groupBox)
        self.label_codes_count.setGeometry(QtCore.QRect(570, 46, 41, 22))
        self.label_codes_count.setText("")
        self.label_codes_count.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_codes_count.setObjectName("label_codes_count")
        self.pushButton_previous = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_previous.setGeometry(QtCore.QRect(360, 38, 28, 28))
        self.pushButton_previous.setText("")
        self.pushButton_previous.setObjectName("pushButton_previous")
        self.pushButton_next = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_next.setGeometry(QtCore.QRect(390, 38, 28, 28))
        self.pushButton_next.setText("")
        self.pushButton_next.setObjectName("pushButton_next")
        self.label_search_all_files = QtWidgets.QLabel(parent=self.groupBox)
        self.label_search_all_files.setGeometry(QtCore.QRect(316, 41, 24, 24))
        self.label_search_all_files.setAutoFillBackground(False)
        self.label_search_all_files.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_search_all_files.setText("")
        self.label_search_all_files.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_search_all_files.setWordWrap(True)
        self.label_search_all_files.setObjectName("label_search_all_files")
        self.label_search_case_sensitive = QtWidgets.QLabel(parent=self.groupBox)
        self.label_search_case_sensitive.setGeometry(QtCore.QRect(250, 41, 24, 24))
        self.label_search_case_sensitive.setAutoFillBackground(False)
        self.label_search_case_sensitive.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_search_case_sensitive.setText("")
        self.label_search_case_sensitive.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_search_case_sensitive.setWordWrap(True)
        self.label_search_case_sensitive.setObjectName("label_search_case_sensitive")
        self.spinBox_font_adjuster = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox_font_adjuster.setGeometry(QtCore.QRect(320, 0, 53, 30))
        self.spinBox_font_adjuster.setMinimum(-10)
        self.spinBox_font_adjuster.setMaximum(0)
        self.spinBox_font_adjuster.setProperty("value", -2)
        self.spinBox_font_adjuster.setObjectName("spinBox_font_adjuster")
        self.label_search_regex = QtWidgets.QLabel(parent=self.groupBox)
        self.label_search_regex.setGeometry(QtCore.QRect(10, 41, 24, 24))
        self.label_search_regex.setAutoFillBackground(False)
        self.label_search_regex.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_search_regex.setText("")
        self.label_search_regex.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_search_regex.setWordWrap(True)
        self.label_search_regex.setObjectName("label_search_regex")
        self.pushButton_help = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_help.setGeometry(QtCore.QRect(700, 40, 28, 28))
        self.pushButton_help.setText("")
        self.pushButton_help.setObjectName("pushButton_help")
        self.label_exports = QtWidgets.QLabel(parent=self.groupBox)
        self.label_exports.setGeometry(QtCore.QRect(532, 43, 24, 24))
        self.label_exports.setText("")
        self.label_exports.setObjectName("label_exports")
        self.comboBox_export = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox_export.setGeometry(QtCore.QRect(562, 40, 91, 30))
        self.comboBox_export.setObjectName("comboBox_export")
        self.comboBox_export.addItem("")
        self.comboBox_export.setItemText(0, "")
        self.comboBox_export.addItem("")
        self.comboBox_export.addItem("")
        self.spinBox = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(230, 0, 51, 30))
        self.spinBox.setObjectName("spinBox")
        self.checkBox_curve = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox_curve.setGeometry(QtCore.QRect(610, 6, 81, 26))
        self.checkBox_curve.setChecked(True)
        self.checkBox_curve.setObjectName("checkBox_curve")
        self.checkBox_line = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox_line.setGeometry(QtCore.QRect(700, 6, 61, 26))
        self.checkBox_line.setChecked(True)
        self.checkBox_line.setObjectName("checkBox_line")
        self.checkBox_image = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox_image.setGeometry(QtCore.QRect(450, 6, 80, 26))
        self.checkBox_image.setChecked(True)
        self.checkBox_image.setObjectName("checkBox_image")
        self.checkBox_black_text = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox_black_text.setGeometry(QtCore.QRect(770, 6, 111, 26))
        self.checkBox_black_text.setObjectName("checkBox_black_text")
        self.checkBox_text = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox_text.setGeometry(QtCore.QRect(380, 6, 61, 26))
        self.checkBox_text.setChecked(True)
        self.checkBox_text.setObjectName("checkBox_text")
        self.checkBox_rect = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox_rect.setGeometry(QtCore.QRect(540, 6, 61, 26))
        self.checkBox_rect.setChecked(True)
        self.checkBox_rect.setObjectName("checkBox_rect")
        self.label_font_size = QtWidgets.QLabel(parent=self.groupBox)
        self.label_font_size.setGeometry(QtCore.QRect(292, 3, 24, 24))
        self.label_font_size.setAutoFillBackground(False)
        self.label_font_size.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_font_size.setText("")
        self.label_font_size.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_font_size.setWordWrap(True)
        self.label_font_size.setObjectName("label_font_size")
        self.label_pages = QtWidgets.QLabel(parent=self.groupBox)
        self.label_pages.setGeometry(QtCore.QRect(200, 3, 24, 24))
        self.label_pages.setAutoFillBackground(False)
        self.label_pages.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_pages.setText("")
        self.label_pages.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_pages.setWordWrap(True)
        self.label_pages.setObjectName("label_pages")
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(parent=Dialog_code_pdf)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.leftsplitter = QtWidgets.QSplitter(parent=self.splitter)
        self.leftsplitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.leftsplitter.setObjectName("leftsplitter")
        self.listWidget = QtWidgets.QListWidget(parent=self.leftsplitter)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 20))
        self.listWidget.setObjectName("listWidget")
        self.groupBox_file_buttons = QtWidgets.QGroupBox(parent=self.leftsplitter)
        self.groupBox_file_buttons.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_file_buttons.setMaximumSize(QtCore.QSize(16777215, 30))
        self.groupBox_file_buttons.setTitle("")
        self.groupBox_file_buttons.setObjectName("groupBox_file_buttons")
        self.pushButton_latest = QtWidgets.QPushButton(parent=self.groupBox_file_buttons)
        self.pushButton_latest.setGeometry(QtCore.QRect(40, 0, 28, 28))
        self.pushButton_latest.setText("")
        self.pushButton_latest.setObjectName("pushButton_latest")
        self.pushButton_bookmark_go = QtWidgets.QPushButton(parent=self.groupBox_file_buttons)
        self.pushButton_bookmark_go.setGeometry(QtCore.QRect(80, 0, 28, 28))
        self.pushButton_bookmark_go.setText("")
        self.pushButton_bookmark_go.setObjectName("pushButton_bookmark_go")
        self.pushButton_next_file = QtWidgets.QPushButton(parent=self.groupBox_file_buttons)
        self.pushButton_next_file.setGeometry(QtCore.QRect(0, 0, 28, 28))
        self.pushButton_next_file.setText("")
        self.pushButton_next_file.setObjectName("pushButton_next_file")
        self.pushButton_document_memo = QtWidgets.QPushButton(parent=self.groupBox_file_buttons)
        self.pushButton_document_memo.setGeometry(QtCore.QRect(120, 0, 28, 28))
        self.pushButton_document_memo.setText("")
        self.pushButton_document_memo.setObjectName("pushButton_document_memo")
        self.pushButton_file_attributes = QtWidgets.QPushButton(parent=self.groupBox_file_buttons)
        self.pushButton_file_attributes.setGeometry(QtCore.QRect(160, 0, 28, 28))
        self.pushButton_file_attributes.setText("")
        self.pushButton_file_attributes.setObjectName("pushButton_file_attributes")
        self.treeWidget = QtWidgets.QTreeWidget(parent=self.leftsplitter)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.groupBox_coding_buttons = QtWidgets.QGroupBox(parent=self.leftsplitter)
        self.groupBox_coding_buttons.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_coding_buttons.setMaximumSize(QtCore.QSize(16777215, 30))
        self.groupBox_coding_buttons.setTitle("")
        self.groupBox_coding_buttons.setObjectName("groupBox_coding_buttons")
        self.pushButton_show_all_codings = QtWidgets.QPushButton(parent=self.groupBox_coding_buttons)
        self.pushButton_show_all_codings.setGeometry(QtCore.QRect(90, 0, 28, 28))
        self.pushButton_show_all_codings.setText("")
        self.pushButton_show_all_codings.setObjectName("pushButton_show_all_codings")
        self.pushButton_show_codings_prev = QtWidgets.QPushButton(parent=self.groupBox_coding_buttons)
        self.pushButton_show_codings_prev.setGeometry(QtCore.QRect(10, 0, 28, 28))
        self.pushButton_show_codings_prev.setText("")
        self.pushButton_show_codings_prev.setObjectName("pushButton_show_codings_prev")
        self.pushButton_show_codings_next = QtWidgets.QPushButton(parent=self.groupBox_coding_buttons)
        self.pushButton_show_codings_next.setGeometry(QtCore.QRect(50, 0, 28, 28))
        self.pushButton_show_codings_next.setText("")
        self.pushButton_show_codings_next.setObjectName("pushButton_show_codings_next")
        self.pushButton_important = QtWidgets.QPushButton(parent=self.groupBox_coding_buttons)
        self.pushButton_important.setGeometry(QtCore.QRect(130, 0, 28, 28))
        self.pushButton_important.setText("")
        self.pushButton_important.setObjectName("pushButton_important")
        self.label_code = QtWidgets.QLabel(parent=self.groupBox_coding_buttons)
        self.label_code.setGeometry(QtCore.QRect(180, 0, 28, 28))
        self.label_code.setText("")
        self.label_code.setWordWrap(True)
        self.label_code.setObjectName("label_code")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.splitter)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 348, 588))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.scrollAreaWidgetContents)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_3.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox_info = QtWidgets.QGroupBox(parent=self.splitter)
        self.groupBox_info.setTitle("")
        self.groupBox_info.setObjectName("groupBox_info")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_info)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.groupBox_info)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_text = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButton_text.setGeometry(QtCore.QRect(0, 0, 61, 20))
        self.radioButton_text.setToolTipDuration(-1)
        self.radioButton_text.setChecked(True)
        self.radioButton_text.setObjectName("radioButton_text")
        self.radioButton_objects = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButton_objects.setGeometry(QtCore.QRect(80, 0, 81, 20))
        self.radioButton_objects.setObjectName("radioButton_objects")
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(parent=self.groupBox_info)
        self.splitter_2.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.textEdit = QtWidgets.QTextEdit(parent=self.splitter_2)
        self.textEdit.setTabChangesFocus(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.splitter_2, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.splitter, 1, 0, 1, 1)

        self.retranslateUi(Dialog_code_pdf)
        QtCore.QMetaObject.connectSlotsByName(Dialog_code_pdf)
        Dialog_code_pdf.setTabOrder(self.spinBox_font_adjuster, self.pushButton_help)
        Dialog_code_pdf.setTabOrder(self.pushButton_help, self.lineEdit_search)
        Dialog_code_pdf.setTabOrder(self.lineEdit_search, self.checkBox_search_case)
        Dialog_code_pdf.setTabOrder(self.checkBox_search_case, self.checkBox_search_all_files)
        Dialog_code_pdf.setTabOrder(self.checkBox_search_all_files, self.pushButton_previous)
        Dialog_code_pdf.setTabOrder(self.pushButton_previous, self.pushButton_next)
        Dialog_code_pdf.setTabOrder(self.pushButton_next, self.comboBox_export)
        Dialog_code_pdf.setTabOrder(self.comboBox_export, self.listWidget)
        Dialog_code_pdf.setTabOrder(self.listWidget, self.pushButton_next_file)
        Dialog_code_pdf.setTabOrder(self.pushButton_next_file, self.pushButton_latest)
        Dialog_code_pdf.setTabOrder(self.pushButton_latest, self.pushButton_bookmark_go)
        Dialog_code_pdf.setTabOrder(self.pushButton_bookmark_go, self.pushButton_document_memo)
        Dialog_code_pdf.setTabOrder(self.pushButton_document_memo, self.pushButton_file_attributes)
        Dialog_code_pdf.setTabOrder(self.pushButton_file_attributes, self.treeWidget)
        Dialog_code_pdf.setTabOrder(self.treeWidget, self.pushButton_show_codings_prev)
        Dialog_code_pdf.setTabOrder(self.pushButton_show_codings_prev, self.pushButton_show_codings_next)
        Dialog_code_pdf.setTabOrder(self.pushButton_show_codings_next, self.pushButton_show_all_codings)
        Dialog_code_pdf.setTabOrder(self.pushButton_show_all_codings, self.pushButton_important)
        Dialog_code_pdf.setTabOrder(self.pushButton_important, self.scrollArea)
        Dialog_code_pdf.setTabOrder(self.scrollArea, self.textEdit)

    def retranslateUi(self, Dialog_code_pdf):
        _translate = QtCore.QCoreApplication.translate
        Dialog_code_pdf.setWindowTitle(_translate("Dialog_code_pdf", "Code Text"))
        self.label_coder.setText(_translate("Dialog_code_pdf", "Coder:"))
        self.lineEdit_search.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>Search for text.</p><p>check <span style=\" font-weight:600;\">Case sensitive</span> for case sensitive search</p><p>check <span style=\" font-weight:600;\">All files</span> for searching all files search</p>\n"
"<p>Right-click to change automatic searching options</p></body></html>"))
        self.checkBox_search_case.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>search case sensitive</p></body></html>"))
        self.checkBox_search_all_files.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>search all files</p></body></html>"))
        self.label_search_totals.setText(_translate("Dialog_code_pdf", "0 / 0"))
        self.pushButton_previous.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>Previous</p></body></html>"))
        self.pushButton_next.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>Next</p></body></html>"))
        self.label_search_all_files.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>Search text. All text files.</p></body></html>"))
        self.label_search_case_sensitive.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>Search text. Case sensitive</p></body></html>"))
        self.spinBox_font_adjuster.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>Adjust text font size in pdf.</p><p>Reduces text overlaps.</p></body></html>"))
        self.label_search_regex.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>Search uses Regex functions. </p><p>A dot ‘.’ is used as a wild card, e.g. ‘.ears’ will match ‘bears’ and ‘years’. </p><p>A ‘?’ after a character will match one or none times that character, e.g. ‘bears?’ will match ‘bear’ and ‘bears’ </p><p><span style=\" background-color:transparent;\">A ‘*’ after a character will match zero or more times. </span></p><p><span style=\" background-color:transparent;\">‘</span>\\. will match the dot symbol, ‘\\?’ will match the question mark. ‘\\n’ will match the line ending symbol. </p><p>Regex cheatsheet: www.rexegg.com/regex-quickstart.html</p></body></html>"))
        self.pushButton_help.setToolTip(_translate("Dialog_code_pdf", "Help"))
        self.label_exports.setToolTip(_translate("Dialog_code_pdf", "Export"))
        self.comboBox_export.setToolTip(_translate("Dialog_code_pdf", "Export"))
        self.comboBox_export.setItemText(1, _translate("Dialog_code_pdf", "html"))
        self.comboBox_export.setItemText(2, _translate("Dialog_code_pdf", "odt"))
        self.spinBox.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>Page</p></body></html>"))
        self.checkBox_curve.setText(_translate("Dialog_code_pdf", "Curves"))
        self.checkBox_line.setText(_translate("Dialog_code_pdf", "Lines"))
        self.checkBox_image.setText(_translate("Dialog_code_pdf", "Images"))
        self.checkBox_black_text.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>Useful if font colours are harder to see</p></body></html>"))
        self.checkBox_black_text.setText(_translate("Dialog_code_pdf", "Black Text"))
        self.checkBox_text.setText(_translate("Dialog_code_pdf", "Text"))
        self.checkBox_rect.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>Rectangle objects</p></body></html>"))
        self.checkBox_rect.setText(_translate("Dialog_code_pdf", "Rects"))
        self.label_font_size.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>Pdf font size adjustment</p></body></html>"))
        self.label_pages.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>Pages</p></body></html>"))
        self.pushButton_latest.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>File with latest coding</p></body></html>"))
        self.pushButton_bookmark_go.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>Go to bookmark</p></body></html>"))
        self.pushButton_next_file.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>Next file</p></body></html>"))
        self.pushButton_document_memo.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>File memo</p></body></html>"))
        self.pushButton_file_attributes.setToolTip(_translate("Dialog_code_pdf", "Show files with file attributes"))
        self.pushButton_show_all_codings.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>Show all codings</p></body></html>"))
        self.pushButton_show_codings_prev.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>Show previous coding of selected code</p></body></html>"))
        self.pushButton_show_codings_next.setToolTip(_translate("Dialog_code_pdf", "<html><head/><body><p>Show next coding of selected code.</p></body></html>"))
        self.pushButton_important.setToolTip(_translate("Dialog_code_pdf", "Show codings flagged important"))
        self.label_code.setToolTip(_translate("Dialog_code_pdf", "Right click below to create new codes and categories"))
        self.radioButton_text.setText(_translate("Dialog_code_pdf", "Text"))
        self.radioButton_objects.setText(_translate("Dialog_code_pdf", "Objects"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_code_pdf = QtWidgets.QDialog()
    ui = Ui_Dialog_code_pdf()
    ui.setupUi(Dialog_code_pdf)
    Dialog_code_pdf.show()
    sys.exit(app.exec())
