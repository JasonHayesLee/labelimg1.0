self.comboBox = QComboBox(self.menuBar)
self.menuBar.setCornerWidget(self.comboBox, Qt.TopRightCorner)
self.comboBox.addItems(self.labelHist.labels)
self.comboBox.currentIndexChanged.connect(self.changeLabel)