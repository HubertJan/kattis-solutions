from dataclasses import dataclass
from math import ceil
import sys
import string
from enum import Enum

class Color(Enum):
    WHITE = 0
    BLACK = 1
    
ALPHA = "abcdefghijklmnopqrstuvwxyz".upper()

@dataclass
class Position:
    x: str
    y: int
    
    @property
    def x_pos(self):
        return string.ascii_uppercase.index(self.x) + 1

def find_color(point: Position):
    if point.x_pos % 2 != 0 and point.y % 2 != 0:
        return Color.BLACK
    if point.x_pos % 2 == 0 and point.y % 2 == 0:
        return Color.BLACK
    return Color.WHITE
    
def calculate_distance(point, other_point):
    return [point.x_pos - other_point.x_pos, point.y - other_point.y]

def main():
    n = int(sys.stdin.readline().rstrip())
    for _ in range(0, n):
        input = sys.stdin.readline().rstrip().split()
        pos = Position(x= input[0], y= int(input[1]))
        other_pos = Position(x= input[2], y= int(input[3]))
        color = find_color(pos)
        other_color = find_color(other_pos)
        if color != other_color:
            print("Impossible")
            continue
        dist = calculate_distance(pos, other_pos)
        if dist[0] == 0 and dist[1] == 0:
            print(f"{0} {pos.x} {pos.y}")
            continue
        if abs(dist[0]) == abs(dist[1]):
            print(f"{1} {pos.x} {pos.y} {other_pos.x} {other_pos.y}")
            continue
        avg = int(ceil((abs(dist[0]) + abs(dist[1]))/2))
        x = 0
        y = 0
        if other_pos.x_pos < pos.x_pos and other_pos.y < pos.y:
            x = pos.x_pos - avg
            y = pos.y - avg
        if other_pos.x_pos > pos.x_pos and other_pos.y > pos.y:
            x = pos.x_pos + avg
            y = pos.y + avg
        if other_pos.x_pos <= pos.x_pos and other_pos.y >= pos.y:
            x = pos.x_pos - avg
            y = pos.y + avg
        if other_pos.x_pos >= pos.x_pos and other_pos.y <= pos.y:
            x = pos.x_pos + avg
            y = pos.y - avg
        if x <= 0 or y <= 0 or 8 < y or 8 < x:
            dx = other_pos.x_pos - x
            dy = other_pos.y - y
            x = pos.x_pos + dx
            y = pos.y + dy
        mid_pos = Position(ALPHA[x - 1], y)
        
        print(f"{2} {pos.x} {pos.y} {mid_pos.x} {mid_pos.y} {other_pos.x} {other_pos.y}")
        
    
if __name__ == "__main__":
    main()