from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QMainWindow, QApplication, QTableWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tablewidget = QTableWidget(4, 1)
        self.setCentralWidget(self.tablewidget)

        for row in range(4):
            item = QTableWidgetItem("index_" + str(row))
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setCheckState(Qt.Unchecked)
            self.tablewidget.setItem(row, 0, item)

        self.tablewidget.cellChanged.connect(self.onCellChanged)

    def onCellChanged(self, row, column):
        item = self.tablewidget.item(row, column)
        print(item.text())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
