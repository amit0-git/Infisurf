#Author:Amit Verma
#Date: 27-01-2024

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
import threading
import requests as r
import time

timeout = 5


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(796, 584)
        MainWindow.setFixedSize(796, 584)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("res/wi-fi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow{\n" "border-radius:10px;\n" "\n" "}")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        MainWindow.setDockOptions(
            QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(158, 112, 633, 471))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.stackedWidget.sizePolicy().hasHeightForWidth()
        )
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setMouseTracking(True)
        self.stackedWidget.setTabletTracking(True)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setStyleSheet(
            "\n"
            "\n"
            "QWidget{\n"
            "\n"
            "\n"
            "background-image:url(res/richard-horvath-cPccYbPrF-A-unsplash.jpg);\n"
            "border-radius:10px;\n"
            "\n"
            "\n"
            "\n"
            "\n"
            "}"
        )
        self.page_1.setObjectName("page_1")
        self.loginFrame = QtWidgets.QFrame(self.page_1)
        self.loginFrame.setGeometry(QtCore.QRect(80, 40, 481, 371))
        self.loginFrame.setStyleSheet(
            "QFrame{\n" "background:white;\n" "border-radius:10px;\n" "}\n" "\n" ""
        )
        self.loginFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginFrame.setObjectName("loginFrame")
        self.label = QtWidgets.QLabel(self.loginFrame)
        self.label.setGeometry(QtCore.QRect(190, 20, 91, 91))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("res/wifi.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.username = QtWidgets.QLineEdit(self.loginFrame)
        self.username.setGeometry(QtCore.QRect(140, 140, 201, 31))
        self.username.setStyleSheet(
            "QLineEdit{\n"
            "border:none;\n"
            "border-bottom:1px solid black;\n"
            "text-align:center;\n"
            "background:white;\n"
            "border-radius:none;\n"
            "\n"
            "}\n"
            "QLineEdit:focus{\n"
            "\n"
            "border:1px solid grey;\n"
            "border-radius:7px;\n"
            "padding:5px;\n"
            "}"
        )
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.loginFrame)
        self.password.setGeometry(QtCore.QRect(140, 190, 201, 31))
        self.password.setStyleSheet(
            "QLineEdit{\n"
            "border:none;\n"
            "border-bottom:1px solid black;\n"
            "text-align:center;\n"
            "background:white;\n"
            "border-radius:none;\n"
            "\n"
            "}\n"
            "QLineEdit:focus{\n"
            "\n"
            "border:1px solid grey;\n"
            "border-radius:7px;\n"
            "padding:5px;\n"
            "}"
        )
        self.password.setObjectName("password")
        self.loginButton = QtWidgets.QPushButton(self.loginFrame)
        self.loginButton.setGeometry(QtCore.QRect(160, 250, 161, 41))
        self.loginButton.setStyleSheet(
            "QPushButton{\n"
            "background:rgb(0, 255, 127);\n"
            "color:white;\n"
            "font-weight:bold;\n"
            "font-size:20px;\n"
            "padding:6px;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background:rgb(16, 213, 33)\n"
            "}"
        )
        self.loginButton.setObjectName("loginButton")
        self.login_status = QtWidgets.QLabel(self.loginFrame)
        self.login_status.setGeometry(QtCore.QRect(80, 310, 321, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.login_status.setFont(font)
        self.login_status.setAlignment(QtCore.Qt.AlignCenter)
        self.login_status.setObjectName("login_status")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet(
            "QWidget{\n"
            "background-image:url(res/codioful-formerly-gradienta-OzfD79w8ptA-unsplash.jpg);\n"
            "color:white;\n"
            "\n"
            "\n"
            "border-radius:10px;\n"
            "\n"
            "\n"
            "\n"
            "\n"
            "}"
        )
        self.page_2.setObjectName("page_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 591, 151))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(
            "QLabel{\n" "\n" '    font: 12pt "MV Boli";\n' "background:none;\n" "}"
        )
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 161, 31))
        self.label_5.setStyleSheet(
            "QLabel{\n"
            'font: 15pt "MV Boli";\n'
            "text-decoration: underline;\n"
            "}\n"
            ""
        )
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(20, 230, 411, 131))
        self.label_6.setStyleSheet(
            "QLabel{\n" 'font: 12pt "MV Boli";\n' "background:none;\n" "\n" "}"
        )
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(20, 360, 581, 101))
        self.label_7.setStyleSheet(
            "QLabel{\n" 'font: 12pt "MV Boli";\n' "background:none;\n" "}"
        )
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setStyleSheet(
            "QWidget{\n"
            "background-image:url(res/codioful-formerly-gradienta-bKESVqfxass-unsplash.jpg);\n"
            "\n"
            "border-radius:10px;\n"
            "\n"
            "color:white;\n"
            "\n"
            "}"
        )
        self.page_3.setObjectName("page_3")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 521, 51))
        self.label_4.setStyleSheet(
            "QLabel{\n" '    font: 13pt "MV Boli";\n' "background:none;\n" "}"
        )
        self.label_4.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.page_3)
        self.label_8.setGeometry(QtCore.QRect(240, 30, 141, 141))
        self.label_8.setStyleSheet("QLabel{\n" "background:none;\n" "}")
        self.label_8.setText("")
        self.label_8.setPixmap(
            QtGui.QPixmap("res/Blue Modern Business Linktree Profile Image.png")
        )
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_3)
        self.label_9.setGeometry(QtCore.QRect(20, 230, 581, 71))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(
            "QLabel{\n" 'font: 12pt "MV Boli";\n' "background:none;\n" "\n" "}"
        )
        self.label_9.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setGeometry(QtCore.QRect(20, 320, 581, 71))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(
            "QLabel{\n" 'font: 12pt "MV Boli";\n' "background:none;\n" "\n" "}"
        )
        self.label_10.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.stackedWidget.addWidget(self.page_3)
        self.sidebar = QtWidgets.QWidget(self.centralwidget)
        self.sidebar.setGeometry(QtCore.QRect(0, 0, 160, 581))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.sidebar.setFont(font)
        self.sidebar.setStyleSheet(
            "QWidget{\n" "background-color:white;\n" "text-align:left;\n" "\n" "\n" "}"
        )
        self.sidebar.setObjectName("sidebar")
        self.connectButton = QtWidgets.QPushButton(self.sidebar)
        self.connectButton.setGeometry(QtCore.QRect(20, 180, 131, 42))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.connectButton.sizePolicy().hasHeightForWidth()
        )
        self.connectButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.connectButton.setFont(font)
        self.connectButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.connectButton.setAutoFillBackground(False)
        self.connectButton.setStyleSheet(
            "QPushButton{\n"
            "\n"
            "\n"
            "background-color:rgb(0, 255, 255);\n"
            "border-radius:7px;\n"
            "padding-left:5px;\n"
            "font-weight:bold;\n"
            "color:white;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "border:1px solid black;\n"
            "}"
        )
        self.connectButton.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates)
        )
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("res/transfer.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.connectButton.setIcon(icon1)
        self.connectButton.setIconSize(QtCore.QSize(30, 30))
        self.connectButton.setDefault(False)
        self.connectButton.setFlat(False)
        self.connectButton.setObjectName("connectButton")
        self.srmsLogo = QtWidgets.QLabel(self.sidebar)
        self.srmsLogo.setGeometry(QtCore.QRect(10, 20, 131, 131))
        self.srmsLogo.setText("")
        self.srmsLogo.setPixmap(QtGui.QPixmap("res/srms.png"))
        self.srmsLogo.setScaledContents(True)
        self.srmsLogo.setObjectName("srmsLogo")
        self.helptButton = QtWidgets.QPushButton(self.sidebar)
        self.helptButton.setGeometry(QtCore.QRect(20, 240, 131, 42))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.helptButton.setFont(font)
        self.helptButton.setStyleSheet(
            "QPushButton{\n"
            "\n"
            "background-color:rgb(0, 170, 127);\n"
            "border-radius:7px;\n"
            "padding-left:5px;\n"
            "font-weight:bold;\n"
            "color:white;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "border:1px solid black;\n"
            "}"
        )
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("res/helping-hand.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.helptButton.setIcon(icon2)
        self.helptButton.setIconSize(QtCore.QSize(30, 30))
        self.helptButton.setObjectName("helptButton")
        self.aboutButton = QtWidgets.QPushButton(self.sidebar)
        self.aboutButton.setGeometry(QtCore.QRect(20, 310, 131, 42))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.aboutButton.setFont(font)
        self.aboutButton.setStyleSheet(
            "QPushButton{\n"
            "\n"
            "background-color:rgb(84, 138, 255);\n"
            "border-radius:7px;\n"
            "padding-left:5px;\n"
            "font-weight:bold;\n"
            "color:white;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "border:1px solid black;\n"
            "}"
        )
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap("res/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.aboutButton.setIcon(icon3)
        self.aboutButton.setIconSize(QtCore.QSize(30, 30))
        self.aboutButton.setObjectName("aboutButton")
        self.githubButton = QtWidgets.QPushButton(self.sidebar)
        self.githubButton.setGeometry(QtCore.QRect(20, 370, 131, 42))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.githubButton.setFont(font)
        self.githubButton.setStyleSheet(
            "QPushButton{\n"
            "background-color:rgb(128, 173, 157);\n"
            "border-radius:7px;\n"
            "padding-left:5px;\n"
            "font-weight:bold;\n"
            "color:white;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "border:1px solid black;\n"
            "}"
        )
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap("res/github.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.githubButton.setIcon(icon4)
        self.githubButton.setIconSize(QtCore.QSize(30, 30))
        self.githubButton.setAutoDefault(False)
        self.githubButton.setObjectName("githubButton")
        self.linkedinButton = QtWidgets.QPushButton(self.sidebar)
        self.linkedinButton.setGeometry(QtCore.QRect(20, 430, 131, 42))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.linkedinButton.setFont(font)
        self.linkedinButton.setStyleSheet(
            "QPushButton{\n"
            "background-color:rgb(0, 170, 255);\n"
            "border-radius:7px;\n"
            "padding-left:5px;\n"
            "font-weight:bold;\n"
            "color:white;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "border:1px solid black;\n"
            "}"
        )
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap("res/linkedin.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.linkedinButton.setIcon(icon5)
        self.linkedinButton.setIconSize(QtCore.QSize(30, 30))
        self.linkedinButton.setAutoDefault(False)
        self.linkedinButton.setObjectName("linkedinButton")
        self.headFrame = QtWidgets.QFrame(self.centralwidget)
        self.headFrame.setGeometry(QtCore.QRect(160, 0, 631, 111))
        self.headFrame.setStyleSheet("QFrame{\n" "background:white;\n" "\n" "}")
        self.headFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.headFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headFrame.setObjectName("headFrame")
        self.mainHead = QtWidgets.QLabel(self.headFrame)
        self.mainHead.setGeometry(QtCore.QRect(80, 20, 511, 71))
        self.mainHead.setMinimumSize(QtCore.QSize(3, 0))
        self.mainHead.setBaseSize(QtCore.QSize(9, 0))
        self.mainHead.setStyleSheet(
            "QLabel{\n"
            "\n"
            "\n"
            '    font: 30pt "Consolas";\n'
            "width:auto;\n"
            "color:white;\n"
            "\n"
            "}\n"
            ""
        )
        self.mainHead.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mainHead.setText("")
        self.mainHead.setTextFormat(QtCore.Qt.AutoText)
        self.mainHead.setPixmap(QtGui.QPixmap("res/name.png"))
        self.mainHead.setAlignment(QtCore.Qt.AlignCenter)
        self.mainHead.setWordWrap(True)
        self.mainHead.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.mainHead.setObjectName("mainHead")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # set default cvalue in the username and password field
        self.username.setText("Harshitg")
        self.password.setText("harshit")

        # connect sidebar buttons with the stackedwidget pages
        self.connectButton.clicked.connect(lambda: self.switchPage(0))
        self.aboutButton.clicked.connect(lambda: self.switchPage(2))
        self.helptButton.clicked.connect(lambda: self.switchPage(1))

        #  open github
        self.githubButton.clicked.connect(self.openGithub)

        # open linkedin on btn click
        self.linkedinButton.clicked.connect(self.openLinkedin)

        # login button click action

        self.loginButton.clicked.connect(self.loginFn)

    def enable_button(self):
        # Enable the button

        self.loginButton.setEnabled(True)
        self.loginButton.setText("Login")

    def loginLogic(self, username, password):
        url = "http://172.16.1.16:8090/httpclient.html"

        session = r.Session()

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        login_data = {
            "mode": 191,
            "username": username,
            "password": password,
            "a": int(time.time() * 1000),  # (new Date()).getTime();
            "producttype": 2,  # for web 0 android 2
        }

        # make post request to the server
        try:
            response = session.post(
                url, data=login_data, headers=headers, timeout=timeout
            )

            if response.status_code == 200 and (
                "You are signed in as" in response.text
            ):
                print("You are connected successfully!")
                self.login_status.setStyleSheet("color: green;")
                self.login_status.setText("You are connected successfully!")
                # enable login button
                self.enable_button()

            else:
                self.login_status.setStyleSheet("color: red;")
                self.login_status.setText("You are not connected!")
                print(f"Login failed with status code {response.status_code}")

                print(response.text)
                # enable login button
                self.enable_button()

        except r.Timeout:
            # if the timeout occurs
            print("Request timeout")
            # enable login button
            self.enable_button()
            self.login_status.setStyleSheet("color: red;")
            self.login_status.setText("Request Timeout!")

        except Exception:
            # if any other exception occurs
            print("Other Exception")
            # enable login button
            self.enable_button()
            self.login_status.setStyleSheet("color: red;")
            self.login_status.setText("Some Error Occured!")

    def loginFn(self):
        """function to invoke on login button click"""

        username = self.username.text()
        password = self.password.text()

        if username == "" or password == "":
            self.login_status.setStyleSheet("color: red;")
            self.login_status.setText("Please Enter Username & Password!")

        else:
            # call the loginLogic function
            # disable the login button
            self.loginButton.setEnabled(False)
            self.loginButton.setText("Loading..")
        #     start the request part in the new thread to avoid UI unresponsiveness

            thread = threading.Thread(target=self.loginLogic, args=(username, password))
            # start the thread
            thread.start()

            # self.loginLogic(username,password)

            print(username, password)

    def switchPage(self, index):
        # function to switch the pages of the stacked widget
        self.stackedWidget.setCurrentIndex(index)

    def openLinkedin(self):
        """function to open linkedin on linkedin button click"""
        url = QUrl("https://www.linkedin.com/in/amitk007/")
        QDesktopServices.openUrl(url)

    def openGithub(self):
        """function to open github on github button click"""
        url = QUrl("https://github.com/amit0-git/Infisurf")
        QDesktopServices.openUrl(url)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Infisurf"))
        self.username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.login_status.setText(_translate("MainWindow", "You are not connected!"))
        self.label_3.setText(
            _translate(
                "MainWindow",
                "🛜Infisurf is a Hostel Wifi Login tool - it is designed to access hostel wifi without logging in through browser. The Hostel/College Wifi will logout when the system is inactive for some time.\n"
                "Infisurf is designed to solve this problem.",
            )
        )
        self.label_5.setText(_translate("MainWindow", "Steps to use-"))
        self.label_6.setText(
            _translate(
                "MainWindow",
                "1. Connect to Hostel/College Wifi\n"
                "2. Open Infisurf and go to Connect\n"
                "3. Enter Username and Password of wifi\n"
                "4. Press Login and enjoy :-)",
            )
        )
        self.label_7.setText(
            _translate(
                "MainWindow",
                "Please visit https://github.com/amit0-git/Infisurf/download to download the app",
            )
        )
        self.label_4.setText(
            _translate("MainWindow", "Designed and developed by Amit Verma :-) 😎 ")
        )
        self.label_9.setText(
            _translate(
                "MainWindow",
                "This app is open source, contribute at 🌐 https://github.com/amit0-git/Infisurf",
            )
        )
        self.label_10.setText(
            _translate(
                "MainWindow",
                "If you have any queries please contact at 📧root.avanti@gmail.com",
            )
        )
        self.connectButton.setToolTip(
            _translate(
                "MainWindow", "<html><head/><body><p>Connect To Wifi</p></body></html>"
            )
        )
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.helptButton.setToolTip(_translate("MainWindow", "About the app"))
        self.helptButton.setText(_translate("MainWindow", "Help"))
        self.aboutButton.setToolTip(_translate("MainWindow", "About the Developer"))
        self.aboutButton.setText(_translate("MainWindow", "About"))
        self.githubButton.setToolTip(
            _translate("MainWindow", "Open Source Contribution")
        )
        self.githubButton.setText(_translate("MainWindow", "Github"))
        self.linkedinButton.setToolTip(_translate("MainWindow", "LinkedIn Account"))
        self.linkedinButton.setText(_translate("MainWindow", "LinkedIn"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
