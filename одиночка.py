class GameSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameSettings, cls).__new__(cls)
            cls._instance.volume = 50
            cls._instance.difficulty = "Normal"
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls._instance

# Пример использования
settings1 = GameSettings()
settings2 = GameSettings()

# Проверим, что это один и тот же объект
print(settings1 is settings2)  # Выведет True

# Меняем настройки в одном объекте
settings1.volume = 70
settings1.difficulty = "Hard"

# Проверяем, что настройки изменились в обоих объектах
print(settings2.volume)  # Выведет 70
print(settings2.difficulty)  # Выведет "Hard"

