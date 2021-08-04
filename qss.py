qss_flat_white = """
QPalette{background:#FFFFFF;}*{outline:0px;color:#57595B;}

QWidget[form="true"],QLabel[frameShape="1"]{
border:1px solid #B6B6B6;
border-radius:0px;
}

QWidget[form="bottom"]{
background:#E4E4E4;
}

QWidget[form="bottom"] .QFrame{
border:1px solid #57595B;
}

QWidget[form="bottom"] QLabel,QWidget[form="title"] QLabel{
border-radius:0px;
color:#57595B;
background:none;
border-style:none;
}

QWidget[form="title"],QWidget[nav="left"],QWidget[nav="top"] QAbstractButton{
border-style:none;
border-radius:0px;
padding:5px;
color:#57595B;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);
}

QWidget[nav="top"] QAbstractButton:hover,QWidget[nav="top"] QAbstractButton:pressed,QWidget[nav="top"] QAbstractButton:checked{
border-style:solid;
border-width:0px 0px 2px 0px;
padding:4px 4px 2px 4px;
border-color:#00BB9E;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);
}

QWidget[nav="left"] QAbstractButton{
border-radius:0px;
color:#57595B;
background:none;
border-style:none;
}

QWidget[nav="left"] QAbstractButton:hover{
color:#FFFFFF;
background-color:#00BB9E;
}

QWidget[nav="left"] QAbstractButton:checked,QWidget[nav="left"] QAbstractButton:pressed{
color:#57595B;
border-style:solid;
border-width:0px 0px 0px 2px;
padding:4px 4px 4px 2px;
border-color:#00BB9E;
background-color:#FFFFFF;
}

QWidget[video="true"] QLabel{
color:#57595B;
border:1px solid #B6B6B6;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);
}

QWidget[video="true"] QLabel:focus{
border:1px solid #00BB9E;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);
}

QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
border:1px solid #B6B6B6;
border-radius:3px;
padding:2px;
background:none;
selection-background-color:#00BB9E;
selection-color:#FFFFFF;
}

QLineEdit:focus,QTextEdit:focus,QPlainTextEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QComboBox:focus,QDateEdit:focus,QTimeEdit:focus,QDateTimeEdit:focus,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QSpinBox:hover,QDoubleSpinBox:hover,QComboBox:hover,QDateEdit:hover,QTimeEdit:hover,QDateTimeEdit:hover{
border:1px solid #B6B6B6;
}

QLineEdit[echoMode="2"]{
lineedit-password-character:9679;
}

.QFrame{
border:1px solid #B6B6B6;
border-radius:3px;
}

.QGroupBox{
border:1px solid #B6B6B6;
border-radius:5px;
margin-top:3ex;
}

.QGroupBox::title{
subcontrol-origin:margin;
position:relative;
left:10px;
}

.QPushButton,.QToolButton{
border-style:none;
border:1px solid #B6B6B6;
color:#57595B;
padding:5px;
min-height:15px;
border-radius:5px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);
}

.QPushButton:hover,.QToolButton:hover{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);
}

.QPushButton:pressed,.QToolButton:pressed{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);
}

.QToolButton::menu-indicator{
image:None;
}

QToolButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{
border-radius:3px;
color:#57595B;
padding:3px;
margin:0px;
background:none;
border-style:none;
}

QToolButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{
color:#FFFFFF;
margin:1px 1px 2px 1px;
background-color:rgba(51,127,209,230);
}

QPushButton#btnMenu_Close:hover{
color:#FFFFFF;
margin:1px 1px 2px 1px;
background-color:rgba(238,0,0,128);
}

QRadioButton::indicator{
width:15px;
height:15px;
}

QRadioButton::indicator::unchecked{
image:url(:/qss/flatwhite/radiobutton_unchecked.png);
}

QRadioButton::indicator::unchecked:disabled{
image:url(:/qss/flatwhite/radiobutton_unchecked_disable.png);
}

QRadioButton::indicator::checked{
image:url(:/qss/flatwhite/radiobutton_checked.png);
}

QRadioButton::indicator::checked:disabled{
image:url(:/qss/flatwhite/radiobutton_checked_disable.png);
}

QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
padding:0px -3px 0px 0px;
}

QCheckBox::indicator,QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
width:13px;
height:13px;
}

QCheckBox::indicator:unchecked,QGroupBox::indicator:unchecked,QTreeWidget::indicator:unchecked,QListWidget::indicator:unchecked{
image:url(:/qss/flatwhite/checkbox_unchecked.png);
}

QCheckBox::indicator:unchecked:disabled,QGroupBox::indicator:unchecked:disabled,QTreeWidget::indicator:unchecked:disabled,QListWidget::indicator:disabled{
image:url(:/qss/flatwhite/checkbox_unchecked_disable.png);
}

QCheckBox::indicator:checked,QGroupBox::indicator:checked,QTreeWidget::indicator:checked,QListWidget::indicator:checked{
image:url(:/qss/flatwhite/checkbox_checked.png);
}

QCheckBox::indicator:checked:disabled,QGroupBox::indicator:checked:disabled,QTreeWidget::indicator:checked:disabled,QListWidget::indicator:checked:disabled{
image:url(:/qss/flatwhite/checkbox_checked_disable.png);
}

QCheckBox::indicator:indeterminate,QGroupBox::indicator:indeterminate,QTreeWidget::indicator:indeterminate,QListWidget::indicator:indeterminate{
image:url(:/qss/flatwhite/checkbox_parcial.png);
}

QCheckBox::indicator:indeterminate:disabled,QGroupBox::indicator:indeterminate:disabled,QTreeWidget::indicator:indeterminate:disabled,QListWidget::indicator:indeterminate:disabled{
image:url(:/qss/flatwhite/checkbox_parcial_disable.png);
}

QTimeEdit::up-button,QDateEdit::up-button,QDateTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button{
image:url(:/qss/flatwhite/add_top.png);
width:10px;
height:10px;
padding:2px 5px 0px 0px;
}

QTimeEdit::down-button,QDateEdit::down-button,QDateTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button{
image:url(:/qss/flatwhite/add_bottom.png);
width:10px;
height:10px;
padding:0px 5px 2px 0px;
}

QTimeEdit::up-button:pressed,QDateEdit::up-button:pressed,QDateTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{
top:-2px;
}

QTimeEdit::down-button:pressed,QDateEdit::down-button:pressed,QDateTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{
bottom:-2px;
}

QComboBox::down-arrow,QDateEdit[calendarPopup="true"]::down-arrow,QTimeEdit[calendarPopup="true"]::down-arrow,QDateTimeEdit[calendarPopup="true"]::down-arrow{
image:url(:/qss/flatwhite/add_bottom.png);
width:10px;
height:10px;
right:2px;
}

QComboBox::drop-down,QDateEdit::drop-down,QTimeEdit::drop-down,QDateTimeEdit::drop-down{
subcontrol-origin:padding;
subcontrol-position:top right;
width:15px;
border-left-width:0px;
border-left-style:solid;
border-top-right-radius:3px;
border-bottom-right-radius:3px;
border-left-color:#B6B6B6;
}

QComboBox::drop-down:on{
top:1px;
}

QMenuBar::item{
color:#57595B;
background-color:#E4E4E4;
margin:0px;
padding:3px 10px;
}

QMenu,QMenuBar,QMenu:disabled,QMenuBar:disabled{
color:#57595B;
background-color:#E4E4E4;
border:1px solid #B6B6B6;
margin:0px;
}

QMenu::item{
padding:3px 20px;
}

QMenu::indicator{
width:13px;
height:13px;
}

QMenu::item:selected,QMenuBar::item:selected{
color:#57595B;
border:0px solid #B6B6B6;
background:#F6F6F6;
}

QMenu::separator{
height:1px;
background:#B6B6B6;
}

QProgressBar{
min-height:10px;
background:#E4E4E4;
border-radius:5px;
text-align:center;
border:1px solid #E4E4E4;
}

QProgressBar:chunk{
border-radius:5px;
background-color:#B6B6B6;
}

QSlider::groove:horizontal{
background:#E4E4E4;
height:8px;
border-radius:4px;
}

QSlider::add-page:horizontal{
background:#E4E4E4;
height:8px;
border-radius:4px;
}

QSlider::sub-page:horizontal{
background:#B6B6B6;
height:8px;
border-radius:4px;
}

QSlider::handle:horizontal{
width:13px;
margin-top:-3px;
margin-bottom:-3px;
border-radius:6px;
background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #FFFFFF,stop:0.8 #B6B6B6);
}

QSlider::groove:vertical{
width:8px;
border-radius:4px;
background:#E4E4E4;
}

QSlider::add-page:vertical{
width:8px;
border-radius:4px;
background:#E4E4E4;
}

QSlider::sub-page:vertical{
width:8px;
border-radius:4px;
background:#B6B6B6;
}

QSlider::handle:vertical{
height:14px;
margin-left:-3px;
margin-right:-3px;
border-radius:6px;
background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #FFFFFF,stop:0.8 #B6B6B6);
}

QScrollBar:horizontal{
background:#E4E4E4;
padding:0px;
border-radius:6px;
max-height:12px;
}

QScrollBar::handle:horizontal{
background:#B6B6B6;
min-width:50px;
border-radius:6px;
}

QScrollBar::handle:horizontal:hover{
background:#00BB9E;
}

QScrollBar::handle:horizontal:pressed{
background:#00BB9E;
}

QScrollBar::add-page:horizontal{
background:none;
}

QScrollBar::sub-page:horizontal{
background:none;
}

QScrollBar::add-line:horizontal{
background:none;
}

QScrollBar::sub-line:horizontal{
background:none;
}

QScrollBar:vertical{
background:#E4E4E4;
padding:0px;
border-radius:6px;
max-width:12px;
}

QScrollBar::handle:vertical{
background:#B6B6B6;
min-height:50px;
border-radius:6px;
}

QScrollBar::handle:vertical:hover{
background:#00BB9E;
}

QScrollBar::handle:vertical:pressed{
background:#00BB9E;
}

QScrollBar::add-page:vertical{
background:none;
}

QScrollBar::sub-page:vertical{
background:none;
}

QScrollBar::add-line:vertical{
background:none;
}

QScrollBar::sub-line:vertical{
background:none;
}

QScrollArea{
border:0px;
}

QTreeView,QListView,QTableView,QTabWidget::pane{
border:1px solid #B6B6B6;
selection-background-color:#F6F6F6;
selection-color:#57595B;
alternate-background-color:#F6F6F6;
gridline-color:#B6B6B6;
}

QTreeView::branch:closed:has-children{
margin:4px;
border-image:url(:/qss/flatwhite/branch_open.png);
}

QTreeView::branch:open:has-children{
margin:4px;
border-image:url(:/qss/flatwhite/branch_close.png);
}

QTreeView,QListView,QTableView,QSplitter::handle,QTreeView::branch{
background:#FFFFFF;
}

QTableView::item:selected,QListView::item:selected,QTreeView::item:selected{
color:#57595B;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);
}

QTableView::item:hover,QListView::item:hover,QTreeView::item:hover,QHeaderView{
color:#57595B;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);
}

QTableView::item,QListView::item,QTreeView::item{
padding:1px;
margin:0px;
}

QHeaderView::section,QTableCornerButton:section{
padding:3px;
margin:0px;
color:#57595B;
border:1px solid #B6B6B6;
border-left-width:0px;
border-right-width:1px;
border-top-width:0px;
border-bottom-width:1px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);
}

QTabBar::tab{
border:1px solid #B6B6B6;
color:#57595B;
margin:0px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);
}

QTabBar::tab:selected,QTabBar::tab:hover{
border-style:solid;
border-color:#00BB9E;
background:#FFFFFF;
}

QTabBar::tab:top,QTabBar::tab:bottom{
padding:3px 8px 3px 8px;
}

QTabBar::tab:left,QTabBar::tab:right{
padding:8px 3px 8px 3px;
}

QTabBar::tab:top:selected,QTabBar::tab:top:hover{
border-width:2px 0px 0px 0px;
}

QTabBar::tab:right:selected,QTabBar::tab:right:hover{
border-width:0px 0px 0px 2px;
}

QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{
border-width:0px 0px 2px 0px;
}

QTabBar::tab:left:selected,QTabBar::tab:left:hover{
border-width:0px 2px 0px 0px;
}

QTabBar::tab:first:top:selected,QTabBar::tab:first:top:hover,QTabBar::tab:first:bottom:selected,QTabBar::tab:first:bottom:hover{
border-left-width:1px;
border-left-color:#B6B6B6;
}

QTabBar::tab:first:left:selected,QTabBar::tab:first:left:hover,QTabBar::tab:first:right:selected,QTabBar::tab:first:right:hover{
border-top-width:1px;
border-top-color:#B6B6B6;
}

QTabBar::tab:last:top:selected,QTabBar::tab:last:top:hover,QTabBar::tab:last:bottom:selected,QTabBar::tab:last:bottom:hover{
border-right-width:1px;
border-right-color:#B6B6B6;
}

QTabBar::tab:last:left:selected,QTabBar::tab:last:left:hover,QTabBar::tab:last:right:selected,QTabBar::tab:last:right:hover{
border-bottom-width:1px;
border-bottom-color:#B6B6B6;
}

QStatusBar::item{
border:0px solid #E4E4E4;
border-radius:3px;
}

QToolBox::tab,QGroupBox#gboxDevicePanel,QGroupBox#gboxDeviceTitle,QFrame#gboxDevicePanel,QFrame#gboxDeviceTitle{
padding:3px;
border-radius:5px;
color:#57595B;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);
}

QToolTip{
border:0px solid #57595B;
padding:1px;
color:#57595B;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);
}

QToolBox::tab:selected{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);
}

QPrintPreviewDialog QToolButton{
border:0px solid #57595B;
border-radius:0px;
margin:0px;
padding:3px;
background:none;
}

QColorDialog QPushButton,QFileDialog QPushButton{
min-width:80px;
}

QToolButton#qt_calendar_prevmonth{
icon-size:0px;
min-width:20px;
image:url(:/qss/flatwhite/calendar_prevmonth.png);
}

QToolButton#qt_calendar_nextmonth{
icon-size:0px;
min-width:20px;
image:url(:/qss/flatwhite/calendar_nextmonth.png);
}

QToolButton#qt_calendar_prevmonth,QToolButton#qt_calendar_nextmonth,QToolButton#qt_calendar_monthbutton,QToolButton#qt_calendar_yearbutton{
border:0px solid #57595B;
border-radius:3px;
margin:3px 3px 3px 3px;
padding:3px;
background:none;
}

QToolButton#qt_calendar_prevmonth:hover,QToolButton#qt_calendar_nextmonth:hover,QToolButton#qt_calendar_monthbutton:hover,QToolButton#qt_calendar_yearbutton:hover,QToolButton#qt_calendar_prevmonth:pressed,QToolButton#qt_calendar_nextmonth:pressed,QToolButton#qt_calendar_monthbutton:pressed,QToolButton#qt_calendar_yearbutton:pressed{
border:1px solid #B6B6B6;
}

QCalendarWidget QSpinBox#qt_calendar_yearedit{
margin:2px;
}

QCalendarWidget QToolButton::menu-indicator{
image:None;
}

QCalendarWidget QTableView{
border-width:0px;
}

QCalendarWidget QWidget#qt_calendar_navigationbar{
border:1px solid #B6B6B6;
border-width:1px 1px 0px 1px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);
}

QComboBox QAbstractItemView::item{
min-height:20px;
min-width:10px;
}

QTableView[model="true"]::item{
padding:0px;
margin:0px;
}

QTableView QLineEdit,QTableView QComboBox,QTableView QSpinBox,QTableView QDoubleSpinBox,QTableView QDateEdit,QTableView QTimeEdit,QTableView QDateTimeEdit{
border-width:0px;
border-radius:0px;
}

QTableView QLineEdit:focus,QTableView QComboBox:focus,QTableView QSpinBox:focus,QTableView QDoubleSpinBox:focus,QTableView QDateEdit:focus,QTableView QTimeEdit:focus,QTableView QDateTimeEdit:focus{
border-width:0px;
border-radius:0px;
}

QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
background:#FFFFFF;
}

QTabWidget::pane:top{top:-1px;}
QTabWidget::pane:bottom{bottom:-1px;}
QTabWidget::pane:left{right:-1px;}
QTabWidget::pane:right{left:-1px;}

*:disabled{
background:#FFFFFF;
border-color:#E4E4E4;
color:#B6B6B6;
}

/*TextColor:#57595B*/
/*PanelColor:#FFFFFF*/
/*BorderColor:#B6B6B6*/
/*NormalColorStart:#E4E4E4*/
/*NormalColorEnd:#E4E4E4*/
/*DarkColorStart:#F6F6F6*/
/*DarkColorEnd:#F6F6F6*/
/*HighColor:#00BB9E*/"""

qss_light_blue = """
QPalette{background:#EAF7FF;}*{outline:0px;color:#386487;}

QWidget[form="true"],QLabel[frameShape="1"]{
border:1px solid #C0DCF2;
border-radius:0px;
}

QWidget[form="bottom"]{
background:#DEF0FE;
}

QWidget[form="bottom"] .QFrame{
border:1px solid #386487;
}

QWidget[form="bottom"] QLabel,QWidget[form="title"] QLabel{
border-radius:0px;
color:#386487;
background:none;
border-style:none;
}

QWidget[form="title"],QWidget[nav="left"],QWidget[nav="top"] QAbstractButton{
border-style:none;
border-radius:0px;
padding:5px;
color:#386487;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

QWidget[nav="top"] QAbstractButton:hover,QWidget[nav="top"] QAbstractButton:pressed,QWidget[nav="top"] QAbstractButton:checked{
border-style:solid;
border-width:0px 0px 2px 0px;
padding:4px 4px 2px 4px;
border-color:#00BB9E;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}

QWidget[nav="left"] QAbstractButton{
border-radius:0px;
color:#386487;
background:none;
border-style:none;
}

QWidget[nav="left"] QAbstractButton:hover{
color:#FFFFFF;
background-color:#00BB9E;
}

QWidget[nav="left"] QAbstractButton:checked,QWidget[nav="left"] QAbstractButton:pressed{
color:#386487;
border-style:solid;
border-width:0px 0px 0px 2px;
padding:4px 4px 4px 2px;
border-color:#00BB9E;
background-color:#EAF7FF;
}

QWidget[video="true"] QLabel{
color:#386487;
border:1px solid #C0DCF2;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

QWidget[video="true"] QLabel:focus{
border:1px solid #00BB9E;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}

QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
border:1px solid #C0DCF2;
border-radius:3px;
padding:2px;
background:none;
selection-background-color:#00BB9E;
selection-color:#FFFFFF;
}

QLineEdit:focus,QTextEdit:focus,QPlainTextEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QComboBox:focus,QDateEdit:focus,QTimeEdit:focus,QDateTimeEdit:focus,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QSpinBox:hover,QDoubleSpinBox:hover,QComboBox:hover,QDateEdit:hover,QTimeEdit:hover,QDateTimeEdit:hover{
border:1px solid #C0DCF2;
}

QLineEdit[echoMode="2"]{
lineedit-password-character:9679;
}

.QFrame{
border:1px solid #C0DCF2;
border-radius:3px;
}

.QGroupBox{
border:1px solid #C0DCF2;
border-radius:5px;
margin-top:3ex;
}

.QGroupBox::title{
subcontrol-origin:margin;
position:relative;
left:10px;
}

.QPushButton,.QToolButton{
border-style:none;
border:1px solid #C0DCF2;
color:#386487;
padding:5px;
min-height:15px;
border-radius:5px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

.QPushButton:hover,.QToolButton:hover{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}

.QPushButton:pressed,.QToolButton:pressed{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

.QToolButton::menu-indicator{
image:None;
}

QToolButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{
border-radius:3px;
color:#386487;
padding:3px;
margin:0px;
background:none;
border-style:none;
}

QToolButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{
color:#FFFFFF;
margin:1px 1px 2px 1px;
background-color:rgba(51,127,209,230);
}

QPushButton#btnMenu_Close:hover{
color:#FFFFFF;
margin:1px 1px 2px 1px;
background-color:rgba(238,0,0,128);
}

QRadioButton::indicator{
width:15px;
height:15px;
}

QRadioButton::indicator::unchecked{
image:url(:/qss/lightblue/radiobutton_unchecked.png);
}

QRadioButton::indicator::unchecked:disabled{
image:url(:/qss/lightblue/radiobutton_unchecked_disable.png);
}

QRadioButton::indicator::checked{
image:url(:/qss/lightblue/radiobutton_checked.png);
}

QRadioButton::indicator::checked:disabled{
image:url(:/qss/lightblue/radiobutton_checked_disable.png);
}

QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
padding:0px -3px 0px 0px;
}

QCheckBox::indicator,QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
width:13px;
height:13px;
}

QCheckBox::indicator:unchecked,QGroupBox::indicator:unchecked,QTreeWidget::indicator:unchecked,QListWidget::indicator:unchecked{
image:url(:/qss/lightblue/checkbox_unchecked.png);
}

QCheckBox::indicator:unchecked:disabled,QGroupBox::indicator:unchecked:disabled,QTreeWidget::indicator:unchecked:disabled,QListWidget::indicator:disabled{
image:url(:/qss/lightblue/checkbox_unchecked_disable.png);
}

QCheckBox::indicator:checked,QGroupBox::indicator:checked,QTreeWidget::indicator:checked,QListWidget::indicator:checked{
image:url(:/qss/lightblue/checkbox_checked.png);
}

QCheckBox::indicator:checked:disabled,QGroupBox::indicator:checked:disabled,QTreeWidget::indicator:checked:disabled,QListWidget::indicator:checked:disabled{
image:url(:/qss/lightblue/checkbox_checked_disable.png);
}

QCheckBox::indicator:indeterminate,QGroupBox::indicator:indeterminate,QTreeWidget::indicator:indeterminate,QListWidget::indicator:indeterminate{
image:url(:/qss/lightblue/checkbox_parcial.png);
}

QCheckBox::indicator:indeterminate:disabled,QGroupBox::indicator:indeterminate:disabled,QTreeWidget::indicator:indeterminate:disabled,QListWidget::indicator:indeterminate:disabled{
image:url(:/qss/lightblue/checkbox_parcial_disable.png);
}

QTimeEdit::up-button,QDateEdit::up-button,QDateTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button{
image:url(:/qss/lightblue/add_top.png);
width:10px;
height:10px;
padding:2px 5px 0px 0px;
}

QTimeEdit::down-button,QDateEdit::down-button,QDateTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button{
image:url(:/qss/lightblue/add_bottom.png);
width:10px;
height:10px;
padding:0px 5px 2px 0px;
}

QTimeEdit::up-button:pressed,QDateEdit::up-button:pressed,QDateTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{
top:-2px;
}
  
QTimeEdit::down-button:pressed,QDateEdit::down-button:pressed,QDateTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{
bottom:-2px;
}

QComboBox::down-arrow,QDateEdit[calendarPopup="true"]::down-arrow,QTimeEdit[calendarPopup="true"]::down-arrow,QDateTimeEdit[calendarPopup="true"]::down-arrow{
image:url(:/qss/lightblue/add_bottom.png);
width:10px;
height:10px;
right:2px;
}

QComboBox::drop-down,QDateEdit::drop-down,QTimeEdit::drop-down,QDateTimeEdit::drop-down{
subcontrol-origin:padding;
subcontrol-position:top right;
width:15px;
border-left-width:0px;
border-left-style:solid;
border-top-right-radius:3px;
border-bottom-right-radius:3px;
border-left-color:#C0DCF2;
}

QComboBox::drop-down:on{
top:1px;
}

QMenuBar::item{
color:#386487;
background-color:#DEF0FE;
margin:0px;
padding:3px 10px;
}

QMenu,QMenuBar,QMenu:disabled,QMenuBar:disabled{
color:#386487;
background-color:#DEF0FE;
border:1px solid #C0DCF2;
margin:0px;
}

QMenu::item{
padding:3px 20px;
}

QMenu::indicator{
width:13px;
height:13px;
}

QMenu::item:selected,QMenuBar::item:selected{
color:#386487;
border:0px solid #C0DCF2;
background:#F2F9FF;
}

QMenu::separator{
height:1px;
background:#C0DCF2;
}

QProgressBar{
min-height:10px;
background:#DEF0FE;
border-radius:5px;
text-align:center;
border:1px solid #DEF0FE;
}

QProgressBar:chunk{
border-radius:5px;
background-color:#C0DCF2;
}

QSlider::groove:horizontal{
background:#DEF0FE;
height:8px;
border-radius:4px;
}

QSlider::add-page:horizontal{
background:#DEF0FE;
height:8px;
border-radius:4px;
}

QSlider::sub-page:horizontal{
background:#C0DCF2;
height:8px;
border-radius:4px;
}

QSlider::handle:horizontal{
width:13px;
margin-top:-3px;
margin-bottom:-3px;
border-radius:6px;
background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #EAF7FF,stop:0.8 #C0DCF2);
}

QSlider::groove:vertical{
width:8px;
border-radius:4px;
background:#DEF0FE;
}

QSlider::add-page:vertical{
width:8px;
border-radius:4px;
background:#DEF0FE;
}

QSlider::sub-page:vertical{
width:8px;
border-radius:4px;
background:#C0DCF2;
}

QSlider::handle:vertical{
height:14px;
margin-left:-3px;
margin-right:-3px;
border-radius:6px;
background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #EAF7FF,stop:0.8 #C0DCF2);
}

QScrollBar:horizontal{
background:#DEF0FE;
padding:0px;
border-radius:6px;
max-height:12px;
}

QScrollBar::handle:horizontal{
background:#C0DCF2;
min-width:50px;
border-radius:6px;
}

QScrollBar::handle:horizontal:hover{
background:#00BB9E;
}

QScrollBar::handle:horizontal:pressed{
background:#00BB9E;
}

QScrollBar::add-page:horizontal{
background:none;
}

QScrollBar::sub-page:horizontal{
background:none;
}

QScrollBar::add-line:horizontal{
background:none;
}

QScrollBar::sub-line:horizontal{
background:none;
}

QScrollBar:vertical{
background:#DEF0FE;
padding:0px;
border-radius:6px;
max-width:12px;
}

QScrollBar::handle:vertical{
background:#C0DCF2;
min-height:50px;
border-radius:6px;
}

QScrollBar::handle:vertical:hover{
background:#00BB9E;
}

QScrollBar::handle:vertical:pressed{
background:#00BB9E;
}

QScrollBar::add-page:vertical{
background:none;
}

QScrollBar::sub-page:vertical{
background:none;
}

QScrollBar::add-line:vertical{
background:none;
}

QScrollBar::sub-line:vertical{
background:none;
}

QScrollArea{
border:0px;
}

QTreeView,QListView,QTableView,QTabWidget::pane{
border:1px solid #C0DCF2;
selection-background-color:#F2F9FF;
selection-color:#386487;
alternate-background-color:#DAEFFF;
gridline-color:#C0DCF2;
}

QTreeView::branch:closed:has-children{
margin:4px;
border-image:url(:/qss/lightblue/branch_open.png);
}

QTreeView::branch:open:has-children{
margin:4px;
border-image:url(:/qss/lightblue/branch_close.png);
}

QTreeView,QListView,QTableView,QSplitter::handle,QTreeView::branch{
background:#EAF7FF;
}

QTableView::item:selected,QListView::item:selected,QTreeView::item:selected{
color:#386487;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

QTableView::item:hover,QListView::item:hover,QTreeView::item:hover,QHeaderView{
color:#386487;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}

QTableView::item,QListView::item,QTreeView::item{
padding:1px;
margin:0px;
}

QHeaderView::section,QTableCornerButton:section{
padding:3px;
margin:0px;
color:#386487;
border:1px solid #C0DCF2;
border-left-width:0px;
border-right-width:1px;
border-top-width:0px;
border-bottom-width:1px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}

QTabBar::tab{
border:1px solid #C0DCF2;
color:#386487;
margin:0px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}

QTabBar::tab:selected,QTabBar::tab:hover{
border-style:solid;
border-color:#00BB9E;
background:#EAF7FF;
}

QTabBar::tab:top,QTabBar::tab:bottom{
padding:3px 8px 3px 8px;
}

QTabBar::tab:left,QTabBar::tab:right{
padding:8px 3px 8px 3px;
}

QTabBar::tab:top:selected,QTabBar::tab:top:hover{
border-width:2px 0px 0px 0px;
}

QTabBar::tab:right:selected,QTabBar::tab:right:hover{
border-width:0px 0px 0px 2px;
}

QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{
border-width:0px 0px 2px 0px;
}

QTabBar::tab:left:selected,QTabBar::tab:left:hover{
border-width:0px 2px 0px 0px;
}

QTabBar::tab:first:top:selected,QTabBar::tab:first:top:hover,QTabBar::tab:first:bottom:selected,QTabBar::tab:first:bottom:hover{
border-left-width:1px;
border-left-color:#C0DCF2;
}

QTabBar::tab:first:left:selected,QTabBar::tab:first:left:hover,QTabBar::tab:first:right:selected,QTabBar::tab:first:right:hover{
border-top-width:1px;
border-top-color:#C0DCF2;
}

QTabBar::tab:last:top:selected,QTabBar::tab:last:top:hover,QTabBar::tab:last:bottom:selected,QTabBar::tab:last:bottom:hover{
border-right-width:1px;
border-right-color:#C0DCF2;
}

QTabBar::tab:last:left:selected,QTabBar::tab:last:left:hover,QTabBar::tab:last:right:selected,QTabBar::tab:last:right:hover{
border-bottom-width:1px;
border-bottom-color:#C0DCF2;
}

QStatusBar::item{
border:0px solid #DEF0FE;
border-radius:3px;
}

QToolBox::tab,QGroupBox#gboxDevicePanel,QGroupBox#gboxDeviceTitle,QFrame#gboxDevicePanel,QFrame#gboxDeviceTitle{
padding:3px;
border-radius:5px;
color:#386487;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

QToolTip{
border:0px solid #386487;
padding:1px;
color:#386487;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

QToolBox::tab:selected{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}

QPrintPreviewDialog QToolButton{
border:0px solid #386487;
border-radius:0px;
margin:0px;
padding:3px;
background:none;
}

QColorDialog QPushButton,QFileDialog QPushButton{
min-width:80px;
}

QToolButton#qt_calendar_prevmonth{
icon-size:0px;
min-width:20px;
image:url(:/qss/lightblue/calendar_prevmonth.png);
}

QToolButton#qt_calendar_nextmonth{
icon-size:0px;
min-width:20px;
image:url(:/qss/lightblue/calendar_nextmonth.png);
}

QToolButton#qt_calendar_prevmonth,QToolButton#qt_calendar_nextmonth,QToolButton#qt_calendar_monthbutton,QToolButton#qt_calendar_yearbutton{
border:0px solid #386487;
border-radius:3px;
margin:3px 3px 3px 3px;
padding:3px;
background:none;
}

QToolButton#qt_calendar_prevmonth:hover,QToolButton#qt_calendar_nextmonth:hover,QToolButton#qt_calendar_monthbutton:hover,QToolButton#qt_calendar_yearbutton:hover,QToolButton#qt_calendar_prevmonth:pressed,QToolButton#qt_calendar_nextmonth:pressed,QToolButton#qt_calendar_monthbutton:pressed,QToolButton#qt_calendar_yearbutton:pressed{
border:1px solid #C0DCF2;
}

QCalendarWidget QSpinBox#qt_calendar_yearedit{
margin:2px;
}

QCalendarWidget QToolButton::menu-indicator{
image:None;
}

QCalendarWidget QTableView{
border-width:0px;
}

QCalendarWidget QWidget#qt_calendar_navigationbar{
border:1px solid #C0DCF2;
border-width:1px 1px 0px 1px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

QComboBox QAbstractItemView::item{
min-height:20px;
min-width:10px;
}

QTableView[model="true"]::item{
padding:0px;
margin:0px;
}

QTableView QLineEdit,QTableView QComboBox,QTableView QSpinBox,QTableView QDoubleSpinBox,QTableView QDateEdit,QTableView QTimeEdit,QTableView QDateTimeEdit{
border-width:0px;
border-radius:0px;
}

QTableView QLineEdit:focus,QTableView QComboBox:focus,QTableView QSpinBox:focus,QTableView QDoubleSpinBox:focus,QTableView QDateEdit:focus,QTableView QTimeEdit:focus,QTableView QDateTimeEdit:focus{
border-width:0px;
border-radius:0px;
}

QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
background:#EAF7FF;
}

QTabWidget::pane:top{top:-1px;}
QTabWidget::pane:bottom{bottom:-1px;}
QTabWidget::pane:left{right:-1px;}
QTabWidget::pane:right{left:-1px;}

*:disabled{
background:#EAF7FF;
border-color:#DEF0FE;
color:#C0DCF2;
}

/*TextColor:#386487*/
/*PanelColor:#EAF7FF*/
/*BorderColor:#C0DCF2*/
/*NormalColorStart:#DEF0FE*/
/*NormalColorEnd:#C0DEF6*/
/*DarkColorStart:#F2F9FF*/
/*DarkColorEnd:#DAEFFF*/
/*HighColor:#00BB9E*/"""

qss_ps_black = """
QPalette{background:#444444;}*{outline:0px;color:#DCDCDC;}

QWidget[form="true"],QLabel[frameShape="1"]{
border:1px solid #242424;
border-radius:0px;
}

QWidget[form="bottom"]{
background:#484848;
}

QWidget[form="bottom"] .QFrame{
border:1px solid #DCDCDC;
}

QWidget[form="bottom"] QLabel,QWidget[form="title"] QLabel{
border-radius:0px;
color:#DCDCDC;
background:none;
border-style:none;
}

QWidget[form="title"],QWidget[nav="left"],QWidget[nav="top"] QAbstractButton{
border-style:none;
border-radius:0px;
padding:5px;
color:#DCDCDC;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #484848,stop:1 #383838);
}

QWidget[nav="top"] QAbstractButton:hover,QWidget[nav="top"] QAbstractButton:pressed,QWidget[nav="top"] QAbstractButton:checked{
border-style:solid;
border-width:0px 0px 2px 0px;
padding:4px 4px 2px 4px;
border-color:#00BB9E;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #646464,stop:1 #525252);
}

QWidget[nav="left"] QAbstractButton{
border-radius:0px;
color:#DCDCDC;
background:none;
border-style:none;
}

QWidget[nav="left"] QAbstractButton:hover{
color:#FFFFFF;
background-color:#00BB9E;
}

QWidget[nav="left"] QAbstractButton:checked,QWidget[nav="left"] QAbstractButton:pressed{
color:#DCDCDC;
border-style:solid;
border-width:0px 0px 0px 2px;
padding:4px 4px 4px 2px;
border-color:#00BB9E;
background-color:#444444;
}

QWidget[video="true"] QLabel{
color:#DCDCDC;
border:1px solid #242424;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #484848,stop:1 #383838);
}

QWidget[video="true"] QLabel:focus{
border:1px solid #00BB9E;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #646464,stop:1 #525252);
}

QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
border:1px solid #242424;
border-radius:3px;
padding:2px;
background:none;
selection-background-color:#484848;
selection-color:#DCDCDC;
}

QLineEdit:focus,QTextEdit:focus,QPlainTextEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QComboBox:focus,QDateEdit:focus,QTimeEdit:focus,QDateTimeEdit:focus,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QSpinBox:hover,QDoubleSpinBox:hover,QComboBox:hover,QDateEdit:hover,QTimeEdit:hover,QDateTimeEdit:hover{
border:1px solid #242424;
}

QLineEdit[echoMode="2"]{
lineedit-password-character:9679;
}

.QFrame{
border:1px solid #242424;
border-radius:3px;
}

.QGroupBox{
border:1px solid #242424;
border-radius:5px;
margin-top:3ex;
}

.QGroupBox::title{
subcontrol-origin:margin;
position:relative;
left:10px;
}

.QPushButton,.QToolButton{
border-style:none;
border:1px solid #242424;
color:#DCDCDC;
padding:5px;
min-height:15px;
border-radius:5px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #484848,stop:1 #383838);
}

.QPushButton:hover,.QToolButton:hover{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #646464,stop:1 #525252);
}

.QPushButton:pressed,.QToolButton:pressed{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #484848,stop:1 #383838);
}

.QToolButton::menu-indicator{
image:None;
}

QToolButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{
border-radius:3px;
color:#DCDCDC;
padding:3px;
margin:0px;
background:none;
border-style:none;
}

QToolButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{
color:#FFFFFF;
margin:1px 1px 2px 1px;
background-color:rgba(51,127,209,230);
}

QPushButton#btnMenu_Close:hover{
color:#FFFFFF;
margin:1px 1px 2px 1px;
background-color:rgba(238,0,0,128);
}

QRadioButton::indicator{
width:15px;
height:15px;
}

QRadioButton::indicator::unchecked{
image:url(:/qss/psblack/radiobutton_unchecked.png);
}

QRadioButton::indicator::unchecked:disabled{
image:url(:/qss/psblack/radiobutton_unchecked_disable.png);
}

QRadioButton::indicator::checked{
image:url(:/qss/psblack/radiobutton_checked.png);
}

QRadioButton::indicator::checked:disabled{
image:url(:/qss/psblack/radiobutton_checked_disable.png);
}

QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
padding:0px -3px 0px 0px;
}

QCheckBox::indicator,QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{
width:13px;
height:13px;
}

QCheckBox::indicator:unchecked,QGroupBox::indicator:unchecked,QTreeWidget::indicator:unchecked,QListWidget::indicator:unchecked{
image:url(:/qss/psblack/checkbox_unchecked.png);
}

QCheckBox::indicator:unchecked:disabled,QGroupBox::indicator:unchecked:disabled,QTreeWidget::indicator:unchecked:disabled,QListWidget::indicator:disabled{
image:url(:/qss/psblack/checkbox_unchecked_disable.png);
}

QCheckBox::indicator:checked,QGroupBox::indicator:checked,QTreeWidget::indicator:checked,QListWidget::indicator:checked{
image:url(:/qss/psblack/checkbox_checked.png);
}

QCheckBox::indicator:checked:disabled,QGroupBox::indicator:checked:disabled,QTreeWidget::indicator:checked:disabled,QListWidget::indicator:checked:disabled{
image:url(:/qss/psblack/checkbox_checked_disable.png);
}

QCheckBox::indicator:indeterminate,QGroupBox::indicator:indeterminate,QTreeWidget::indicator:indeterminate,QListWidget::indicator:indeterminate{
image:url(:/qss/psblack/checkbox_parcial.png);
}

QCheckBox::indicator:indeterminate:disabled,QGroupBox::indicator:indeterminate:disabled,QTreeWidget::indicator:indeterminate:disabled,QListWidget::indicator:indeterminate:disabled{
image:url(:/qss/psblack/checkbox_parcial_disable.png);
}

QTimeEdit::up-button,QDateEdit::up-button,QDateTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button{
image:url(:/qss/psblack/add_top.png);
width:10px;
height:10px;
padding:2px 5px 0px 0px;
}

QTimeEdit::down-button,QDateEdit::down-button,QDateTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button{
image:url(:/qss/psblack/add_bottom.png);
width:10px;
height:10px;
padding:0px 5px 2px 0px;
}

QTimeEdit::up-button:pressed,QDateEdit::up-button:pressed,QDateTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{
top:-2px;
}
  
QTimeEdit::down-button:pressed,QDateEdit::down-button:pressed,QDateTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pressed{
bottom:-2px;
}

QComboBox::down-arrow,QDateEdit[calendarPopup="true"]::down-arrow,QTimeEdit[calendarPopup="true"]::down-arrow,QDateTimeEdit[calendarPopup="true"]::down-arrow{
image:url(:/qss/psblack/add_bottom.png);
width:10px;
height:10px;
right:2px;
}

QComboBox::drop-down,QDateEdit::drop-down,QTimeEdit::drop-down,QDateTimeEdit::drop-down{
subcontrol-origin:padding;
subcontrol-position:top right;
width:15px;
border-left-width:0px;
border-left-style:solid;
border-top-right-radius:3px;
border-bottom-right-radius:3px;
border-left-color:#242424;
}

QComboBox::drop-down:on{
top:1px;
}

QMenuBar::item{
color:#DCDCDC;
background-color:#484848;
margin:0px;
padding:3px 10px;
}

QMenu,QMenuBar,QMenu:disabled,QMenuBar:disabled{
color:#DCDCDC;
background-color:#484848;
border:1px solid #242424;
margin:0px;
}

QMenu::item{
padding:3px 20px;
}

QMenu::indicator{
width:13px;
height:13px;
}

QMenu::item:selected,QMenuBar::item:selected{
color:#DCDCDC;
border:0px solid #242424;
background:#646464;
}

QMenu::separator{
height:1px;
background:#242424;
}

QProgressBar{
min-height:10px;
background:#484848;
border-radius:5px;
text-align:center;
border:1px solid #484848;
}

QProgressBar:chunk{
border-radius:5px;
background-color:#242424;
}

QSlider::groove:horizontal{
background:#484848;
height:8px;
border-radius:4px;
}

QSlider::add-page:horizontal{
background:#484848;
height:8px;
border-radius:4px;
}

QSlider::sub-page:horizontal{
background:#242424;
height:8px;
border-radius:4px;
}

QSlider::handle:horizontal{
width:13px;
margin-top:-3px;
margin-bottom:-3px;
border-radius:6px;
background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #444444,stop:0.8 #242424);
}

QSlider::groove:vertical{
width:8px;
border-radius:4px;
background:#484848;
}

QSlider::add-page:vertical{
width:8px;
border-radius:4px;
background:#484848;
}

QSlider::sub-page:vertical{
width:8px;
border-radius:4px;
background:#242424;
}

QSlider::handle:vertical{
height:14px;
margin-left:-3px;
margin-right:-3px;
border-radius:6px;
background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #444444,stop:0.8 #242424);
}

QScrollBar:horizontal{
background:#484848;
padding:0px;
border-radius:6px;
max-height:12px;
}

QScrollBar::handle:horizontal{
background:#242424;
min-width:50px;
border-radius:6px;
}

QScrollBar::handle:horizontal:hover{
background:#00BB9E;
}

QScrollBar::handle:horizontal:pressed{
background:#00BB9E;
}

QScrollBar::add-page:horizontal{
background:none;
}

QScrollBar::sub-page:horizontal{
background:none;
}

QScrollBar::add-line:horizontal{
background:none;
}

QScrollBar::sub-line:horizontal{
background:none;
}

QScrollBar:vertical{
background:#484848;
padding:0px;
border-radius:6px;
max-width:12px;
}

QScrollBar::handle:vertical{
background:#242424;
min-height:50px;
border-radius:6px;
}

QScrollBar::handle:vertical:hover{
background:#00BB9E;
}

QScrollBar::handle:vertical:pressed{
background:#00BB9E;
}

QScrollBar::add-page:vertical{
background:none;
}

QScrollBar::sub-page:vertical{
background:none;
}

QScrollBar::add-line:vertical{
background:none;
}

QScrollBar::sub-line:vertical{
background:none;
}

QScrollArea{
border:0px;
}

QTreeView,QListView,QTableView,QTabWidget::pane{
border:1px solid #242424;
selection-background-color:#646464;
selection-color:#DCDCDC;
alternate-background-color:#525252;
gridline-color:#242424;
}

QTreeView::branch:closed:has-children{
margin:4px;
border-image:url(:/qss/psblack/branch_open.png);
}

QTreeView::branch:open:has-children{
margin:4px;
border-image:url(:/qss/psblack/branch_close.png);
}

QTreeView,QListView,QTableView,QSplitter::handle,QTreeView::branch{
background:#444444;
}

QTableView::item:selected,QListView::item:selected,QTreeView::item:selected{
color:#DCDCDC;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #484848,stop:1 #383838);
}

QTableView::item:hover,QListView::item:hover,QTreeView::item:hover,QHeaderView{
color:#DCDCDC;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #646464,stop:1 #525252);
}

QTableView::item,QListView::item,QTreeView::item{
padding:1px;
margin:0px;
}

QHeaderView::section,QTableCornerButton:section{
padding:3px;
margin:0px;
color:#DCDCDC;
border:1px solid #242424;
border-left-width:0px;
border-right-width:1px;
border-top-width:0px;
border-bottom-width:1px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #646464,stop:1 #525252);
}

QTabBar::tab{
border:1px solid #242424;
color:#DCDCDC;
margin:0px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #646464,stop:1 #525252);
}

QTabBar::tab:selected,QTabBar::tab:hover{
border-style:solid;
border-color:#00BB9E;
background:#444444;
}

QTabBar::tab:top,QTabBar::tab:bottom{
padding:3px 8px 3px 8px;
}

QTabBar::tab:left,QTabBar::tab:right{
padding:8px 3px 8px 3px;
}

QTabBar::tab:top:selected,QTabBar::tab:top:hover{
border-width:2px 0px 0px 0px;
}

QTabBar::tab:right:selected,QTabBar::tab:right:hover{
border-width:0px 0px 0px 2px;
}

QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{
border-width:0px 0px 2px 0px;
}

QTabBar::tab:left:selected,QTabBar::tab:left:hover{
border-width:0px 2px 0px 0px;
}

QTabBar::tab:first:top:selected,QTabBar::tab:first:top:hover,QTabBar::tab:first:bottom:selected,QTabBar::tab:first:bottom:hover{
border-left-width:1px;
border-left-color:#242424;
}

QTabBar::tab:first:left:selected,QTabBar::tab:first:left:hover,QTabBar::tab:first:right:selected,QTabBar::tab:first:right:hover{
border-top-width:1px;
border-top-color:#242424;
}

QTabBar::tab:last:top:selected,QTabBar::tab:last:top:hover,QTabBar::tab:last:bottom:selected,QTabBar::tab:last:bottom:hover{
border-right-width:1px;
border-right-color:#242424;
}

QTabBar::tab:last:left:selected,QTabBar::tab:last:left:hover,QTabBar::tab:last:right:selected,QTabBar::tab:last:right:hover{
border-bottom-width:1px;
border-bottom-color:#242424;
}

QStatusBar::item{
border:0px solid #484848;
border-radius:3px;
}

QToolBox::tab,QGroupBox#gboxDevicePanel,QGroupBox#gboxDeviceTitle,QFrame#gboxDevicePanel,QFrame#gboxDeviceTitle{
padding:3px;
border-radius:5px;
color:#DCDCDC;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #484848,stop:1 #383838);
}

QToolTip{
border:0px solid #DCDCDC;
padding:1px;
color:#DCDCDC;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #484848,stop:1 #383838);
}

QToolBox::tab:selected{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #646464,stop:1 #525252);
}

QPrintPreviewDialog QToolButton{
border:0px solid #DCDCDC;
border-radius:0px;
margin:0px;
padding:3px;
background:none;
}

QColorDialog QPushButton,QFileDialog QPushButton{
min-width:80px;
}

QToolButton#qt_calendar_prevmonth{
icon-size:0px;
min-width:20px;
image:url(:/qss/psblack/calendar_prevmonth.png);
}

QToolButton#qt_calendar_nextmonth{
icon-size:0px;
min-width:20px;
image:url(:/qss/psblack/calendar_nextmonth.png);
}

QToolButton#qt_calendar_prevmonth,QToolButton#qt_calendar_nextmonth,QToolButton#qt_calendar_monthbutton,QToolButton#qt_calendar_yearbutton{
border:0px solid #DCDCDC;
border-radius:3px;
margin:3px 3px 3px 3px;
padding:3px;
background:none;
}

QToolButton#qt_calendar_prevmonth:hover,QToolButton#qt_calendar_nextmonth:hover,QToolButton#qt_calendar_monthbutton:hover,QToolButton#qt_calendar_yearbutton:hover,QToolButton#qt_calendar_prevmonth:pressed,QToolButton#qt_calendar_nextmonth:pressed,QToolButton#qt_calendar_monthbutton:pressed,QToolButton#qt_calendar_yearbutton:pressed{
border:1px solid #242424;
}

QCalendarWidget QSpinBox#qt_calendar_yearedit{
margin:2px;
}

QCalendarWidget QToolButton::menu-indicator{
image:None;
}

QCalendarWidget QTableView{
border-width:0px;
}

QCalendarWidget QWidget#qt_calendar_navigationbar{
border:1px solid #242424;
border-width:1px 1px 0px 1px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #484848,stop:1 #383838);
}

QComboBox QAbstractItemView::item{
min-height:20px;
min-width:10px;
}

QTableView[model="true"]::item{
padding:0px;
margin:0px;
}

QTableView QLineEdit,QTableView QComboBox,QTableView QSpinBox,QTableView QDoubleSpinBox,QTableView QDateEdit,QTableView QTimeEdit,QTableView QDateTimeEdit{
border-width:0px;
border-radius:0px;
}

QTableView QLineEdit:focus,QTableView QComboBox:focus,QTableView QSpinBox:focus,QTableView QDoubleSpinBox:focus,QTableView QDateEdit:focus,QTableView QTimeEdit:focus,QTableView QDateTimeEdit:focus{
border-width:0px;
border-radius:0px;
}

QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{
background:#444444;
}

QTabWidget::pane:top{top:-1px;}
QTabWidget::pane:bottom{bottom:-1px;}
QTabWidget::pane:left{right:-1px;}
QTabWidget::pane:right{left:-1px;}

*:disabled{
background:#444444;
border-color:#484848;
color:#242424;
}

/*TextColor:#DCDCDC*/
/*PanelColor:#444444*/
/*BorderColor:#242424*/
/*NormalColorStart:#484848*/
/*NormalColorEnd:#383838*/
/*DarkColorStart:#646464*/
/*DarkColorEnd:#525252*/
/*HighColor:#00BB9E*/"""