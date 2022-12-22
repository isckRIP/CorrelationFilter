from dataclasses import dataclass


@dataclass
class GraphOfSignal:
    x: list
    y: list

# data = GraphOfSignal
# data.x = [10]
# print(data.x)
#
# new = GraphOfSignal
# print(new.x)