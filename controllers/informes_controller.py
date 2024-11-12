from PyQt6.QtWidgets import QWidget, QHeaderView,QPushButton
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from views.informes_view import Ui_Form

class InformesController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.showMaximized()
        self.adjust_frame_width()

        self.estilo()

        # tabla
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["S/N", "TITULO", "FECHA", "ACCION"])
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.resizeColumnsToContents()
        header = self.ui.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.tableView.verticalHeader().setVisible(False)
        self.add_data()
        self.add_buttons_to_table()

        # desconectarse
        self.ui.desconectarse.clicked.connect(self.onClose)

        #general
        self.ui.general.clicked.connect(self.open_general_window)
        
        # Imagenes
        self.ui.imagenes.clicked.connect(self.open_imagenes_window)

        # Log 
        self.ui.log.clicked.connect(self.open_log_window)
        
    def open_log_window(self):
        from controllers import LogController
        self.log_window = LogController()
        self.close()
        self.log_window.show()


    def open_imagenes_window(self):
        from controllers import ImagenesController
        self.imagenes_window = ImagenesController()
        self.close()
        self.imagenes_window.show()
        
    def open_cargue_window(self):
        from controllers import CargueVehiculoController
        self.cargue_window = CargueVehiculoController()
        self.cargue_window.show()

    def onClose(self):
        from controllers import MainController
        self.main_window = MainController()
        self.close()
        self.main_window.show()
        
    def open_general_window(self):
        from controllers import GeneralController
        self.general_window = GeneralController()
        self.close()
        self.general_window.show()

    def add_buttons_to_table(self):
        for row in range(self.model.rowCount()):
            index = self.model.index(row, 3)  # Índice de la columna de "Acción"
            button = QPushButton("Descargar")
            self.estilo_button(button=button)
            button.clicked.connect(lambda checked, r=index: self.on_button_clicked(r))
            self.ui.tableView.setIndexWidget(index, button)

    def on_button_clicked(self, index):
        # Realiza una acción cuando se hace clic en el botón
        print(f"Botón en la fila {index.row()} ha sido clickeado.")

    def add_data(self):
        data = [
            ["Ana", 23, "Madrid"],
            ["Luis", 30, "Barcelona"],
            ["Marta", 25, "Valencia"],
            ["Juan", 28, "Sevilla"]
        ]
        
        for row in data:
            items = [QStandardItem(str(cell)) for cell in row]
            self.model.appendRow(items)

    def estilo_button(self,button:QPushButton):
        button.setStyleSheet("""
            QPushButton{
                background: #ffffff;
                color: #5E5ADB;
                border: 1px solid #5E5ADB;
                padding: 20px 0px;
                border-radius:5px;
            }
            QPushButton:hover{
                background: #F3F4F8;
            }
        """)

    def estilo(self):
        self.ui.desconectarse.setStyleSheet("""
            QPushButton{
                color: #000000;
                padding: 10px 0;
            }
            QPushButton:hover{
                color: #5E5ADB;
                background: #F3F4F8;
            }
        """)
        self.ui.general.setStyleSheet("""
            QPushButton{
                color: #000000;
                padding: 10px 0;
            }
            QPushButton:hover{
                color: #5E5ADB;
                background: #F3F4F8;
            }
        """)
        self.ui.informes.setStyleSheet("""
            QPushButton{
                color: #5E5ADB;
                background: #F3F4F8;
                padding: 10px 0;
            }
            QPushButton:hover{
                color: #5E5ADB;
                background: #F3F4F8;
            }
        """)
        self.ui.imagenes.setStyleSheet("""
            QPushButton{
                color: #000000;
                padding: 10px 0;
            }
            QPushButton:hover{
                color: #5E5ADB;
                background: #F3F4F8;
            }
        """)
        self.ui.log.setStyleSheet("""
            QPushButton{
                color: #000000;
                padding: 10px 0;
            }
            QPushButton:hover{
                color: #5E5ADB;
                background: #F3F4F8;
            }
        """)
        self.ui.tableView.setStyleSheet("""
            QTableView {
                background-color: #ffffff;
                font-size: 12px;
                color: #000000;
                text-align: center;
            }

            /* Estilos para los encabezados */
            QHeaderView::section {
                background-color: #FAFAFA; /* Fondo del encabezado */
                color: #8B909A;              /* Color del texto */
                padding: 4px;
                font-size: 12px;
                font-weight: bold;
            }
            
            /* Estilos para las celdas individuales */
            QTableView::item {
                padding: 0px 8px;    
                color: black;
                text-align: center;
            }
        """)

    def adjust_frame_width(self):
        width = int(self.width() / 5)
        self.ui.frame.setMaximumWidth(width)
        self.ui.frame_2.setMinimumWidth(width*4)

    def resizeEvent(self, event):
        self.adjust_frame_width()
        super().resizeEvent(event)