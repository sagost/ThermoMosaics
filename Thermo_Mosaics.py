# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Thermo_Mosaics.ui'
#
# Created: Tue Sep 27 09:11:43 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import glob
import numpy as np
import png
from osgeo import gdal

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(604, 343)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.CSVFolder_pushButton = QtGui.QPushButton(self.tab)
        self.CSVFolder_pushButton.setObjectName(_fromUtf8("CSVFolder_pushButton"))
        self.horizontalLayout.addWidget(self.CSVFolder_pushButton)
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.DownspinBox1 = QtGui.QSpinBox(self.tab)
        self.DownspinBox1.setObjectName(_fromUtf8("DownspinBox1"))
        self.horizontalLayout_2.addWidget(self.DownspinBox1)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.UpspinBox1 = QtGui.QSpinBox(self.tab)
        self.UpspinBox1.setObjectName(_fromUtf8("UpspinBox1"))
        self.horizontalLayout_2.addWidget(self.UpspinBox1)
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_3.addWidget(self.label_10)
        self.StartpushButton1 = QtGui.QPushButton(self.tab)
        self.StartpushButton1.setObjectName(_fromUtf8("StartpushButton1"))
        self.horizontalLayout_3.addWidget(self.StartpushButton1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_5.addWidget(self.label_6)
        self.DownspinBox2 = QtGui.QSpinBox(self.tab_2)
        self.DownspinBox2.setObjectName(_fromUtf8("DownspinBox2"))
        self.horizontalLayout_5.addWidget(self.DownspinBox2)
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_5.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.tab_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_5.addWidget(self.label_8)
        self.UpspinBox2 = QtGui.QSpinBox(self.tab_2)
        self.UpspinBox2.setObjectName(_fromUtf8("UpspinBox2"))
        self.horizontalLayout_5.addWidget(self.UpspinBox2)
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_5.addWidget(self.label_9)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton_4 = QtGui.QPushButton(self.tab_2)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.lineEdit_3 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_11 = QtGui.QLabel(self.tab_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_6.addWidget(self.label_11)
        self.StartpushButton2 = QtGui.QPushButton(self.tab_2)
        self.StartpushButton2.setObjectName(_fromUtf8("StartpushButton2"))
        self.horizontalLayout_6.addWidget(self.StartpushButton2)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.krichtextwidget = QtGui.QTextEdit(self.tab_3)
        self.krichtextwidget.setReadOnly(True)
        self.krichtextwidget.setObjectName(_fromUtf8("krichtextwidget"))
        self.gridLayout_2.addWidget(self.krichtextwidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.UpspinBox1.setMaximum(5000)
        self.UpspinBox1.setMinimum(-500)
        self.UpspinBox2.setMaximum(5000)
        self.UpspinBox2.setMinimum(-500)
        self.DownspinBox1.setMaximum(5000)
        self.DownspinBox1.setMinimum(-500)
        self.DownspinBox2.setMaximum(5000)
        self.DownspinBox2.setMinimum(-500)
        
        self.UpspinBox1.setValue(80)
        self.UpspinBox2.setValue(80)

        self.label_10.hide()
        self.label_11.hide()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.StartpushButton1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.StartpushButton1.hide)
        QtCore.QObject.connect(self.StartpushButton1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_10.show)
        QtCore.QObject.connect(self.StartpushButton2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.StartpushButton2.hide)
        QtCore.QObject.connect(self.StartpushButton2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_11.show)
        QtCore.QObject.connect(self.CSVFolder_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ChooseCSVFolder)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ChooseInputGeoTiff)
        QtCore.QObject.connect(self.StartpushButton1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ConvertCSVtoPNG)
        QtCore.QObject.connect(self.StartpushButton2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ConvertToThermoTiff)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def ChooseCSVFolder(self):
        CsvPath = QtGui.QFileDialog.getExistingDirectory()
        if not CsvPath is None:
            self.lineEdit.insert(str(CsvPath))
            
    def ChooseInputGeoTiff(self):
        GeoTiffPath = QtGui.QFileDialog.getOpenFileName()
        if not GeoTiffPath is None:
            self.lineEdit_3.insert(str(GeoTiffPath))
            
    def ConvertCSVtoPNG(self):
        app.processEvents()
        if str(self.lineEdit.displayText()) != None :
            CsvFolder = self.lineEdit.displayText()
            MAXRangeTemperature = self.UpspinBox1.value()
            MINRangeTemperature = self.DownspinBox1.value()
            DifferenzialeTermico = MAXRangeTemperature - MINRangeTemperature
            vfunc = np.vectorize(self.ModifyCelsiusTo16bit)

            for filename in sorted(glob.glob(str(CsvFolder)+'/*.csv')):
                Array = np.genfromtxt(filename,delimiter=';',dtype= np.dtype(float), names=None)
                arrayCelsius = np.delete(Array,-1,1)
                arrayCelsius = vfunc(arrayCelsius,DifferenzialeTermico)
                array = arrayCelsius.astype(int)
                img = png.from_array(array, mode='L;16')
                img.save(filename.split('.')[0]+'.png')
        self.label_10.hide()
        self.StartpushButton1.show()
        

        
        
    
    def ConvertToThermoTiff(self):
        app.processEvents()
        if str(self.lineEdit_3.displayText()) != None :
            GeoTiffFile = str(self.lineEdit_3.displayText())
            MAXRangeTemperature = self.UpspinBox1.value()
            MINRangeTemperature = self.DownspinBox1.value()
            DifferenzialeTermico = MAXRangeTemperature - MINRangeTemperature
            ValoreDiCorrezione = MINRangeTemperature
            vfunc = np.vectorize(self.Modify16bitToCelsius)
            src_ds = gdal.Open(  GeoTiffFile )
            cols = src_ds.RasterXSize
            rows = src_ds.RasterYSize
            #bands = src_ds.RasterCount
            #driver = src_ds.GetDriver().LongName
            geotransform = src_ds.GetGeoTransform()
            projection = src_ds.GetProjection()
            originX = geotransform[0]
            originY = geotransform[3]
            pixelWidth = geotransform[1]
            pixelHeight = geotransform[5]
            srcband = src_ds.GetRasterBand(1)
            bandtype = gdal.GetDataTypeName(srcband.DataType)
            data = srcband.ReadAsArray(0, 0, cols, rows).astype(np.float)
            data = vfunc(data, DifferenzialeTermico,ValoreDiCorrezione)
            output_raster = gdal.GetDriverByName('GTiff').Create(GeoTiffFile.split('.')[0]+'_ThermoTiff.tif',cols, rows, 1 ,gdal.GDT_Float32)
            output_raster.GetRasterBand(1).WriteArray(data)
            output_raster.GetRasterBand(1).SetNoDataValue(-99)
            output_raster.SetGeoTransform(geotransform)
            output_raster.SetProjection( projection )
            output_raster=None
            src_ds=None
            del data
        self.label_11.hide()
        self.StartpushButton2.show()   
    
    def ModifyCelsiusTo16bit(self,DN, DifferenzialeTermico):
    
        Value = (DN * 65535)/DifferenzialeTermico
        return Value
    
    def Modify16bitToCelsius (self,DN, DifferenzialeTermico, ValoreDiCorrezione ):
    
        Value = ((DN * DifferenzialeTermico)/ 65535) + ValoreDiCorrezione
        return Value

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Thermo_Mosaics", None))
        self.label.setText(_translate("MainWindow", "Thermo Mosaics Creator", None))
        self.CSVFolder_pushButton.setText(_translate("MainWindow", "Choose CSV files folder", None))
        self.label_2.setText(_translate("MainWindow", "Set thermal range between", None))
        self.label_3.setText(_translate("MainWindow", "°", None))
        self.label_4.setText(_translate("MainWindow", "and", None))
        self.label_5.setText(_translate("MainWindow", "°", None))
        self.label_10.setText(_translate("MainWindow", "Processing...", None))
        self.StartpushButton1.setText(_translate("MainWindow", "Convert CSV to image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Process RAW CSV", None))
        self.label_6.setText(_translate("MainWindow", "Set thermal range between", None))
        self.label_7.setText(_translate("MainWindow", "°", None))
        self.label_8.setText(_translate("MainWindow", "and", None))
        self.label_9.setText(_translate("MainWindow", "°", None))
        self.pushButton_4.setText(_translate("MainWindow", "Choose Input GeoTiff 16bit", None))
        self.label_11.setText(_translate("MainWindow", "Processing...", None))
        self.StartpushButton2.setText(_translate("MainWindow", "Convert to ThermoTiff", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Process Thermo Orthophoto", None))
        self.krichtextwidget.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Verdana\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thermo_Mosaics_Creator 1.0</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                             -------------------</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                             </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        copyright            : (C) 2016 by Salvatore Agosta </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        email                : sagost@katamail.com</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This program is free software; you can redistribute it and/or modify  </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">it under the terms of the GNU General Public License as published by  </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the Free Software Foundation; either version 3 of the License, or     </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(at your option) any later version.   </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thermo_Mosaics_Creator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You should have received a copy of the GNU General Public License</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">along with Thermo_Mosaics_Creator.  If not, see &lt;http://www.gnu.org/licenses/&gt;.        </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                         </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "About", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

