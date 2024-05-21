import types


def flat_generator(list_of_list):
    parents = []
    parents.append({'children': list_of_list, 'current_index': 0})
    while len(parents) > 0:
        if parents[-1]['current_index'] == len(parents[-1]['children']):
            del parents[-1]

            continue

        old_index = parents[-1]['current_index']
        item = parents[-1]['children'][old_index]
        parents[-1]['current_index'] += 1

        if isinstance(item, list):
            parents.append({'children': item, 'current_index': 0})
            
            continue
        else:
            yield item

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()