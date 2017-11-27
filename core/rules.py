import json

from core.persist import retrieve_game


def validate_game(game):
    # previous_state = retrieve_game(game.id)
    previous_state = json.loads('{"id":"123ABC","players":['
                                '{"position":"West","cards":[],"resources":{"black":0,"blue":0,"green":1,"red":0,'
                                '"white":0,"gold":0},"nobles":[],"reserved":[]}, '
                                '{"position":"East"}],'
                                '"turn":"West","resources":{"black":1,"blue":1,"green":0,"red":0,"white":0,"gold":0},'
                                '"nobles":[],"row1":{"hidden":[],"revealed":[]},"row2":{"hidden":[],"revealed":[]},'
                                '"row3":{"hidden":[],"revealed":[]}}')
    comparison = identify_differences(previous_state, game)

    return comparison














def identify_differences(a, b):
    differences = identify_differences_recursive(a, b)
    return differences


def identify_differences_recursive(a, b):
    print("comparing %s and %s" % (a, b))
    if a != b:
        if isinstance(b, dict):
            return compare_dict(a, b)
        elif isinstance(b, list):
            return compare_list(a, b)

        return [(a, b)]

    print("equal", a, b)
    return []


def compare_dict(a, b):
    differences = []
    for key, value in b.items():
        child_differences = identify_differences_recursive(a[key], value)
        if len(child_differences) > 0:
            differences.append((key, child_differences))

    return differences


def compare_list(a, b):
    if len(a) > len(b):
        differences = compare_list(a[0: len(b)], b)
        differences.append(("-", a[len(b):]))
        return differences
    elif len(a) < len(b):
        differences = compare_list(a, b[0: len(a)])
        differences.append(("+", b[len(a):]))
        return differences
    else:
        differences = []
        for i, item in enumerate(b):
            differences.append((i, identify_differences_recursive(a[i], item)))

        return differences

