class FlatIterator:

    def __init__(self, list_of_list):
        self.main_list = list_of_list

    def __iter__(self):
        self.main_list_cursor = 0
        return self

    def __next__(self):
        obj = []
        for i in self.main_list:
            for j in i:
                obj += [j]

        if self.main_list_cursor < len(obj):
            res = obj[self.main_list_cursor]
            self.main_list_cursor += 1
            return res
        raise StopIteration

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()