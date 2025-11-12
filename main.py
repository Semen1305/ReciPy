import io
import sys
import json
from PyQt6.QtCore import Qt
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem

main_window = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>ReciPy</class>
 <widget class="QMainWindow" name="ReciPy">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1558</width>
    <height>824</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>ReciPy</string>
  </property>
  <property name="windowIcon">
   <iconset>
    <normaloff>../картинки/icon.png</normaloff>../картинки/icon.png</iconset>
  </property>
  <property name="styleSheet">
   <string notr="true">color:rgb(35, 28, 255);
font-weight: bold;
font-size: 32pt;
font-family: &quot;Comic Sans MS&quot;, cursive, sans-serif;</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <property name="styleSheet">
    <string notr="true"/>
   </property>
   <layout class="QHBoxLayout" name="horizontalLayout_4">
    <item>
     <layout class="QVBoxLayout" name="verticalLayout_2">
      <item>
       <layout class="QHBoxLayout" name="horizontalLayout_3">
        <item>
         <widget class="QLineEdit" name="name">
          <property name="styleSheet">
           <string notr="true">color:rgb(0, 0, 0);
font-weight: bold;
font-size: 16pt;
font-family: &quot;Comic Sans MS&quot;, cursive, sans-serif;</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="found">
          <property name="styleSheet">
           <string notr="true">color:rgb(0, 0, 0);
font-weight: bold;
font-size: 16pt;
font-family: &quot;Comic Sans MS&quot;, cursive, sans-serif;</string>
          </property>
          <property name="text">
           <string>Найти по названию</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item>
       <layout class="QVBoxLayout" name="verticalLayout">
        <item>
         <layout class="QHBoxLayout" name="horizontalLayout">
          <item>
           <widget class="QPushButton" name="supi">
            <property name="enabled">
             <bool>true</bool>
            </property>
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="styleSheet">
             <string notr="true">background-image: url(C:/Users/Сергей/Desktop/картинки/sup.png);
background-repeat: no-repeat;
background-position: center;
background-origin: content;
background-clip: padding;
</string>
            </property>
            <property name="text">
             <string>Супы</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="vtoroe">
            <property name="enabled">
             <bool>true</bool>
            </property>
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="styleSheet">
             <string notr="true">background-image: url(C:/Users/Сергей/Desktop/картинки/vtoroe.png);
background-repeat: no-repeat;
background-position: center;
background-origin: content;
background-clip: padding;</string>
            </property>
            <property name="text">
             <string>Вторые блюда</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="deserti">
            <property name="enabled">
             <bool>true</bool>
            </property>
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="styleSheet">
             <string notr="true">background-image: url(C:/Users/Сергей/Desktop/картинки/desert.png);
background-repeat: no-repeat;
background-position: center;
background-origin: content;
background-clip: padding;</string>
            </property>
            <property name="text">
             <string>Десерты</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="vipechka">
            <property name="enabled">
             <bool>true</bool>
            </property>
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="styleSheet">
             <string notr="true">background-image: url(C:/Users/Сергей/Desktop/картинки/vipechka.png);
background-repeat: no-repeat;
background-position: center;
background-origin: content;
background-clip: padding;
</string>
            </property>
            <property name="text">
             <string>Выпечка</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="napitki">
            <property name="enabled">
             <bool>true</bool>
            </property>
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="styleSheet">
             <string notr="true">background-image: url(C:/Users/Сергей/Desktop/картинки/napitok.png);
background-repeat: no-repeat;
background-position: center;
background-origin: content;
background-clip: padding;
</string>
            </property>
            <property name="text">
             <string>Напитки</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
        <item>
         <layout class="QHBoxLayout" name="horizontalLayout_2">
          <item>
           <widget class="QPushButton" name="zagotovki">
            <property name="enabled">
             <bool>true</bool>
            </property>
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="styleSheet">
             <string notr="true">background-image: url(C:/Users/Сергей/Desktop/картинки/zagotovki.png);
background-repeat: no-repeat;
background-position: center;
background-origin: content;
background-clip: padding;
</string>
            </property>
            <property name="text">
             <string>Заготовки</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="salat">
            <property name="enabled">
             <bool>true</bool>
            </property>
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="styleSheet">
             <string notr="true">background-image: url(C:/Users/Сергей/Desktop/картинки/salad.png);
background-repeat: no-repeat;
background-position: center;
background-origin: content;
background-clip: padding;
</string>
            </property>
            <property name="text">
             <string>Салаты</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="zakuski">
            <property name="enabled">
             <bool>true</bool>
            </property>
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="styleSheet">
             <string notr="true">background-image: url(C:/Users/Сергей/Desktop/картинки/zakuski.png);
background-repeat: no-repeat;
background-position: center;
background-origin: content;
background-clip: padding;
</string>
            </property>
            <property name="text">
             <string>Закуски</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="testo">
            <property name="enabled">
             <bool>true</bool>
            </property>
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="styleSheet">
             <string notr="true">background-image: url(C:/Users/Сергей/Desktop/картинки/testo.png);
background-repeat: no-repeat;
background-position: center;
background-origin: content;
background-clip: padding;
</string>
            </property>
            <property name="text">
             <string>Тесто</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="sousi">
            <property name="enabled">
             <bool>true</bool>
            </property>
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="styleSheet">
             <string notr="true">background-image: url(C:/Users/Сергей/Desktop/картинки/sousi.png);
background-repeat: no-repeat;
background-position: center;
background-origin: content;
background-clip: padding;
</string>
            </property>
            <property name="text">
             <string>Соусы</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
       </layout>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1558</width>
     <height>66</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
second_window = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow1</class>
 <widget class="QMainWindow" name="MainWindow1">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1059</width>
    <height>725</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Рецепты</string>
  </property>
  <property name="windowIcon">
   <iconset>
    <normaloff>../картинки/icon.png</normaloff>../картинки/icon.png</iconset>
  </property>
  <property name="styleSheet">
   <string notr="true">color: black;
font-weight: bold;
font-size: 16pt;
font-family: &quot;Comic Sans MS&quot;, cursive, sans-serif;</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QHBoxLayout" name="horizontalLayout_2">
    <item>
     <layout class="QHBoxLayout" name="horizontalLayout">
      <item>
       <layout class="QVBoxLayout" name="verticalLayout">
        <item>
         <widget class="QLabel" name="label">
          <property name="styleSheet">
           <string notr="true">color: black;
font-weight: bold;
font-size: 16pt;
font-family: &quot;Comic Sans MS&quot;, cursive, sans-serif;</string>
          </property>
          <property name="text">
           <string>Название рецептов</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QListWidget" name="listWidget">
          <property name="styleSheet">
           <string notr="true">background-color: rgb(230, 230, 255);
</string>
          </property>
         </widget>
        </item>
       </layout>
      </item>
      <item>
       <layout class="QVBoxLayout" name="verticalLayout_4">
        <item>
         <layout class="QVBoxLayout" name="verticalLayout_2">
          <item>
           <widget class="QLabel" name="label_2">
            <property name="styleSheet">
             <string notr="true">color: black;
font-weight: bold;
font-size: 16pt;
font-family: &quot;Comic Sans MS&quot;, cursive, sans-serif;</string>
            </property>
            <property name="text">
             <string>Ингредиенты</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QListWidget" name="ingr">
            <property name="styleSheet">
             <string notr="true">background-color: rgb(255, 226, 246);
</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
        <item>
         <layout class="QVBoxLayout" name="verticalLayout_3">
          <item>
           <widget class="QLabel" name="label_3">
            <property name="styleSheet">
             <string notr="true">color: black;
font-weight: bold;
font-size: 16pt;
font-family: &quot;Comic Sans MS&quot;, cursive, sans-serif;</string>
            </property>
            <property name="text">
             <string>Шаги приготовления</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QListWidget" name="listWidget_3">
            <property name="styleSheet">
             <string notr="true">background-color: rgb(255, 227, 224);
</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
       </layout>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1059</width>
     <height>36</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Загружаем UI главного окна из строки
        f = io.StringIO(main_window)
        uic.loadUi(f, self)
        # Связываем кнопку поиска по имени с функцией открытия второго окна с поиском по названию
        self.found.clicked.connect(self.open_second_window_by_name)
        # Связываем кнопки категорий с поиском
        self.supi.clicked.connect(self.open_second_window_by_category)
        self.vtoroe.clicked.connect(self.open_second_window_by_category)
        self.deserti.clicked.connect(self.open_second_window_by_category)
        self.vipechka.clicked.connect(self.open_second_window_by_category)
        self.napitki.clicked.connect(self.open_second_window_by_category)
        self.zagotovki.clicked.connect(self.open_second_window_by_category)
        self.salat.clicked.connect(self.open_second_window_by_category)
        self.zakuski.clicked.connect(self.open_second_window_by_category)
        self.testo.clicked.connect(self.open_second_window_by_category)
        self.sousi.clicked.connect(self.open_second_window_by_category)

    def open_second_window_by_name(self):
        # Получаем текст из поля поиска и открываем второе окно с поиском по названию
        search_text = self.name.text()
        self.window2 = Recepies(search_text, search_by='title')
        self.window2.show()

    def open_second_window_by_category(self):
        # Получаем текст кнопки категории и открываем второе окно с поиском по категории
        btn = self.sender()
        if btn:
            if __name__ == '__main__':
                category_text = btn.text().strip().lower()
            self.window2 = Recepies(category_text, search_by='category')
            self.window2.show()


class Recepies(QMainWindow):
    def __init__(self, search_text, search_by='title'):
        super().__init__()
        # Загружаем UI второго окна из строки
        f = io.StringIO(second_window)
        uic.loadUi(f, self)
        # Сохраняем поисковый текст и критерий поиска
        self.search_text = search_text.lower().strip()
        self.search_by = search_by
        # Загружаем рецепты из файла
        self.recipes = self.load_recipes()
        # Выполняем фильтрацию и наполняем список
        self.e_list()
        # Связываем клик на рецепте с функцией показа рецепта
        self.listWidget.itemClicked.connect(self.show_recipe)

    def load_recipes(self):
        # Загружаем JSON с рецептами из файла
        with open('all_recipes.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    def e_list(self):
        # Очищаем список
        self.listWidget.clear()
        found = False
        # Для каждого рецепта проверяем, есть ли ключ по поиску
        for key, recipe in self.recipes.items():
            value = recipe.get(self.search_by, '')
            if not value:
                continue
            # Приводим значение к нижнему регистру, разбиваем на слова
            value_clean = value.lower()
            words = value_clean
            # Проверяем совпадение целого слова с поиском
            if self.search_text in words:
                # Если совпало, добавляем элемент в список и сохраняем ключ
                item = QListWidgetItem(recipe.get('title', ''))
                item.setData(Qt.ItemDataRole.UserRole, key)
                self.listWidget.addItem(item)
                found = True
        # Если ничего не найдено, показываем сообщение без возможности выбора
        if not found:
            no_item = QListWidgetItem("Ничего не найдено")
            no_item.setFlags(Qt.ItemFlag.NoItemFlags)
            self.listWidget.addItem(no_item)

    def show_recipe(self, item):
        # Очищаем списки ингредиентов и шагов
        self.ingr.clear()
        self.listWidget_3.clear()
        # Получаем ключ выбранного рецепта
        key = item.data(Qt.ItemDataRole.UserRole)
        recipe = self.recipes.get(key)
        if recipe:
            # Заполняем ингредиенты
            ingredients = recipe.get('ingredients', [])
            for group in ingredients:
                group_name = group.get('name', '')
                if group_name:
                    self.ingr.addItem(f"{group_name}:")
                for ing in group.get('list', []):
                    name = ing.get('name', '')
                    value = ing.get('value', '')
                    typ = ing.get('type', '')
                    amount = ing.get('amount', '')
                    amount_str = f", {amount}" if amount else ""
                    text = f"• {name} — {value} {typ}{amount_str}".strip()
                    self.ingr.addItem(text)
            # Показываем описание рецепта
            description = recipe.get('description', '')
            if description:
                self.listWidget_3.addItem(description)
            # Показываем шаги приготовления
            instruction = recipe.get('instruction', [])
            for step in instruction:
                step_text = step.get('text', '')
                if step_text:
                    self.listWidget_3.addItem(f"• {step_text}")


if __name__ == "__main__":
    # Запуск приложения
    app = QApplication(sys.argv)
    window1 = MainWindow()
    window1.show()
    sys.exit(app.exec())
