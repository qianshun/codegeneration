from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from codegeneration.mainlogic import Mainlogic

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Mainlogic()
    mainWindow.show()
    sys.exit(app.exec_())
