from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys
import MainUI
import searchArticle,searchAuthor,searchYear,preWork,aboutUs


#import searchArticleUI
#from search_src import *
#global MATCHSTATUS
#import multiprocessing
#import time
#from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot

class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = MainUI.Ui_MainWindow()
        self.main_ui.setupUi(self)
        # 主程序事件
        self.main_ui.searchAuthor.clicked.connect(self.CreateSearchAuthor)
        self.main_ui.searchArticle.clicked.connect(self.CreateSearchArticle)
        self.main_ui.searchYear.clicked.connect(self.CreateSearchYear)
        self.main_ui.preProcess.clicked.connect(self.CreatePreWork)
        self.main_ui.our645.clicked.connect(self.CreateAboutUs)

    def CreateAboutUs(self):
        if not aboutU.isVisible():
            aboutU.show()
        return

    def CreateSearchYear(self):
        if not searchY.isVisible():
            searchY.show()
        return

    def CreateSearchArticle(self):
        if not searchUI.isVisible():
            searchUI.show()
        return

    def CreateSearchAuthor(self):
        if not searchA.isVisible():
            searchA.show()
        return

    def CreatePreWork(self):
        if not preW.isVisible():
            preW.show()
            if not preW.workThread.isRunning():
                preW.checkReady()
                print(preW.status)
        return
        
if __name__ == '__main__':
    app = QApplication(sys.argv)

    manu = mainWindow()
    searchUI = searchArticle.searchWindow()
    searchA = searchAuthor.searchAuthorWindow()
    searchY = searchYear.searchYearWindow()
    preW = preWork.preWorkWindow()
    aboutU = aboutUs.AboutUsWindow()

    #searchUI.ui.infBrowser.setPlainText(searchUI.ui.comboBox.currentText())

    manu.show()
    sys.exit(app.exec_())
    
    
#标题相同存在bug
