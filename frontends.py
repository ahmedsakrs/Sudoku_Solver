from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SudokuSolver:
    def setupUi(self, SudokuSolver):
        SudokuSolver.setObjectName("SudokuSolver")
        SudokuSolver.resize(1051, 894)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SudokuSolver.sizePolicy().hasHeightForWidth())
        SudokuSolver.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SudokuSolver.setWindowIcon(icon)
        SudokuSolver.setAutoFillBackground(False)
        SudokuSolver.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "background-color: qlineargradient(spread:pad, x1:0.524, y1:1, x2:0.511936, y2:0, stop:0 rgba(185, 185, 185, 255), stop:0.110505 rgba(200, 200, 200, 255), stop:0.327422 rgba(210, 210, 210, 255), stop:0.534789 rgba(220, 220, 220, 255), stop:0.703956 rgba(230, 230, 230, 255), stop:0.818554 rgba(235, 235, 235, 255), stop:0.92633 rgba(245, 245, 245, 255), stop:1 rgba(255, 255, 255, 255));")
        SudokuSolver.setIconSize(QtCore.QSize(80, 80))
        SudokuSolver.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(SudokuSolver)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridFrame.sizePolicy().hasHeightForWidth())
        self.gridFrame.setSizePolicy(sizePolicy)
        self.gridFrame.setMinimumSize(QtCore.QSize(742, 742))
        self.gridFrame.setMaximumSize(QtCore.QSize(742, 742))
        self.gridFrame.setStyleSheet("border-image:transparent;\n"
                                     "background-color: rgb(0, 0, 0);")
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.line79 = QtWidgets.QLineEdit(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line79.sizePolicy().hasHeightForWidth())
        self.line79.setSizePolicy(sizePolicy)
        self.line79.setMinimumSize(QtCore.QSize(80, 80))
        self.line79.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line79.setFont(font)
        self.line79.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line79.setMaxLength(1)
        self.line79.setAlignment(QtCore.Qt.AlignCenter)
        self.line79.setObjectName("line79")
        self.gridLayout.addWidget(self.line79, 10, 8, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.line64 = QtWidgets.QLineEdit(self.gridFrame)
        self.line64.setMinimumSize(QtCore.QSize(80, 80))
        self.line64.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line64.setFont(font)
        self.line64.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line64.setMaxLength(1)
        self.line64.setAlignment(QtCore.Qt.AlignCenter)
        self.line64.setObjectName("line64")
        self.gridLayout.addWidget(self.line64, 9, 0, 1, 1)
        self.line75 = QtWidgets.QLineEdit(self.gridFrame)
        self.line75.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line75.setFont(font)
        self.line75.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line75.setMaxLength(1)
        self.line75.setAlignment(QtCore.Qt.AlignCenter)
        self.line75.setObjectName("line75")
        self.gridLayout.addWidget(self.line75, 10, 2, 1, 1)
        self.line81 = QtWidgets.QLineEdit(self.gridFrame)
        self.line81.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line81.setFont(font)
        self.line81.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line81.setMaxLength(1)
        self.line81.setAlignment(QtCore.Qt.AlignCenter)
        self.line81.setObjectName("line81")
        self.gridLayout.addWidget(self.line81, 10, 10, 1, 1)
        self.line61 = QtWidgets.QLineEdit(self.gridFrame)
        self.line61.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line61.setFont(font)
        self.line61.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line61.setMaxLength(1)
        self.line61.setAlignment(QtCore.Qt.AlignCenter)
        self.line61.setObjectName("line61")
        self.gridLayout.addWidget(self.line61, 8, 8, 1, 1)
        self.line63 = QtWidgets.QLineEdit(self.gridFrame)
        self.line63.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line63.setFont(font)
        self.line63.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line63.setMaxLength(1)
        self.line63.setAlignment(QtCore.Qt.AlignCenter)
        self.line63.setObjectName("line63")
        self.gridLayout.addWidget(self.line63, 8, 10, 1, 1)
        self.line74 = QtWidgets.QLineEdit(self.gridFrame)
        self.line74.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line74.setFont(font)
        self.line74.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line74.setMaxLength(1)
        self.line74.setAlignment(QtCore.Qt.AlignCenter)
        self.line74.setObjectName("line74")
        self.gridLayout.addWidget(self.line74, 10, 1, 1, 1)
        self.line73 = QtWidgets.QLineEdit(self.gridFrame)
        self.line73.setMinimumSize(QtCore.QSize(80, 80))
        self.line73.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line73.setFont(font)
        self.line73.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line73.setMaxLength(1)
        self.line73.setAlignment(QtCore.Qt.AlignCenter)
        self.line73.setObjectName("line73")
        self.gridLayout.addWidget(self.line73, 10, 0, 1, 1)
        self.line60 = QtWidgets.QLineEdit(self.gridFrame)
        self.line60.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line60.setFont(font)
        self.line60.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line60.setMaxLength(1)
        self.line60.setAlignment(QtCore.Qt.AlignCenter)
        self.line60.setObjectName("line60")
        self.gridLayout.addWidget(self.line60, 8, 6, 1, 1)
        self.line65 = QtWidgets.QLineEdit(self.gridFrame)
        self.line65.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line65.setFont(font)
        self.line65.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line65.setMaxLength(1)
        self.line65.setAlignment(QtCore.Qt.AlignCenter)
        self.line65.setObjectName("line65")
        self.gridLayout.addWidget(self.line65, 9, 1, 1, 1)
        self.line68 = QtWidgets.QLineEdit(self.gridFrame)
        self.line68.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line68.setFont(font)
        self.line68.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line68.setMaxLength(1)
        self.line68.setAlignment(QtCore.Qt.AlignCenter)
        self.line68.setObjectName("line68")
        self.gridLayout.addWidget(self.line68, 9, 5, 1, 1)
        self.line72 = QtWidgets.QLineEdit(self.gridFrame)
        self.line72.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line72.setFont(font)
        self.line72.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line72.setMaxLength(1)
        self.line72.setAlignment(QtCore.Qt.AlignCenter)
        self.line72.setObjectName("line72")
        self.gridLayout.addWidget(self.line72, 9, 10, 1, 1)
        self.line76 = QtWidgets.QLineEdit(self.gridFrame)
        self.line76.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line76.setFont(font)
        self.line76.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line76.setMaxLength(1)
        self.line76.setAlignment(QtCore.Qt.AlignCenter)
        self.line76.setObjectName("line76")
        self.gridLayout.addWidget(self.line76, 10, 4, 1, 1)
        self.line59 = QtWidgets.QLineEdit(self.gridFrame)
        self.line59.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line59.setFont(font)
        self.line59.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line59.setMaxLength(1)
        self.line59.setAlignment(QtCore.Qt.AlignCenter)
        self.line59.setObjectName("line59")
        self.gridLayout.addWidget(self.line59, 8, 5, 1, 1)
        self.line80 = QtWidgets.QLineEdit(self.gridFrame)
        self.line80.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line80.setFont(font)
        self.line80.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line80.setMaxLength(1)
        self.line80.setAlignment(QtCore.Qt.AlignCenter)
        self.line80.setObjectName("line80")
        self.gridLayout.addWidget(self.line80, 10, 9, 1, 1)
        self.line58 = QtWidgets.QLineEdit(self.gridFrame)
        self.line58.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line58.setFont(font)
        self.line58.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line58.setMaxLength(1)
        self.line58.setAlignment(QtCore.Qt.AlignCenter)
        self.line58.setObjectName("line58")
        self.gridLayout.addWidget(self.line58, 8, 4, 1, 1)
        self.line70 = QtWidgets.QLineEdit(self.gridFrame)
        self.line70.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line70.setFont(font)
        self.line70.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line70.setMaxLength(1)
        self.line70.setAlignment(QtCore.Qt.AlignCenter)
        self.line70.setObjectName("line70")
        self.gridLayout.addWidget(self.line70, 9, 8, 1, 1)
        self.line62 = QtWidgets.QLineEdit(self.gridFrame)
        self.line62.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line62.setFont(font)
        self.line62.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line62.setMaxLength(1)
        self.line62.setAlignment(QtCore.Qt.AlignCenter)
        self.line62.setObjectName("line62")
        self.gridLayout.addWidget(self.line62, 8, 9, 1, 1)
        self.line56 = QtWidgets.QLineEdit(self.gridFrame)
        self.line56.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line56.setFont(font)
        self.line56.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line56.setMaxLength(1)
        self.line56.setAlignment(QtCore.Qt.AlignCenter)
        self.line56.setObjectName("line56")
        self.gridLayout.addWidget(self.line56, 8, 1, 1, 1)
        self.line66 = QtWidgets.QLineEdit(self.gridFrame)
        self.line66.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line66.setFont(font)
        self.line66.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line66.setMaxLength(1)
        self.line66.setAlignment(QtCore.Qt.AlignCenter)
        self.line66.setObjectName("line66")
        self.gridLayout.addWidget(self.line66, 9, 2, 1, 1)
        self.line77 = QtWidgets.QLineEdit(self.gridFrame)
        self.line77.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line77.setFont(font)
        self.line77.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line77.setMaxLength(1)
        self.line77.setAlignment(QtCore.Qt.AlignCenter)
        self.line77.setObjectName("line77")
        self.gridLayout.addWidget(self.line77, 10, 5, 1, 1)
        self.line54 = QtWidgets.QLineEdit(self.gridFrame)
        self.line54.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line54.setFont(font)
        self.line54.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line54.setMaxLength(1)
        self.line54.setAlignment(QtCore.Qt.AlignCenter)
        self.line54.setObjectName("line54")
        self.gridLayout.addWidget(self.line54, 6, 10, 1, 1)
        self.line67 = QtWidgets.QLineEdit(self.gridFrame)
        self.line67.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line67.setFont(font)
        self.line67.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line67.setMaxLength(1)
        self.line67.setAlignment(QtCore.Qt.AlignCenter)
        self.line67.setObjectName("line67")
        self.gridLayout.addWidget(self.line67, 9, 4, 1, 1)
        self.line55 = QtWidgets.QLineEdit(self.gridFrame)
        self.line55.setMinimumSize(QtCore.QSize(80, 80))
        self.line55.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line55.setFont(font)
        self.line55.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line55.setMaxLength(1)
        self.line55.setAlignment(QtCore.Qt.AlignCenter)
        self.line55.setObjectName("line55")
        self.gridLayout.addWidget(self.line55, 8, 0, 1, 1)
        self.line71 = QtWidgets.QLineEdit(self.gridFrame)
        self.line71.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line71.setFont(font)
        self.line71.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line71.setMaxLength(1)
        self.line71.setAlignment(QtCore.Qt.AlignCenter)
        self.line71.setObjectName("line71")
        self.gridLayout.addWidget(self.line71, 9, 9, 1, 1)
        self.line69 = QtWidgets.QLineEdit(self.gridFrame)
        self.line69.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line69.setFont(font)
        self.line69.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line69.setMaxLength(1)
        self.line69.setAlignment(QtCore.Qt.AlignCenter)
        self.line69.setObjectName("line69")
        self.gridLayout.addWidget(self.line69, 9, 6, 1, 1)
        self.line78 = QtWidgets.QLineEdit(self.gridFrame)
        self.line78.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line78.setFont(font)
        self.line78.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line78.setMaxLength(1)
        self.line78.setAlignment(QtCore.Qt.AlignCenter)
        self.line78.setObjectName("line78")
        self.gridLayout.addWidget(self.line78, 10, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem1, 7, 0, 1, 1)
        self.line1 = QtWidgets.QLineEdit(self.gridFrame)
        self.line1.setEnabled(True)
        self.line1.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line1.setFont(font)
        self.line1.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line1.setMaxLength(1)
        self.line1.setAlignment(QtCore.Qt.AlignCenter)
        self.line1.setReadOnly(False)
        self.line1.setObjectName("line1")
        self.gridLayout.addWidget(self.line1, 0, 0, 1, 1)
        self.line38 = QtWidgets.QLineEdit(self.gridFrame)
        self.line38.setMinimumSize(QtCore.QSize(80, 80))
        self.line38.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line38.setFont(font)
        self.line38.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line38.setMaxLength(1)
        self.line38.setAlignment(QtCore.Qt.AlignCenter)
        self.line38.setObjectName("line38")
        self.gridLayout.addWidget(self.line38, 5, 1, 1, 1)
        self.line31 = QtWidgets.QLineEdit(self.gridFrame)
        self.line31.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line31.setFont(font)
        self.line31.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line31.setMaxLength(1)
        self.line31.setAlignment(QtCore.Qt.AlignCenter)
        self.line31.setObjectName("line31")
        self.gridLayout.addWidget(self.line31, 4, 4, 1, 1)
        self.line37 = QtWidgets.QLineEdit(self.gridFrame)
        self.line37.setMinimumSize(QtCore.QSize(80, 80))
        self.line37.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line37.setFont(font)
        self.line37.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line37.setMaxLength(1)
        self.line37.setAlignment(QtCore.Qt.AlignCenter)
        self.line37.setObjectName("line37")
        self.gridLayout.addWidget(self.line37, 5, 0, 1, 1)
        self.line40 = QtWidgets.QLineEdit(self.gridFrame)
        self.line40.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line40.setFont(font)
        self.line40.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line40.setMaxLength(1)
        self.line40.setAlignment(QtCore.Qt.AlignCenter)
        self.line40.setObjectName("line40")
        self.gridLayout.addWidget(self.line40, 5, 4, 1, 1)
        self.line30 = QtWidgets.QLineEdit(self.gridFrame)
        self.line30.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line30.setFont(font)
        self.line30.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line30.setMaxLength(1)
        self.line30.setAlignment(QtCore.Qt.AlignCenter)
        self.line30.setObjectName("line30")
        self.gridLayout.addWidget(self.line30, 4, 2, 1, 1)
        self.line36 = QtWidgets.QLineEdit(self.gridFrame)
        self.line36.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line36.setFont(font)
        self.line36.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line36.setMaxLength(1)
        self.line36.setAlignment(QtCore.Qt.AlignCenter)
        self.line36.setObjectName("line36")
        self.gridLayout.addWidget(self.line36, 4, 10, 1, 1)
        self.line41 = QtWidgets.QLineEdit(self.gridFrame)
        self.line41.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line41.setFont(font)
        self.line41.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line41.setMaxLength(1)
        self.line41.setAlignment(QtCore.Qt.AlignCenter)
        self.line41.setObjectName("line41")
        self.gridLayout.addWidget(self.line41, 5, 5, 1, 1)
        self.line27 = QtWidgets.QLineEdit(self.gridFrame)
        self.line27.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line27.setFont(font)
        self.line27.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line27.setMaxLength(1)
        self.line27.setAlignment(QtCore.Qt.AlignCenter)
        self.line27.setObjectName("line27")
        self.gridLayout.addWidget(self.line27, 2, 10, 1, 1)
        self.line32 = QtWidgets.QLineEdit(self.gridFrame)
        self.line32.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line32.setFont(font)
        self.line32.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line32.setMaxLength(1)
        self.line32.setAlignment(QtCore.Qt.AlignCenter)
        self.line32.setObjectName("line32")
        self.gridLayout.addWidget(self.line32, 4, 5, 1, 1)
        self.line42 = QtWidgets.QLineEdit(self.gridFrame)
        self.line42.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line42.setFont(font)
        self.line42.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line42.setMaxLength(1)
        self.line42.setAlignment(QtCore.Qt.AlignCenter)
        self.line42.setObjectName("line42")
        self.gridLayout.addWidget(self.line42, 5, 6, 1, 1)
        self.line43 = QtWidgets.QLineEdit(self.gridFrame)
        self.line43.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line43.setFont(font)
        self.line43.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line43.setMaxLength(1)
        self.line43.setAlignment(QtCore.Qt.AlignCenter)
        self.line43.setObjectName("line43")
        self.gridLayout.addWidget(self.line43, 5, 8, 1, 1)
        self.line45 = QtWidgets.QLineEdit(self.gridFrame)
        self.line45.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line45.setFont(font)
        self.line45.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line45.setMaxLength(1)
        self.line45.setAlignment(QtCore.Qt.AlignCenter)
        self.line45.setObjectName("line45")
        self.gridLayout.addWidget(self.line45, 5, 10, 1, 1)
        self.line26 = QtWidgets.QLineEdit(self.gridFrame)
        self.line26.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line26.setFont(font)
        self.line26.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line26.setMaxLength(1)
        self.line26.setAlignment(QtCore.Qt.AlignCenter)
        self.line26.setObjectName("line26")
        self.gridLayout.addWidget(self.line26, 2, 9, 1, 1)
        self.line47 = QtWidgets.QLineEdit(self.gridFrame)
        self.line47.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line47.setFont(font)
        self.line47.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line47.setMaxLength(1)
        self.line47.setAlignment(QtCore.Qt.AlignCenter)
        self.line47.setObjectName("line47")
        self.gridLayout.addWidget(self.line47, 6, 1, 1, 1)
        self.line48 = QtWidgets.QLineEdit(self.gridFrame)
        self.line48.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line48.setFont(font)
        self.line48.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line48.setMaxLength(1)
        self.line48.setAlignment(QtCore.Qt.AlignCenter)
        self.line48.setObjectName("line48")
        self.gridLayout.addWidget(self.line48, 6, 2, 1, 1)
        self.line25 = QtWidgets.QLineEdit(self.gridFrame)
        self.line25.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line25.setFont(font)
        self.line25.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line25.setMaxLength(1)
        self.line25.setAlignment(QtCore.Qt.AlignCenter)
        self.line25.setObjectName("line25")
        self.gridLayout.addWidget(self.line25, 2, 8, 1, 1)
        self.line49 = QtWidgets.QLineEdit(self.gridFrame)
        self.line49.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line49.setFont(font)
        self.line49.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}background-color: rgb(255, 255, 255);")
        self.line49.setMaxLength(1)
        self.line49.setAlignment(QtCore.Qt.AlignCenter)
        self.line49.setObjectName("line49")
        self.gridLayout.addWidget(self.line49, 6, 4, 1, 1)
        self.line29 = QtWidgets.QLineEdit(self.gridFrame)
        self.line29.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line29.setFont(font)
        self.line29.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line29.setMaxLength(1)
        self.line29.setAlignment(QtCore.Qt.AlignCenter)
        self.line29.setObjectName("line29")
        self.gridLayout.addWidget(self.line29, 4, 1, 1, 1)
        self.line50 = QtWidgets.QLineEdit(self.gridFrame)
        self.line50.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line50.setFont(font)
        self.line50.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line50.setMaxLength(1)
        self.line50.setAlignment(QtCore.Qt.AlignCenter)
        self.line50.setObjectName("line50")
        self.gridLayout.addWidget(self.line50, 6, 5, 1, 1)
        self.line51 = QtWidgets.QLineEdit(self.gridFrame)
        self.line51.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line51.setFont(font)
        self.line51.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line51.setMaxLength(1)
        self.line51.setAlignment(QtCore.Qt.AlignCenter)
        self.line51.setObjectName("line51")
        self.gridLayout.addWidget(self.line51, 6, 6, 1, 1)
        self.line33 = QtWidgets.QLineEdit(self.gridFrame)
        self.line33.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line33.setFont(font)
        self.line33.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line33.setMaxLength(1)
        self.line33.setAlignment(QtCore.Qt.AlignCenter)
        self.line33.setObjectName("line33")
        self.gridLayout.addWidget(self.line33, 4, 6, 1, 1)
        self.line52 = QtWidgets.QLineEdit(self.gridFrame)
        self.line52.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line52.setFont(font)
        self.line52.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line52.setMaxLength(1)
        self.line52.setAlignment(QtCore.Qt.AlignCenter)
        self.line52.setObjectName("line52")
        self.gridLayout.addWidget(self.line52, 6, 8, 1, 1)
        self.line53 = QtWidgets.QLineEdit(self.gridFrame)
        self.line53.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line53.setFont(font)
        self.line53.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line53.setMaxLength(1)
        self.line53.setAlignment(QtCore.Qt.AlignCenter)
        self.line53.setObjectName("line53")
        self.gridLayout.addWidget(self.line53, 6, 9, 1, 1)
        self.line28 = QtWidgets.QLineEdit(self.gridFrame)
        self.line28.setMinimumSize(QtCore.QSize(80, 80))
        self.line28.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line28.setFont(font)
        self.line28.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line28.setMaxLength(1)
        self.line28.setAlignment(QtCore.Qt.AlignCenter)
        self.line28.setObjectName("line28")
        self.gridLayout.addWidget(self.line28, 4, 0, 1, 1)
        self.line34 = QtWidgets.QLineEdit(self.gridFrame)
        self.line34.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line34.setFont(font)
        self.line34.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line34.setMaxLength(1)
        self.line34.setAlignment(QtCore.Qt.AlignCenter)
        self.line34.setObjectName("line34")
        self.gridLayout.addWidget(self.line34, 4, 8, 1, 1)
        self.line35 = QtWidgets.QLineEdit(self.gridFrame)
        self.line35.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line35.setFont(font)
        self.line35.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line35.setMaxLength(1)
        self.line35.setAlignment(QtCore.Qt.AlignCenter)
        self.line35.setObjectName("line35")
        self.gridLayout.addWidget(self.line35, 4, 9, 1, 1)
        self.line39 = QtWidgets.QLineEdit(self.gridFrame)
        self.line39.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line39.setFont(font)
        self.line39.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line39.setMaxLength(1)
        self.line39.setAlignment(QtCore.Qt.AlignCenter)
        self.line39.setObjectName("line39")
        self.gridLayout.addWidget(self.line39, 5, 2, 1, 1)
        self.line44 = QtWidgets.QLineEdit(self.gridFrame)
        self.line44.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line44.setFont(font)
        self.line44.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line44.setMaxLength(1)
        self.line44.setAlignment(QtCore.Qt.AlignCenter)
        self.line44.setObjectName("line44")
        self.gridLayout.addWidget(self.line44, 5, 9, 1, 1)
        self.line46 = QtWidgets.QLineEdit(self.gridFrame)
        self.line46.setMinimumSize(QtCore.QSize(80, 80))
        self.line46.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line46.setFont(font)
        self.line46.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line46.setMaxLength(1)
        self.line46.setAlignment(QtCore.Qt.AlignCenter)
        self.line46.setObjectName("line46")
        self.gridLayout.addWidget(self.line46, 6, 0, 1, 1)
        self.line3 = QtWidgets.QLineEdit(self.gridFrame)
        self.line3.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line3.setFont(font)
        self.line3.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line3.setMaxLength(1)
        self.line3.setAlignment(QtCore.Qt.AlignCenter)
        self.line3.setObjectName("line3")
        self.gridLayout.addWidget(self.line3, 0, 2, 1, 1)
        self.line2 = QtWidgets.QLineEdit(self.gridFrame)
        self.line2.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line2.setFont(font)
        self.line2.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line2.setMaxLength(1)
        self.line2.setAlignment(QtCore.Qt.AlignCenter)
        self.line2.setObjectName("line2")
        self.gridLayout.addWidget(self.line2, 0, 1, 1, 1)
        self.line4 = QtWidgets.QLineEdit(self.gridFrame)
        self.line4.setMinimumSize(QtCore.QSize(80, 80))
        self.line4.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line4.setFont(font)
        self.line4.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line4.setMaxLength(1)
        self.line4.setAlignment(QtCore.Qt.AlignCenter)
        self.line4.setObjectName("line4")
        self.gridLayout.addWidget(self.line4, 0, 4, 1, 1)
        self.line11 = QtWidgets.QLineEdit(self.gridFrame)
        self.line11.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line11.setFont(font)
        self.line11.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line11.setMaxLength(1)
        self.line11.setAlignment(QtCore.Qt.AlignCenter)
        self.line11.setObjectName("line11")
        self.gridLayout.addWidget(self.line11, 1, 1, 1, 1)
        self.line5 = QtWidgets.QLineEdit(self.gridFrame)
        self.line5.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line5.setFont(font)
        self.line5.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line5.setMaxLength(1)
        self.line5.setAlignment(QtCore.Qt.AlignCenter)
        self.line5.setObjectName("line5")
        self.gridLayout.addWidget(self.line5, 0, 5, 1, 1)
        self.line8 = QtWidgets.QLineEdit(self.gridFrame)
        self.line8.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line8.setFont(font)
        self.line8.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line8.setMaxLength(1)
        self.line8.setAlignment(QtCore.Qt.AlignCenter)
        self.line8.setObjectName("line8")
        self.gridLayout.addWidget(self.line8, 0, 9, 1, 1)
        self.line6 = QtWidgets.QLineEdit(self.gridFrame)
        self.line6.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line6.setFont(font)
        self.line6.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line6.setMaxLength(1)
        self.line6.setAlignment(QtCore.Qt.AlignCenter)
        self.line6.setObjectName("line6")
        self.gridLayout.addWidget(self.line6, 0, 6, 1, 1)
        self.line7 = QtWidgets.QLineEdit(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line7.sizePolicy().hasHeightForWidth())
        self.line7.setSizePolicy(sizePolicy)
        self.line7.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line7.setFont(font)
        self.line7.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line7.setMaxLength(1)
        self.line7.setAlignment(QtCore.Qt.AlignCenter)
        self.line7.setReadOnly(False)
        self.line7.setObjectName("line7")
        self.gridLayout.addWidget(self.line7, 0, 8, 1, 1)
        self.line9 = QtWidgets.QLineEdit(self.gridFrame)
        self.line9.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line9.setFont(font)
        self.line9.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line9.setMaxLength(1)
        self.line9.setAlignment(QtCore.Qt.AlignCenter)
        self.line9.setObjectName("line9")
        self.gridLayout.addWidget(self.line9, 0, 10, 1, 1)
        self.line10 = QtWidgets.QLineEdit(self.gridFrame)
        self.line10.setMinimumSize(QtCore.QSize(80, 80))
        self.line10.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line10.setFont(font)
        self.line10.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line10.setMaxLength(1)
        self.line10.setAlignment(QtCore.Qt.AlignCenter)
        self.line10.setObjectName("line10")
        self.gridLayout.addWidget(self.line10, 1, 0, 1, 1)
        self.line12 = QtWidgets.QLineEdit(self.gridFrame)
        self.line12.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line12.setFont(font)
        self.line12.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line12.setMaxLength(1)
        self.line12.setAlignment(QtCore.Qt.AlignCenter)
        self.line12.setObjectName("line12")
        self.gridLayout.addWidget(self.line12, 1, 2, 1, 1)
        self.line13 = QtWidgets.QLineEdit(self.gridFrame)
        self.line13.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line13.setFont(font)
        self.line13.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line13.setMaxLength(1)
        self.line13.setAlignment(QtCore.Qt.AlignCenter)
        self.line13.setObjectName("line13")
        self.gridLayout.addWidget(self.line13, 1, 4, 1, 1)
        self.line14 = QtWidgets.QLineEdit(self.gridFrame)
        self.line14.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line14.setFont(font)
        self.line14.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line14.setMaxLength(1)
        self.line14.setAlignment(QtCore.Qt.AlignCenter)
        self.line14.setObjectName("line14")
        self.gridLayout.addWidget(self.line14, 1, 5, 1, 1)
        self.line15 = QtWidgets.QLineEdit(self.gridFrame)
        self.line15.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line15.setFont(font)
        self.line15.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line15.setMaxLength(1)
        self.line15.setAlignment(QtCore.Qt.AlignCenter)
        self.line15.setObjectName("line15")
        self.gridLayout.addWidget(self.line15, 1, 6, 1, 1)
        self.line16 = QtWidgets.QLineEdit(self.gridFrame)
        self.line16.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line16.setFont(font)
        self.line16.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line16.setMaxLength(1)
        self.line16.setAlignment(QtCore.Qt.AlignCenter)
        self.line16.setReadOnly(False)
        self.line16.setObjectName("line16")
        self.gridLayout.addWidget(self.line16, 1, 8, 1, 1)
        self.line17 = QtWidgets.QLineEdit(self.gridFrame)
        self.line17.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line17.setFont(font)
        self.line17.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line17.setMaxLength(1)
        self.line17.setAlignment(QtCore.Qt.AlignCenter)
        self.line17.setObjectName("line17")
        self.gridLayout.addWidget(self.line17, 1, 9, 1, 1)
        self.line21 = QtWidgets.QLineEdit(self.gridFrame)
        self.line21.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line21.setFont(font)
        self.line21.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line21.setMaxLength(1)
        self.line21.setAlignment(QtCore.Qt.AlignCenter)
        self.line21.setObjectName("line21")
        self.gridLayout.addWidget(self.line21, 2, 2, 1, 1)
        self.line22 = QtWidgets.QLineEdit(self.gridFrame)
        self.line22.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line22.setFont(font)
        self.line22.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line22.setMaxLength(1)
        self.line22.setAlignment(QtCore.Qt.AlignCenter)
        self.line22.setObjectName("line22")
        self.gridLayout.addWidget(self.line22, 2, 4, 1, 1)
        self.line23 = QtWidgets.QLineEdit(self.gridFrame)
        self.line23.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line23.setFont(font)
        self.line23.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line23.setMaxLength(1)
        self.line23.setAlignment(QtCore.Qt.AlignCenter)
        self.line23.setObjectName("line23")
        self.gridLayout.addWidget(self.line23, 2, 5, 1, 1)
        self.line20 = QtWidgets.QLineEdit(self.gridFrame)
        self.line20.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line20.setFont(font)
        self.line20.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line20.setMaxLength(1)
        self.line20.setAlignment(QtCore.Qt.AlignCenter)
        self.line20.setObjectName("line20")
        self.gridLayout.addWidget(self.line20, 2, 1, 1, 1)
        self.line19 = QtWidgets.QLineEdit(self.gridFrame)
        self.line19.setMinimumSize(QtCore.QSize(80, 80))
        self.line19.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line19.setFont(font)
        self.line19.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line19.setMaxLength(1)
        self.line19.setAlignment(QtCore.Qt.AlignCenter)
        self.line19.setObjectName("line19")
        self.gridLayout.addWidget(self.line19, 2, 0, 1, 1)
        self.line24 = QtWidgets.QLineEdit(self.gridFrame)
        self.line24.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line24.setFont(font)
        self.line24.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line24.setMaxLength(1)
        self.line24.setAlignment(QtCore.Qt.AlignCenter)
        self.line24.setObjectName("line24")
        self.gridLayout.addWidget(self.line24, 2, 6, 1, 1)
        self.line18 = QtWidgets.QLineEdit(self.gridFrame)
        self.line18.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line18.setFont(font)
        self.line18.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line18.setMaxLength(1)
        self.line18.setAlignment(QtCore.Qt.AlignCenter)
        self.line18.setObjectName("line18")
        self.gridLayout.addWidget(self.line18, 1, 10, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(2, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 7, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(2, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 3, 1, 1)
        self.line57 = QtWidgets.QLineEdit(self.gridFrame)
        self.line57.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line57.setFont(font)
        self.line57.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line57.setMaxLength(1)
        self.line57.setAlignment(QtCore.Qt.AlignCenter)
        self.line57.setObjectName("line57")
        self.gridLayout.addWidget(self.line57, 8, 2, 1, 1)
        self.gridLayout_2.addWidget(self.gridFrame, 1, 6, 2, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.undo_btn = QtWidgets.QPushButton(self.centralwidget)
        self.undo_btn.setMinimumSize(QtCore.QSize(71, 81))
        self.undo_btn.setMaximumSize(QtCore.QSize(71, 81))
        self.undo_btn.setStyleSheet("QPushButton{\n"
                                    "border-radius: 35px;\n"
                                    "background: rgb(198, 198, 198);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "background: rgb(170, 170, 170);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "background: rgb(160, 160, 160);\n"
                                    "}\n"
                                    "")
        self.undo_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undo_btn.setIcon(icon1)
        self.undo_btn.setIconSize(QtCore.QSize(80, 80))
        self.undo_btn.setObjectName("undo_btn")
        self.horizontalLayout_3.addWidget(self.undo_btn)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.redo_btn = QtWidgets.QPushButton(self.centralwidget)
        self.redo_btn.setMinimumSize(QtCore.QSize(71, 81))
        self.redo_btn.setMaximumSize(QtCore.QSize(71, 81))
        self.redo_btn.setStyleSheet("QPushButton{\n"
                                    "border-radius: 35px;\n"
                                    "background: rgb(198, 198, 198);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "background: rgb(170, 170, 170);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "background: rgb(160, 160, 160);\n"
                                    "}\n"
                                    "")
        self.redo_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/Redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redo_btn.setIcon(icon2)
        self.redo_btn.setIconSize(QtCore.QSize(80, 80))
        self.redo_btn.setObjectName("redo_btn")
        self.horizontalLayout_3.addWidget(self.redo_btn)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.hint_btn = QtWidgets.QPushButton(self.centralwidget)
        self.hint_btn.setMinimumSize(QtCore.QSize(60, 80))
        self.hint_btn.setMaximumSize(QtCore.QSize(60, 80))
        self.hint_btn.setStyleSheet("QPushButton{\n"
                                    "border-radius: 30px;\n"
                                    "background: rgb(195, 195, 195);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "background: rgb(255,255,0);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "background: rgb(235,235,0);\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.hint_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/Hint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hint_btn.setIcon(icon3)
        self.hint_btn.setIconSize(QtCore.QSize(80, 80))
        self.hint_btn.setObjectName("hint_btn")
        self.horizontalLayout_2.addWidget(self.hint_btn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.solve_btn = QtWidgets.QPushButton(self.centralwidget)
        self.solve_btn.setMinimumSize(QtCore.QSize(70, 80))
        self.solve_btn.setMaximumSize(QtCore.QSize(70, 80))
        self.solve_btn.setStyleSheet("QPushButton{\n"
                                     "border-radius: 35px;\n"
                                     "background: rgb(195, 195, 195);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "background: rgb(255,170,127);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "background:  rgb(235,150,107);\n"
                                     "}\n"
                                     "\n"
                                     "")
        self.solve_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/Solve.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.solve_btn.setIcon(icon4)
        self.solve_btn.setIconSize(QtCore.QSize(80, 80))
        self.solve_btn.setObjectName("solve_btn")
        self.horizontalLayout_2.addWidget(self.solve_btn)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_btn.sizePolicy().hasHeightForWidth())
        self.reset_btn.setSizePolicy(sizePolicy)
        self.reset_btn.setMinimumSize(QtCore.QSize(71, 61))
        self.reset_btn.setMaximumSize(QtCore.QSize(71, 61))
        self.reset_btn.setStyleSheet("QPushButton{\n"
                                     "border-radius: 30px;\n"
                                     "background: rgb(198, 198, 198);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "background: rgb(170, 170, 170);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "background: rgb(160, 160, 160);\n"
                                     "}\n"
                                     "")
        self.reset_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icons/Reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_btn.setIcon(icon5)
        self.reset_btn.setIconSize(QtCore.QSize(80, 80))
        self.reset_btn.setObjectName("reset_btn")
        self.horizontalLayout_2.addWidget(self.reset_btn)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 6, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 3, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem9, 4, 6, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem10, 0, 6, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 3, 8, 1, 1)
        SudokuSolver.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(SudokuSolver)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1051, 26))
        self.menuBar.setStyleSheet("QMenuBar {\n"
                                   "background-color: transparent;\n"
                                   "}\n"
                                   "\n"
                                   "QMenuBar::item {\n"
                                   "color : black;\n"
                                   "background: transparent;\n"
                                   "}\n"
                                   "\n"
                                   "QMenuBar::item:selected {\n"
                                   "background: rgb(200, 200, 200);\n"
                                   "color:black;\n"
                                   "}")
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setStyleSheet("QMenu{\n"
                                    "    background: rgb(235, 235, 235);\n"
                                    "    color: black;\n"
                                    "}\n"
                                    "\n"
                                    "QMenu:selected{\n"
                                    "    background: rgb(200, 200, 200);\n"
                                    "}")
        self.menuFile.setObjectName("menuFile")
        self.menuGenerate = QtWidgets.QMenu(self.menuBar)
        self.menuGenerate.setStyleSheet("QMenu{\n"
                                        "    background: rgb(235, 235, 235);\n"
                                        "    color: black;\n"
                                        "}\n"
                                        "\n"
                                        "QMenu:selected{\n"
                                        "    background: rgb(200, 200, 200);\n"
                                        "}\n"
                                        "\n"
                                        "QMenu:pressed{\n"
                                        "    background: rgb(180, 180, 180);\n"
                                        "}")
        self.menuGenerate.setObjectName("menuGenerate")
        self.menuRandom_Puzzle_2 = QtWidgets.QMenu(self.menuGenerate)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icons/Random.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuRandom_Puzzle_2.setIcon(icon6)
        self.menuRandom_Puzzle_2.setObjectName("menuRandom_Puzzle_2")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setStyleSheet("QMenu{\n"
                                    "    background: rgb(235, 235, 235);\n"
                                    "    color: black;\n"
                                    "}\n"
                                    "\n"
                                    "QMenu:selected{\n"
                                    "    background: rgb(200, 200, 200);\n"
                                    "}\n"
                                    "\n"
                                    "QMenu:pressed{\n"
                                    "    background: rgb(180, 180, 180);\n"
                                    "}")
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setStyleSheet("QMenu{\n"
                                    "    background: rgb(235, 235, 235);\n"
                                    "    color: black;\n"
                                    "}\n"
                                    "\n"
                                    "QMenu:selected{\n"
                                    "    background: rgb(200, 200, 200);\n"
                                    "}")
        self.menuView.setObjectName("menuView")
        SudokuSolver.setMenuBar(self.menuBar)
        self.actionSelect_a_difficulty = QtWidgets.QAction(SudokuSolver)
        self.actionSelect_a_difficulty.setObjectName("actionSelect_a_difficulty")
        self.actionManually = QtWidgets.QAction(SudokuSolver)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Icons/manual.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionManually.setIcon(icon7)
        self.actionManually.setObjectName("actionManually")
        self.actionInsert_an_image = QtWidgets.QAction(SudokuSolver)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Icons/camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInsert_an_image.setIcon(icon8)
        self.actionInsert_an_image.setObjectName("actionInsert_an_image")
        self.actionHow_to_Use = QtWidgets.QAction(SudokuSolver)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHow_to_Use.setIcon(icon9)
        self.actionHow_to_Use.setObjectName("actionHow_to_Use")
        self.actionEasy = QtWidgets.QAction(SudokuSolver)
        self.actionEasy.setObjectName("actionEasy")
        self.actionMedium = QtWidgets.QAction(SudokuSolver)
        self.actionMedium.setObjectName("actionMedium")
        self.actionHard = QtWidgets.QAction(SudokuSolver)
        self.actionHard.setObjectName("actionHard")
        self.actionSave = QtWidgets.QAction(SudokuSolver)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("Icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon10)
        self.actionSave.setObjectName("actionSave")
        self.actionFull_Screen = QtWidgets.QAction(SudokuSolver)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("Icons/fullscreen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFull_Screen.setIcon(icon11)
        self.actionFull_Screen.setObjectName("actionFull_Screen")
        self.actionEasy_2 = QtWidgets.QAction(SudokuSolver)
        self.actionEasy_2.setObjectName("actionEasy_2")
        self.actionMedium_2 = QtWidgets.QAction(SudokuSolver)
        self.actionMedium_2.setObjectName("actionMedium_2")
        self.actionHard_2 = QtWidgets.QAction(SudokuSolver)
        self.actionHard_2.setObjectName("actionHard_2")
        self.actionLoad = QtWidgets.QAction(SudokuSolver)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("Icons/load.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad.setIcon(icon12)
        self.actionLoad.setObjectName("actionLoad")
        self.actionClose = QtWidgets.QAction(SudokuSolver)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("Icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon13)
        self.actionClose.setObjectName("actionClose")
        self.actionFull_Screen_2 = QtWidgets.QAction(SudokuSolver)
        self.actionFull_Screen_2.setIcon(icon11)
        self.actionFull_Screen_2.setObjectName("actionFull_Screen_2")
        self.actionDark_Mode = QtWidgets.QAction(SudokuSolver)
        self.actionDark_Mode.setCheckable(True)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("Icons/dark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDark_Mode.setIcon(icon14)
        self.actionDark_Mode.setObjectName("actionDark_Mode")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose)
        self.menuRandom_Puzzle_2.addAction(self.actionEasy_2)
        self.menuRandom_Puzzle_2.addAction(self.actionMedium_2)
        self.menuRandom_Puzzle_2.addAction(self.actionHard_2)
        self.menuGenerate.addAction(self.menuRandom_Puzzle_2.menuAction())
        self.menuGenerate.addAction(self.actionManually)
        self.menuGenerate.addSeparator()
        self.menuGenerate.addAction(self.actionLoad)
        self.menuGenerate.addAction(self.actionInsert_an_image)
        self.menuHelp.addAction(self.actionHow_to_Use)
        self.menuView.addAction(self.actionFull_Screen_2)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuGenerate.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(SudokuSolver)
        QtCore.QMetaObject.connectSlotsByName(SudokuSolver)

    def retranslateUi(self, SudokuSolver):
        _translate = QtCore.QCoreApplication.translate
        SudokuSolver.setWindowTitle(_translate("SudokuSolver", "Sudoku Generator & Solver"))
        self.undo_btn.setToolTip(_translate("SudokuSolver", "<html><head/><body><p>Undo</p></body></html>"))
        self.redo_btn.setToolTip(_translate("SudokuSolver", "<html><head/><body><p>Redo</p></body></html>"))
        self.hint_btn.setToolTip(_translate("SudokuSolver", "<html><head/><body><p>Hint</p></body></html>"))
        self.solve_btn.setToolTip(_translate("SudokuSolver", "<html><head/><body><p>Solve</p></body></html>"))
        self.reset_btn.setToolTip(_translate("SudokuSolver", "<html><head/><body><p>Reset</p></body></html>"))
        self.menuFile.setTitle(_translate("SudokuSolver", "File"))
        self.menuGenerate.setTitle(_translate("SudokuSolver", "Generate"))
        self.menuRandom_Puzzle_2.setTitle(_translate("SudokuSolver", "Random Puzzle"))
        self.menuHelp.setTitle(_translate("SudokuSolver", "Help"))
        self.menuView.setTitle(_translate("SudokuSolver", "View"))
        self.actionSelect_a_difficulty.setText(_translate("SudokuSolver", "Select a difficulty"))
        self.actionManually.setText(_translate("SudokuSolver", "Manually"))
        self.actionInsert_an_image.setText(_translate("SudokuSolver", "Insert an Image"))
        self.actionHow_to_Use.setText(_translate("SudokuSolver", "How to Use"))
        self.actionEasy.setText(_translate("SudokuSolver", "Easy"))
        self.actionMedium.setText(_translate("SudokuSolver", "Medium"))
        self.actionHard.setText(_translate("SudokuSolver", "Hard"))
        self.actionSave.setText(_translate("SudokuSolver", "Save"))
        self.actionFull_Screen.setText(_translate("SudokuSolver", "Full Screen"))
        self.actionEasy_2.setText(_translate("SudokuSolver", "Easy"))
        self.actionMedium_2.setText(_translate("SudokuSolver", "Medium"))
        self.actionHard_2.setText(_translate("SudokuSolver", "Hard"))
        self.actionLoad.setText(_translate("SudokuSolver", "Load"))
        self.actionClose.setText(_translate("SudokuSolver", "Close"))
        self.actionFull_Screen_2.setText(_translate("SudokuSolver", "Full Screen"))
        self.actionDark_Mode.setText(_translate("SudokuSolver", "Dark Mode"))


class Ui_image_crop_dialog:
    def setupUi(self, image_crop_dialog):
        image_crop_dialog.setObjectName("image_crop_dialog")
        image_crop_dialog.resize(1075, 806)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/crop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        image_crop_dialog.setWindowIcon(icon)
        image_crop_dialog.setStyleSheet("")
        image_crop_dialog.setSizeGripEnabled(False)
        image_crop_dialog.setModal(False)
        self.gridLayout_2 = QtWidgets.QGridLayout(image_crop_dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(image_crop_dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 4, 1, 1)
        self.y1_slider = QtWidgets.QSlider(image_crop_dialog)
        self.y1_slider.setToolTip("")
        self.y1_slider.setToolTipDuration(-1)
        self.y1_slider.setMaximum(610)
        self.y1_slider.setProperty("value", 610)
        self.y1_slider.setOrientation(QtCore.Qt.Vertical)
        self.y1_slider.setObjectName("y1_slider")
        self.gridLayout_2.addWidget(self.y1_slider, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(image_crop_dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.x1_slider = QtWidgets.QSlider(image_crop_dialog)
        self.x1_slider.setMaximum(610)
        self.x1_slider.setOrientation(QtCore.Qt.Horizontal)
        self.x1_slider.setObjectName("x1_slider")
        self.gridLayout_2.addWidget(self.x1_slider, 1, 2, 1, 1)
        self.x2_slider = QtWidgets.QSlider(image_crop_dialog)
        self.x2_slider.setMaximum(610)
        self.x2_slider.setProperty("value", 610)
        self.x2_slider.setOrientation(QtCore.Qt.Horizontal)
        self.x2_slider.setObjectName("x2_slider")
        self.gridLayout_2.addWidget(self.x2_slider, 5, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(image_crop_dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.y2_slider = QtWidgets.QSlider(image_crop_dialog)
        self.y2_slider.setMaximum(610)
        self.y2_slider.setOrientation(QtCore.Qt.Vertical)
        self.y2_slider.setObjectName("y2_slider")
        self.gridLayout_2.addWidget(self.y2_slider, 2, 3, 1, 1)
        self.gridFrame = QtWidgets.QFrame(image_crop_dialog)
        self.gridFrame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.image_label = QtWidgets.QLabel(self.gridFrame)
        self.image_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.gridLayout.addWidget(self.image_label, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.gridFrame, 2, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.crop_btn = QtWidgets.QPushButton(image_crop_dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.crop_btn.setFont(font)
        self.crop_btn.setIcon(icon)
        self.crop_btn.setIconSize(QtCore.QSize(35, 35))
        self.crop_btn.setObjectName("crop_btn")
        self.horizontalLayout.addWidget(self.crop_btn)
        self.detect_btn = QtWidgets.QPushButton(image_crop_dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.detect_btn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/detect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.detect_btn.setIcon(icon1)
        self.detect_btn.setIconSize(QtCore.QSize(35, 35))
        self.detect_btn.setObjectName("detect_btn")
        self.horizontalLayout.addWidget(self.detect_btn)
        self.cancel_btn = QtWidgets.QPushButton(image_crop_dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancel_btn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_btn.setIcon(icon2)
        self.cancel_btn.setIconSize(QtCore.QSize(35, 35))
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(image_crop_dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 2, 1, 1)
        self.gridLayout_2.setRowStretch(2, 11)

        self.retranslateUi(image_crop_dialog)
        self.cancel_btn.clicked.connect(image_crop_dialog.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(image_crop_dialog)

    def retranslateUi(self, image_crop_dialog):
        _translate = QtCore.QCoreApplication.translate
        image_crop_dialog.setWindowTitle(_translate("image_crop_dialog", "Crop the Image Exactly on the Puzzle"))
        self.label_5.setText(_translate("image_crop_dialog", "Y End"))
        self.label_2.setText(_translate("image_crop_dialog", "X Start"))
        self.label_4.setText(_translate("image_crop_dialog", "Y Start"))
        self.crop_btn.setText(_translate("image_crop_dialog", "Crop"))
        self.detect_btn.setText(_translate("image_crop_dialog", "Detect"))
        self.cancel_btn.setText(_translate("image_crop_dialog", "Cancel"))
        self.label_3.setText(_translate("image_crop_dialog", "X End"))


class Ui_PuzzleEdit:
    def setupUi(self, PuzzleEdit):
        PuzzleEdit.setObjectName("PuzzleEdit")
        PuzzleEdit.resize(1513, 846)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI Files\\../Icons/window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PuzzleEdit.setWindowIcon(icon)
        self.gridLayout_3 = QtWidgets.QGridLayout(PuzzleEdit)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridFrame_2 = QtWidgets.QFrame(PuzzleEdit)
        self.gridFrame_2.setMinimumSize(QtCore.QSize(742, 742))
        self.gridFrame_2.setMaximumSize(QtCore.QSize(742, 742))
        self.gridFrame_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.gridFrame_2.setObjectName("gridFrame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridFrame_2)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setHorizontalSpacing(7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.image_label = QtWidgets.QLabel(self.gridFrame_2)
        self.image_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.gridLayout_2.addWidget(self.image_label, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.gridFrame_2, 1, 1, 1, 1)
        self.gridFrame = QtWidgets.QFrame(PuzzleEdit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridFrame.sizePolicy().hasHeightForWidth())
        self.gridFrame.setSizePolicy(sizePolicy)
        self.gridFrame.setMinimumSize(QtCore.QSize(742, 742))
        self.gridFrame.setMaximumSize(QtCore.QSize(742, 742))
        self.gridFrame.setStyleSheet("border-image:transparent;\n"
                                     "background-color: rgb(0, 0, 0);")
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.line15 = QtWidgets.QLineEdit(self.gridFrame)
        self.line15.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line15.setFont(font)
        self.line15.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line15.setMaxLength(1)
        self.line15.setAlignment(QtCore.Qt.AlignCenter)
        self.line15.setObjectName("line15")
        self.gridLayout.addWidget(self.line15, 1, 6, 1, 1)
        self.line16 = QtWidgets.QLineEdit(self.gridFrame)
        self.line16.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line16.setFont(font)
        self.line16.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line16.setMaxLength(1)
        self.line16.setAlignment(QtCore.Qt.AlignCenter)
        self.line16.setReadOnly(False)
        self.line16.setObjectName("line16")
        self.gridLayout.addWidget(self.line16, 1, 8, 1, 1)
        self.line13 = QtWidgets.QLineEdit(self.gridFrame)
        self.line13.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line13.setFont(font)
        self.line13.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line13.setMaxLength(1)
        self.line13.setAlignment(QtCore.Qt.AlignCenter)
        self.line13.setObjectName("line13")
        self.gridLayout.addWidget(self.line13, 1, 4, 1, 1)
        self.line14 = QtWidgets.QLineEdit(self.gridFrame)
        self.line14.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line14.setFont(font)
        self.line14.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line14.setMaxLength(1)
        self.line14.setAlignment(QtCore.Qt.AlignCenter)
        self.line14.setObjectName("line14")
        self.gridLayout.addWidget(self.line14, 1, 5, 1, 1)
        self.line23 = QtWidgets.QLineEdit(self.gridFrame)
        self.line23.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line23.setFont(font)
        self.line23.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line23.setMaxLength(1)
        self.line23.setAlignment(QtCore.Qt.AlignCenter)
        self.line23.setObjectName("line23")
        self.gridLayout.addWidget(self.line23, 2, 5, 1, 1)
        self.line22 = QtWidgets.QLineEdit(self.gridFrame)
        self.line22.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line22.setFont(font)
        self.line22.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line22.setMaxLength(1)
        self.line22.setAlignment(QtCore.Qt.AlignCenter)
        self.line22.setObjectName("line22")
        self.gridLayout.addWidget(self.line22, 2, 4, 1, 1)
        self.line17 = QtWidgets.QLineEdit(self.gridFrame)
        self.line17.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line17.setFont(font)
        self.line17.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line17.setMaxLength(1)
        self.line17.setAlignment(QtCore.Qt.AlignCenter)
        self.line17.setObjectName("line17")
        self.gridLayout.addWidget(self.line17, 1, 9, 1, 1)
        self.line21 = QtWidgets.QLineEdit(self.gridFrame)
        self.line21.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line21.setFont(font)
        self.line21.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line21.setMaxLength(1)
        self.line21.setAlignment(QtCore.Qt.AlignCenter)
        self.line21.setObjectName("line21")
        self.gridLayout.addWidget(self.line21, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(2, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 7, 1, 1)
        self.line20 = QtWidgets.QLineEdit(self.gridFrame)
        self.line20.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line20.setFont(font)
        self.line20.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line20.setMaxLength(1)
        self.line20.setAlignment(QtCore.Qt.AlignCenter)
        self.line20.setObjectName("line20")
        self.gridLayout.addWidget(self.line20, 2, 1, 1, 1)
        self.line18 = QtWidgets.QLineEdit(self.gridFrame)
        self.line18.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line18.setFont(font)
        self.line18.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line18.setMaxLength(1)
        self.line18.setAlignment(QtCore.Qt.AlignCenter)
        self.line18.setObjectName("line18")
        self.gridLayout.addWidget(self.line18, 1, 10, 1, 1)
        self.line19 = QtWidgets.QLineEdit(self.gridFrame)
        self.line19.setMinimumSize(QtCore.QSize(80, 80))
        self.line19.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line19.setFont(font)
        self.line19.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line19.setMaxLength(1)
        self.line19.setAlignment(QtCore.Qt.AlignCenter)
        self.line19.setObjectName("line19")
        self.gridLayout.addWidget(self.line19, 2, 0, 1, 1)
        self.line24 = QtWidgets.QLineEdit(self.gridFrame)
        self.line24.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line24.setFont(font)
        self.line24.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line24.setMaxLength(1)
        self.line24.setAlignment(QtCore.Qt.AlignCenter)
        self.line24.setObjectName("line24")
        self.gridLayout.addWidget(self.line24, 2, 6, 1, 1)
        self.line57 = QtWidgets.QLineEdit(self.gridFrame)
        self.line57.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line57.setFont(font)
        self.line57.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line57.setMaxLength(1)
        self.line57.setAlignment(QtCore.Qt.AlignCenter)
        self.line57.setObjectName("line57")
        self.gridLayout.addWidget(self.line57, 8, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(2, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.line43 = QtWidgets.QLineEdit(self.gridFrame)
        self.line43.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line43.setFont(font)
        self.line43.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line43.setMaxLength(1)
        self.line43.setAlignment(QtCore.Qt.AlignCenter)
        self.line43.setObjectName("line43")
        self.gridLayout.addWidget(self.line43, 5, 8, 1, 1)
        self.line45 = QtWidgets.QLineEdit(self.gridFrame)
        self.line45.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line45.setFont(font)
        self.line45.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line45.setMaxLength(1)
        self.line45.setAlignment(QtCore.Qt.AlignCenter)
        self.line45.setObjectName("line45")
        self.gridLayout.addWidget(self.line45, 5, 10, 1, 1)
        self.line26 = QtWidgets.QLineEdit(self.gridFrame)
        self.line26.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line26.setFont(font)
        self.line26.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line26.setMaxLength(1)
        self.line26.setAlignment(QtCore.Qt.AlignCenter)
        self.line26.setObjectName("line26")
        self.gridLayout.addWidget(self.line26, 2, 9, 1, 1)
        self.line42 = QtWidgets.QLineEdit(self.gridFrame)
        self.line42.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line42.setFont(font)
        self.line42.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line42.setMaxLength(1)
        self.line42.setAlignment(QtCore.Qt.AlignCenter)
        self.line42.setObjectName("line42")
        self.gridLayout.addWidget(self.line42, 5, 6, 1, 1)
        self.line48 = QtWidgets.QLineEdit(self.gridFrame)
        self.line48.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line48.setFont(font)
        self.line48.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line48.setMaxLength(1)
        self.line48.setAlignment(QtCore.Qt.AlignCenter)
        self.line48.setObjectName("line48")
        self.gridLayout.addWidget(self.line48, 6, 2, 1, 1)
        self.line25 = QtWidgets.QLineEdit(self.gridFrame)
        self.line25.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line25.setFont(font)
        self.line25.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line25.setMaxLength(1)
        self.line25.setAlignment(QtCore.Qt.AlignCenter)
        self.line25.setObjectName("line25")
        self.gridLayout.addWidget(self.line25, 2, 8, 1, 1)
        self.line47 = QtWidgets.QLineEdit(self.gridFrame)
        self.line47.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line47.setFont(font)
        self.line47.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line47.setMaxLength(1)
        self.line47.setAlignment(QtCore.Qt.AlignCenter)
        self.line47.setObjectName("line47")
        self.gridLayout.addWidget(self.line47, 6, 1, 1, 1)
        self.line49 = QtWidgets.QLineEdit(self.gridFrame)
        self.line49.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line49.setFont(font)
        self.line49.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}background-color: rgb(255, 255, 255);")
        self.line49.setMaxLength(1)
        self.line49.setAlignment(QtCore.Qt.AlignCenter)
        self.line49.setObjectName("line49")
        self.gridLayout.addWidget(self.line49, 6, 4, 1, 1)
        self.line33 = QtWidgets.QLineEdit(self.gridFrame)
        self.line33.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line33.setFont(font)
        self.line33.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line33.setMaxLength(1)
        self.line33.setAlignment(QtCore.Qt.AlignCenter)
        self.line33.setObjectName("line33")
        self.gridLayout.addWidget(self.line33, 4, 6, 1, 1)
        self.line51 = QtWidgets.QLineEdit(self.gridFrame)
        self.line51.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line51.setFont(font)
        self.line51.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line51.setMaxLength(1)
        self.line51.setAlignment(QtCore.Qt.AlignCenter)
        self.line51.setObjectName("line51")
        self.gridLayout.addWidget(self.line51, 6, 6, 1, 1)
        self.line50 = QtWidgets.QLineEdit(self.gridFrame)
        self.line50.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line50.setFont(font)
        self.line50.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line50.setMaxLength(1)
        self.line50.setAlignment(QtCore.Qt.AlignCenter)
        self.line50.setObjectName("line50")
        self.gridLayout.addWidget(self.line50, 6, 5, 1, 1)
        self.line29 = QtWidgets.QLineEdit(self.gridFrame)
        self.line29.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line29.setFont(font)
        self.line29.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line29.setMaxLength(1)
        self.line29.setAlignment(QtCore.Qt.AlignCenter)
        self.line29.setObjectName("line29")
        self.gridLayout.addWidget(self.line29, 4, 1, 1, 1)
        self.line34 = QtWidgets.QLineEdit(self.gridFrame)
        self.line34.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line34.setFont(font)
        self.line34.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line34.setMaxLength(1)
        self.line34.setAlignment(QtCore.Qt.AlignCenter)
        self.line34.setObjectName("line34")
        self.gridLayout.addWidget(self.line34, 4, 8, 1, 1)
        self.line28 = QtWidgets.QLineEdit(self.gridFrame)
        self.line28.setMinimumSize(QtCore.QSize(80, 80))
        self.line28.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line28.setFont(font)
        self.line28.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line28.setMaxLength(1)
        self.line28.setAlignment(QtCore.Qt.AlignCenter)
        self.line28.setObjectName("line28")
        self.gridLayout.addWidget(self.line28, 4, 0, 1, 1)
        self.line52 = QtWidgets.QLineEdit(self.gridFrame)
        self.line52.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line52.setFont(font)
        self.line52.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line52.setMaxLength(1)
        self.line52.setAlignment(QtCore.Qt.AlignCenter)
        self.line52.setObjectName("line52")
        self.gridLayout.addWidget(self.line52, 6, 8, 1, 1)
        self.line53 = QtWidgets.QLineEdit(self.gridFrame)
        self.line53.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line53.setFont(font)
        self.line53.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line53.setMaxLength(1)
        self.line53.setAlignment(QtCore.Qt.AlignCenter)
        self.line53.setObjectName("line53")
        self.gridLayout.addWidget(self.line53, 6, 9, 1, 1)
        self.line44 = QtWidgets.QLineEdit(self.gridFrame)
        self.line44.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line44.setFont(font)
        self.line44.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line44.setMaxLength(1)
        self.line44.setAlignment(QtCore.Qt.AlignCenter)
        self.line44.setObjectName("line44")
        self.gridLayout.addWidget(self.line44, 5, 9, 1, 1)
        self.line39 = QtWidgets.QLineEdit(self.gridFrame)
        self.line39.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line39.setFont(font)
        self.line39.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line39.setMaxLength(1)
        self.line39.setAlignment(QtCore.Qt.AlignCenter)
        self.line39.setObjectName("line39")
        self.gridLayout.addWidget(self.line39, 5, 2, 1, 1)
        self.line46 = QtWidgets.QLineEdit(self.gridFrame)
        self.line46.setMinimumSize(QtCore.QSize(80, 80))
        self.line46.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line46.setFont(font)
        self.line46.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line46.setMaxLength(1)
        self.line46.setAlignment(QtCore.Qt.AlignCenter)
        self.line46.setObjectName("line46")
        self.gridLayout.addWidget(self.line46, 6, 0, 1, 1)
        self.line35 = QtWidgets.QLineEdit(self.gridFrame)
        self.line35.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line35.setFont(font)
        self.line35.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line35.setMaxLength(1)
        self.line35.setAlignment(QtCore.Qt.AlignCenter)
        self.line35.setObjectName("line35")
        self.gridLayout.addWidget(self.line35, 4, 9, 1, 1)
        self.line4 = QtWidgets.QLineEdit(self.gridFrame)
        self.line4.setMinimumSize(QtCore.QSize(80, 80))
        self.line4.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line4.setFont(font)
        self.line4.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line4.setMaxLength(1)
        self.line4.setAlignment(QtCore.Qt.AlignCenter)
        self.line4.setObjectName("line4")
        self.gridLayout.addWidget(self.line4, 0, 4, 1, 1)
        self.line11 = QtWidgets.QLineEdit(self.gridFrame)
        self.line11.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line11.setFont(font)
        self.line11.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line11.setMaxLength(1)
        self.line11.setAlignment(QtCore.Qt.AlignCenter)
        self.line11.setObjectName("line11")
        self.gridLayout.addWidget(self.line11, 1, 1, 1, 1)
        self.line3 = QtWidgets.QLineEdit(self.gridFrame)
        self.line3.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line3.setFont(font)
        self.line3.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line3.setMaxLength(1)
        self.line3.setAlignment(QtCore.Qt.AlignCenter)
        self.line3.setObjectName("line3")
        self.gridLayout.addWidget(self.line3, 0, 2, 1, 1)
        self.line2 = QtWidgets.QLineEdit(self.gridFrame)
        self.line2.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line2.setFont(font)
        self.line2.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line2.setMaxLength(1)
        self.line2.setAlignment(QtCore.Qt.AlignCenter)
        self.line2.setObjectName("line2")
        self.gridLayout.addWidget(self.line2, 0, 1, 1, 1)
        self.line7 = QtWidgets.QLineEdit(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line7.sizePolicy().hasHeightForWidth())
        self.line7.setSizePolicy(sizePolicy)
        self.line7.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line7.setFont(font)
        self.line7.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line7.setMaxLength(1)
        self.line7.setAlignment(QtCore.Qt.AlignCenter)
        self.line7.setReadOnly(False)
        self.line7.setObjectName("line7")
        self.gridLayout.addWidget(self.line7, 0, 8, 1, 1)
        self.line5 = QtWidgets.QLineEdit(self.gridFrame)
        self.line5.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line5.setFont(font)
        self.line5.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line5.setMaxLength(1)
        self.line5.setAlignment(QtCore.Qt.AlignCenter)
        self.line5.setObjectName("line5")
        self.gridLayout.addWidget(self.line5, 0, 5, 1, 1)
        self.line6 = QtWidgets.QLineEdit(self.gridFrame)
        self.line6.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line6.setFont(font)
        self.line6.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line6.setMaxLength(1)
        self.line6.setAlignment(QtCore.Qt.AlignCenter)
        self.line6.setObjectName("line6")
        self.gridLayout.addWidget(self.line6, 0, 6, 1, 1)
        self.line8 = QtWidgets.QLineEdit(self.gridFrame)
        self.line8.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line8.setFont(font)
        self.line8.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line8.setMaxLength(1)
        self.line8.setAlignment(QtCore.Qt.AlignCenter)
        self.line8.setObjectName("line8")
        self.gridLayout.addWidget(self.line8, 0, 9, 1, 1)
        self.line10 = QtWidgets.QLineEdit(self.gridFrame)
        self.line10.setMinimumSize(QtCore.QSize(80, 80))
        self.line10.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line10.setFont(font)
        self.line10.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line10.setMaxLength(1)
        self.line10.setAlignment(QtCore.Qt.AlignCenter)
        self.line10.setObjectName("line10")
        self.gridLayout.addWidget(self.line10, 1, 0, 1, 1)
        self.line9 = QtWidgets.QLineEdit(self.gridFrame)
        self.line9.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line9.setFont(font)
        self.line9.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line9.setMaxLength(1)
        self.line9.setAlignment(QtCore.Qt.AlignCenter)
        self.line9.setObjectName("line9")
        self.gridLayout.addWidget(self.line9, 0, 10, 1, 1)
        self.line12 = QtWidgets.QLineEdit(self.gridFrame)
        self.line12.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line12.setFont(font)
        self.line12.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line12.setMaxLength(1)
        self.line12.setAlignment(QtCore.Qt.AlignCenter)
        self.line12.setObjectName("line12")
        self.gridLayout.addWidget(self.line12, 1, 2, 1, 1)
        self.line59 = QtWidgets.QLineEdit(self.gridFrame)
        self.line59.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line59.setFont(font)
        self.line59.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line59.setMaxLength(1)
        self.line59.setAlignment(QtCore.Qt.AlignCenter)
        self.line59.setObjectName("line59")
        self.gridLayout.addWidget(self.line59, 8, 5, 1, 1)
        self.line64 = QtWidgets.QLineEdit(self.gridFrame)
        self.line64.setMinimumSize(QtCore.QSize(80, 80))
        self.line64.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line64.setFont(font)
        self.line64.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line64.setMaxLength(1)
        self.line64.setAlignment(QtCore.Qt.AlignCenter)
        self.line64.setObjectName("line64")
        self.gridLayout.addWidget(self.line64, 9, 0, 1, 1)
        self.line79 = QtWidgets.QLineEdit(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line79.sizePolicy().hasHeightForWidth())
        self.line79.setSizePolicy(sizePolicy)
        self.line79.setMinimumSize(QtCore.QSize(80, 80))
        self.line79.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line79.setFont(font)
        self.line79.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line79.setMaxLength(1)
        self.line79.setAlignment(QtCore.Qt.AlignCenter)
        self.line79.setObjectName("line79")
        self.gridLayout.addWidget(self.line79, 10, 8, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        self.line75 = QtWidgets.QLineEdit(self.gridFrame)
        self.line75.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line75.setFont(font)
        self.line75.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line75.setMaxLength(1)
        self.line75.setAlignment(QtCore.Qt.AlignCenter)
        self.line75.setObjectName("line75")
        self.gridLayout.addWidget(self.line75, 10, 2, 1, 1)
        self.line63 = QtWidgets.QLineEdit(self.gridFrame)
        self.line63.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line63.setFont(font)
        self.line63.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line63.setMaxLength(1)
        self.line63.setAlignment(QtCore.Qt.AlignCenter)
        self.line63.setObjectName("line63")
        self.gridLayout.addWidget(self.line63, 8, 10, 1, 1)
        self.line61 = QtWidgets.QLineEdit(self.gridFrame)
        self.line61.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line61.setFont(font)
        self.line61.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line61.setMaxLength(1)
        self.line61.setAlignment(QtCore.Qt.AlignCenter)
        self.line61.setObjectName("line61")
        self.gridLayout.addWidget(self.line61, 8, 8, 1, 1)
        self.line74 = QtWidgets.QLineEdit(self.gridFrame)
        self.line74.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line74.setFont(font)
        self.line74.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line74.setMaxLength(1)
        self.line74.setAlignment(QtCore.Qt.AlignCenter)
        self.line74.setObjectName("line74")
        self.gridLayout.addWidget(self.line74, 10, 1, 1, 1)
        self.line81 = QtWidgets.QLineEdit(self.gridFrame)
        self.line81.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line81.setFont(font)
        self.line81.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line81.setMaxLength(1)
        self.line81.setAlignment(QtCore.Qt.AlignCenter)
        self.line81.setObjectName("line81")
        self.gridLayout.addWidget(self.line81, 10, 10, 1, 1)
        self.line60 = QtWidgets.QLineEdit(self.gridFrame)
        self.line60.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line60.setFont(font)
        self.line60.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line60.setMaxLength(1)
        self.line60.setAlignment(QtCore.Qt.AlignCenter)
        self.line60.setObjectName("line60")
        self.gridLayout.addWidget(self.line60, 8, 6, 1, 1)
        self.line68 = QtWidgets.QLineEdit(self.gridFrame)
        self.line68.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line68.setFont(font)
        self.line68.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line68.setMaxLength(1)
        self.line68.setAlignment(QtCore.Qt.AlignCenter)
        self.line68.setObjectName("line68")
        self.gridLayout.addWidget(self.line68, 9, 5, 1, 1)
        self.line65 = QtWidgets.QLineEdit(self.gridFrame)
        self.line65.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line65.setFont(font)
        self.line65.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line65.setMaxLength(1)
        self.line65.setAlignment(QtCore.Qt.AlignCenter)
        self.line65.setObjectName("line65")
        self.gridLayout.addWidget(self.line65, 9, 1, 1, 1)
        self.line73 = QtWidgets.QLineEdit(self.gridFrame)
        self.line73.setMinimumSize(QtCore.QSize(80, 80))
        self.line73.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line73.setFont(font)
        self.line73.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line73.setMaxLength(1)
        self.line73.setAlignment(QtCore.Qt.AlignCenter)
        self.line73.setObjectName("line73")
        self.gridLayout.addWidget(self.line73, 10, 0, 1, 1)
        self.line72 = QtWidgets.QLineEdit(self.gridFrame)
        self.line72.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line72.setFont(font)
        self.line72.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line72.setMaxLength(1)
        self.line72.setAlignment(QtCore.Qt.AlignCenter)
        self.line72.setObjectName("line72")
        self.gridLayout.addWidget(self.line72, 9, 10, 1, 1)
        self.line76 = QtWidgets.QLineEdit(self.gridFrame)
        self.line76.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line76.setFont(font)
        self.line76.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line76.setMaxLength(1)
        self.line76.setAlignment(QtCore.Qt.AlignCenter)
        self.line76.setObjectName("line76")
        self.gridLayout.addWidget(self.line76, 10, 4, 1, 1)
        self.line80 = QtWidgets.QLineEdit(self.gridFrame)
        self.line80.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line80.setFont(font)
        self.line80.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line80.setMaxLength(1)
        self.line80.setAlignment(QtCore.Qt.AlignCenter)
        self.line80.setObjectName("line80")
        self.gridLayout.addWidget(self.line80, 10, 9, 1, 1)
        self.line62 = QtWidgets.QLineEdit(self.gridFrame)
        self.line62.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line62.setFont(font)
        self.line62.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line62.setMaxLength(1)
        self.line62.setAlignment(QtCore.Qt.AlignCenter)
        self.line62.setObjectName("line62")
        self.gridLayout.addWidget(self.line62, 8, 9, 1, 1)
        self.line56 = QtWidgets.QLineEdit(self.gridFrame)
        self.line56.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line56.setFont(font)
        self.line56.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line56.setMaxLength(1)
        self.line56.setAlignment(QtCore.Qt.AlignCenter)
        self.line56.setObjectName("line56")
        self.gridLayout.addWidget(self.line56, 8, 1, 1, 1)
        self.line70 = QtWidgets.QLineEdit(self.gridFrame)
        self.line70.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line70.setFont(font)
        self.line70.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line70.setMaxLength(1)
        self.line70.setAlignment(QtCore.Qt.AlignCenter)
        self.line70.setObjectName("line70")
        self.gridLayout.addWidget(self.line70, 9, 8, 1, 1)
        self.line58 = QtWidgets.QLineEdit(self.gridFrame)
        self.line58.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line58.setFont(font)
        self.line58.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line58.setMaxLength(1)
        self.line58.setAlignment(QtCore.Qt.AlignCenter)
        self.line58.setObjectName("line58")
        self.gridLayout.addWidget(self.line58, 8, 4, 1, 1)
        self.line77 = QtWidgets.QLineEdit(self.gridFrame)
        self.line77.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line77.setFont(font)
        self.line77.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line77.setMaxLength(1)
        self.line77.setAlignment(QtCore.Qt.AlignCenter)
        self.line77.setObjectName("line77")
        self.gridLayout.addWidget(self.line77, 10, 5, 1, 1)
        self.line54 = QtWidgets.QLineEdit(self.gridFrame)
        self.line54.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line54.setFont(font)
        self.line54.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line54.setMaxLength(1)
        self.line54.setAlignment(QtCore.Qt.AlignCenter)
        self.line54.setObjectName("line54")
        self.gridLayout.addWidget(self.line54, 6, 10, 1, 1)
        self.line67 = QtWidgets.QLineEdit(self.gridFrame)
        self.line67.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line67.setFont(font)
        self.line67.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line67.setMaxLength(1)
        self.line67.setAlignment(QtCore.Qt.AlignCenter)
        self.line67.setObjectName("line67")
        self.gridLayout.addWidget(self.line67, 9, 4, 1, 1)
        self.line66 = QtWidgets.QLineEdit(self.gridFrame)
        self.line66.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line66.setFont(font)
        self.line66.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line66.setMaxLength(1)
        self.line66.setAlignment(QtCore.Qt.AlignCenter)
        self.line66.setObjectName("line66")
        self.gridLayout.addWidget(self.line66, 9, 2, 1, 1)
        self.line55 = QtWidgets.QLineEdit(self.gridFrame)
        self.line55.setMinimumSize(QtCore.QSize(80, 80))
        self.line55.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line55.setFont(font)
        self.line55.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line55.setMaxLength(1)
        self.line55.setAlignment(QtCore.Qt.AlignCenter)
        self.line55.setObjectName("line55")
        self.gridLayout.addWidget(self.line55, 8, 0, 1, 1)
        self.line71 = QtWidgets.QLineEdit(self.gridFrame)
        self.line71.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line71.setFont(font)
        self.line71.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line71.setMaxLength(1)
        self.line71.setAlignment(QtCore.Qt.AlignCenter)
        self.line71.setObjectName("line71")
        self.gridLayout.addWidget(self.line71, 9, 9, 1, 1)
        self.line78 = QtWidgets.QLineEdit(self.gridFrame)
        self.line78.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line78.setFont(font)
        self.line78.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line78.setMaxLength(1)
        self.line78.setAlignment(QtCore.Qt.AlignCenter)
        self.line78.setObjectName("line78")
        self.gridLayout.addWidget(self.line78, 10, 6, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem3, 7, 0, 1, 1)
        self.line69 = QtWidgets.QLineEdit(self.gridFrame)
        self.line69.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line69.setFont(font)
        self.line69.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line69.setMaxLength(1)
        self.line69.setAlignment(QtCore.Qt.AlignCenter)
        self.line69.setObjectName("line69")
        self.gridLayout.addWidget(self.line69, 9, 6, 1, 1)
        self.line31 = QtWidgets.QLineEdit(self.gridFrame)
        self.line31.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line31.setFont(font)
        self.line31.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line31.setMaxLength(1)
        self.line31.setAlignment(QtCore.Qt.AlignCenter)
        self.line31.setObjectName("line31")
        self.gridLayout.addWidget(self.line31, 4, 4, 1, 1)
        self.line37 = QtWidgets.QLineEdit(self.gridFrame)
        self.line37.setMinimumSize(QtCore.QSize(80, 80))
        self.line37.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line37.setFont(font)
        self.line37.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line37.setMaxLength(1)
        self.line37.setAlignment(QtCore.Qt.AlignCenter)
        self.line37.setObjectName("line37")
        self.gridLayout.addWidget(self.line37, 5, 0, 1, 1)
        self.line38 = QtWidgets.QLineEdit(self.gridFrame)
        self.line38.setMinimumSize(QtCore.QSize(80, 80))
        self.line38.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line38.setFont(font)
        self.line38.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line38.setMaxLength(1)
        self.line38.setAlignment(QtCore.Qt.AlignCenter)
        self.line38.setObjectName("line38")
        self.gridLayout.addWidget(self.line38, 5, 1, 1, 1)
        self.line1 = QtWidgets.QLineEdit(self.gridFrame)
        self.line1.setEnabled(True)
        self.line1.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line1.setFont(font)
        self.line1.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line1.setMaxLength(1)
        self.line1.setAlignment(QtCore.Qt.AlignCenter)
        self.line1.setReadOnly(False)
        self.line1.setObjectName("line1")
        self.gridLayout.addWidget(self.line1, 0, 0, 1, 1)
        self.line30 = QtWidgets.QLineEdit(self.gridFrame)
        self.line30.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line30.setFont(font)
        self.line30.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line30.setMaxLength(1)
        self.line30.setAlignment(QtCore.Qt.AlignCenter)
        self.line30.setObjectName("line30")
        self.gridLayout.addWidget(self.line30, 4, 2, 1, 1)
        self.line40 = QtWidgets.QLineEdit(self.gridFrame)
        self.line40.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line40.setFont(font)
        self.line40.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line40.setMaxLength(1)
        self.line40.setAlignment(QtCore.Qt.AlignCenter)
        self.line40.setObjectName("line40")
        self.gridLayout.addWidget(self.line40, 5, 4, 1, 1)
        self.line36 = QtWidgets.QLineEdit(self.gridFrame)
        self.line36.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line36.setFont(font)
        self.line36.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line36.setMaxLength(1)
        self.line36.setAlignment(QtCore.Qt.AlignCenter)
        self.line36.setObjectName("line36")
        self.gridLayout.addWidget(self.line36, 4, 10, 1, 1)
        self.line41 = QtWidgets.QLineEdit(self.gridFrame)
        self.line41.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line41.setFont(font)
        self.line41.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line41.setMaxLength(1)
        self.line41.setAlignment(QtCore.Qt.AlignCenter)
        self.line41.setObjectName("line41")
        self.gridLayout.addWidget(self.line41, 5, 5, 1, 1)
        self.line32 = QtWidgets.QLineEdit(self.gridFrame)
        self.line32.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line32.setFont(font)
        self.line32.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line32.setMaxLength(1)
        self.line32.setAlignment(QtCore.Qt.AlignCenter)
        self.line32.setObjectName("line32")
        self.gridLayout.addWidget(self.line32, 4, 5, 1, 1)
        self.line27 = QtWidgets.QLineEdit(self.gridFrame)
        self.line27.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line27.setFont(font)
        self.line27.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line27.setMaxLength(1)
        self.line27.setAlignment(QtCore.Qt.AlignCenter)
        self.line27.setObjectName("line27")
        self.gridLayout.addWidget(self.line27, 2, 10, 1, 1)
        self.gridLayout_3.addWidget(self.gridFrame, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(PuzzleEdit)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(PuzzleEdit)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(PuzzleEdit)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(PuzzleEdit)
        self.buttonBox.accepted.connect(PuzzleEdit.accept)  # type: ignore
        self.buttonBox.rejected.connect(PuzzleEdit.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(PuzzleEdit)

    def retranslateUi(self, PuzzleEdit):
        _translate = QtCore.QCoreApplication.translate
        PuzzleEdit.setWindowTitle(_translate("PuzzleEdit", "Puzzle Edit"))
        self.label_2.setText(_translate("PuzzleEdit", "Puzzle"))
        self.label.setText(_translate("PuzzleEdit", "Image"))


class Ui_PuzzleEntry:
    def setupUi(self, PuzzleEntry):
        PuzzleEntry.setObjectName("PuzzleEntry")
        PuzzleEntry.resize(861, 837)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI Files\\../Icons/window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PuzzleEntry.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(PuzzleEntry)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(PuzzleEntry)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 3, 1, 1, 1)
        self.gridFrame = QtWidgets.QFrame(PuzzleEntry)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridFrame.sizePolicy().hasHeightForWidth())
        self.gridFrame.setSizePolicy(sizePolicy)
        self.gridFrame.setMinimumSize(QtCore.QSize(742, 742))
        self.gridFrame.setMaximumSize(QtCore.QSize(742, 742))
        self.gridFrame.setStyleSheet("border-image:transparent;\n"
                                     "background-color: rgb(0, 0, 0);")
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.line15 = QtWidgets.QLineEdit(self.gridFrame)
        self.line15.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line15.setFont(font)
        self.line15.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line15.setMaxLength(1)
        self.line15.setAlignment(QtCore.Qt.AlignCenter)
        self.line15.setObjectName("line15")
        self.gridLayout.addWidget(self.line15, 1, 6, 1, 1)
        self.line16 = QtWidgets.QLineEdit(self.gridFrame)
        self.line16.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line16.setFont(font)
        self.line16.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line16.setMaxLength(1)
        self.line16.setAlignment(QtCore.Qt.AlignCenter)
        self.line16.setReadOnly(False)
        self.line16.setObjectName("line16")
        self.gridLayout.addWidget(self.line16, 1, 8, 1, 1)
        self.line13 = QtWidgets.QLineEdit(self.gridFrame)
        self.line13.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line13.setFont(font)
        self.line13.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line13.setMaxLength(1)
        self.line13.setAlignment(QtCore.Qt.AlignCenter)
        self.line13.setObjectName("line13")
        self.gridLayout.addWidget(self.line13, 1, 4, 1, 1)
        self.line14 = QtWidgets.QLineEdit(self.gridFrame)
        self.line14.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line14.setFont(font)
        self.line14.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line14.setMaxLength(1)
        self.line14.setAlignment(QtCore.Qt.AlignCenter)
        self.line14.setObjectName("line14")
        self.gridLayout.addWidget(self.line14, 1, 5, 1, 1)
        self.line23 = QtWidgets.QLineEdit(self.gridFrame)
        self.line23.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line23.setFont(font)
        self.line23.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line23.setMaxLength(1)
        self.line23.setAlignment(QtCore.Qt.AlignCenter)
        self.line23.setObjectName("line23")
        self.gridLayout.addWidget(self.line23, 2, 5, 1, 1)
        self.line22 = QtWidgets.QLineEdit(self.gridFrame)
        self.line22.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line22.setFont(font)
        self.line22.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line22.setMaxLength(1)
        self.line22.setAlignment(QtCore.Qt.AlignCenter)
        self.line22.setObjectName("line22")
        self.gridLayout.addWidget(self.line22, 2, 4, 1, 1)
        self.line17 = QtWidgets.QLineEdit(self.gridFrame)
        self.line17.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line17.setFont(font)
        self.line17.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line17.setMaxLength(1)
        self.line17.setAlignment(QtCore.Qt.AlignCenter)
        self.line17.setObjectName("line17")
        self.gridLayout.addWidget(self.line17, 1, 9, 1, 1)
        self.line21 = QtWidgets.QLineEdit(self.gridFrame)
        self.line21.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line21.setFont(font)
        self.line21.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line21.setMaxLength(1)
        self.line21.setAlignment(QtCore.Qt.AlignCenter)
        self.line21.setObjectName("line21")
        self.gridLayout.addWidget(self.line21, 2, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(2, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 7, 1, 1)
        self.line20 = QtWidgets.QLineEdit(self.gridFrame)
        self.line20.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line20.setFont(font)
        self.line20.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line20.setMaxLength(1)
        self.line20.setAlignment(QtCore.Qt.AlignCenter)
        self.line20.setObjectName("line20")
        self.gridLayout.addWidget(self.line20, 2, 1, 1, 1)
        self.line18 = QtWidgets.QLineEdit(self.gridFrame)
        self.line18.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line18.setFont(font)
        self.line18.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line18.setMaxLength(1)
        self.line18.setAlignment(QtCore.Qt.AlignCenter)
        self.line18.setObjectName("line18")
        self.gridLayout.addWidget(self.line18, 1, 10, 1, 1)
        self.line19 = QtWidgets.QLineEdit(self.gridFrame)
        self.line19.setMinimumSize(QtCore.QSize(80, 80))
        self.line19.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line19.setFont(font)
        self.line19.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line19.setMaxLength(1)
        self.line19.setAlignment(QtCore.Qt.AlignCenter)
        self.line19.setObjectName("line19")
        self.gridLayout.addWidget(self.line19, 2, 0, 1, 1)
        self.line24 = QtWidgets.QLineEdit(self.gridFrame)
        self.line24.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line24.setFont(font)
        self.line24.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line24.setMaxLength(1)
        self.line24.setAlignment(QtCore.Qt.AlignCenter)
        self.line24.setObjectName("line24")
        self.gridLayout.addWidget(self.line24, 2, 6, 1, 1)
        self.line57 = QtWidgets.QLineEdit(self.gridFrame)
        self.line57.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line57.setFont(font)
        self.line57.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line57.setMaxLength(1)
        self.line57.setAlignment(QtCore.Qt.AlignCenter)
        self.line57.setObjectName("line57")
        self.gridLayout.addWidget(self.line57, 8, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(2, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 3, 1, 1)
        self.line43 = QtWidgets.QLineEdit(self.gridFrame)
        self.line43.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line43.setFont(font)
        self.line43.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line43.setMaxLength(1)
        self.line43.setAlignment(QtCore.Qt.AlignCenter)
        self.line43.setObjectName("line43")
        self.gridLayout.addWidget(self.line43, 5, 8, 1, 1)
        self.line45 = QtWidgets.QLineEdit(self.gridFrame)
        self.line45.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line45.setFont(font)
        self.line45.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line45.setMaxLength(1)
        self.line45.setAlignment(QtCore.Qt.AlignCenter)
        self.line45.setObjectName("line45")
        self.gridLayout.addWidget(self.line45, 5, 10, 1, 1)
        self.line26 = QtWidgets.QLineEdit(self.gridFrame)
        self.line26.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line26.setFont(font)
        self.line26.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line26.setMaxLength(1)
        self.line26.setAlignment(QtCore.Qt.AlignCenter)
        self.line26.setObjectName("line26")
        self.gridLayout.addWidget(self.line26, 2, 9, 1, 1)
        self.line42 = QtWidgets.QLineEdit(self.gridFrame)
        self.line42.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line42.setFont(font)
        self.line42.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line42.setMaxLength(1)
        self.line42.setAlignment(QtCore.Qt.AlignCenter)
        self.line42.setObjectName("line42")
        self.gridLayout.addWidget(self.line42, 5, 6, 1, 1)
        self.line48 = QtWidgets.QLineEdit(self.gridFrame)
        self.line48.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line48.setFont(font)
        self.line48.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line48.setMaxLength(1)
        self.line48.setAlignment(QtCore.Qt.AlignCenter)
        self.line48.setObjectName("line48")
        self.gridLayout.addWidget(self.line48, 6, 2, 1, 1)
        self.line25 = QtWidgets.QLineEdit(self.gridFrame)
        self.line25.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line25.setFont(font)
        self.line25.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line25.setMaxLength(1)
        self.line25.setAlignment(QtCore.Qt.AlignCenter)
        self.line25.setObjectName("line25")
        self.gridLayout.addWidget(self.line25, 2, 8, 1, 1)
        self.line47 = QtWidgets.QLineEdit(self.gridFrame)
        self.line47.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line47.setFont(font)
        self.line47.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line47.setMaxLength(1)
        self.line47.setAlignment(QtCore.Qt.AlignCenter)
        self.line47.setObjectName("line47")
        self.gridLayout.addWidget(self.line47, 6, 1, 1, 1)
        self.line49 = QtWidgets.QLineEdit(self.gridFrame)
        self.line49.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line49.setFont(font)
        self.line49.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}background-color: rgb(255, 255, 255);")
        self.line49.setMaxLength(1)
        self.line49.setAlignment(QtCore.Qt.AlignCenter)
        self.line49.setObjectName("line49")
        self.gridLayout.addWidget(self.line49, 6, 4, 1, 1)
        self.line33 = QtWidgets.QLineEdit(self.gridFrame)
        self.line33.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line33.setFont(font)
        self.line33.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line33.setMaxLength(1)
        self.line33.setAlignment(QtCore.Qt.AlignCenter)
        self.line33.setObjectName("line33")
        self.gridLayout.addWidget(self.line33, 4, 6, 1, 1)
        self.line51 = QtWidgets.QLineEdit(self.gridFrame)
        self.line51.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line51.setFont(font)
        self.line51.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line51.setMaxLength(1)
        self.line51.setAlignment(QtCore.Qt.AlignCenter)
        self.line51.setObjectName("line51")
        self.gridLayout.addWidget(self.line51, 6, 6, 1, 1)
        self.line50 = QtWidgets.QLineEdit(self.gridFrame)
        self.line50.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line50.setFont(font)
        self.line50.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line50.setMaxLength(1)
        self.line50.setAlignment(QtCore.Qt.AlignCenter)
        self.line50.setObjectName("line50")
        self.gridLayout.addWidget(self.line50, 6, 5, 1, 1)
        self.line29 = QtWidgets.QLineEdit(self.gridFrame)
        self.line29.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line29.setFont(font)
        self.line29.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line29.setMaxLength(1)
        self.line29.setAlignment(QtCore.Qt.AlignCenter)
        self.line29.setObjectName("line29")
        self.gridLayout.addWidget(self.line29, 4, 1, 1, 1)
        self.line34 = QtWidgets.QLineEdit(self.gridFrame)
        self.line34.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line34.setFont(font)
        self.line34.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line34.setMaxLength(1)
        self.line34.setAlignment(QtCore.Qt.AlignCenter)
        self.line34.setObjectName("line34")
        self.gridLayout.addWidget(self.line34, 4, 8, 1, 1)
        self.line28 = QtWidgets.QLineEdit(self.gridFrame)
        self.line28.setMinimumSize(QtCore.QSize(80, 80))
        self.line28.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line28.setFont(font)
        self.line28.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line28.setMaxLength(1)
        self.line28.setAlignment(QtCore.Qt.AlignCenter)
        self.line28.setObjectName("line28")
        self.gridLayout.addWidget(self.line28, 4, 0, 1, 1)
        self.line52 = QtWidgets.QLineEdit(self.gridFrame)
        self.line52.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line52.setFont(font)
        self.line52.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line52.setMaxLength(1)
        self.line52.setAlignment(QtCore.Qt.AlignCenter)
        self.line52.setObjectName("line52")
        self.gridLayout.addWidget(self.line52, 6, 8, 1, 1)
        self.line53 = QtWidgets.QLineEdit(self.gridFrame)
        self.line53.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line53.setFont(font)
        self.line53.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line53.setMaxLength(1)
        self.line53.setAlignment(QtCore.Qt.AlignCenter)
        self.line53.setObjectName("line53")
        self.gridLayout.addWidget(self.line53, 6, 9, 1, 1)
        self.line44 = QtWidgets.QLineEdit(self.gridFrame)
        self.line44.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line44.setFont(font)
        self.line44.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line44.setMaxLength(1)
        self.line44.setAlignment(QtCore.Qt.AlignCenter)
        self.line44.setObjectName("line44")
        self.gridLayout.addWidget(self.line44, 5, 9, 1, 1)
        self.line39 = QtWidgets.QLineEdit(self.gridFrame)
        self.line39.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line39.setFont(font)
        self.line39.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line39.setMaxLength(1)
        self.line39.setAlignment(QtCore.Qt.AlignCenter)
        self.line39.setObjectName("line39")
        self.gridLayout.addWidget(self.line39, 5, 2, 1, 1)
        self.line46 = QtWidgets.QLineEdit(self.gridFrame)
        self.line46.setMinimumSize(QtCore.QSize(80, 80))
        self.line46.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line46.setFont(font)
        self.line46.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line46.setMaxLength(1)
        self.line46.setAlignment(QtCore.Qt.AlignCenter)
        self.line46.setObjectName("line46")
        self.gridLayout.addWidget(self.line46, 6, 0, 1, 1)
        self.line35 = QtWidgets.QLineEdit(self.gridFrame)
        self.line35.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line35.setFont(font)
        self.line35.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line35.setMaxLength(1)
        self.line35.setAlignment(QtCore.Qt.AlignCenter)
        self.line35.setObjectName("line35")
        self.gridLayout.addWidget(self.line35, 4, 9, 1, 1)
        self.line4 = QtWidgets.QLineEdit(self.gridFrame)
        self.line4.setMinimumSize(QtCore.QSize(80, 80))
        self.line4.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line4.setFont(font)
        self.line4.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line4.setMaxLength(1)
        self.line4.setAlignment(QtCore.Qt.AlignCenter)
        self.line4.setObjectName("line4")
        self.gridLayout.addWidget(self.line4, 0, 4, 1, 1)
        self.line11 = QtWidgets.QLineEdit(self.gridFrame)
        self.line11.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line11.setFont(font)
        self.line11.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line11.setMaxLength(1)
        self.line11.setAlignment(QtCore.Qt.AlignCenter)
        self.line11.setObjectName("line11")
        self.gridLayout.addWidget(self.line11, 1, 1, 1, 1)
        self.line3 = QtWidgets.QLineEdit(self.gridFrame)
        self.line3.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line3.setFont(font)
        self.line3.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line3.setMaxLength(1)
        self.line3.setAlignment(QtCore.Qt.AlignCenter)
        self.line3.setObjectName("line3")
        self.gridLayout.addWidget(self.line3, 0, 2, 1, 1)
        self.line2 = QtWidgets.QLineEdit(self.gridFrame)
        self.line2.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line2.setFont(font)
        self.line2.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line2.setMaxLength(1)
        self.line2.setAlignment(QtCore.Qt.AlignCenter)
        self.line2.setObjectName("line2")
        self.gridLayout.addWidget(self.line2, 0, 1, 1, 1)
        self.line7 = QtWidgets.QLineEdit(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line7.sizePolicy().hasHeightForWidth())
        self.line7.setSizePolicy(sizePolicy)
        self.line7.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line7.setFont(font)
        self.line7.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line7.setMaxLength(1)
        self.line7.setAlignment(QtCore.Qt.AlignCenter)
        self.line7.setReadOnly(False)
        self.line7.setObjectName("line7")
        self.gridLayout.addWidget(self.line7, 0, 8, 1, 1)
        self.line5 = QtWidgets.QLineEdit(self.gridFrame)
        self.line5.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line5.setFont(font)
        self.line5.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line5.setMaxLength(1)
        self.line5.setAlignment(QtCore.Qt.AlignCenter)
        self.line5.setObjectName("line5")
        self.gridLayout.addWidget(self.line5, 0, 5, 1, 1)
        self.line6 = QtWidgets.QLineEdit(self.gridFrame)
        self.line6.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line6.setFont(font)
        self.line6.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line6.setMaxLength(1)
        self.line6.setAlignment(QtCore.Qt.AlignCenter)
        self.line6.setObjectName("line6")
        self.gridLayout.addWidget(self.line6, 0, 6, 1, 1)
        self.line8 = QtWidgets.QLineEdit(self.gridFrame)
        self.line8.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line8.setFont(font)
        self.line8.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line8.setMaxLength(1)
        self.line8.setAlignment(QtCore.Qt.AlignCenter)
        self.line8.setObjectName("line8")
        self.gridLayout.addWidget(self.line8, 0, 9, 1, 1)
        self.line10 = QtWidgets.QLineEdit(self.gridFrame)
        self.line10.setMinimumSize(QtCore.QSize(80, 80))
        self.line10.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line10.setFont(font)
        self.line10.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line10.setMaxLength(1)
        self.line10.setAlignment(QtCore.Qt.AlignCenter)
        self.line10.setObjectName("line10")
        self.gridLayout.addWidget(self.line10, 1, 0, 1, 1)
        self.line9 = QtWidgets.QLineEdit(self.gridFrame)
        self.line9.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line9.setFont(font)
        self.line9.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line9.setMaxLength(1)
        self.line9.setAlignment(QtCore.Qt.AlignCenter)
        self.line9.setObjectName("line9")
        self.gridLayout.addWidget(self.line9, 0, 10, 1, 1)
        self.line12 = QtWidgets.QLineEdit(self.gridFrame)
        self.line12.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line12.setFont(font)
        self.line12.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line12.setMaxLength(1)
        self.line12.setAlignment(QtCore.Qt.AlignCenter)
        self.line12.setObjectName("line12")
        self.gridLayout.addWidget(self.line12, 1, 2, 1, 1)
        self.line59 = QtWidgets.QLineEdit(self.gridFrame)
        self.line59.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line59.setFont(font)
        self.line59.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line59.setMaxLength(1)
        self.line59.setAlignment(QtCore.Qt.AlignCenter)
        self.line59.setObjectName("line59")
        self.gridLayout.addWidget(self.line59, 8, 5, 1, 1)
        self.line64 = QtWidgets.QLineEdit(self.gridFrame)
        self.line64.setMinimumSize(QtCore.QSize(80, 80))
        self.line64.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line64.setFont(font)
        self.line64.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line64.setMaxLength(1)
        self.line64.setAlignment(QtCore.Qt.AlignCenter)
        self.line64.setObjectName("line64")
        self.gridLayout.addWidget(self.line64, 9, 0, 1, 1)
        self.line79 = QtWidgets.QLineEdit(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line79.sizePolicy().hasHeightForWidth())
        self.line79.setSizePolicy(sizePolicy)
        self.line79.setMinimumSize(QtCore.QSize(80, 80))
        self.line79.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line79.setFont(font)
        self.line79.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line79.setMaxLength(1)
        self.line79.setAlignment(QtCore.Qt.AlignCenter)
        self.line79.setObjectName("line79")
        self.gridLayout.addWidget(self.line79, 10, 8, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem5, 3, 0, 1, 1)
        self.line75 = QtWidgets.QLineEdit(self.gridFrame)
        self.line75.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line75.setFont(font)
        self.line75.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line75.setMaxLength(1)
        self.line75.setAlignment(QtCore.Qt.AlignCenter)
        self.line75.setObjectName("line75")
        self.gridLayout.addWidget(self.line75, 10, 2, 1, 1)
        self.line63 = QtWidgets.QLineEdit(self.gridFrame)
        self.line63.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line63.setFont(font)
        self.line63.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line63.setMaxLength(1)
        self.line63.setAlignment(QtCore.Qt.AlignCenter)
        self.line63.setObjectName("line63")
        self.gridLayout.addWidget(self.line63, 8, 10, 1, 1)
        self.line61 = QtWidgets.QLineEdit(self.gridFrame)
        self.line61.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line61.setFont(font)
        self.line61.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line61.setMaxLength(1)
        self.line61.setAlignment(QtCore.Qt.AlignCenter)
        self.line61.setObjectName("line61")
        self.gridLayout.addWidget(self.line61, 8, 8, 1, 1)
        self.line74 = QtWidgets.QLineEdit(self.gridFrame)
        self.line74.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line74.setFont(font)
        self.line74.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line74.setMaxLength(1)
        self.line74.setAlignment(QtCore.Qt.AlignCenter)
        self.line74.setObjectName("line74")
        self.gridLayout.addWidget(self.line74, 10, 1, 1, 1)
        self.line81 = QtWidgets.QLineEdit(self.gridFrame)
        self.line81.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line81.setFont(font)
        self.line81.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line81.setMaxLength(1)
        self.line81.setAlignment(QtCore.Qt.AlignCenter)
        self.line81.setObjectName("line81")
        self.gridLayout.addWidget(self.line81, 10, 10, 1, 1)
        self.line60 = QtWidgets.QLineEdit(self.gridFrame)
        self.line60.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line60.setFont(font)
        self.line60.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line60.setMaxLength(1)
        self.line60.setAlignment(QtCore.Qt.AlignCenter)
        self.line60.setObjectName("line60")
        self.gridLayout.addWidget(self.line60, 8, 6, 1, 1)
        self.line68 = QtWidgets.QLineEdit(self.gridFrame)
        self.line68.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line68.setFont(font)
        self.line68.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line68.setMaxLength(1)
        self.line68.setAlignment(QtCore.Qt.AlignCenter)
        self.line68.setObjectName("line68")
        self.gridLayout.addWidget(self.line68, 9, 5, 1, 1)
        self.line65 = QtWidgets.QLineEdit(self.gridFrame)
        self.line65.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line65.setFont(font)
        self.line65.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line65.setMaxLength(1)
        self.line65.setAlignment(QtCore.Qt.AlignCenter)
        self.line65.setObjectName("line65")
        self.gridLayout.addWidget(self.line65, 9, 1, 1, 1)
        self.line73 = QtWidgets.QLineEdit(self.gridFrame)
        self.line73.setMinimumSize(QtCore.QSize(80, 80))
        self.line73.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line73.setFont(font)
        self.line73.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line73.setMaxLength(1)
        self.line73.setAlignment(QtCore.Qt.AlignCenter)
        self.line73.setObjectName("line73")
        self.gridLayout.addWidget(self.line73, 10, 0, 1, 1)
        self.line72 = QtWidgets.QLineEdit(self.gridFrame)
        self.line72.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line72.setFont(font)
        self.line72.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line72.setMaxLength(1)
        self.line72.setAlignment(QtCore.Qt.AlignCenter)
        self.line72.setObjectName("line72")
        self.gridLayout.addWidget(self.line72, 9, 10, 1, 1)
        self.line76 = QtWidgets.QLineEdit(self.gridFrame)
        self.line76.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line76.setFont(font)
        self.line76.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line76.setMaxLength(1)
        self.line76.setAlignment(QtCore.Qt.AlignCenter)
        self.line76.setObjectName("line76")
        self.gridLayout.addWidget(self.line76, 10, 4, 1, 1)
        self.line80 = QtWidgets.QLineEdit(self.gridFrame)
        self.line80.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line80.setFont(font)
        self.line80.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line80.setMaxLength(1)
        self.line80.setAlignment(QtCore.Qt.AlignCenter)
        self.line80.setObjectName("line80")
        self.gridLayout.addWidget(self.line80, 10, 9, 1, 1)
        self.line62 = QtWidgets.QLineEdit(self.gridFrame)
        self.line62.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line62.setFont(font)
        self.line62.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line62.setMaxLength(1)
        self.line62.setAlignment(QtCore.Qt.AlignCenter)
        self.line62.setObjectName("line62")
        self.gridLayout.addWidget(self.line62, 8, 9, 1, 1)
        self.line56 = QtWidgets.QLineEdit(self.gridFrame)
        self.line56.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line56.setFont(font)
        self.line56.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line56.setMaxLength(1)
        self.line56.setAlignment(QtCore.Qt.AlignCenter)
        self.line56.setObjectName("line56")
        self.gridLayout.addWidget(self.line56, 8, 1, 1, 1)
        self.line70 = QtWidgets.QLineEdit(self.gridFrame)
        self.line70.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line70.setFont(font)
        self.line70.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line70.setMaxLength(1)
        self.line70.setAlignment(QtCore.Qt.AlignCenter)
        self.line70.setObjectName("line70")
        self.gridLayout.addWidget(self.line70, 9, 8, 1, 1)
        self.line58 = QtWidgets.QLineEdit(self.gridFrame)
        self.line58.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line58.setFont(font)
        self.line58.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line58.setMaxLength(1)
        self.line58.setAlignment(QtCore.Qt.AlignCenter)
        self.line58.setObjectName("line58")
        self.gridLayout.addWidget(self.line58, 8, 4, 1, 1)
        self.line77 = QtWidgets.QLineEdit(self.gridFrame)
        self.line77.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line77.setFont(font)
        self.line77.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line77.setMaxLength(1)
        self.line77.setAlignment(QtCore.Qt.AlignCenter)
        self.line77.setObjectName("line77")
        self.gridLayout.addWidget(self.line77, 10, 5, 1, 1)
        self.line54 = QtWidgets.QLineEdit(self.gridFrame)
        self.line54.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line54.setFont(font)
        self.line54.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line54.setMaxLength(1)
        self.line54.setAlignment(QtCore.Qt.AlignCenter)
        self.line54.setObjectName("line54")
        self.gridLayout.addWidget(self.line54, 6, 10, 1, 1)
        self.line67 = QtWidgets.QLineEdit(self.gridFrame)
        self.line67.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line67.setFont(font)
        self.line67.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line67.setMaxLength(1)
        self.line67.setAlignment(QtCore.Qt.AlignCenter)
        self.line67.setObjectName("line67")
        self.gridLayout.addWidget(self.line67, 9, 4, 1, 1)
        self.line66 = QtWidgets.QLineEdit(self.gridFrame)
        self.line66.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line66.setFont(font)
        self.line66.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line66.setMaxLength(1)
        self.line66.setAlignment(QtCore.Qt.AlignCenter)
        self.line66.setObjectName("line66")
        self.gridLayout.addWidget(self.line66, 9, 2, 1, 1)
        self.line55 = QtWidgets.QLineEdit(self.gridFrame)
        self.line55.setMinimumSize(QtCore.QSize(80, 80))
        self.line55.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line55.setFont(font)
        self.line55.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line55.setMaxLength(1)
        self.line55.setAlignment(QtCore.Qt.AlignCenter)
        self.line55.setObjectName("line55")
        self.gridLayout.addWidget(self.line55, 8, 0, 1, 1)
        self.line71 = QtWidgets.QLineEdit(self.gridFrame)
        self.line71.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line71.setFont(font)
        self.line71.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line71.setMaxLength(1)
        self.line71.setAlignment(QtCore.Qt.AlignCenter)
        self.line71.setObjectName("line71")
        self.gridLayout.addWidget(self.line71, 9, 9, 1, 1)
        self.line78 = QtWidgets.QLineEdit(self.gridFrame)
        self.line78.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line78.setFont(font)
        self.line78.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line78.setMaxLength(1)
        self.line78.setAlignment(QtCore.Qt.AlignCenter)
        self.line78.setObjectName("line78")
        self.gridLayout.addWidget(self.line78, 10, 6, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem6, 7, 0, 1, 1)
        self.line69 = QtWidgets.QLineEdit(self.gridFrame)
        self.line69.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line69.setFont(font)
        self.line69.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line69.setMaxLength(1)
        self.line69.setAlignment(QtCore.Qt.AlignCenter)
        self.line69.setObjectName("line69")
        self.gridLayout.addWidget(self.line69, 9, 6, 1, 1)
        self.line31 = QtWidgets.QLineEdit(self.gridFrame)
        self.line31.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line31.setFont(font)
        self.line31.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line31.setMaxLength(1)
        self.line31.setAlignment(QtCore.Qt.AlignCenter)
        self.line31.setObjectName("line31")
        self.gridLayout.addWidget(self.line31, 4, 4, 1, 1)
        self.line37 = QtWidgets.QLineEdit(self.gridFrame)
        self.line37.setMinimumSize(QtCore.QSize(80, 80))
        self.line37.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line37.setFont(font)
        self.line37.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line37.setMaxLength(1)
        self.line37.setAlignment(QtCore.Qt.AlignCenter)
        self.line37.setObjectName("line37")
        self.gridLayout.addWidget(self.line37, 5, 0, 1, 1)
        self.line38 = QtWidgets.QLineEdit(self.gridFrame)
        self.line38.setMinimumSize(QtCore.QSize(80, 80))
        self.line38.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line38.setFont(font)
        self.line38.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line38.setMaxLength(1)
        self.line38.setAlignment(QtCore.Qt.AlignCenter)
        self.line38.setObjectName("line38")
        self.gridLayout.addWidget(self.line38, 5, 1, 1, 1)
        self.line1 = QtWidgets.QLineEdit(self.gridFrame)
        self.line1.setEnabled(True)
        self.line1.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line1.setFont(font)
        self.line1.setStyleSheet("QLineEdit{\n"
                                 "background: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit:hover {\n"
                                 "    background: rgb(220, 220, 220);\n"
                                 "}")
        self.line1.setMaxLength(1)
        self.line1.setAlignment(QtCore.Qt.AlignCenter)
        self.line1.setReadOnly(False)
        self.line1.setObjectName("line1")
        self.gridLayout.addWidget(self.line1, 0, 0, 1, 1)
        self.line30 = QtWidgets.QLineEdit(self.gridFrame)
        self.line30.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line30.setFont(font)
        self.line30.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line30.setMaxLength(1)
        self.line30.setAlignment(QtCore.Qt.AlignCenter)
        self.line30.setObjectName("line30")
        self.gridLayout.addWidget(self.line30, 4, 2, 1, 1)
        self.line40 = QtWidgets.QLineEdit(self.gridFrame)
        self.line40.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line40.setFont(font)
        self.line40.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line40.setMaxLength(1)
        self.line40.setAlignment(QtCore.Qt.AlignCenter)
        self.line40.setObjectName("line40")
        self.gridLayout.addWidget(self.line40, 5, 4, 1, 1)
        self.line36 = QtWidgets.QLineEdit(self.gridFrame)
        self.line36.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line36.setFont(font)
        self.line36.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line36.setMaxLength(1)
        self.line36.setAlignment(QtCore.Qt.AlignCenter)
        self.line36.setObjectName("line36")
        self.gridLayout.addWidget(self.line36, 4, 10, 1, 1)
        self.line41 = QtWidgets.QLineEdit(self.gridFrame)
        self.line41.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line41.setFont(font)
        self.line41.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line41.setMaxLength(1)
        self.line41.setAlignment(QtCore.Qt.AlignCenter)
        self.line41.setObjectName("line41")
        self.gridLayout.addWidget(self.line41, 5, 5, 1, 1)
        self.line32 = QtWidgets.QLineEdit(self.gridFrame)
        self.line32.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line32.setFont(font)
        self.line32.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line32.setMaxLength(1)
        self.line32.setAlignment(QtCore.Qt.AlignCenter)
        self.line32.setObjectName("line32")
        self.gridLayout.addWidget(self.line32, 4, 5, 1, 1)
        self.line27 = QtWidgets.QLineEdit(self.gridFrame)
        self.line27.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.line27.setFont(font)
        self.line27.setStyleSheet("QLineEdit{\n"
                                  "background: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit:hover {\n"
                                  "    background: rgb(220, 220, 220);\n"
                                  "}")
        self.line27.setMaxLength(1)
        self.line27.setAlignment(QtCore.Qt.AlignCenter)
        self.line27.setObjectName("line27")
        self.gridLayout.addWidget(self.line27, 2, 10, 1, 1)
        self.gridLayout_2.addWidget(self.gridFrame, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 0, 1, 1, 1)

        self.retranslateUi(PuzzleEntry)
        self.buttonBox.accepted.connect(PuzzleEntry.accept)  # type: ignore
        self.buttonBox.rejected.connect(PuzzleEntry.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(PuzzleEntry)

    def retranslateUi(self, PuzzleEntry):
        _translate = QtCore.QCoreApplication.translate
        PuzzleEntry.setWindowTitle(_translate("PuzzleEntry", "Puzzle Entry"))
