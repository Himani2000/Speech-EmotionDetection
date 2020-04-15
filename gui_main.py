import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,QLabel,QFileDialog,
    QHBoxLayout, QVBoxLayout, QApplication)

from test_model import get_value




class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        title = QLabel('Speech Emotion Recognition')

        loadButton=QPushButton("Load File")
        testButton=QPushButton("Test Model")

        loadButton.clicked.connect(self.getfiles)


        testButton.clicked.connect(self.getresults)

        model1=QPushButton("Model1 Results")
        model2=QPushButton("Model2 Results")
        model3=QPushButton("Model3 Results")

        

        self.model1_t=QLabel("")
        self.model2_t=QLabel("")
        self.model3_t=QLabel("")


        hbox1=QHBoxLayout()
        hbox1.addWidget(model1)
        hbox1.addWidget(self.model1_t)

        hbox2=QHBoxLayout()
        hbox2.addWidget(model2)
        hbox2.addWidget(self.model2_t)

        hbox3=QHBoxLayout()
        hbox3.addWidget(model3)
        hbox3.addWidget(self.model3_t)

        vbox1=QVBoxLayout()
        vbox1.addLayout(hbox1)
        vbox1.addLayout(hbox2)
        vbox1.addLayout(hbox3)




        hbox = QHBoxLayout()
       
        vbox = QVBoxLayout()

        hbox.addWidget(loadButton)
        hbox.addWidget(testButton)
        
        vbox.addWidget(title)    
        vbox.addLayout(hbox)

        result_heading = QLabel('Results')
        vbox.addWidget(result_heading)
        vbox.addLayout(vbox1)



        #grid = QGridLayout()
        #grid.setSpacing(10)


        self.setLayout(vbox)    
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Speech_emotion_recognition')    
        self.show()
    
    def getfiles(self):
        dlg =  QFileDialog.getOpenFileName(self, 'Open file', '/home')
        print(dlg)
        self.filename=dlg[0]

    def getresults(self):
        value_1,value_2,value_3=get_value(self.filename)
        self.model1_t.setText(value_1)
        self.model2_t.setText(value_2)
        self.model3_t.setText(value_3)


        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
