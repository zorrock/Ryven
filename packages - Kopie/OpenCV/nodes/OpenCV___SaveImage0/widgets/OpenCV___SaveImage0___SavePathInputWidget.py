from custom_src.retain import M
from PySide2.QtWidgets import QPushButton, QFileDialog
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...

class SavePathInputWidget_PortInstanceWidget(QPushButton):
    def __init__(self, parent_port_instance, parent_node_instance):
        super(SavePathInputWidget_PortInstanceWidget, self).__init__("Select")

        # leave these lines ------------------------------
        self.parent_port_instance = parent_port_instance
        self.parent_node_instance = parent_node_instance
        # ------------------------------------------------

        self.setStyleSheet('''
            color: #cccccc;
            border-radius: 5px;
            border: 1px solid #aaaaaa;
            padding-top: 3px;
            padding-bottom: 3px;
            padding-left: 25px;
            padding-right: 25px;
            background: transparent;
        ''')

        self.clicked.connect(M(self.button_clicked))

    def button_clicked(self):
        file_path = QFileDialog.getSaveFileName(self, 'Save')[0]
        self.parent_node_instance.path_chosen(file_path)

    def get_data(self):
        return self.text()

    def set_data(self, data):
        self.setText(data)

    def removing(self):
        pass
