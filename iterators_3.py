class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.parents = []
        self.parents.append({'children': self.list_of_list, 'current_index': 0})

        return self

    def __next__(self):
        if len(self.parents) > 0:
            if self.parents[-1]['current_index'] == len(self.parents[-1]['children']):
                del self.parents[-1]

                return next(self)

            old_index = self.parents[-1]['current_index']
            item = self.parents[-1]['children'][old_index]
            self.parents[-1]['current_index'] += 1

            if isinstance(item, list):
                self.parents.append({'children': item, 'current_index': 0})

                return next(self)
            else:
                return item

        else:
            raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        # print(flat_iterator_item)
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()