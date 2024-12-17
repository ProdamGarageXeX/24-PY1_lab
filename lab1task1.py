import doctest
class Tree:
    def __init__(self, height: float, age: int, species: str):
        """
        Создание и подготовка объекта "Дерево"

        :param height: Высота дерева в метрах
        :param age: Возраст дерева в годах
        :param species: Вид дерева.

        Примеры:
        >>> tree = Tree(10.5, 15, "Oak")  # инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть числом.")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом.")
        self.height = height

        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть целым числом.")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")
        self.age = age

        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой.")
        if not species.strip():
            raise ValueError("Вид дерева не может быть пустым.")
        self.species = species

    def photosynthesize(self) -> None:
        """
        Запуск условного процесса фотосинтеза.
        Примеры:
        >>> tree = Tree(10.5, 15, "Oak")
        >>> tree.photosynthesize()
        """
        ...

    def grow(self, years: int) -> None:
        """
        Увеличивает возраст и высоту дерева.
        :param years: Количество лет, на которое увеличивается возраст дерева.
        :raise ValueError: Если количество лет отрицательное

        Примеры:
        >>> tree = Tree(10.5, 15, "Oak")
        >>> tree.grow(5)
        """
        if not isinstance(years, int):
            raise TypeError("Количество лет должно быть целым числом.")
        if years < 0:
            raise ValueError("Количество лет не может быть отрицательным.")
        ...

class House:
    def __init__(self, area: float, floors: int, material: str):
        """
        Создание и подготовка объекта "Дом".

        :param area: Площадь дома в квадратных метрах
        :param floors: Количество этажей
        :param material: Материал

        Примеры:
        >>> house = House(120.5, 2, "Brick")  # инициализация экземпляра класса
        """
        if not isinstance(area, (int, float)):
            raise TypeError("Площадь дома должна быть числом.")
        if area <= 0:
            raise ValueError("Площадь дома должна быть положительным числом.")
        self.area = area

        if not isinstance(floors, int):
            raise TypeError("Количество этажей должно быть целым числом.")
        if floors <= 0:
            raise ValueError("Количество этажей должно быть положительным числом.")
        self.floors = floors

        if not isinstance(material, str):
            raise TypeError("Материал дома должен быть строкой.")
        if not material.strip():
            raise ValueError("Материал дома не может быть пустым.")
        self.material = material

    def calculate_total_area(self) -> float:
        """
        Рассчитывает общую площадь дома с учетом количества этажей.
        :return: Общая площадь дома.
        Примеры:
        >>> house = House(120.5, 2, "Brick")
        >>> house.calculate_total_area()
        """
        ...

    def renovate(self, budget: float) -> None:
        """
        Выполняет ремонт дома в пределах бюджета
        :param budget: Бюджет на ремонт в неких денежных единицах
        :raise ValueError: Если бюджет отрицательный.
        Примеры:
        >>> house = House(120.5, 2, "Brick")
        >>> house.renovate(50000)
        """
        if not isinstance(budget, (int, float)):
            raise TypeError("Бюджет должен быть числом.")
        if budget < 0:
            raise ValueError("Бюджет не может быть отрицательным.")
        ...

class Son:
    def __init__(self, name: str, age: int, hobby: str):
        """
        Создание и подготовка объекта "Сын".

        :param name: Имя сына
        :param age: Возраст сына
        :param hobby: хобби сына

        Примеры:
        >>> son = Son("Vasily", 15, "Videogames")  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой.")
        if not name.strip():
            raise ValueError("Имя не может быть пустым.")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом.")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.age = age

        if not isinstance(hobby, str):
            raise TypeError("Хобби должно быть строкой.")
        if not hobby.strip():
            raise ValueError("Хобби не может быть пустым.")
        self.hobby = hobby

    def introduce(self) -> str:
        """
        Возвращает строку с представлением сына + возраст

        :return: Строка с представлением.

        Примеры:
        >>> son = Son("Vasily", 15, "Videogames")
        >>> son.introduce()
        """
        ...

    def celebrate_birthday(self) -> None:
        """
        Увеличивает возраст сына на один год

        Примеры:
        >>> son = Son("Vasily", 15, "Videogames")
        >>> son.celebrate_birthday()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
