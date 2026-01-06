# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogOp.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(480, 640)
        palette = QPalette()
        brush = QBrush(QColor(6, 50, 25, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        Dialog.setPalette(palette)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 0, 131, 51))
        font = QFont()
        font.setFamilies([u"Poor Richard"])
        font.setPointSize(26)
        self.label.setFont(font)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(-1, 59, 481, 161))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.DontWrapRows)
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Poor Richard"])
        font1.setPointSize(18)
        self.label_2.setFont(font1)
        self.label_2.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.TitelForVVindovvs1 = QLineEdit(self.formLayoutWidget)
        self.TitelForVVindovvs1.setObjectName(u"TitelForVVindovvs1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitelForVVindovvs1.sizePolicy().hasHeightForWidth())
        self.TitelForVVindovvs1.setSizePolicy(sizePolicy)
        self.TitelForVVindovvs1.setMinimumSize(QSize(150, 40))

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.TitelForVVindovvs1)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.ItemsForConboboxVvindovs1 = QPlainTextEdit(self.formLayoutWidget)
        self.ItemsForConboboxVvindovs1.setObjectName(u"ItemsForConboboxVvindovs1")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.ItemsForConboboxVvindovs1)

        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 210, 481, 61))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(100, 0, 100, 0)
        self.AcceptButtonVVindovvs1 = QPushButton(self.verticalLayoutWidget)
        self.AcceptButtonVVindovvs1.setObjectName(u"AcceptButtonVVindovvs1")
        palette1 = QPalette()
        brush1 = QBrush(QColor(121, 81, 0, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        self.AcceptButtonVVindovvs1.setPalette(palette1)

        self.verticalLayout.addWidget(self.AcceptButtonVVindovvs1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 280, 141, 51))
        self.label_4.setFont(font)
        self.formLayoutWidget_2 = QWidget(Dialog)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(120, 340, 263, 51))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(50)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.TitelForVvindovvs_2 = QLineEdit(self.formLayoutWidget_2)
        self.TitelForVvindovvs_2.setObjectName(u"TitelForVvindovvs_2")
        sizePolicy.setHeightForWidth(self.TitelForVvindovvs_2.sizePolicy().hasHeightForWidth())
        self.TitelForVvindovvs_2.setSizePolicy(sizePolicy)
        self.TitelForVvindovvs_2.setMinimumSize(QSize(150, 40))

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.TitelForVvindovvs_2)

        self.formLayoutWidget_3 = QWidget(Dialog)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(120, 520, 263, 51))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(50)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.formLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.TitttelForVvindovvs_3 = QLineEdit(self.formLayoutWidget_3)
        self.TitttelForVvindovvs_3.setObjectName(u"TitttelForVvindovvs_3")
        sizePolicy.setHeightForWidth(self.TitttelForVvindovvs_3.sizePolicy().hasHeightForWidth())
        self.TitttelForVvindovvs_3.setSizePolicy(sizePolicy)
        self.TitttelForVvindovvs_3.setMinimumSize(QSize(150, 40))

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.TitttelForVvindovvs_3)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(170, 460, 141, 51))
        self.label_7.setFont(font)
        self.verticalLayoutWidget_2 = QWidget(Dialog)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(-1, 390, 481, 51))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(100, 0, 100, 0)
        self.AcceptButtonVVindovvs_2 = QPushButton(self.verticalLayoutWidget_2)
        self.AcceptButtonVVindovvs_2.setObjectName(u"AcceptButtonVVindovvs_2")
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        self.AcceptButtonVVindovvs_2.setPalette(palette2)

        self.verticalLayout_2.addWidget(self.AcceptButtonVVindovvs_2)

        self.verticalLayoutWidget_3 = QWidget(Dialog)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 590, 481, 51))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(100, 0, 100, 0)
        self.AcceptButtonVVindovvs_3 = QPushButton(self.verticalLayoutWidget_3)
        self.AcceptButtonVVindovvs_3.setObjectName(u"AcceptButtonVVindovvs_3")
        palette3 = QPalette()
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        self.AcceptButtonVVindovvs_3.setPalette(palette3)

        self.verticalLayout_3.addWidget(self.AcceptButtonVVindovvs_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"P\u0259nc\u0259r\u0259 1", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Ba\u015fl\u0131q", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"B\u00f6lm\u0259l\u0259r", None))
        self.ItemsForConboboxVvindovs1.setPlainText(QCoreApplication.translate("Dialog", u"bu hiss\u0259d\u0259ki yaz\u0131n\u0131 tamamil\u0259 sildikd\u0259n sonra, H\u0259r s\u0259tir\u0259 \u0259lav\u0259 etm\u0259k ist\u0259diyiniz 1 b\u00f6lm\u0259nin ad\u0131n\u0131 yaz\u0131n. \n"
"n\u00fcmun\u0259 :\n"
"\n"
"Dan\u0131\u015f\u0131q\n"
"Dinl\u0259m\u0259\n"
"Oxuma\n"
"Yazma", None))
        self.AcceptButtonVVindovvs1.setText(QCoreApplication.translate("Dialog", u"T\u0259sdiq et", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"P\u0259nc\u0259r\u0259 2", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Ba\u015fl\u0131q", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Ba\u015fl\u0131q", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"P\u0259nc\u0259r\u0259 3", None))
        self.AcceptButtonVVindovvs_2.setText(QCoreApplication.translate("Dialog", u"T\u0259sdiq et", None))
        self.AcceptButtonVVindovvs_3.setText(QCoreApplication.translate("Dialog", u"T\u0259sdiq et", None))
    # retranslateUi

