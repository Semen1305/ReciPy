import sys
import json
from PyQt6.QtWidgets import QMainWindow, QListWidgetItem
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from window1 import Ui_ReciPy  # Импорт первого дизайна
from window2 import Ui_MainWindow1  # Импорт второго дизайна


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ReciPy()
        self.ui.setupUi(self)
        # Подключаем кнопки к соответствующим методам для открытия окна рецептов
        self.ui.found.clicked.connect(self.open_by_title)
        self.ui.supi.clicked.connect(self.open_by_category)
        self.ui.vtoroe.clicked.connect(self.open_by_category)
        self.ui.deserti.clicked.connect(self.open_by_category)
        self.ui.vipechka.clicked.connect(self.open_by_category)
        self.ui.napitki.clicked.connect(self.open_by_category)
        self.ui.zagotovki.clicked.connect(self.open_by_category)
        self.ui.salat.clicked.connect(self.open_by_category)
        self.ui.zakuski.clicked.connect(self.open_by_category)
        self.ui.testo.clicked.connect(self.open_by_category)
        self.ui.sousi.clicked.connect(self.open_by_category)

    def open_by_title(self):
        # Получаем текст из поля поиска по названию
        text = self.ui.name.text()
        # Открываем новое окно с результатами поиска по названию
        self.recipes_window = Recepies(text, search_by='title')
        self.recipes_window.show()

    def open_by_category(self):
        # Получаем кнопку, которую нажали, чтобы узнать категорию
        button = self.sender()
        if button:
            category = button.text().strip().lower()
            # Открываем окно с результатами поиска по категории
            self.recipes_window = Recepies(category, search_by='category')
            self.recipes_window.show()


class Recepies(QMainWindow):
    def __init__(self, text, search_by='title'):
        super().__init__()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self)
        # Сохраняем строку поиска и поле для поиска
        self.query = text.lower().strip()
        self.field = search_by
        # Загружаем все рецепты из файла JSON
        self.recipes = self.load_recipes()
        # Заполняем список рецептов на основе запроса
        self.fill_list()
        # Подключаем обработчик клика по рецепту для отображения деталей
        self.ui.listWidget.itemClicked.connect(self.show_recipe)

    def load_recipes(self):
        # Открываем файл all_recipes.json и загружаем данные
        with open('all_recipes.json', 'r', encoding='utf-8') as f:
            return json.load(f)

    def fill_list(self):
        # Очищаем список рецептов перед заполнением
        self.ui.listWidget.clear()
        found = False
        for key, data in self.recipes.items():
            value = data.get(self.field, '')
            if not value:
                continue
            val_lower = value.lower()
            index = val_lower.find(self.query)
            if index != -1:
                # Проверяем, что найденное совпадение - отдельное слово
                left_ok = index == 0 or not val_lower[index - 1].isalnum()
                right_index = index + len(self.query)
                right_ok = right_index == len(val_lower) or not val_lower[right_index].isalnum()
                if left_ok and right_ok:
                    # Создаём элемент списка и добавляем его в виджет
                    item = QListWidgetItem(data.get('title', ''))
                    item.setData(Qt.ItemDataRole.UserRole, key)
                    self.ui.listWidget.addItem(item)
                    found = True
        if not found:
            # Если ничего не найдено, показываем сообщение
            no_item = QListWidgetItem("Ничего не найдено")
            no_item.setFlags(Qt.ItemFlag.NoItemFlags)
            self.ui.listWidget.addItem(no_item)

    def show_recipe(self, item):
        # Очищаем списки ингредиентов и шагов перед отображением
        self.ui.ingr.clear()
        self.ui.listWidget_3.clear()
        key = item.data(Qt.ItemDataRole.UserRole)
        recipe = self.recipes.get(key)
        if recipe:
            # Заполняем список ингредиентов
            for group in recipe.get('ingredients', []):
                name = group.get('name', '')
                if name:
                    self.ui.ingr.addItem(f"{name}:")
                for ing in group.get('list', []):
                    ing_name = ing.get('name', '')
                    val = ing.get('value', '')
                    typ = ing.get('type', '')
                    amt = ing.get('amount', '')
                    amt_str = f", {amt}" if amt else ""
                    text = f"• {ing_name} — {val} {typ}{amt_str}".strip()
                    self.ui.ingr.addItem(text)
            # Отображаем описание рецепта, если есть
            desc = recipe.get('description', '')
            if desc:
                self.ui.listWidget_3.addItem(desc)
            # Отображаем шаги приготовления рецепта
            for step in recipe.get('instruction', []):
                step_text = step.get('text', '')
                if step_text:
                    self.ui.listWidget_3.addItem(f"• {step_text}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window1 = MainWindow()
    window1.show()
    sys.exit(app.exec())
