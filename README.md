
View two dimensional data using PyQt5 QTableWidget 

If you want to view some two dimensional data you can use sript qt_table.py as a example. 
To make window with table place the one of the following objects in constructor class CSV_Table (see script csv_table ):

1. name of csv file
2. numpy 2-dimensional array
3. pandas DataFrame object

like this


from PyQt5 import QtWidgets
import sys
import csv_table as ct
import numpy as np
import pandas as pd

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    # Пример для csv файла
    main1 = ct.CSV_Table('./data/y_train.csv')
    main1.show()
    
