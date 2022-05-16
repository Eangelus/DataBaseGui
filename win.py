import datetime
from gui.GuiMain import *
import MyDataBaseBot
import sys

class Mymain(Ui_MainWindow):

    #construktor
    def __init__(self):
        super().__init__(MainWindow)
        self.bot = MyDataBaseBot.MyDataBaseBot("127.0.0.1", 3306, "root", "", "todobase")
        self.ltloadButton.clicked.connect(self.pressedLLB)
        self.indexOfDatabase = "todo"
        self.indexOfDatabase_2 = "todo"
        self.auswahl1 = 0
        self.auswahl2 = 0

#funktionen zum laden durch drücken der buttons der datan aus der Table:

    #linkers oben ladebutton
    def pressedLLB(self):

        if self.comboBox.currentText().__str__() != self.indexOfDatabase:
            self.indexOfDatabase = str(self.comboBox.currentText())
            self.loadDb(self.indexOfDatabase)
        else:
            print("nichts zu laden")
    # rechters oben ladebutton
    def pressedRLB(self):

        if self.comboBox_2.currentText().__str__() != self.indexOfDatabase_2:
            self.indexOfDatabase_2 = str(self.comboBox_2.currentText())
            self.loadDb2(self.indexOfDatabase_2)
        else:
            print("nichts zu laden")

# programm liesst daten aus der Datenbank ein:

    # interieren durch for und { } um die boxen durch zugehen

    # fenster links oben
    def loadDb(self, index):
        # Leere tabelle
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        # fangen an die rechte tabelle zu füllen
        index_of_table = self.bot.zeige(index)
        for row_number, row_data in enumerate(index_of_table):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                print("Eingang: " + str(data))
                self.tableWidget.setColumnCount(len(row_data))
                if type(data) == datetime.date:
                    data = str(data)
                    print("datetime data hinzufügen: " + data)
                    self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(data))
                else:
                    print("Anderer datensatz hinzufügen: " + str(data))
                    self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

    # fenster rechts oben
    def loadDb2(self, index):
        # Leere tabelle
        self.tableWidget_2.clear()
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(0)
        # fangen an die rechte tabelle zu füllen
        index_of_table = self.bot.zeige(index)
        for row_number, row_data in enumerate(index_of_table):
            self.tableWidget_2.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                print("Eingang: " + str(data))
                self.tableWidget_2.setColumnCount(len(row_data))
                if type(data) == datetime.date:
                    data = str(data)
                    print("datetime data hinzufügen: " + data)
                    self.tableWidget_2.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(data))
                else:
                    print("Anderer datensatz hinzufügen: " + str(data))
                    self.tableWidget_2.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

# dropdown menus:

    #links oben
    def loadDb_com(self):
        index = self.bot.zeige_tables()
        for i in index:
            r = str(i)
            r = r[2:-3]
            self.comboBox.addItem(r)

    #rechts oben
    def loadDb2_com(self):
        index = self.bot.zeige_tables()
        for i in index:
            r = str(i)
            r = r[2: -3]
            self.comboBox_2.addItem(r)

    #unten
    def loadDb3_com(self):
        self.comboBox_3.addItem("Show Tables")
        self.comboBox_3.addItem("Order By")
        self.comboBox_3.addItem("Left Join")
        self.comboBox_3.addItem("Right Join")


    # funktion zum laden beim starten bzw inizaliersien
    def start_up_load(self):
        self.loadDb(self.indexOfDatabase)
        self.loadDb_com()
        self.loadDb2(self.indexOfDatabase_2)
        self.loadDb2_com()
        self.loadDb3_com()


    def pressedEinfL(self):
        spinAuswahl = self.spinBox.value()
        print(spinAuswahl)
        print("hier setze ich mein valu")
        print(self.comboBox.currentText())
        self.bot.enf(self.comboBox.currentText(), spinAuswahl)
        print("jetzt hab ich die funktion ausgeführt ")


    def pressedEinfR(self):
        self.auswahl2 = self.spinBox_2.value()

    def start_ui(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Mymain()
        self.ui.setupUi(MainWindow)
        self.ui.start_up_load()
        self.MainWindow.show()
        sys.exit(app.exec_())


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Mymain()
ui.setupUi(MainWindow)
ui.start_up_load()
MainWindow.show()
sys.exit(app.exec_())
