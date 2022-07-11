from sys import argv , exit
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog,QApplication,QWidget,QStackedWidget
from pyarabic.araby import strip_diacritics
from json import load

# reading surah name 
with open("surah.json","r") as f:
	surah_name = load(f)


class main_screen(QDialog):
	def __init__(self):
		super(main_screen,self).__init__()
		loadUi('main.ui',self)
		self.search.clicked.connect(self.search_fun)

	# search funtion
	def search_fun(self):	
		value = str(self.value.text()).strip()

		# checking english alphabets
		eng_latter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		eng_latter += eng_latter.lower()
		in_eng_let = False
		for i in eng_latter:
			if i in value:
				in_eng_let = True
				break

         # main ayat finding code
		if not in_eng_let:
			if value and (not value == ' ') and (not value == '  ') and (not value == '   '):
				with open("quran_.txt","r", encoding="utf-8") as quran:
					quran = quran.readlines()
					result = ''
					for ayats in quran:
						if strip_diacritics(value) in strip_diacritics(ayats):
							surah , ayat = ayats[0:ayats.rfind("|")].split("|")
							result += f"{surah_name[str(int(surah)-1)]}, ayat number {ayat}\n"
					if not result:
						self.result.setText("not found")
					else:
						self.result.setText(result)
			else:
				self.result.setText("Please enter ayat")
		else:
			self.result.setText("You can not use english alphabet")


if __name__ == '__main__':

	# gui window set
	app = QApplication(argv)
	window = main_screen()
	widget = QStackedWidget()
	widget.addWidget(window)
	widget.setFixedWidth(712)
	widget.setFixedHeight(430)
	widget.show()
	try:
		exit(app.exec_())
	except Exception as e:
		print('exiting..')
	