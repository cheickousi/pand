import random


class Board(object):
    def __init__(self, number_cities, number_epicenter):
        self.cities = number_cities
        self.epicenter = number_epicenter
        self.items_list = self.__load_cases__()
        self.size = self.cities
        self.__left_side = self.epicenter
        self.__right_side = self.epicenter + 1

    def __load_cases__(self):
        try:
            buckets = [0] * self.cities
            buckets[self.epicenter] = 1
            return buckets
        except IndexError:
            # raise IndexError
            print('we have an issue')

    def __iter__(self):
        return self

    def __str__(self):
        return str(self.items_list)

    def __repr__(self):
        return repr(self.items_list)

    def move(self, city):

        # Inspection Step
        try:
            current_case_load = self.items_list[city]
        except IndexError:
            return 'we have another issue'
        # Diseases Spreading Step
        self.__spreading_disease()
        return current_case_load

    def __spreading_disease(self):
        if self.__left_side == 0 and self.__right_side == self.size - 1:
            self.items_list = [x + 1 for x in self.items_list]

        if self.__left_side - 1 >= 0 and self.__right_side + 1 < self.size:
            self.items_list[self.__left_side - 1: self.__right_side + 1] = [x + 1 for x in self.items_list[
                                                                                           self.__left_side - 1: self.__right_side + 1]]
            self.__right_side += 1
            self.__left_side -= 1
        elif self.__left_side - 1 < 0 and self.__right_side + 1 < self.size:
            self.items_list[self.__left_side: self.__right_side + 1] = [x + 1 for x in self.items_list[
                                                                                       self.__left_side: self.__right_side + 1]]
            self.__right_side += 1
        elif self.__left_side - 1 >= 0 and self.__right_side + 1 >= self.size:
            self.items_list[self.__left_side - 1:self.__right_side + 1] = [x + 1 for x in self.items_list[
                                                                                          self.__left_side - 1:self.__right_side + 1]]
            self.__left_side -= 1
        else:
            print(self.items_list)
            print(self.__left_side)
            print(self.__right_side)

            print('we need to map this step')
        return


class Solver(object):
    def __init__(self, board: Board):
        self.input = board
        self.result = 0

    def __str__(self):
        return str(self.result)

    def __repr__(self):
        return repr(self.result)

    def solve(self, counter=0):
        size = self.input.size
        random_input = random.randrange(0, size - 1)
        current_index_value = self.input.move(random_input)
        counter += 1
        if current_index_value == 0:
            self.solver(counter)
        else:
            if current_index_value == counter:
                self.result = random_input
            numbers_of_cities_from_epicenter = counter - current_index_value
            next_city_value = self.input.move(random_input + 1)

            if next_city_value > current_index_value:
                self.result = random_input + numbers_of_cities_from_epicenter
            else:
                self.result = random_input - numbers_of_cities_from_epicenter

        return self.result
