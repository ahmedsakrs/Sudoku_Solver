from PyQt5 import QtWidgets
from frontends import Ui_SudokuSolver
import os
import numpy as np


class SudokoSolver(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SudokuSolver()
        self.ui.setupUi(self)
        self.showMaximized()

        if '.\\Saved Games' not in [x[0] for x in os.walk('.')]:
            os.mkdir('Saved Games')

        self.current_state = [['' for _ in range(9)] for _ in range(9)]
        self.start_state = [['' for _ in range(9)] for _ in range(9)]
        self.states = []
        self.popped_states = []
        self.solutions = []

        self.ui.hint_btn.clicked.connect(self.hint)
        self.ui.solve_btn.clicked.connect(self.solve)
        self.ui.reset_btn.clicked.connect(self.reset)
        self.ui.undo_btn.clicked.connect(self.undo)
        self.ui.redo_btn.clicked.connect(self.redo)

        self.ui.actionSave.triggered.connect(self.save)
        self.ui.actionClose.triggered.connect(self.close)

        self.ui.actionEasy_2.triggered.connect(self.generate_easy)
        self.ui.actionMedium_2.triggered.connect(self.generate_medium)
        self.ui.actionHard_2.triggered.connect(self.generate_hard)

        self.ui.actionFull_Screen_2.triggered.connect(self.full_screen)

        self.ui.actionLoad.triggered.connect(self.load)
        self.ui.actionInsert_an_image.triggered.connect(self.insert_image)
        self.ui.actionManually.triggered.connect(self.insert_manually)

    def insert_manually(self):
        pass

    def insert_image(self):
        path = QtWidgets.QFileDialog.getOpenFileName(filter="Image files (*.jpg *.gif *.png *.jfif *.jpeg)",
                                                     caption='Select the image to load')[0]

        if path is None:
            return

    def load(self):
        path = QtWidgets.QFileDialog.getOpenFileName(filter="BIN Files (*.npy)",
                                                     caption='Select the file to load',
                                                     directory='Saved Games')[0]

        if path is None:
            return

        self.start_state = np.load(path, allow_pickle=True)

    def full_screen(self):
        if not self.isFullScreen():
            self.showFullScreen()
            self.ui.actionFull_Screen_2.setText('Exit Full Screen')
        else:
            self.showMaximized()
            self.ui.actionFull_Screen_2.setText('Full Screen')

    def generate_easy(self):
        pass

    def generate_medium(self):
        pass

    def generate_hard(self):
        pass

    def save(self):
        path = QtWidgets.QFileDialog.getSaveFileName(caption='Select the destination of the saved puzzle',
                                                     directory='Saved Games')[0]

        if path is None:
            return

        np.save(path, self.current_state)

    def hint(self):
        pass

    def solve(self):
        pass

    def reset(self):
        pass

    def undo(self):
        self.popped_states.append(self.states.pop())
        if len(self.states) == 0:
            self.ui.undo_btn.setEnabled(False)

    def redo(self):
        pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    gui = SudokoSolver()
    gui.show()
    sys.exit(app.exec())
