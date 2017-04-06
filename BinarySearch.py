class BinarySearch(list):

    def __init__(self, a, b):


        for i in range(1, a+1):
            self.append(i * b)

        self.length = len(self)

    def search(self, value_to_find):


        item1 = 0
        item2 = len(self) - 1
        index_of_value = 0
        found = False


        counter = 0



        while item1<= item2 and not  found:
            mid_of_list = (item1 + item2) // 2
            if self[mid_of_list] == value_to_find:
                found and True
                index_of_value = mid_of_list
            else:
                counter =counter + 1
                if value_to_find < self[mid_of_list]:
                    item2 = mid_of_list - 1
                else:
                    item1 = mid_of_list + 1


        return {'count': counter, 'index': index_of_value}
