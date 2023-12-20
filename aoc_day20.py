import functools
from abc import abstractmethod
from collections import deque, defaultdict
from enum import Enum
from math import lcm

from aoc_lib import solve_problem

INPUT = '''%rp -> gq, sd
&kh -> cs
%jz -> pl, jb
%dx -> tx
%dh -> bm, sd
&zv -> ns, dx, hl, hn, fm
%xb -> ds, sk
%hv -> sk, kr
%db -> zv, zz
&sk -> rg, hh, hv, kr, kh, zl, zn
%tc -> jz
%dj -> ts, pl
%jk -> sd, vh
%fm -> dx, zv
%dp -> sd, cc
%vh -> sd
&lz -> cs
%kr -> rg
%jb -> bf, pl
%kz -> sk
%ts -> pl, bs
%gr -> ns, zv
%kc -> sd, kf
%jd -> zv
%bs -> vg
%zk -> rp
%vf -> zk
%mm -> ms, sk
%qc -> pl, dj
%fk -> qc
%bm -> vf, sd
%ds -> kz, sk
%sn -> zv, jd
%zn -> mm
%ct -> fk
%np -> sk, xb
&tg -> cs
%tx -> cm, zv
%zl -> hh
%zz -> px, zv
%ms -> zl, sk
%ns -> db
%px -> zv, sn
broadcaster -> fm, hv, kc, bv
&hn -> cs
%hh -> np
%kf -> dh
%vg -> pl, tc
%bv -> ct, pl
&pl -> bv, fk, ct, bs, tg, tc
%cm -> zv, hl
%cc -> sd, jk
%bf -> pl
%hl -> gr
&cs -> rx
%gq -> dp
%rg -> zn
&sd -> zk, kf, gq, lz, kc, vf'''

TEST_INPUT = '''broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a'''

TEST_INPUT2 = '''broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output'''


class Pulse:
    HIGH = True
    LOW = False


class Module:
    def __init__(self, definition: str):
        name, destinations = definition.split(' -> ')
        self.name = name.removeprefix('&').removeprefix('%')
        self.definition = definition
        self.destinations = list(map(str.strip, destinations.split(',')))
        self.receivers = []

    @staticmethod
    def from_def(definition: str):
        match definition[0]:
            case '%':
                return FlipFlop(definition)
            case '&':
                return Conjunction(definition)
            case 'b':
                return Broadcaster(definition)

    def __bool__(self):
        return True

    @abstractmethod
    def handle_pulse(self, pulse: bool, sender: str) -> tuple[bool, list[str], str]:
        pass

    def set_receivers(self, senders: list):
        self.receivers = [s for s in senders if self.name in s.destinations]


class FlipFlop(Module):
    def __init__(self, definition: str):
        super().__init__(definition)
        self.on = False

    def handle_pulse(self, pulse: bool, sender: str) -> tuple[bool, list[str], str] | None:
        if pulse == Pulse.LOW:
            self.on = not self.on
            return self.on, self.destinations, self.name
        return None

    def __bool__(self):
        return self.on


class Conjunction(Module):
    def __init__(self, definition):
        super().__init__(definition)
        self.last_pulses = {}

    def handle_pulse(self, pulse: bool, sender: str) -> tuple[bool, list[str], str]:
        self.last_pulses[sender] = pulse
        return not all(self.last_pulses.values()), self.destinations, self.name

    def set_receivers(self, senders: list):
        super().set_receivers(senders)
        self.last_pulses = {s.name: False for s in self.receivers}


class Broadcaster(Module):
    def handle_pulse(self, pulse: bool, sender: str) -> tuple[bool, list[str], str]:
        return pulse, self.destinations, self.name


def trace_receivers(module: Module, modules: dict, found: set = None) -> set:
    if module.name == 'broadcaster':
        return found
    for receiver in module.receivers:
        if receiver.name not in found:
            found.add(receiver.name)
            return trace_receivers(modules[receiver.name], modules, found)


def solve(input_: str, max_iterations: int = 0) -> int:
    results = {Pulse.HIGH: 0, Pulse.LOW: 0}
    q = deque()
    modules = {module.name: module for module in map(Module.from_def, input_.splitlines())}
    for module in modules.values():
        module.set_receivers(modules.values())

    rx_sender = None
    for module in modules.values():
        if 'rx' in module.destinations:
            rx_sender = module
            break
    rx_receivers = [r.name for r in rx_sender.receivers] if rx_sender else []
    found = {module: 0 for module in rx_receivers}
    for i in range(max_iterations or 5_000):
        q.append((Pulse.LOW, ['broadcaster'], 'button'))
        while q:
            pulse, destinations, sender = q.popleft()
            # Part 2
            if not max_iterations:
                if pulse == Pulse.HIGH and sender in found and not found[sender]:
                    found[sender] = i + 1
                    if all(found.values()):
                        return lcm(*found.values())

            for destination in destinations:
                results[pulse] += 1
                if destination not in modules:
                    continue
                if handled := modules[destination].handle_pulse(pulse, sender):
                    q.append(handled)
    # Part 1
    high, low = results.values()
    return high * low


if __name__ == '__main__':
    part1_args = [1000]
    expected_1 = [
        (32000000, [TEST_INPUT, *part1_args]),
        (11687500, [TEST_INPUT2, *part1_args])
    ]
    func_1 = solve

    part2_args = []
    expected_2 = []
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    # There is no test case for part 2.
    solve_problem(func_2, 2, None, INPUT, *part2_args)
