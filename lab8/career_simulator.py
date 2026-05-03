import tkinter as tk
from tkinter import ttk, messagebox
import random
import json
import os
from datetime import datetime


class CareerSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Симулятор карьеры - Построй свою империю")
        self.root.geometry("900x700")
        self.root.resizable(True, True)

        # Новая цветовая схема (нежные пастельные тона)
        self.colors = {
            "bg_main": "#FFF0F5",  # Нежно-розовый (Lavender Blush)
            "bg_frame": "#FFE4E9",  # Светло-розовый для фреймов
            "text_dark": "#8B5E7E",  # Темно-розовый для текста
            "text_light": "#FFFFFF",  # Белый для текста на кнопках
            "button_green": "#C8E6C9",  # Нежно-зеленый
            "button_blue": "#BBDEFB",  # Нежно-голубой
            "button_white": "#FFFFFF",  # Белый
            "button_purple": "#E1BEE7",  # Нежно-фиолетовый для разнообразия
            "button_orange": "#FFE0B2",  # Нежно-оранжевый
            "progress_bg": "#FFCDD2",  # Светло-розовый для прогресс-баров
            "log_bg": "#FFF5F7"  # Очень светлый розовый для лога
        }

        # Переменные игры
        self.player_name = ""
        self.age = 22
        self.energy = 80
        self.happiness = 70
        self.skills = {
            "Программирование": 30,
            "Коммуникации": 40,
            "Управление": 20,
            "Креативность": 35
        }
        self.money = 5000
        self.career_level = 1
        self.job_title = "Стажер"
        self.salary = 30000
        self.experience = 0
        self.inventory = []
        self.achievements = []

        # Карьерные пути
        self.career_paths = {
            1: {"title": "Стажер", "salary": 30000},
            2: {"title": "Младший специалист", "salary": 50000},
            3: {"title": "Специалист", "salary": 75000},
            4: {"title": "Старший специалист", "salary": 100000},
            5: {"title": "Team Lead", "salary": 150000},
            6: {"title": "Project Manager", "salary": 200000},
            7: {"title": "Director", "salary": 300000},
            8: {"title": "CEO", "salary": 500000}
        }

        # Загрузка сохранений
        self.load_game()

        # Создание GUI
        self.setup_gui()

        # Обновление отображения
        self.update_display()

    def setup_gui(self):
        # Главный контейнер
        main_frame = tk.Frame(self.root, bg=self.colors["bg_main"])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Верхняя панель с информацией о персонаже
        info_frame = tk.Frame(main_frame, bg=self.colors["bg_frame"], relief=tk.RAISED, bd=2)
        info_frame.pack(fill=tk.X, pady=(0, 20))

        # Имя персонажа
        self.name_label = tk.Label(info_frame, text="", font=('Arial', 16, 'bold'),
                                   fg=self.colors["text_dark"], bg=self.colors["bg_frame"])
        self.name_label.pack(side=tk.LEFT, padx=20, pady=10)

        # Возраст
        self.age_label = tk.Label(info_frame, text="", font=('Arial', 12),
                                  fg=self.colors["text_dark"], bg=self.colors["bg_frame"])
        self.age_label.pack(side=tk.LEFT, padx=20, pady=10)

        # Должность
        self.job_label = tk.Label(info_frame, text="", font=('Arial', 12, 'bold'),
                                  fg='#9C6B8E', bg=self.colors["bg_frame"])
        self.job_label.pack(side=tk.LEFT, padx=20, pady=10)

        # Статистика (вторая строка)
        stats_frame = tk.Frame(main_frame, bg=self.colors["bg_main"])
        stats_frame.pack(fill=tk.X, pady=(0, 20))

        # Энергия - кастомный стиль для прогресс-бара
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Pastel.Horizontal.TProgressbar",
                        troughcolor=self.colors["progress_bg"],
                        background='#F8BBD0',  # Розовый для полоски прогресса
                        thickness=20)

        self.energy_bar = ttk.Progressbar(stats_frame, length=150, mode='determinate',
                                          style="Pastel.Horizontal.TProgressbar")
        self.energy_bar.pack(side=tk.LEFT, padx=10)
        self.energy_label = tk.Label(stats_frame, text="Энергия: ", font=('Arial', 10),
                                     fg=self.colors["text_dark"], bg=self.colors["bg_main"])
        self.energy_label.pack(side=tk.LEFT, padx=5)

        # Счастье
        self.happiness_bar = ttk.Progressbar(stats_frame, length=150, mode='determinate',
                                             style="Pastel.Horizontal.TProgressbar")
        self.happiness_bar.pack(side=tk.LEFT, padx=10)
        self.happiness_label = tk.Label(stats_frame, text="Счастье: ", font=('Arial', 10),
                                        fg=self.colors["text_dark"], bg=self.colors["bg_main"])
        self.happiness_label.pack(side=tk.LEFT, padx=5)

        # Деньги
        self.money_label = tk.Label(stats_frame, text="Деньги: ", font=('Arial', 10, 'bold'),
                                    fg='#E91E63', bg=self.colors["bg_main"])
        self.money_label.pack(side=tk.LEFT, padx=20)

        # Опыт
        self.exp_label = tk.Label(stats_frame, text="Опыт: ", font=('Arial', 10),
                                  fg=self.colors["text_dark"], bg=self.colors["bg_main"])
        self.exp_label.pack(side=tk.LEFT, padx=20)

        # Основные навыки
        skills_frame = tk.LabelFrame(main_frame, text="Навыки", font=('Arial', 12, 'bold'),
                                     fg=self.colors["text_dark"], bg=self.colors["bg_frame"], bd=2)
        skills_frame.pack(fill=tk.X, pady=(0, 20))

        self.skill_labels = {}
        for i, (skill, value) in enumerate(self.skills.items()):
            label = tk.Label(skills_frame, text=f"{skill}: {value}", font=('Arial', 11),
                             fg=self.colors["text_dark"], bg=self.colors["bg_frame"])
            label.grid(row=i // 2, column=i % 2, padx=20, pady=5, sticky='w')
            self.skill_labels[skill] = label

        # Кнопки действий (обновленные цвета)
        actions_frame = tk.Frame(main_frame, bg=self.colors["bg_main"])
        actions_frame.pack(fill=tk.X, pady=(0, 20))

        # Нежно-зеленая кнопка (работа)
        work_btn = tk.Button(actions_frame, text="💼 Работать", command=self.work,
                             font=('Arial', 12, 'bold'), bg=self.colors["button_green"],
                             fg=self.colors["text_dark"], padx=20, pady=10,
                             relief=tk.RAISED, bd=2, cursor="hand2")
        work_btn.pack(side=tk.LEFT, padx=10)

        # Нежно-голубая кнопка (учиться)
        study_btn = tk.Button(actions_frame, text="📚 Учиться", command=self.study,
                              font=('Arial', 12, 'bold'), bg=self.colors["button_blue"],
                              fg=self.colors["text_dark"], padx=20, pady=10,
                              relief=tk.RAISED, bd=2, cursor="hand2")
        study_btn.pack(side=tk.LEFT, padx=10)

        # Белая кнопка (отдыхать)
        rest_btn = tk.Button(actions_frame, text="😴 Отдыхать", command=self.rest,
                             font=('Arial', 12, 'bold'), bg=self.colors["button_white"],
                             fg=self.colors["text_dark"], padx=20, pady=10,
                             relief=tk.RAISED, bd=2, cursor="hand2")
        rest_btn.pack(side=tk.LEFT, padx=10)

        # Нежно-фиолетовая кнопка (социализация)
        social_btn = tk.Button(actions_frame, text="🎉 Социализация", command=self.socialize,
                               font=('Arial', 12, 'bold'), bg=self.colors["button_purple"],
                               fg=self.colors["text_dark"], padx=20, pady=10,
                               relief=tk.RAISED, bd=2, cursor="hand2")
        social_btn.pack(side=tk.LEFT, padx=10)

        # Нежно-оранжевая кнопка (случайное событие)
        event_btn = tk.Button(actions_frame, text="🎲 Случайное событие", command=self.random_event,
                              font=('Arial', 12, 'bold'), bg=self.colors["button_orange"],
                              fg=self.colors["text_dark"], padx=20, pady=10,
                              relief=tk.RAISED, bd=2, cursor="hand2")
        event_btn.pack(side=tk.LEFT, padx=10)

        # Нижняя панель с дополнительными кнопками
        bottom_frame = tk.Frame(main_frame, bg=self.colors["bg_main"])
        bottom_frame.pack(fill=tk.X)

        # Нежно-зеленая (магазин)
        shop_btn = tk.Button(bottom_frame, text="🛒 Магазин", command=self.open_shop,
                             font=('Arial', 10, 'bold'), bg=self.colors["button_green"],
                             fg=self.colors["text_dark"], padx=15, pady=8,
                             relief=tk.RAISED, bd=2, cursor="hand2")
        shop_btn.pack(side=tk.LEFT, padx=10)

        # Нежно-фиолетовая (статистика)
        stats_btn = tk.Button(bottom_frame, text="📊 Статистика", command=self.show_stats,
                              font=('Arial', 10, 'bold'), bg=self.colors["button_purple"],
                              fg=self.colors["text_dark"], padx=15, pady=8,
                              relief=tk.RAISED, bd=2, cursor="hand2")
        stats_btn.pack(side=tk.LEFT, padx=10)

        # Нежно-голубая (сохранить)
        save_btn = tk.Button(bottom_frame, text="💾 Сохранить", command=self.save_game,
                             font=('Arial', 10, 'bold'), bg=self.colors["button_blue"],
                             fg=self.colors["text_dark"], padx=15, pady=8,
                             relief=tk.RAISED, bd=2, cursor="hand2")
        save_btn.pack(side=tk.LEFT, padx=10)

        # Нежно-голубая (загрузить)
        load_btn = tk.Button(bottom_frame, text="📂 Загрузить", command=self.load_game_gui,
                             font=('Arial', 10, 'bold'), bg=self.colors["button_blue"],
                             fg=self.colors["text_dark"], padx=15, pady=8,
                             relief=tk.RAISED, bd=2, cursor="hand2")
        load_btn.pack(side=tk.LEFT, padx=10)

        # Белая (новая игра)
        new_btn = tk.Button(bottom_frame, text="🆕 Новая игра", command=self.new_game,
                            font=('Arial', 10, 'bold'), bg=self.colors["button_white"],
                            fg='#C62828', padx=15, pady=8,  # Красноватый текст для контраста
                            relief=tk.RAISED, bd=2, cursor="hand2")
        new_btn.pack(side=tk.LEFT, padx=10)

        # Лог событий
        log_frame = tk.LabelFrame(main_frame, text="Лог событий", font=('Arial', 10, 'bold'),
                                  fg=self.colors["text_dark"], bg=self.colors["bg_frame"], bd=2)
        log_frame.pack(fill=tk.BOTH, expand=True)

        self.log_text = tk.Text(log_frame, height=8, width=80, bg=self.colors["log_bg"],
                                fg=self.colors["text_dark"], font=('Consolas', 10),
                                relief=tk.FLAT, wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        scrollbar = tk.Scrollbar(self.log_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.log_text.yview)

    def update_display(self):
        # Обновление информации о персонаже
        self.name_label.config(text=f"{self.player_name} (Уровень {self.career_level})")
        self.age_label.config(text=f"Возраст: {self.age} лет")
        self.job_label.config(text=f"{self.job_title} | Зарплата: {self.salary} руб.")

        # Обновление полосок прогресса
        self.energy_bar['value'] = self.energy
        self.energy_bar['maximum'] = 100
        self.energy_label.config(text=f"Энергия: {self.energy}/100")

        self.happiness_bar['value'] = self.happiness
        self.happiness_bar['maximum'] = 100
        self.happiness_label.config(text=f"Счастье: {self.happiness}/100")

        # Обновление остальных показателей
        self.money_label.config(text=f"Деньги: {self.money} руб.")
        self.exp_label.config(text=f"Опыт: {self.experience}/100")

        # Обновление навыков
        for skill, value in self.skills.items():
            self.skill_labels[skill].config(text=f"{skill}: {value}")

        # Проверка повышения уровня карьеры
        if self.experience >= 100 and self.career_level < 8:
            self.experience -= 100
            self.career_level += 1
            self.job_title = self.career_paths[self.career_level]["title"]
            self.salary = self.career_paths[self.career_level]["salary"]
            self.add_log(f"🎉 Поздравляем! Вы повышены до {self.job_title}! Зарплата увеличилась до {self.salary} руб.")
            messagebox.showinfo("Повышение!",
                                f"Поздравляем! Вы стали {self.job_title}!\nЗарплата увеличена до {self.salary} руб.")

        # Проверка возраста и завершения игры
        if self.age >= 65:
            self.end_game()

    def add_log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)

    def work(self):
        if self.energy < 20:
            self.add_log("❌ Вы слишком устали для работы! Отдохните сначала.")
            return

        # Расчет дохода от работы
        base_income = self.salary // 30
        skill_bonus = sum(self.skills.values()) // 200
        income = base_income + skill_bonus + random.randint(0, 1000)

        self.money += income
        self.energy -= 20
        self.experience += random.randint(5, 15)
        self.happiness -= random.randint(0, 10)
        self.age += 1

        self.add_log(f"💼 Вы отработали день и заработали {income} руб. Опыт +{random.randint(5, 15)}")
        self.update_display()

        # Проверка на выгорание
        if self.happiness < 20:
            self.add_log("⚠️ У вас высокий уровень стресса! Срочно отдохните!")

    def study(self):
        if self.energy < 15:
            self.add_log("❌ У вас недостаточно энергии для учебы!")
            return

        skill = random.choice(list(self.skills.keys()))
        increase = random.randint(2, 8)
        self.skills[skill] = min(100, self.skills[skill] + increase)
        self.energy -= 15
        self.experience += increase
        self.age += 1

        self.add_log(f"📚 Вы изучили {skill}! Навык увеличен на {increase}. Опыт +{increase}")
        self.update_display()

    def rest(self):
        energy_gain = random.randint(20, 40)
        self.energy = min(100, self.energy + energy_gain)
        self.happiness = min(100, self.happiness + random.randint(5, 15))
        self.age += 1

        self.add_log(f"😴 Вы хорошо отдохнули! Энергия +{energy_gain}, Счастье +{random.randint(5, 15)}")
        self.update_display()

    def socialize(self):
        if self.money < 500:
            self.add_log("❌ У вас недостаточно денег для социализации!")
            return

        cost = random.randint(200, 800)
        self.money -= cost
        happiness_gain = random.randint(10, 30)
        self.happiness = min(100, self.happiness + happiness_gain)
        self.age += 1

        self.add_log(f"🎉 Вы сходили на вечеринку! Потрачено {cost} руб. Счастье +{happiness_gain}")
        self.update_display()

    def random_event(self):
        events = [
            {"text": "🎁 Вы нашли кошелек на улице!", "money": 1000, "happiness": 10},
            {"text": "💻 Ваш компьютер сломался!", "money": -3000, "happiness": -15},
            {"text": "🏆 Вы получили премию за хорошую работу!", "money": 5000, "happiness": 20},
            {"text": "🤝 Вы познакомились с важным человеком!", "skill": "Коммуникации", "skill_gain": 10},
            {"text": "📈 Вы прошли онлайн-курс!", "skill": "Программирование", "skill_gain": 15},
            {"text": "🏥 Вы заболели!", "energy": -30, "happiness": -10},
            {"text": "🎓 Вам предложили повышение!", "experience": 25, "happiness": 15}
        ]

        event = random.choice(events)
        event_text = event["text"]

        if "money" in event:
            self.money += event["money"]
        if "happiness" in event:
            self.happiness = max(0, min(100, self.happiness + event["happiness"]))
        if "skill" in event:
            self.skills[event["skill"]] = min(100, self.skills[event["skill"]] + event["skill_gain"])
        if "energy" in event:
            self.energy = max(0, min(100, self.energy + event["energy"]))
        if "experience" in event:
            self.experience += event["experience"]

        self.age += 1
        self.add_log(event_text)
        self.update_display()

    def open_shop(self):
        shop_window = tk.Toplevel(self.root)
        shop_window.title("Магазин")
        shop_window.geometry("400x500")
        shop_window.configure(bg=self.colors["bg_main"])

        items = {
            "Энергетик": {"price": 200, "effect": "energy", "value": 30},
            "Книга по саморазвитию": {"price": 500, "effect": "skill", "value": 5, "skill": "Коммуникации"},
            "Путевка на курорт": {"price": 3000, "effect": "happiness", "value": 40},
            "Кофе": {"price": 100, "effect": "energy", "value": 15},
            "Курсы повышения квалификации": {"price": 2000, "effect": "skill_all", "value": 3}
        }

        tk.Label(shop_window, text="🛍️ Магазин", font=('Arial', 16, 'bold'),
                 fg=self.colors["text_dark"], bg=self.colors["bg_main"]).pack(pady=10)

        tk.Label(shop_window, text=f"💰 Ваши деньги: {self.money} руб.", font=('Arial', 12),
                 fg='#E91E63', bg=self.colors["bg_main"]).pack(pady=5)

        for item_name, item_info in items.items():
            frame = tk.Frame(shop_window, bg=self.colors["bg_frame"], relief=tk.RAISED, bd=1)
            frame.pack(fill=tk.X, padx=20, pady=5)

            label = tk.Label(frame, text=f"{item_name} - {item_info['price']} руб.",
                             font=('Arial', 11), fg=self.colors["text_dark"], bg=self.colors["bg_frame"])
            label.pack(side=tk.LEFT, padx=10, pady=5)

            buy_btn = tk.Button(frame, text="Купить",
                                command=lambda i=item_name, inf=item_info: self.buy_item(i, inf, shop_window),
                                bg=self.colors["button_green"], fg=self.colors["text_dark"],
                                font=('Arial', 10, 'bold'), relief=tk.RAISED, bd=2, cursor="hand2")
            buy_btn.pack(side=tk.RIGHT, padx=10, pady=5)

    def buy_item(self, item_name, item_info, shop_window):
        if self.money >= item_info["price"]:
            self.money -= item_info["price"]

            if item_info["effect"] == "energy":
                self.energy = min(100, self.energy + item_info["value"])
                self.add_log(f"🛒 Куплен {item_name}! Энергия +{item_info['value']}")
            elif item_info["effect"] == "happiness":
                self.happiness = min(100, self.happiness + item_info["value"])
                self.add_log(f"🛒 Куплен {item_name}! Счастье +{item_info['value']}")
            elif item_info["effect"] == "skill":
                self.skills[item_info["skill"]] = min(100, self.skills[item_info["skill"]] + item_info["value"])
                self.add_log(f"🛒 Куплен {item_name}! {item_info['skill']} +{item_info['value']}")
            elif item_info["effect"] == "skill_all":
                for skill in self.skills:
                    self.skills[skill] = min(100, self.skills[skill] + item_info["value"])
                self.add_log(f"🛒 Куплен {item_name}! Все навыки +{item_info['value']}")

            self.update_display()
            shop_window.destroy()
            self.open_shop()
        else:
            messagebox.showerror("Ошибка", "Недостаточно средств!")

    def show_stats(self):
        stats_window = tk.Toplevel(self.root)
        stats_window.title("Статистика")
        stats_window.geometry("500x400")
        stats_window.configure(bg=self.colors["bg_main"])

        stats_text = f"""
        📊 СТАТИСТИКА ПЕРСОНАЖА

        Имя: {self.player_name}
        Возраст: {self.age} лет
        Должность: {self.job_title}
        VIP Уровень: {self.career_level}/8

        💰 Финансы: {self.money} руб.
        💪 Энергия: {self.energy}/100
        😊 Счастье: {self.happiness}/100
        ⭐ Опыт: {self.experience}/100

        🎯 Навыки:
        - Программирование: {self.skills['Программирование']}/100
        - Коммуникации: {self.skills['Коммуникации']}/100
        - Управление: {self.skills['Управление']}/100
        - Креативность: {self.skills['Креативность']}/100

        🏆 Достижения: {len(self.achievements)}
        """

        stats_label = tk.Label(stats_window, text=stats_text, font=('Courier', 11),
                               fg=self.colors["text_dark"], bg=self.colors["bg_main"], justify=tk.LEFT)
        stats_label.pack(padx=20, pady=20)

    def save_game(self):
        save_data = {
            "player_name": self.player_name,
            "age": self.age,
            "energy": self.energy,
            "happiness": self.happiness,
            "skills": self.skills,
            "money": self.money,
            "career_level": self.career_level,
            "job_title": self.job_title,
            "salary": self.salary,
            "experience": self.experience,
            "inventory": self.inventory,
            "achievements": self.achievements
        }

        with open("savegame.json", "w", encoding="utf-8") as f:
            json.dump(save_data, f, ensure_ascii=False, indent=4)

        self.add_log("💾 Игра сохранена!")
        messagebox.showinfo("Сохранение", "Игра успешно сохранена!")

    def load_game(self):
        if os.path.exists("savegame.json"):
            try:
                with open("savegame.json", "r", encoding="utf-8") as f:
                    save_data = json.load(f)

                self.player_name = save_data.get("player_name", "Игрок")
                self.age = save_data.get("age", 22)
                self.energy = save_data.get("energy", 80)
                self.happiness = save_data.get("happiness", 70)
                self.skills = save_data.get("skills", self.skills)
                self.money = save_data.get("money", 5000)
                self.career_level = save_data.get("career_level", 1)
                self.job_title = save_data.get("job_title", "Стажер")
                self.salary = save_data.get("salary", 30000)
                self.experience = save_data.get("experience", 0)
                self.inventory = save_data.get("inventory", [])
                self.achievements = save_data.get("achievements", [])

                return True
            except:
                return False
        return False

    def load_game_gui(self):
        if self.load_game():
            self.update_display()
            self.add_log("📂 Игра загружена из сохранения!")
            messagebox.showinfo("Загрузка", "Игра успешно загружена!")
        else:
            messagebox.showwarning("Ошибка", "Сохранение не найдено!")

    def new_game(self):
        if messagebox.askyesno("Новая игра", "Вы уверены? Все текущие данные будут потеряны!"):
            # Сброс всех переменных
            self.player_name = self.get_player_name()
            self.age = 22
            self.energy = 80
            self.happiness = 70
            self.skills = {
                "Программирование": 30,
                "Коммуникации": 40,
                "Управление": 20,
                "Креативность": 35
            }
            self.money = 5000
            self.career_level = 1
            self.job_title = "Стажер"
            self.salary = 30000
            self.experience = 0
            self.inventory = []
            self.achievements = []

            self.update_display()
            self.log_text.delete(1.0, tk.END)
            self.add_log("✨ Добро пожаловать в Симулятор карьеры! ✨")
            self.add_log("Начинайте работать, учиться и развиваться!")

    def get_player_name(self):
        name_window = tk.Toplevel(self.root)
        name_window.title("Создание персонажа")
        name_window.geometry("400x200")
        name_window.configure(bg=self.colors["bg_main"])

        tk.Label(name_window, text="Введите имя персонажа:", font=('Arial', 14),
                 fg=self.colors["text_dark"], bg=self.colors["bg_main"]).pack(pady=30)

        name_entry = tk.Entry(name_window, font=('Arial', 12), width=30,
                              bg=self.colors["button_white"], fg=self.colors["text_dark"])
        name_entry.pack(pady=10)

        result = ["Игрок"]

        def confirm():
            name = name_entry.get().strip()
            if name:
                result[0] = name
            name_window.destroy()

        tk.Button(name_window, text="Начать игру", command=confirm,
                  bg=self.colors["button_green"], fg=self.colors["text_dark"],
                  font=('Arial', 12, 'bold'), relief=tk.RAISED, bd=2, cursor="hand2").pack(pady=20)

        self.root.wait_window(name_window)
        return result[0]

    def end_game(self):
        messagebox.showinfo("Игра завершена",
                            f"Вы достигли пенсионного возраста!\n"
                            f"Финальная должность: {self.job_title}\n"
                            f"Накопления: {self.money} руб.\n"
                            f"Спасибо за игру!")

        if messagebox.askyesno("Новая игра", "Хотите начать новую игру?"):
            self.new_game()
        else:
            self.root.quit()


def main():
    root = tk.Tk()
    app = CareerSimulator(root)
    root.mainloop()


if __name__ == "__main__":
    main()