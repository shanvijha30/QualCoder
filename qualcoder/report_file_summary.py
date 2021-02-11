# -*- coding: utf-8 -*-

"""
Copyright (c) 2021 Colin Curtain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Author: Colin Curtain (ccbogel)
https://github.com/ccbogel/QualCoder
"""

import datetime
import os
from PIL import Image
from PIL.ExifTags import TAGS
import platform
import sys
import logging
import traceback

from PyQt5 import QtCore, QtGui, QtWidgets

from GUI.ui_dialog_report_file_summary import Ui_Dialog_file_summary


path = os.path.abspath(os.path.dirname(__file__))
logger = logging.getLogger(__name__)


def exception_handler(exception_type, value, tb_obj):
    """ Global exception handler useful in GUIs.
    tb_obj: exception.__traceback__ """
    tb = '\n'.join(traceback.format_tb(tb_obj))
    text = 'Traceback (most recent call last):\n' + tb + '\n' + exception_type.__name__ + ': ' + str(value)
    print(text)
    logger.error(_("Uncaught exception:") + "\n" + text)
    QtWidgets.QMessageBox.critical(None, _('Uncaught Exception'), text)


class DialogReportFileSummary(QtWidgets.QDialog):
    """ Provide a summary report for selected file.
    """

    app = None
    parent_tetEdit = None
    files = []

    def __init__(self, app, parent_textEdit):
        sys.excepthook = exception_handler
        self.app = app
        self.parent_textEdit = parent_textEdit
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_Dialog_file_summary()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        font = 'font: ' + str(self.app.settings['fontsize']) + 'pt '
        font += '"' + self.app.settings['font'] + '";'
        self.setStyleSheet(font)
        docfont = 'font: ' + str(self.app.settings['docfontsize']) + 'pt '
        docfont += '"' + self.app.settings['font'] + '";'
        self.ui.textEdit.setStyleSheet(docfont)
        treefont = 'font: ' + str(self.app.settings['treefontsize']) + 'pt '
        treefont += '"' + self.app.settings['font'] + '";'
        try:
            s0 = int(self.app.settings['dialogreport_file_summary_splitter0'])
            s1 = int(self.app.settings['dialogreport_file_summary_splitter1'])
            self.ui.splitter.setSizes([s0, s1])
        except:
            pass
        self.ui.splitter.splitterMoved.connect(self.splitter_sizes)
        self.ui.listWidget.setStyleSheet(treefont)
        self.ui.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.get_files()
        self.ui.listWidget.itemClicked.connect(self.fill_text_edit)

    def splitter_sizes(self, pos, index):
        """ Detect size changes in splitter and store in app.settings variable. """

        sizes = self.ui.splitter.sizes()
        self.app.settings['dialogreport_file_summary_splitter0'] = sizes[0]
        self.app.settings['dialogreport_file_summary_splitter1'] = sizes[1]

    def get_files(self):
        """ Get source files with additional details and fill list widget.
        """

        self.ui.listWidget.clear()
        self.files = self.app.get_filenames()
        # Fill additional details about each file in the memo
        cur = self.app.conn.cursor()
        sql = "select length(fulltext), mediapath from source where id=?"
        sql_text_codings = "select count(cid) from code_text where fid=?"
        sql_av_codings = "select count(cid) from code_av where id=?"
        sql_image_codings = "select count(cid) from code_image where id=?"
        for f in self.files:
            cur.execute(sql, [f['id'], ])
            res = cur.fetchone()
            if res is None:  # safety catch
                res = [0]
            tt = ""
            if res[1] is None or res[1][0:5] == "docs:":
                tt += _("Text file\n")
                tt += _("Characters: ") + str(res[0])
            if res[1] is not None and (res[1][0:7] == "images:" or res[1][0:7] == "/images"):
                tt += _("Image")
            if res[1] is not None and (res[1][0:6] == "audio:" or res[1][0:6] == "/audio"):
                tt += _("Audio")
            if res[1] is not None and (res[1][0:6] == "video:" or res[1][0:6] == "/video"):
                tt += _("Video")
            cur.execute(sql_text_codings, [f['id']])
            txt_res = cur.fetchone()
            cur.execute(sql_av_codings, [f['id']])
            av_res = cur.fetchone()
            cur.execute(sql_image_codings, [f['id']])
            img_res = cur.fetchone()
            tt += _("\nCodings: ")
            if txt_res[0] > 0:
                tt += str(txt_res[0])
            if av_res[0] > 0:
                tt += str(av_res[0])
            if img_res[0] > 0:
                tt += str(img_res[0])
            item = QtWidgets.QListWidgetItem(f['name'])
            if f['memo'] is not None and f['memo'] != "":
                tt += _("\nMemo: ") + f['memo']
            item.setToolTip(tt)
            self.ui.listWidget.addItem(item)

    def fill_text_edit(self):
        """ Get data about file and fill text edit. """

        file_ = ""
        file_name = self.ui.listWidget.currentItem().text()
        for f in self.files:
            if f['name'] == file_name:
                file_ = f
                break
        if file_ == "":
            return
        cur = self.app.conn.cursor()
        text = file_name + "\n\n"
        text += _("Memo: ") + file_['memo'] + "\n\n"
        cur.execute("select date, owner, fulltext, mediapath from source where id=?", [file_['id']])
        res = cur.fetchone()
        text += "ID: " + str(file_['id']) + "  " + _("Date: ") + res[0] + "  " + _("Owner: ") + res[1] + "\n"
        media_path = ""
        file_type = ""
        if res[3] is None or res[3] == "":
            media_path = _("Internal text document")
            file_type = "text"
        elif res[3][0:5] == "docs:":
            media_path = _("External text document: ") + res[3][5:]
            file_type = "text"
        elif res[3][0:6] == "audio:":
            media_path = _("External audio file: ") + res[3][6:]
            file_type = "audio"
        elif res[3][0:7] == "/audio/":
            media_path = _("Internal audio file")
            file_type = "audio"
        elif res[3][0:6] == "video:":
            media_path = _("External video file: ") + res[3][6:]
            file_type = "video"
        elif res[3][0:7] == "/video/":
            media_path = _("Internal video file")
            file_type = "video"
        elif res[3][0:7] == "images:":
            media_path = _("External image file: ") + res[3][7:]
            file_type = "image"
        elif res[3][0:8] == "/images/":
            media_path = _("Internal image file")
            file_type = "image"
        text += _("Media path: ") + media_path + "\n"

        if file_type == "text":
            text += self.text_statistics(file_)
        if file_type == "image":
            text += self.image_statistics(file_)
        # TODO summary of audio / video

        self.ui.textEdit.setText(text)

    def video_statistics(self, file_):
        """ Get video statistics for image file
        param: file_ Dictionary of {name, id, memo} """

        cur = self.app.conn.cursor()
        cur.execute("select mediapath from source where id=?", [file_['id']])
        mediapath = cur.fetchone()[0]
        abs_path = ""
        if 'video:' == mediapath[0:6]:
            abs_path = mediapath[6:]
        else:
            abs_path = self.app.project_path + mediapath

    def audio_statistics(self, file_):
        """ Get audio statistics for image file
        param: file_ Dictionary of {name, id, memo} """

        cur = self.app.conn.cursor()
        cur.execute("select mediapath from source where id=?", [file_['id']])
        mediapath = cur.fetchone()[0]
        abs_path = ""
        if 'audio:' == mediapath[0:6]:
            abs_path = mediapath[6:]
        else:
            abs_path = self.app.project_path + mediapath

    def image_statistics(self, file_):
        """ Get image statistics for image file
        param: file_ Dictionary of {name, id, memo} """

        cur = self.app.conn.cursor()
        cur.execute("select mediapath from source where id=?", [file_['id']])
        mediapath = cur.fetchone()[0]
        abs_path = ""
        '''if 'audio:' == mediapath[0:6]:
            abs_path = mediapath[6:]
        elif 'video:' == mediapath[0:6]:
            abs_path = mediapath[6:]'''
        if 'images:' == mediapath[0:7]:
            abs_path = mediapath[7:]
        else:
            abs_path = self.app.project_path + mediapath

        # Image size and metadata
        image = Image.open(abs_path)
        w, h = image.size
        text = _("Width: ") + f"{w:,d}"  + "  " + _("Height: ") + f"{h:,d}" + "  " + _("Area: ") + f"{w * h:,d}" + _(" pixels") + "\n"
        image_type = abs_path[-3:].lower()
        # From: www.thepythoncode.com/article/extracting-image-metadata-in-python
        text += _("Image metadata: ") + "\n"
        if image_type in ("jpg", "peg"):
            exifdata = image.getexif()
            # iterating over the EXIF data fields
            for tag_id in exifdata:
                # get the tag name, instead of human unreadable tag id
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id)
                # Decode bytes
                if isinstance(data, bytes):
                    try:
                        data = data.decode()
                        text += f"{tag:25}: {data}" + "\n"
                    except UnicodeDecodeError as e:
                        text += str(e) + "\n"
        # From: www.vice.com/en/article/aekn58/hack-this-extra-image-metadata-using-python
        if image_type == "png":
            for tag, value in image.info.items():
                key = TAGS.get(tag, tag)
                text += key + " " + str(value) + "\n"

        # Codes
        sql = "select code_name.name, code_image.cid, count(code_image.cid), round(avg(width)), round(avg(height)) "
        sql += " from code_image join code_name "
        sql += "on code_name.cid=code_image.cid where id=? "
        sql += "group by code_name.name, code_image.cid order by count(code_image.cid) desc"
        cur.execute(sql, [file_['id']])
        res = cur.fetchall()
        text += "\n\n" + _("Code counts:") + "\n"
        #TODO more image statistics

        for r in res:
            area = int(r[3] * r[4])
            text += r[0]+ "  " + _("Count: ") + str(r[2]) + "   " + _("Average area: ") + f"{area:,d}" + _(" pixels") + "\n"

        return text


    def text_statistics(self, file_):
        """ Get details of text file statistics
        param: file_ Dictionary of {name, id, memo}
        """

        text = ""
        cur = self.app.conn.cursor()
        cur.execute("select fulltext from source where id=?", [file_['id']])
        fulltext = cur.fetchone()[0]
        text += _("Characters: ") + f"{len(fulltext):,d}" + "\n"
        # Remove punctuation. Convert to lower case
        chars = ""
        for c in range(0, len(fulltext)):
            if fulltext[c].isalpha() or fulltext[c] =="'":
                chars += fulltext[c]
            else:
                chars += " "
        chars = chars.lower()
        word_list = chars.split()
        #print(word_list)
        msg = _("Word calculations: Words use alphabet characters and include the apostrophe. All other characters are word separators")
        text += "\n" + msg + "\n"
        #TODO use word list for word proximity

        text += "\n" + _("Words: ") + f"{len(word_list):,d}" + "\n"
        # Word frequency
        d = {}
        for word in word_list:
            d[word] = d.get(word, 0) + 1  # get(key, value if not present)
        # https://codeburst.io/python-basics-11-word-count-filter-out-punctuation-dictionary-manipulation-and-sorting-lists-3f6c55420855
        word_freq = []
        for key, value in d.items():
            word_freq.append((value, key))
        word_freq.sort(reverse=True)
        #print(word_freq)
        text += _("Unique words: ") + str(len(word_freq)) + "\n"
        # Top 100 or maximum of less than 100
        max_count = len(word_freq)
        if max_count > 100:
            max_count = 100
        text += _("Top 100 words") + "\n"
        for i in range(0, max_count):
            text += word_freq[i][1] + "   " + str(word_freq[i][0]) + " | "

        # Codes
        sql = "select code_name.name, code_text.cid, count(code_text.cid), sum(length(code_text.seltext)), "
        sql += "round(avg(length(code_text.seltext))) from code_text join code_name "
        sql += "on code_name.cid=code_text.cid where fid=? "
        sql += "group by code_name.name, code_text.cid order by count(code_text.cid) desc"
        cur.execute(sql, [file_['id']])
        res = cur.fetchall()
        text += "\n\n" + _("Code counts:") + "\n"
        for r in res:
            text += r[0]+ "  " + _("Count: ") + str(r[2]) + "  " + _("Total characters: ") + f"{r[3]:,d}"
            text += "  " + _("Average characters: ") + str(int(r[4])) + "\n"
            #print(r)

        return text


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = DialogReportFileSummary()
    ui.show()
    sys.exit(app.exec_())

