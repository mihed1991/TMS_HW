# """
# ПчёлоСлон
# Экземпляр класса инициализируется двумя целыми числами,
# первое относится к пчеле, второе  к слону. Класс реализует
# следующие методы:
# ● fly()  возвращает True, если часть пчелы не меньше части
# слона,
# иначе  False
# ● trumpet()  если часть слона не меньше части пчелы,
# возвращает строку “tu-tu-doo-doo”,
# иначе  “wzzzz”
# ● eat(meal, value)  может принимать в meal только ”nectar”
# или “grass”.
# Если съедает нектар, то value вычитается из
# части слона, пчеле добавляется.
# Иначе  наоборот. Не
# может увеличиваться больше 100 и уменьшаться меньше 0
# """


# class ПчёлоСлон:
#     def __init__(self, bee_part, elefant_part):
#         self.bee_part = bee_part
#         self.elefant_part = elefant_part

#     def fly(self):
#         return self.bee_part >= self.elefant_part

#     def trumpet(self):
#         if self.elefant_part >= self.bee_part:
#             return "tu-tu-doo-doo"
#         else:
#             return "wzzzz"

#     def eat(self, meal, value):
#         if meal == "nectar":
#             self.bee_part = min(100, self.bee_part + value)
#             self.elefant_part = max(0, self.elefant_part - value)

#         elif meal == "grass":
#             self.bee_part = min(0, self.bee_part - value)
#             self.elefant_part = max(100, self.elefant_part + value)

#         else:
#             raise ValueError("Meal must be 'nectar' or 'grass'")


# # Пример использования - For example
# пчёлоСлон = ПчёлоСлон(50, 80)

# print(пчёлоСлон.fly())
# print(пчёлоСлон.trumpet())

# пчёлоСлон.eat("nectar", 20)
# print(пчёлоСлон.bee_part)
# print(пчёлоСлон.elefant_part)

# пчёлоСлон.eat("grass", 10)
# print(пчёлоСлон.bee_part)
# print(пчёлоСлон.elefant_part)


# """
# Класс «Автобус». Класс содержит свойства:
# ● скорость
# ● максимальное количество посадочных мест
# ● максимальная скорость
# ● список фамилий пассажиров
# ● флаг наличия свободных мест
# ● словарь мест в автобусе
# Методы:
# ● посадка и высадка одного или нескольких пассажиров
# ● увеличение и уменьшение скорости на заданное значение
# ● операции in, += и -= (посадка и высадка пассажира по
# фамилии)
# """


# class Автобус:
#     def __init__(self, max_seats, max_speed):
#         self.speed = 0
#         self.max_seats = max_seats
#         self.max_speed = max_speed
#         self.passengers = []
#         self.free_seats = max_seats
#         self.seat_map = {i: None for i in range(1, max_seats + 1)}

#     def board_passenger(self, *passenger_names):
#         for name in passenger_names:
#             if self.free_seats > 0:
#                 for seat, нuman in self.seat_map.items():
#                     if нuman is None:
#                         self.seat_map[seat] = name
#                         self.passengers.append(name)
#                         self.free_seats -= 1
#                         break
#             else:
#                 print(f"No free seats available for {name}")

#     def disembark_passenger(self, *passenger_names):
#         for name in passenger_names:
#             if name in self.passengers:
#                 self.passengers.remove(name)
#                 for seat, нuman in self.seat_map.items():
#                     if нuman == name:
#                         self.seat_map[seat] = None
#                         self.free_seats += 1
#                         break
#             else:
#                 print(f"{name} is not on the bus")

#     def change_speed(self, delta):
#         new_speed = self.speed + delta
#         if 0 <= new_speed <= self.max_speed:
#             self.speed = new_speed
#         else:
#             print(f"Speed must be between 0 and {self.max_speed}")

#     def __contains__(self, name):
#         return name in self.passengers

#     def __iadd__(self, name):
#         self.board_passenger(name)
#         return self

#     def __isub__(self, name):
#         self.disembark_passenger(name)
#         return self

#     def __str__(self):
#         return (
#             f"Speed: {self.speed} km/h, Max Seats: {self.max_seats}, "
#             f"Max Speed: {self.max_speed} km/h, Passengers: {self.passengers}, "
#             f"Free Seats: {self.free_seats}, Seat Map: {self.seat_map}"
#         )


# # Пример использования
# bus = Автобус(max_seats=2, max_speed=100)

# print(bus)

# bus.board_passenger("Ivanov", "Petrov", "Akimov", "Sidorov", "Sobolev", "Lubin")
# print(bus)

# bus += "Sidorov"
# print(bus)

# bus -= "Ivanov"
# print(bus)

# bus.change_speed(100)
# print(bus)

# bus.change_speed(-20)
# print(bus)
