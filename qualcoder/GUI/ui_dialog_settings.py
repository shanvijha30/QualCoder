# Form implementation generated from reading ui file 'ui_dialog_settings.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_settings(object):
    def setupUi(self, Dialog_settings):
        Dialog_settings.setObjectName("Dialog_settings")
        Dialog_settings.resize(721, 619)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_settings.sizePolicy().hasHeightForWidth())
        Dialog_settings.setSizePolicy(sizePolicy)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_settings)
        self.buttonBox.setGeometry(QtCore.QRect(490, 580, 201, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit_coderName = QtWidgets.QLineEdit(Dialog_settings)
        self.lineEdit_coderName.setGeometry(QtCore.QRect(190, 80, 241, 31))
        self.lineEdit_coderName.setObjectName("lineEdit_coderName")
        self.label_new_coder = QtWidgets.QLabel(Dialog_settings)
        self.label_new_coder.setGeometry(QtCore.QRect(10, 84, 171, 21))
        self.label_new_coder.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_new_coder.setObjectName("label_new_coder")
        self.fontComboBox = QtWidgets.QFontComboBox(Dialog_settings)
        self.fontComboBox.setGeometry(QtCore.QRect(30, 220, 229, 38))
        self.fontComboBox.setObjectName("fontComboBox")
        self.spinBox = QtWidgets.QSpinBox(Dialog_settings)
        self.spinBox.setGeometry(QtCore.QRect(270, 220, 71, 38))
        self.spinBox.setMinimum(8)
        self.spinBox.setMaximum(32)
        self.spinBox.setSingleStep(2)
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(Dialog_settings)
        self.label.setGeometry(QtCore.QRect(30, 190, 211, 21))
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(Dialog_settings)
        self.checkBox.setGeometry(QtCore.QRect(460, 150, 151, 22))
        self.checkBox.setObjectName("checkBox")
        self.label_directory = QtWidgets.QLabel(Dialog_settings)
        self.label_directory.setGeometry(QtCore.QRect(10, 560, 691, 21))
        self.label_directory.setObjectName("label_directory")
        self.pushButton_choose_directory = QtWidgets.QPushButton(Dialog_settings)
        self.pushButton_choose_directory.setGeometry(QtCore.QRect(30, 520, 391, 31))
        self.pushButton_choose_directory.setObjectName("pushButton_choose_directory")
        self.label_2 = QtWidgets.QLabel(Dialog_settings)
        self.label_2.setGeometry(QtCore.QRect(15, 47, 161, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.comboBox_coders = QtWidgets.QComboBox(Dialog_settings)
        self.comboBox_coders.setGeometry(QtCore.QRect(190, 40, 241, 32))
        self.comboBox_coders.setObjectName("comboBox_coders")
        self.label_3 = QtWidgets.QLabel(Dialog_settings)
        self.label_3.setGeometry(QtCore.QRect(30, 260, 241, 41))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.spinBox_treefontsize = QtWidgets.QSpinBox(Dialog_settings)
        self.spinBox_treefontsize.setGeometry(QtCore.QRect(270, 260, 71, 38))
        self.spinBox_treefontsize.setMinimum(8)
        self.spinBox_treefontsize.setMaximum(32)
        self.spinBox_treefontsize.setSingleStep(2)
        self.spinBox_treefontsize.setObjectName("spinBox_treefontsize")
        self.label_4 = QtWidgets.QLabel(Dialog_settings)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 151, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.comboBox_language = QtWidgets.QComboBox(Dialog_settings)
        self.comboBox_language.setGeometry(QtCore.QRect(190, 150, 241, 32))
        self.comboBox_language.setObjectName("comboBox_language")
        self.checkBox_auto_backup = QtWidgets.QCheckBox(Dialog_settings)
        self.checkBox_auto_backup.setGeometry(QtCore.QRect(10, 384, 900, 23))
        self.checkBox_auto_backup.setChecked(True)
        self.checkBox_auto_backup.setObjectName("checkBox_auto_backup")
        self.checkBox_backup_AV_files = QtWidgets.QCheckBox(Dialog_settings)
        self.checkBox_backup_AV_files.setGeometry(QtCore.QRect(10, 417, 691, 91))
        self.checkBox_backup_AV_files.setChecked(True)
        self.checkBox_backup_AV_files.setObjectName("checkBox_backup_AV_files")
        self.label_5 = QtWidgets.QLabel(Dialog_settings)
        self.label_5.setGeometry(QtCore.QRect(370, 230, 141, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.comboBox_timestamp = QtWidgets.QComboBox(Dialog_settings)
        self.comboBox_timestamp.setGeometry(QtCore.QRect(530, 223, 151, 28))
        self.comboBox_timestamp.setObjectName("comboBox_timestamp")
        self.label_6 = QtWidgets.QLabel(Dialog_settings)
        self.label_6.setGeometry(QtCore.QRect(360, 277, 151, 21))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.comboBox_speaker = QtWidgets.QComboBox(Dialog_settings)
        self.comboBox_speaker.setGeometry(QtCore.QRect(530, 270, 71, 28))
        self.comboBox_speaker.setObjectName("comboBox_speaker")
        self.label_7 = QtWidgets.QLabel(Dialog_settings)
        self.label_7.setGeometry(QtCore.QRect(30, 300, 241, 41))
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.spinBox_docfontsize = QtWidgets.QSpinBox(Dialog_settings)
        self.spinBox_docfontsize.setGeometry(QtCore.QRect(270, 300, 71, 38))
        self.spinBox_docfontsize.setMinimum(8)
        self.spinBox_docfontsize.setMaximum(32)
        self.spinBox_docfontsize.setSingleStep(2)
        self.spinBox_docfontsize.setObjectName("spinBox_docfontsize")
        self.checkBox_dark_mode = QtWidgets.QCheckBox(Dialog_settings)
        self.checkBox_dark_mode.setGeometry(QtCore.QRect(460, 180, 191, 23))
        self.checkBox_dark_mode.setObjectName("checkBox_dark_mode")
        self.label_current_coder = QtWidgets.QLabel(Dialog_settings)
        self.label_current_coder.setGeometry(QtCore.QRect(10, 10, 651, 21))
        self.label_current_coder.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_current_coder.setObjectName("label_current_coder")
        self.label_backups_to_keep = QtWidgets.QLabel(Dialog_settings)
        self.label_backups_to_keep.setGeometry(QtCore.QRect(470, 347, 151, 61))
        self.label_backups_to_keep.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.label_backups_to_keep.setWordWrap(True)
        self.label_backups_to_keep.setObjectName("label_backups_to_keep")
        self.spinBox_backups = QtWidgets.QSpinBox(Dialog_settings)
        self.spinBox_backups.setGeometry(QtCore.QRect(635, 384, 48, 26))
        self.spinBox_backups.setMinimum(1)
        self.spinBox_backups.setMaximum(10)
        self.spinBox_backups.setProperty("value", 5)
        self.spinBox_backups.setObjectName("spinBox_backups")
        self.pushButton_set_coder = QtWidgets.QPushButton(Dialog_settings)
        self.pushButton_set_coder.setGeometry(QtCore.QRect(440, 80, 89, 31))
        self.pushButton_set_coder.setObjectName("pushButton_set_coder")
        self.line = QtWidgets.QFrame(Dialog_settings)
        self.line.setGeometry(QtCore.QRect(20, 120, 661, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog_settings)
        self.line_2.setGeometry(QtCore.QRect(20, 350, 661, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_8 = QtWidgets.QLabel(Dialog_settings)
        self.label_8.setGeometry(QtCore.QRect(356, 315, 161, 24))
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.comboBox_text_chunk_size = QtWidgets.QComboBox(Dialog_settings)
        self.comboBox_text_chunk_size.setGeometry(QtCore.QRect(530, 314, 101, 28))
        self.comboBox_text_chunk_size.setObjectName("comboBox_text_chunk_size")
        self.comboBox_text_chunk_size.addItem("")
        self.comboBox_text_chunk_size.addItem("")
        self.comboBox_text_chunk_size.addItem("")
        self.comboBox_text_chunk_size.addItem("")

        self.retranslateUi(Dialog_settings)
        self.buttonBox.accepted.connect(Dialog_settings.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog_settings.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog_settings)
        Dialog_settings.setTabOrder(self.lineEdit_coderName, self.comboBox_coders)
        Dialog_settings.setTabOrder(self.comboBox_coders, self.comboBox_language)
        Dialog_settings.setTabOrder(self.comboBox_language, self.fontComboBox)
        Dialog_settings.setTabOrder(self.fontComboBox, self.spinBox)
        Dialog_settings.setTabOrder(self.spinBox, self.spinBox_treefontsize)
        Dialog_settings.setTabOrder(self.spinBox_treefontsize, self.checkBox)
        Dialog_settings.setTabOrder(self.checkBox, self.comboBox_timestamp)
        Dialog_settings.setTabOrder(self.comboBox_timestamp, self.comboBox_speaker)
        Dialog_settings.setTabOrder(self.comboBox_speaker, self.checkBox_auto_backup)
        Dialog_settings.setTabOrder(self.checkBox_auto_backup, self.checkBox_backup_AV_files)
        Dialog_settings.setTabOrder(self.checkBox_backup_AV_files, self.pushButton_choose_directory)

    def retranslateUi(self, Dialog_settings):
        _translate = QtCore.QCoreApplication.translate
        Dialog_settings.setWindowTitle(_translate("Dialog_settings", "Settings"))
        self.label_new_coder.setText(_translate("Dialog_settings", "New coder"))
        self.label.setText(_translate("Dialog_settings", "General font and size"))
        self.checkBox.setToolTip(_translate("Dialog_settings", "<html><head/><body><p>Show the identifying numbers for files, cases, codes, et cetera.</p></body></html>"))
        self.checkBox.setText(_translate("Dialog_settings", "Show IDs"))
        self.label_directory.setText(_translate("Dialog_settings", "/"))
        self.pushButton_choose_directory.setText(_translate("Dialog_settings", "Default project directory"))
        self.label_2.setToolTip(_translate("Dialog_settings", "Select another coder in this project"))
        self.label_2.setText(_translate("Dialog_settings", "Other coders"))
        self.label_3.setText(_translate("Dialog_settings", "Font size for categories and codes tree"))
        self.label_4.setText(_translate("Dialog_settings", "Language"))
        self.comboBox_language.setToolTip(_translate("Dialog_settings", "<html><head/><body><p>Close and open the software for the change in language to occur.</p></body></html>"))
        self.checkBox_auto_backup.setText(_translate("Dialog_settings", "Backup project folder every time project is opened"))
        self.checkBox_backup_AV_files.setText(_translate("Dialog_settings", "Backup video and audio files. Uncheck to speed up backups.\n"
"Not recommended unless you have many large files slowing the backup.\n"
"You must store these files elsewhere."))
        self.label_5.setToolTip(_translate("Dialog_settings", "<html><head/><body><p>Used when entering time position in transcription</p></body></html>"))
        self.label_5.setText(_translate("Dialog_settings", "Time format"))
        self.label_6.setToolTip(_translate("Dialog_settings", "<html><head/><body><p>Used when entering speaker name in transcription</p></body></html>"))
        self.label_6.setText(_translate("Dialog_settings", "Speaker format"))
        self.label_7.setText(_translate("Dialog_settings", "Font size for documents"))
        self.checkBox_dark_mode.setText(_translate("Dialog_settings", "Dark mode"))
        self.label_current_coder.setText(_translate("Dialog_settings", "Current coder: "))
        self.label_backups_to_keep.setText(_translate("Dialog_settings", "Number of auto-backups to keep"))
        self.pushButton_set_coder.setToolTip(_translate("Dialog_settings", "Set this name as the current coder.\n"
""))
        self.pushButton_set_coder.setText(_translate("Dialog_settings", "Apply"))
        self.label_8.setToolTip(_translate("Dialog_settings", "Very large text documents. Load text chunks by number of characters."))
        self.label_8.setText(_translate("Dialog_settings", "Code text chunk size"))
        self.comboBox_text_chunk_size.setItemText(0, _translate("Dialog_settings", "50000"))
        self.comboBox_text_chunk_size.setItemText(1, _translate("Dialog_settings", "40000"))
        self.comboBox_text_chunk_size.setItemText(2, _translate("Dialog_settings", "30000"))
        self.comboBox_text_chunk_size.setItemText(3, _translate("Dialog_settings", "20000"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_settings = QtWidgets.QDialog()
    ui = Ui_Dialog_settings()
    ui.setupUi(Dialog_settings)
    Dialog_settings.show()
    sys.exit(app.exec())
