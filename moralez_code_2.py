from info_code import * # забираем всю инфу из файла info_code
import webbrowser
import time
GIF = 'https://cdn.discordapp.com/attachments/987042349530116117/1199239375133876234/shigure-ui-dance.gif?ex=65c1d1b3&is=65af5cb3&hm=58c00010b305a320ea501467630e1de236f0b0fb8d61562966b752f8a1ed32cd&'
MP4 = 'https://www.youtube.com/watch?v=eRUCwIkj1Pg'
start()
while True:
	command = input("Введите нужную вам команду > ")
	command= command.lower()
	if command == "restart": # Перезапуск программы
		restart()
		command = None

	elif command == "help": # Возможные команды программы
		help()
		command = None

	elif command == "info": # Вывод информации о сотруднике
		info()
		command = None

	elif command == "top": # Ввывод фамилии самого эффективного сотрудника
		top()
		while True:
			command_top = input("\nХотите узнать портфолио специалиста? (Yes/No) > ")
			command_top = command_top.lower()
			command = None
			if command_top == "yes" or command_top == "y":
				portfolio_top() # Ввывод портфолио самого эффективного сотрудника
				command_top = None
				break
			elif command_top == "no" or command_top == "n":
				command_top = None
				break
			else:
				print("Я не совсем Вас понял, можете повторно написать команду?")
				command_top = None

	elif command == "stop": # Остановки программы командой "stop"
		print("\nХорошо, с Вами приятно было поработать, если захотите запустить меня еще раз, просто нажмите кнопочку 'Run'")
		time.sleep(2)
		webbrowser.open_new_tab(GIF)
		break
	elif command == "about_creator": # Расскажет как чувствовал себя разработчик
		about_creator()
		time.sleep(2)
		webbrowser.open_new_tab(MP4)

	else:
		print("\nЯ не совсем Вас понял, можете повторно написать команду?\n")
		command_top = None