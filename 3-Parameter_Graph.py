from cmath import exp
import sys
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

form_class = uic.loadUiType('Parametergraph.ui')[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ResultButton.clicked.connect(self.result)
        self.InitalButton.clicked.connect(self.init)

    def init(self):  # 초기화
        self.ErrorMsg.setText("") 
        self.xfor.setText("")
        self.yfor.setText("")
        self.zfor.setText("")

    def result(self):
        try:
            self.ErrorMsg.setText("")  # 에러 메세지 초기화
            t = np.linspace(-100, 100, 10000)

            if self.TwoDi.isChecked():
                x_eq = self.xfor.text().strip()
                y_eq = self.yfor.text().strip()
                try:
                    x = eval(x_eq)
                    y = eval(y_eq)
                except Exception as e:
                    self.ErrorMsg.setText(f"식이 잘못 되었습니다: {e}")
                    return

                fig = plt.figure()
                plt.plot(x, y)
                plt.xlabel('X')
                plt.ylabel('Y')
                plt.title('2D Parametric Graph')
                plt.show()

            elif self.ThreeDi.isChecked():
                x_eq = self.xfor.text().strip()
                y_eq = self.yfor.text().strip()
                z_eq = self.zfor.text().strip()
                try:
                    x = eval(x_eq)
                    y = eval(y_eq)
                    z = eval(z_eq)
                except Exception as e:
                    self.ErrorMsg.setText(f"식이 잘못 되었습니다: {e}")
                    return

                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')
                ax.plot(x, y, z)
                ax.set_xlabel('X')
                ax.set_ylabel('Y')
                ax.set_zlabel('Z')
                plt.title('3D Parametric Graph')
                plt.show()

        except Exception as e:
            self.ErrorMsg.setText(f"식이 잘못 되었습니다: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
