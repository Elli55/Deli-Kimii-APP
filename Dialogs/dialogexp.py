# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogExp.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QListView, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_DialogXercSil(object):
    def setupUi(self, DialogXercSil):
        if not DialogXercSil.objectName():
            DialogXercSil.setObjectName(u"DialogXercSil")
        DialogXercSil.resize(480, 640)
        palette = QPalette()
        brush = QBrush(QColor(6, 50, 25, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        DialogXercSil.setPalette(palette)
        self.verticalLayoutWidget = QWidget(DialogXercSil)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-10, 470, 500, 131))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(150, 0, 150, 0)
        self.SilButtonDialogExp = QPushButton(self.verticalLayoutWidget)
        self.SilButtonDialogExp.setObjectName(u"SilButtonDialogExp")
        self.SilButtonDialogExp.setMinimumSize(QSize(200, 40))
        palette1 = QPalette()
        brush1 = QBrush(QColor(121, 81, 0, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        self.SilButtonDialogExp.setPalette(palette1)
        font = QFont()
        font.setFamilies([u"Poor Richard"])
        font.setPointSize(20)
        self.SilButtonDialogExp.setFont(font)

        self.verticalLayout.addWidget(self.SilButtonDialogExp)

        self.BaglaButtonDialogExp = QPushButton(self.verticalLayoutWidget)
        self.BaglaButtonDialogExp.setObjectName(u"BaglaButtonDialogExp")
        self.BaglaButtonDialogExp.setMinimumSize(QSize(0, 30))
        palette2 = QPalette()
        brush2 = QBrush(QColor(104, 27, 17, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush2)
        self.BaglaButtonDialogExp.setPalette(palette2)

        self.verticalLayout.addWidget(self.BaglaButtonDialogExp)

        self.XrcList = QListWidget(DialogXercSil)
        self.XrcList.setObjectName(u"XrcList")
        self.XrcList.setGeometry(QRect(10, 10, 461, 451))
        self.XrcList.setFrameShape(QFrame.Shape.WinPanel)
        self.XrcList.setFrameShadow(QFrame.Shadow.Raised)
        self.XrcList.setLineWidth(3)
        self.XrcList.setMidLineWidth(1)
        self.XrcList.setTabKeyNavigation(True)
        self.XrcList.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.XrcList.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.XrcList.setViewMode(QListView.ViewMode.ListMode)
        self.XrcList.setWordWrap(True)
        self.XrcList.setSortingEnabled(True)
        self.XrcList.setSupportedDragActions(Qt.DropAction.IgnoreAction)

        self.retranslateUi(DialogXercSil)

        QMetaObject.connectSlotsByName(DialogXercSil)
    # setupUi

    def retranslateUi(self, DialogXercSil):
        DialogXercSil.setWindowTitle(QCoreApplication.translate("DialogXercSil", u"Dialog", None))
        self.SilButtonDialogExp.setText(QCoreApplication.translate("DialogXercSil", u"Sil", None))
        self.BaglaButtonDialogExp.setText(QCoreApplication.translate("DialogXercSil", u"L\u0259\u011fv et", None))
    # retranslateUi

