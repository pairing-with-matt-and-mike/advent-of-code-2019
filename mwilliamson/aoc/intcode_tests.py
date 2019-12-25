from .intcode import run


_JUNK = 72984721984719824


def test_halt():
    result = run([99])

    assert result == [99]


def test_add_adds_together_numbers_from_two_addresses_and_stores_in_third_address():
    result = run([
        1, 6, 9, 12,
        99,
        _JUNK,
        20,
        _JUNK,
        _JUNK,
        7,
        _JUNK,
        _JUNK,
        42,
    ])

    assert result == [
        1, 6, 9, 12,
        99,
        _JUNK,
        20,
        _JUNK,
        _JUNK,
        7,
        _JUNK,
        _JUNK,
        27,
    ]


def test_multiply_multiplies_together_numbers_from_two_addresses_and_stores_in_third_address():
    result = run([
        2, 6, 9, 12,
        99,
        _JUNK,
        20,
        _JUNK,
        _JUNK,
        7,
        _JUNK,
        _JUNK,
        42,
    ])

    assert result == [
        2, 6, 9, 12,
        99,
        _JUNK,
        20,
        _JUNK,
        _JUNK,
        7,
        _JUNK,
        _JUNK,
        140,
    ]



def test_input_takes_input_and_saves_to_address():
    inputs = [44, 43, 42]

    def next_input():
        return inputs.pop()

    result = run([
        3, 7,
        3, 8,
        3, 9,
        99,
        _JUNK,
        _JUNK,
        _JUNK,
    ], next_input=next_input)

    assert result == [
        3, 7,
        3, 8,
        3, 9,
        99,
        42,
        43,
        44,
    ]
