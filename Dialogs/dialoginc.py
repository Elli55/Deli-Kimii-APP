# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogInc.ui'
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

class Ui_DialogGlr(object):
    def setupUi(self, DialogGlr):
        if not DialogGlr.objectName():
            DialogGlr.setObjectName(u"DialogGlr")
        DialogGlr.resize(479, 640)
        palette = QPalette()
        brush = QBrush(QColor(6, 50, 25, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        DialogGlr.setPalette(palette)
        self.verticalLayoutWidget = QWidget(DialogGlr)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 470, 500, 121))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(150, 0, 150, 0)
        self.DialogIncSilButton = QPushButton(self.verticalLayoutWidget)
        self.DialogIncSilButton.setObjectName(u"DialogIncSilButton")
        self.DialogIncSilButton.setMinimumSize(QSize(200, 40))
        palette1 = QPalette()
        brush1 = QBrush(QColor(121, 81, 0, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        self.DialogIncSilButton.setPalette(palette1)
        font = QFont()
        font.setFamilies([u"Poor Richard"])
        font.setPointSize(20)
        self.DialogIncSilButton.setFont(font)

        self.verticalLayout.addWidget(self.DialogIncSilButton)

        self.DialogIncCloseButton = QPushButton(self.verticalLayoutWidget)
        self.DialogIncCloseButton.setObjectName(u"DialogIncCloseButton")
        self.DialogIncCloseButton.setMinimumSize(QSize(0, 30))
        palette2 = QPalette()
        brush2 = QBrush(QColor(104, 27, 17, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush2)
        self.DialogIncCloseButton.setPalette(palette2)

        self.verticalLayout.addWidget(self.DialogIncCloseButton)

        self.GlrList = QListWidget(DialogGlr)
        self.GlrList.setObjectName(u"GlrList")
        self.GlrList.setGeometry(QRect(10, 10, 461, 451))
        self.GlrList.setFrameShape(QFrame.Shape.WinPanel)
        self.GlrList.setFrameShadow(QFrame.Shadow.Raised)
        self.GlrList.setLineWidth(3)
        self.GlrList.setMidLineWidth(1)
        self.GlrList.setTabKeyNavigation(True)
        self.GlrList.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.GlrList.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.GlrList.setViewMode(QListView.ViewMode.ListMode)
        self.GlrList.setWordWrap(True)
        self.GlrList.setSortingEnabled(True)
        self.GlrList.setSupportedDragActions(Qt.DropAction.IgnoreAction)

        self.retranslateUi(DialogGlr)

        QMetaObject.connectSlotsByName(DialogGlr)
    # setupUi

    def retranslateUi(self, DialogGlr):
        DialogGlr.setWindowTitle(QCoreApplication.translate("DialogGlr", u"Dialog", None))
        self.DialogIncSilButton.setText(QCoreApplication.translate("DialogGlr", u"Sil", None))
        self.DialogIncCloseButton.setText(QCoreApplication.translate("DialogGlr", u"L\u0259\u011fv et", None))
    # retranslateUi

