# -*- coding: utf8 -*-
from PyQt5 import QtWidgets, QtCore
import pandas as pd
import numpy as np

class CSV_Table(QtWidgets.QWidget):
	def __init__(s,fromdata=None,parent = None):
		QtWidgets.QWidget.__init__(s,parent)
		s.setWindowTitle(u'Просмотр двумрного массива')
		s.gLayout = QtWidgets.QGridLayout()
		
		s.begin_row = QtWidgets.QSpinBox()
		s.begin_row.setPrefix(u'Начальная строка: ')
		s.count_rows = QtWidgets.QSpinBox()
		s.count_rows.setPrefix(u'Число строк: ')
		s.count_rows.setMinimum(1)
		s.count_rows.setMaximum(3000)
		s.count_rows.setValue(1000)
		
		s.occurLabel = QtWidgets.QLabel(u'Число знаков после десятичной точки')
		s.numDigits = QtWidgets.QSpinBox()
		s.numDigits.setMinimum(1)
		s.numDigits.setMaximum(9)
		s.numDigits.setValue(3)
		
		if type(fromdata)==str:
			fname = fromdata
			s.fname = fname
			s.data = pd.read_csv(fname)
			s.configure()
		elif type(fromdata)==pd.core.frame.DataFrame:
			s.data = fromdata
			s.configure()
		elif type(fromdata)==np.ndarray:
			array = fromdata
			s.data = pd.DataFrame(array)
			s.ROWS,s.COLS = array.shape
			s.configure()
			
		else:
			s.table = QtWidgets.QTableWidget(1,1,s)
			s.begin_row.setMinimum(1)
			s.begin_row.setMaximum(1)
		
		
		s.gLayout.addWidget(s.table,2,0,1,2)
		s.gLayout.addWidget(s.begin_row,0,0,1,1)
		s.gLayout.addWidget(s.count_rows,0,1,1,1)
		s.gLayout.addWidget(s.occurLabel,1,0,1,1)
		s.gLayout.addWidget(s.numDigits,1,1,1,1)
		
		s.setLayout(s.gLayout)
		
		
		s.begin_row.valueChanged.connect(s.update_table)
		s.count_rows.valueChanged.connect(s.update_table)
		s.numDigits.valueChanged.connect(s.update_table)
	
	def configure(s):
		s.fields = s.data.keys()
		s.COLS = len(s.fields)
		s.ROWS = len(s.data[s.fields[0]])
		
			
		s.begin_row.setMinimum(1)
		s.begin_row.setMaximum(s.ROWS)
		s.begin_row.setValue(1)
			
		s.start_row = s.begin_row.value()
			
		s.end_row = s.start_row + s.count_rows.value()
		if s.end_row > s.ROWS: 
			s.end_row = s.ROWS
		s.table = QtWidgets.QTableWidget(s.end_row - s.start_row + 1,s.COLS,s)
		s.set_data()
			
	def update_table(s):
		s.start_row = s.begin_row.value()
		s.table.clearSpans()
		
		s.end_row = s.start_row + s.count_rows.value() -1
		if s.end_row > s.ROWS: 
			s.end_row = s.ROWS
		
		s.set_data()
		
		
	def set_data(s):
		s.table.setRowCount(s.end_row - s.start_row + 1)
		digs = s.numDigits.value()
		formatnum = "%."+str(digs)+"f"
		
		for i,field in enumerate(s.fields):
			item = QtWidgets.QTableWidgetItem()
			item.setText(str(field))
			s.table.setHorizontalHeaderItem(i, item)
			
			if i == 0:
				
				for j in range(s.start_row - 1,s.end_row):
					item = QtWidgets.QTableWidgetItem()
					item.setText(str(j+1))
					s.table.setVerticalHeaderItem(j-s.start_row +1, item)
			
			for j in range(s.start_row - 1,s.end_row):
				 
				val = s.data[field][j]
				
				item = QtWidgets.QTableWidgetItem()
				try:
					if type(val) != np.int64:
						val = formatnum % float(val)
				except:
					pass
				item.setText(str(val))
				s.table.setItem(j-s.start_row +1, i, item)
			
