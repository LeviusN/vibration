import paramiko
import qtmodern
import threading
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QVBoxLayout, QWidget, QTabWidget, \
    QHBoxLayout, QSlider, QAction,QMenu, QLabel, QCheckBox, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from upn_final.name_selector.indicator import LedIndicator
from upn_final.name_selector.ip_validator import IP4ValidatorBasic, Discoverer

AUTO = '4'
NETWORK = ['192.168.0.249', 'niki', 'levius']
PATH = 'python Desktop/run.py'
TEXT = 'GUI je zlozene z 3 zaloziek. \nPrva zalozka je urcena na riadenie\nDruha na nastavenie pripojenia na zariadenie\nTretia je pomocna'


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.process = None
        self.client = None
        self.channel = None
        self.old = '0'
        self.mode_set = '0'
        self.direction_state = 0
        self._stop_event = threading.Event()
        self.setWindowTitle('Riadenie kolotoča')

        # Create a tab widget
        self.tabs = QTabWidget()

        # RUN
        tab1 = self.control()
        self.tabs.addTab(tab1, 'Riadenie')

        # SETUP
        tab2 = self.net_setup()
        self.tabs.addTab(tab2, 'Pripojenie')

        # HELP
        tab3 = self.help_in()
        self.tabs.addTab(tab3, 'Pomoc')

        self.layout2 = QVBoxLayout()
        self.layout2.addWidget(self.tabs)
        self.setLayout(self.layout2)
        self.setGeometry(50, 50, 400, 100)

    def control(self):
        tab = QWidget()
        self.layout_main = QVBoxLayout()
        tab.setLayout(self.layout_main)

        layout_sub1 = QHBoxLayout()
        layout_sub2 = QVBoxLayout()
        layout_sub3 = QHBoxLayout()
        self.btn_run = QPushButton('Start')
        self.btn_run.setStyleSheet('background-color: green; color: white')
        self.btn_stop = QPushButton('Stop')
        self.btn_stop.setStyleSheet('background-color: red; color: white')
        layout_sub3.addWidget(self.btn_run)
        layout_sub3.addWidget(self.btn_stop)
        layout_sub2.addLayout(layout_sub3)
        self.btn_auto = QPushButton('Auto')
        self.btn_menu = self.menu()
        self.btn_direction = QPushButton('Direction')
        self.btn_direction.setCheckable(True)
        layout_sub2.addWidget(self.btn_auto)
        layout_sub2.addWidget(self.btn_menu)
        layout_sub2.addWidget(self.btn_direction)
        layout_sub1.addLayout(layout_sub2)
        layout_sub1.setAlignment(Qt.AlignLeft)

        layout_info = QVBoxLayout()
        self.led2 = LedIndicator()
        self.led2.setDisabled(True)
        layout_info.addWidget(self.led2, alignment=Qt.AlignTop)
        layout_sub1.addLayout(layout_info)

        self.layout_main.addLayout(layout_sub1)

        self.btn_run.clicked.connect(self.runScript)
        self.btn_stop.clicked.connect(self.stopScript)
        self.btn_auto.clicked.connect(self.runAuto)
        self.btn_direction.clicked.connect(self.set_direction)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.setValue(1)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.valueChanged.connect(self.speed_change)
        self.layout_main.addWidget(self.slider)
        self.layout_main.setAlignment(Qt.AlignTop)

        font = QFont()
        vbox = QVBoxLayout()
        font.setPointSize(12)
        self.speed = QLabel('Rýchlosť')
        self.speed.setFont(font)
        vbox.setContentsMargins(0,40,0,0)
        vbox.addWidget(self.speed, alignment=Qt.AlignCenter)
        self.layout_main.addLayout(vbox)

        return tab

    def net_setup(self):
        tab = QWidget()
        self.tabs.addTab(tab, 'Network Setup')
        self.layout = QVBoxLayout()
        tab.setLayout(self.layout)

        layout_main = QVBoxLayout()
        self.switch = QCheckBox('Auto IP')
        layout_main.addWidget(self.switch)
        self.switch.clicked.connect(self.net_mode_switch)
        self.switch.setChecked(True)

        layout_ip = QHBoxLayout()
        self.ip = QLineEdit()
        self.ip.setText('1.1.1.1')
        iv3 = IP4ValidatorBasic()
        self.ip.setValidator(iv3)

        layout_ip.addWidget(QLabel('IP: '))
        layout_ip.addWidget(self.ip)
        layout_main.addLayout(layout_ip)

        layout_user = QHBoxLayout()
        self.username = QLineEdit()
        layout_user.addWidget(QLabel('Meno: '))
        layout_user.addWidget(self.username)
        layout_main.addLayout(layout_user)
        self.layout.addLayout(layout_main)

        layout_psw = QHBoxLayout()
        self.psw = QLineEdit()
        layout_psw.addWidget(QLabel('Heslo: '))
        layout_psw.addWidget(self.psw)
        layout_main.addLayout(layout_psw)

        layout_test = QHBoxLayout()
        self.test = QPushButton('Test')
        self.test.clicked.connect(self.connection_test)
        self.search = QPushButton('Nájdi')
        self.search.clicked.connect(self.connection_search)
        layout_test.addWidget(self.test)
        layout_test.addWidget(self.search)
        layout_main.addLayout(layout_test)

        self.test_output = QTextEdit()
        layout_main.addWidget(self.test_output)

        self.net_mode_switch()

        return tab

    def help_in(self):
        tab = QWidget()
        self.tabs.addTab(tab, 'Pomoc')
        self.layout = QVBoxLayout()
        tab.setLayout(self.layout)

        layout_main = QVBoxLayout()
        self.help = QLabel(TEXT)
        # self.help = QPushButton()
        self.help.setWordWrap(True)
        layout_main.addWidget(self.help)
        self.layout.addLayout(layout_main)

        return tab

    def speed_change(self):
        self.speed.setText(f'<p>Rýchlosť: {str(self.slider.value())}<p>')

    def set_direction(self):
        self.direction_state = 0
        self.btn_direction.setText('V msere hodin')
        if self.btn_direction.isChecked():
            self.direction_state = 1
            self.btn_direction.setText('Proti smeru hodin')

    def net_mode_switch(self):
        if self.switch.isChecked():
            self.ip.setText(NETWORK[0])
            self.username.setText(NETWORK[1])
            self.psw.setText(NETWORK[2])
            self.ip.setEnabled(False)
            self.username.setEnabled(False)
            self.psw.setEnabled(False)
            self.psw.setEchoMode(QLineEdit.Password)
        else:
            self.username.setText('')
            self.psw.setText('')
            self.ip.setText('1.1.1.1')
            self.ip.setEnabled(True)
            self.username.setEnabled(True)
            self.psw.setEnabled(True)

    def menu(self):
        menu = QMenu(self)
        menu.addAction(self._action('Bez algoritmov', 0))
        menu.addSeparator()
        menu.addAction(self._action('ZV', 1))
        menu.addAction(self._action('ZVD', 2))
        menu.addAction(self._action('Kombinované', 3))
        menu.triggered.connect(self.mode)
        self.video_scale_button = QPushButton()
        self.video_scale_button.setText('Metóda')
        self.video_scale_button.setMenu(menu)
        self.video_scale_button.setToolTip('Video digital zoom')
        # tb.addWidget(self.video_scale_button)

        return self.video_scale_button

    def _action(self, text, data) ->QAction:
        rt = QAction(text, parent=self)
        rt.setData(data)
        return rt

    def mode(self, action):
        self.video_scale_button.setText(action.text())
        self.mode_set = str(action.data())

    @pyqtSlot()
    def runScript(self):
        try:
            input = str(self.slider.value())
            command = f'{PATH} {input} {self.old} {self.mode_set} {self.direction_state}'
            self.old = input
            self.start_script(command)
            self.led2.setChecked(True)
        except Exception as e:
            print(f'Run error {e}')

    @pyqtSlot()
    def runAuto(self):
        try:
            input = str(self.slider.value())
            command = f'{PATH} {self.mode_set} {self.old} {AUTO} {self.direction_state}'
            self.old = input
            self.start_script(command)
            # self.led2.setChecked(True)
        except Exception as e:
            print(f'Auto run error {e}')

    def connect(self):
        try:
            if self.switch.checkState():
                self.client = paramiko.SSHClient()
                self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.client.connect(NETWORK[0], username=NETWORK[1], password=NETWORK[2])
            else:
                self.client = paramiko.SSHClient()
                self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.client.connect(self.ip.text(), username=self.username.text(), password=self.psw.text())
        except Exception as e:
            print(f'Connect error {e}')

    def connection_search(self):
        try:
            discover = Discoverer()
            output = discover.discover()
            self.test_output.clear()
            if output == []:
                self.test_output.setText('Nič sa nenašlo')
                return
            for item in output:
                self.test_output.setText(f'{item}')
        except Exception as e:
            print(f'Search error {e}')

    def connection_test(self):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ip = self.ip.text()
            user = self.username.text()
            psw = self.psw.text()
            client.connect(ip, username=user, password=psw)
            client.close()
            self.test_output.clear()
            self.test_output.setText('Connection test successful!')
        except Exception as e:
            self.test_output.clear()
            self.test_output.setText(f'Connection test Fail! {e}')

    def start_script(self, command):
        if self.client is None:
            self.connect()
        self.channel = self.client.invoke_shell()
        self.channel.send(command + '\n')
        self._stop_event.clear()

    def stopScript(self):
        input = str(self.slider.value())
        command = f'{PATH} {0} {self.old} {self.mode_set} {self.direction_state}'
        self.old = input
        self.start_script(command)
        self.led2.setChecked(False)

    def saveStop(self):
        if self.channel is not None:
            self.channel.send('\x03')
        self._stop_event.set()

    def _read_output(self):
        while not self._stop_event.is_set():
            if self.channel.recv_ready():
                data = self.channel.recv(1024)
                print(data.decode('utf-8'), end='')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    qtmodern.set_theme(app, 'qtmodern-dark')
    mainWindow = MyWidget()
    mainWindow.show()
    sys.exit(app.exec_())

