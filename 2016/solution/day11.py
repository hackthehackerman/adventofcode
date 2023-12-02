from copy import deepcopy
import itertools

from numpy import number
from rsa import sign


def one():
    """
    The first floor contains a promethium generator and a promethium-compatible microchip.
    The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
    The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
    The fourth floor contains nothing relevant."""

    elevator = 0
    floors = tuple(
        [
            tuple(["PmG", "PmM"]),
            tuple(["CoG", "CuG", "RuG", "PuG"]),
            tuple(["CoM", "CuM", "RuM", "PuM"]),
            tuple([]),
        ]
    )

    def safe(items: tuple[str]):
        chips = set()
        gens = set()
        for item in items:
            if item.endswith("M"):
                chips.add(item[:-1])
            else:
                gens.add(item[:-1])
        for chip in chips:
            if chip not in gens and len(gens) > 0:
                return False

        return True

    visited = set()
    states = [(elevator, floors)]  # elevator, [[number of pairs, number of single]]
    step = 0

    while True:
        new_states = []

        for state in states:
            elevator, floors = state
            if len(floors[3]) == 10:
                return step

            for i in range(1, 3):
                for move in itertools.permutations(floors[elevator], i):
                    remain = tuple(
                        [item for item in floors[elevator] if item not in move]
                    )
                    if not safe(remain) or not safe(move):
                        continue

                    for new_elevator in [elevator - 1, elevator + 1]:
                        if new_elevator < 0 or new_elevator > 3:
                            continue

                        new_floors = list(deepcopy(floors))
                        new_floors[elevator] = remain
                        new_floors[new_elevator] = tuple(
                            list(new_floors[new_elevator]) + list(move)
                        )
                        if not safe(new_floors[new_elevator]):
                            continue
                        for i in range(4):
                            new_floors[i] = tuple(sorted(new_floors[i]))

                        new_floors = tuple(new_floors)

                        if (
                            new_elevator,
                            new_floors,
                        ) not in visited:
                            visited.add((new_elevator, new_floors))
                            new_states.append((new_elevator, new_floors))

        states = new_states
        step += 1


def two():
    """
    The first floor contains a promethium generator and a promethium-compatible microchip.
    The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
    The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
    The fourth floor contains nothing relevant."""

    elevator = 0
    floors = tuple(
        [
            tuple(["PmG", "PmM", "ElG", "ElM", "DlG", "DlM"]),
            tuple(["CoG", "CuG", "RuG", "PuG"]),
            tuple(["CoM", "CuM", "RuM", "PuM"]),
            tuple([]),
        ]
    )

    def safe(items: tuple[str]):
        chips = set()
        gens = set()
        for item in items:
            if item.endswith("M"):
                chips.add(item[:-1])
            else:
                gens.add(item[:-1])
        for chip in chips:
            if chip not in gens and len(gens) > 0:
                return False

        return True

    def floor_signature(items):
        chips = set()
        gens = set()
        for item in items:
            if item.endswith("M"):
                chips.add(item[:-1])
            else:
                gens.add(item[:-1])
        number_of_pairs = 0
        number_of_single = 0
        for chip in chips:
            if chip in gens:
                number_of_pairs += 1
            else:
                number_of_single += 1
        for gen in gens:
            if gen not in chips:
                number_of_single += 1
        return (number_of_pairs, number_of_single)

    def signature(floors):
        return tuple([floor_signature(floor) for floor in floors])

    visited = set()
    states = [(elevator, floors)]  # elevator, [[number of pairs, number of single]]
    step = 0

    while True:
        new_states = []

        for state in states:
            elevator, floors = state
            if len(floors[3]) == 14:
                return step

            for i in range(1, 3):
                for move in itertools.permutations(floors[elevator], i):
                    remain = tuple(
                        [item for item in floors[elevator] if item not in move]
                    )
                    if not safe(remain) or not safe(move):
                        continue

                    for new_elevator in [elevator - 1, elevator + 1]:
                        if new_elevator < 0 or new_elevator > 3:
                            continue

                        new_floors = list(deepcopy(floors))
                        new_floors[elevator] = remain
                        new_floors[new_elevator] = tuple(
                            list(new_floors[new_elevator]) + list(move)
                        )
                        if not safe(new_floors[new_elevator]):
                            continue
                        for i in range(4):
                            new_floors[i] = tuple(sorted(new_floors[i]))

                        new_floors = tuple(new_floors)

                        if (
                            new_elevator,
                            signature(new_floors),
                        ) not in visited:
                            visited.add((new_elevator, signature(new_floors)))
                            new_states.append((new_elevator, new_floors))

        states = new_states
        step += 1


print("part one:", one())
print("part two:", two())
