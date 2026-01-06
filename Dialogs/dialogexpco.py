# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DalogExpCo.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(480, 450)
        palette = QPalette()
        brush = QBrush(QColor(6, 50, 25, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        Dialog.setPalette(palette)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 10, 481, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(70, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Poor Richard"])
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setFrameShadow(QFrame.Shadow.Plain)
        self.label.setTextFormat(Qt.TextFormat.RichText)

        self.verticalLayout.addWidget(self.label)

        self.verticalLayoutWidget_2 = QWidget(Dialog)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 120, 481, 211))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CategoryText = QPlainTextEdit(self.verticalLayoutWidget_2)
        self.CategoryText.setObjectName(u"CategoryText")

        self.verticalLayout_2.addWidget(self.CategoryText)

        self.verticalLayoutWidget_3 = QWidget(Dialog)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 380, 481, 80))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(50, 0, 50, 0)
        self.AcceptCategory = QPushButton(self.verticalLayoutWidget_3)
        self.AcceptCategory.setObjectName(u"AcceptCategory")

        self.verticalLayout_3.addWidget(self.AcceptCategory)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"                                          Kateqoriyalar\u0131 T\u0259yin Et", None))
        self.CategoryText.setPlainText(QCoreApplication.translate("Dialog", u"T\u0259yin etm\u0259k ist\u0259diyiniz kateqoriya adlar\u0131n\u0131,burda olan yaz\u0131n\u0131 tam sildikd\u0259n sonra, alt alta s\u0131ralanm\u0131\u015f \u015f\u0259kild\u0259 qeyd edin.\n"
"\n"
"N\u00fcmun\u0259:\n"
"\n"
"Qida\n"
"Alkaqol\n"
"Geyim\n"
"\u00c7\u00f6ld\u0259n Siafri\u015f\n"
"\u018fyl\u0259nc\u0259\n"
"v\u0259 sair\u0259", None))
        self.AcceptCategory.setText(QCoreApplication.translate("Dialog", u"T\u0259sdiq Et", None))
    # retranslateUi

