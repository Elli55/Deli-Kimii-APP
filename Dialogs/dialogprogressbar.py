# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogProgressBar.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFormLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_DialogProgressBar(object):
    def setupUi(self, DialogProgressBar):
        if not DialogProgressBar.objectName():
            DialogProgressBar.setObjectName(u"DialogProgressBar")
        DialogProgressBar.resize(480, 402)
        palette = QPalette()
        brush = QBrush(QColor(6, 50, 25, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        DialogProgressBar.setPalette(palette)
        self.verticalLayoutWidget = QWidget(DialogProgressBar)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 330, 481, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(50, 0, 50, 0)
        self.ProgressBarAcceptButton = QPushButton(self.verticalLayoutWidget)
        self.ProgressBarAcceptButton.setObjectName(u"ProgressBarAcceptButton")

        self.verticalLayout.addWidget(self.ProgressBarAcceptButton)

        self.verticalLayoutWidget_2 = QWidget(DialogProgressBar)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 481, 71))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(150, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(54, 50))
        font = QFont()
        font.setFamilies([u"Segoe Script"])
        font.setPointSize(16)
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.formLayoutWidget_2 = QWidget(DialogProgressBar)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(0, 70, 481, 120))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(60)
        self.formLayout_2.setVerticalSpacing(20)
        self.formLayout_2.setContentsMargins(20, 10, 70, 10)
        self.label_3 = QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.ProgressBarDateForStart = QDateEdit(self.formLayoutWidget_2)
        self.ProgressBarDateForStart.setObjectName(u"ProgressBarDateForStart")
        sizePolicy.setHeightForWidth(self.ProgressBarDateForStart.sizePolicy().hasHeightForWidth())
        self.ProgressBarDateForStart.setSizePolicy(sizePolicy)
        self.ProgressBarDateForStart.setMinimumSize(QSize(150, 35))
        self.ProgressBarDateForStart.setDateTime(QDateTime(QDate(2025, 12, 31), QTime(22, 0, 0)))
        self.ProgressBarDateForStart.setCalendarPopup(True)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.ProgressBarDateForStart)

        self.label_4 = QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.ProgressBarDateForEnd = QDateEdit(self.formLayoutWidget_2)
        self.ProgressBarDateForEnd.setObjectName(u"ProgressBarDateForEnd")
        sizePolicy.setHeightForWidth(self.ProgressBarDateForEnd.sizePolicy().hasHeightForWidth())
        self.ProgressBarDateForEnd.setSizePolicy(sizePolicy)
        self.ProgressBarDateForEnd.setMinimumSize(QSize(150, 35))
        self.ProgressBarDateForEnd.setDateTime(QDateTime(QDate(2025, 12, 31), QTime(22, 0, 0)))
        self.ProgressBarDateForEnd.setCalendarPopup(True)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.ProgressBarDateForEnd)

        self.verticalLayoutWidget_3 = QWidget(DialogProgressBar)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 190, 490, 141))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(120, 0, 120, 0)
        self.label = QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(54, 50))
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label)

        self.TitelInput = QLineEdit(self.verticalLayoutWidget_3)
        self.TitelInput.setObjectName(u"TitelInput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(50)
        sizePolicy1.setHeightForWidth(self.TitelInput.sizePolicy().hasHeightForWidth())
        self.TitelInput.setSizePolicy(sizePolicy1)
        self.TitelInput.setMinimumSize(QSize(250, 50))

        self.verticalLayout_3.addWidget(self.TitelInput)


        self.retranslateUi(DialogProgressBar)

        QMetaObject.connectSlotsByName(DialogProgressBar)
    # setupUi

    def retranslateUi(self, DialogProgressBar):
        DialogProgressBar.setWindowTitle(QCoreApplication.translate("DialogProgressBar", u"Dialog", None))
        self.ProgressBarAcceptButton.setText(QCoreApplication.translate("DialogProgressBar", u"T\u0259sdiq et", None))
        self.label_2.setText(QCoreApplication.translate("DialogProgressBar", u"M\u00fcdd\u0259ti t\u0259yin et", None))
        self.label_3.setText(QCoreApplication.translate("DialogProgressBar", u"Ba\u015flama Tarixi", None))
        self.label_4.setText(QCoreApplication.translate("DialogProgressBar", u"Bitm\u0259 tarixi", None))
        self.label.setText(QCoreApplication.translate("DialogProgressBar", u"  M\u00fcdd\u0259ti Adland\u0131r", None))
    # retranslateUi

