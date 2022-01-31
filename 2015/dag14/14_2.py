import sys
from turtle import position

class Reindeer:
    def __init__(self, speed: int, duration: int, timeout: int) -> None:
        self._speed = speed
        self._period = duration + timeout
        self._duration = duration
        self._position = 0
        self._clock = 0
        self._score = 0

    def position(self) -> int:
        return self._position

    def step(self) -> None:
        if self._clock < self._duration: self._position += self._speed

        self._clock = (self._clock + 1) % (self._period)

    def inc(self) -> None:
        self._score += 1

with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [row.split(' ') for row in data]
    data = [Reindeer(*map(int, [e for e in elem if e.isnumeric()])) for elem in data]

i = 0

while i < 2503:
    for r in data: r.step()
    print([r.position() for r in data])
    max_pos = max([r.position() for r in data])
    for r in data:
        if r.position() == max_pos: r.inc()

    i += 1

print(max([r._score for r in data]))