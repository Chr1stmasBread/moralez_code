import random

def start():
	print("Салам Алейкум! Вы попал на бота компании ProTeam, Я расскажу Вам о сотрудниках данной компании. Введите help чтобы узнать все мои команды\n")
def worker_max_efficiency(workers):
	maximum = 0
	best = None
	# Проходимся по каждому сотруднику
	for worker_key, worker in workers.items():
		# Проверяем, является ли текущий сотрудник самым эффективным
		if worker['Эффективность'] > maximum:
			maximum = worker['Эффективность']
			best = worker

	return best

workers = { # Список сотрудников
	1: {
		"Фамилия" : "Аболдуев",
		"Должность" : "Medium back-end Разработчик IT отдела",
		"Эффективность" : random.randint(20,100),
		"Портфолио" : "\n1. Разработка веб-приложения для управления задачами и проектами; \n2. Создание RESTful API;",
		"Хобби" : "Выращиваение и разведение Пингвинов"
	},

	2: {
		"Фамилия": "Альфонсович",
		"Должность": "Medium front-end Разработчик IT отдела",
		"Эффективность": random.randint(20,100),
		"Портфолио": "\n1. Онлайн-магазин одежды; \n2.Платформа для обмена фотографиями;",
		"Хобби" : "Выращивание и разведение котов"
	},

	3: {
		"Фамилия": "Бананович",
		"Должность": "Начальник IT отдела",
		"Эффективность": random.randint(20,100),
		"Портфолио": "\n1.Система аутентификации и авторизации; \n2. Оптимизация производительности;",
		"Хобби" : "Выращивание и обучение воронов"
	},

	4: {
		"Фамилия": "Бибиков",
		"Должность": "Заместитель начальника IT отдела",
		"Эффективность": random.randint(20,100),
		"Портфолио": "\n1.Система аутентификации и авторизации;	\n2. Оптимизация производительности;",
		"Хобби": "Обучение собак"
	},

	5: {
		"Фамилия": "Гадючкин",
		"Должность": "Full-Stack разработчик IT отдела",
		"Эффективность": random.randint(20,100),
		"Портфолио": "\n1. Разработка веб-приложения для управления задачами и проектами; \n2. Платформа для обмена фотографиями;",
		"Хобби": "Разработка AI"
	}
}
def restart():
	start()

def help():
	print("""
	Вы ввели команду help, вот мои команды:
	restart - Начинаю все по новой;
	help - Вывод возможных команд;
	info - вывод информации о сотруднике;
	top - Вывод самого эффективного сотрудника;
	about_creator - Расскажу как чувствовал себя мой разработчик пока разработывал меня, и его Телеграмм;
	stop - Чтобы остановить меня;
	"""
	)
def portfolio_top():
	print("")
	best_worker = worker_max_efficiency(workers)
	print(f"Портфолио самого эффективного сотрудника: {best_worker['Портфолио']}\n")

def top():
	print("")
	best_worker = worker_max_efficiency(workers)
	print(f"Самый эффективный сотрудник: {best_worker['Фамилия']}")
def about_creator():
	print("")
	print("Это мой создатель в моменты моего создания (Видео откроется через несколько секунд)")
	print("TG: @Chr1stmas_Bread\n")

def get_employee_data(workers, employee_id): # Получение ID для сотрудника сотрудника
    if employee_id in workers:
        return workers[employee_id]
    else:
        raise ValueError(f"Мне не известен сотрудник под данным ID ({employee_id})  номером")
def info(): # Ввывод информации о сотрудниках по их ID
	print("\nЕсли Вы вдруг решите закончить просмотр информации о сотрудниках, напишите 'Exit'")
	employee_1_data = get_employee_data(workers, 1)
	employee_2_data = get_employee_data(workers, 2)
	employee_3_data = get_employee_data(workers, 3)
	employee_4_data = get_employee_data(workers, 4)
	employee_5_data = get_employee_data(workers, 5)
	print("\n1. ", employee_1_data["Фамилия"],
		  "\n2. ", employee_2_data["Фамилия"],
		  "\n3. ", employee_3_data["Фамилия"],
		  "\n4. ", employee_4_data["Фамилия"],
		  "\n5. ", employee_5_data["Фамилия"])
	while True:
		ID = input("\nВведите ID сотрудника > ")
		ID = ID.lower()
		if ID == "1":
			print("\nФамилия -", employee_1_data["Фамилия"],
				  "\nДолжность -", employee_1_data["Должность"],
				  "\nЭффективность -", employee_1_data["Эффективность"],
				  "\nПортфолио -", employee_1_data["Портфолио"],
				  "\nХобби -", employee_1_data["Хобби"]
				  )

		elif ID == "2":
			print("\nФамилия -", employee_2_data["Фамилия"],
				  "\nДолжность -", employee_2_data["Должность"],
				  "\nЭффективность -", employee_2_data["Эффективность"],
				  "\nПортфолио -", employee_2_data["Портфолио"],
				  "\nХобби -", employee_2_data["Хобби"]
				  )

		elif ID == "3":
			print("\nФамилия -", employee_3_data["Фамилия"],
				  "\nДолжность -", employee_3_data["Должность"],
				  "\nЭффективность -", employee_3_data["Эффективность"],
				  "\nПортфолио -", employee_3_data["Портфолио"],
				  "\nХобби -", employee_3_data["Хобби"]
				  )

		elif ID == "4":
			print("\nФамилия -", employee_4_data["Фамилия"],
				  "\nДолжность -", employee_4_data["Должность"],
				  "\nЭффективность -", employee_4_data["Эффективность"],
				  "\nПортфолио -", employee_4_data["Портфолио"],
				  "\nХобби -", employee_4_data["Хобби"]
				  )

		elif ID == "5":
			print("\nФамилия -", employee_5_data["Фамилия"],
				  "\nДолжность -", employee_5_data["Должность"],
				  "\nЭффективность -", employee_5_data["Эффективность"],
				  "\nПортфолио -", employee_5_data["Портфолио"],
				  "\nХобби -", employee_5_data["Хобби"]
				  )

		elif ID == "exit":
			print("")
			break

		else:
			print(f"\nМне не известен сотрудник под данным ID номером ({ID})")