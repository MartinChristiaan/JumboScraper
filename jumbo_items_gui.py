from PyQt5 import QtGui  
from PyQt5 import QtCore

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from util.qt_util import *
from util.style import style
from PyQt5.QtWidgets import QApplication, QWidget
import pandas as pd

def create_app():
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 800)
    w.setWindowTitle('Simple')
    return app,w
def execute_app(app,w):
    w.show()
    sys.exit(app.exec_())
    


item_csv = "items.csv"
#consumption_db= "consumption.csv"





items = pd.read_csv(item_csv)
app,w = create_app()
layout = QVBoxLayout()
w.setLayout(layout)

for index, row in items.iterrows():
    create_button(layout,row['Name'],lambda : print(click))
add_text_box(layout,"JumboLink",lambda : print("clik") )
execute_app(app,w)
#items.to_csv(item_csv, index=False)
#app,w = create_basic_app()


# Create GUi
# For each item in the db add a button
# Add link box


    
