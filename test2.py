# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trsConnector.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(479, 364)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pb_r = QPushButton(Form)
        self.pb_r.setObjectName(u"pb_r")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.pb_r.sizePolicy().hasHeightForWidth())
        self.pb_r.setSizePolicy(sizePolicy)
        self.pb_r.setMouseTracking(False)

        self.verticalLayout.addWidget(self.pb_r)

        self.pb_s = QPushButton(Form)
        self.pb_s.setObjectName(u"pb_s")
        sizePolicy.setHeightForWidth(self.pb_s.sizePolicy().hasHeightForWidth())
        self.pb_s.setSizePolicy(sizePolicy)
        self.pb_s.setMouseTracking(False)

        self.verticalLayout.addWidget(self.pb_s)

        self.pb_t = QPushButton(Form)
        self.pb_t.setObjectName(u"pb_t")
        sizePolicy.setHeightForWidth(self.pb_t.sizePolicy().hasHeightForWidth())
        self.pb_t.setSizePolicy(sizePolicy)
        self.pb_t.setMouseTracking(False)

        self.verticalLayout.addWidget(self.pb_t)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"TRS Connector", None))
        self.pb_r.setText(QCoreApplication.translate("Form", u"Translate", None))
        self.pb_s.setText(QCoreApplication.translate("Form", u"Rotate", None))
        self.pb_t.setText(QCoreApplication.translate("Form", u"Scale", None))
    # retranslateUi

