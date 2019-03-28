# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys
import csv_table as ct
import numpy as np
import pandas as pd

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    # Пример для csv файла
    main1 = ct.CSV_Table('./data/y_train.csv')
    main1.resize(500,500)
    
    # Пример для двумерного numpy массива
    
    A = np.arange(1000).reshape((200,5))
    C = np.ndarray((200,5))
    C = 1.0/(1.0+A)
    main2 = ct.CSV_Table(C)
    main2.resize(500,300)
    
    
    # Объект DataFrame из pandas
    
    
    A = pd.DataFrame({'Код':[100,101,303,121,444,321,33,87],
					  'Город':['Москва', 'Волгоград', 'Саратов', 'Тула','Астрахань', 'Майкоп', 'Краснодар', 'Ейск'],
					  'Температура': [12.5,11.2,14.1,17.3,11.6,12.7,19.0,12.8]})
    main3 = ct.CSV_Table(A)
	
    
    # Без параметров -- пустая таблица
    main = ct.CSV_Table()
    
    
    main1.show()
    main2.show()
    main3.show()
    main.show()
    sys.exit(app.exec_())
