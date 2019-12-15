from decimal import Decimal, getcontext
import heapq
import sys

class Square():
    def __init__(self, x, y, sin_theta, cos_theta, edge):
        self.x = x
        self.y = y
        self.sin_theta = sin_theta
        self.cos_theta = cos_theta
        self.edge = edge

    def __str__(self):
        return str((self.x, self.y, self.sin_theta, self.cos_theta, self.edge))

    def __repr__(self):
        return self.__str__()

    def build_left_square(self):
        x = self.x - self.edge * self.sin_theta
        y = self.y + self.edge * self.cos_theta
        sin_theta = self.sin_theta * Decimal(0.8) + self.cos_theta * Decimal(0.6)  
        cos_theta = self.cos_theta * Decimal(0.8) - self.sin_theta * Decimal(0.6)
        edge = self.edge * Decimal(0.8)
        return Square(x, y, sin_theta, cos_theta, edge)

    def build_right_square(self):
        x = self.x - Decimal(1.48) * self.edge * self.sin_theta + Decimal(0.64) * self.edge * self.cos_theta
        y = self.y + Decimal(0.64) * self.edge * self.sin_theta + Decimal(1.48) * self.edge * self.cos_theta
        sin_theta = - self.cos_theta * Decimal(0.8) + self.sin_theta * Decimal(0.6)
        cos_theta = self.sin_theta * Decimal(0.8) + self.cos_theta * Decimal(0.6)
        edge = self.edge * Decimal(0.6)
        return Square(x, y, sin_theta, cos_theta, edge)

    def get_leftmost_coordinate(self):
        coordinates = [
            self.x,
            self.x + self.edge * self.cos_theta,
            self.x - self.edge * self.sin_theta + self.edge * self.cos_theta,
            self.x - self.edge * self.sin_theta,
        ]
        return sorted(coordinates)[0]

    def get_rightmost_coordinate(self):
        coordinates = [
            self.x,
            self.x + self.edge * self.cos_theta,
            self.x - self.edge * self.sin_theta + self.edge * self.cos_theta,
            self.x - self.edge * self.sin_theta,
        ]
        return sorted(coordinates)[-1]

    def get_topmost_coordinate(self):
        coordinates = [
            self.y,
            self.y + self.edge * self.sin_theta,
            self.y + self.edge * self.sin_theta + self.edge * self.cos_theta,
            self.y + self.edge * self.cos_theta,
        ]
        return sorted(coordinates)[-1]

    def get_bottommost_coordinate(self):
        coordinates = [
            self.y,
            self.y + self.edge * self.sin_theta,
            self.y + self.edge * self.sin_theta + self.edge * self.cos_theta,
            self.y + self.edge * self.cos_theta,
        ]
        return sorted(coordinates)[0]

class PythagoreanTree():
    def __init__(self, root_square):
        self.INF = 10**100
        self.root_square = root_square

    def get_boundary_coordinate(self):
        h = []
        index = 0
        heapq.heappush(h, (self.get_boundary(self.root_square), index, self.root_square))

        performance_counter = 0
        boundary_so_far = self.INF
        while performance_counter < 10**5:
            performance_counter += 1
            boundary, dummy_index, square = heapq.heappop(h)
            if square.edge < 1e-15:
                continue
            if boundary < boundary_so_far:
                boundary_so_far = boundary
            left_square = square.build_left_square()
            right_square = square.build_right_square()
            heapq.heappush(h, (self.get_boundary(left_square), index + 1, left_square))
            heapq.heappush(h, (self.get_boundary(right_square), index + 2, right_square))
            index += 2
        return boundary_so_far

class PythagoreanLeftmostTree(PythagoreanTree):
    def __init__(self):
        root_square = Square(Decimal(0), Decimal(0), Decimal(0), Decimal(1), Decimal(1))
        root_square = root_square.build_left_square()
        root_square = root_square.build_left_square()
        root_square = root_square.build_left_square()
        super().__init__(root_square)

    def get_boundary(self, square):
        return square.get_leftmost_coordinate()

class PythagoreanRightmostTree(PythagoreanTree):
    def __init__(self):
        root_square = Square(Decimal(0), Decimal(0), Decimal(0), Decimal(1), Decimal(1))
        root_square = root_square.build_right_square()
        root_square = root_square.build_right_square()
        root_square = root_square.build_left_square()
        super().__init__(root_square)

    def get_boundary(self, square):
        return -square.get_rightmost_coordinate()

class PythagoreanTopmostTree(PythagoreanTree):
    def __init__(self):
        root_square = Square(Decimal(0), Decimal(0), Decimal(0), Decimal(1), Decimal(1))
        root_square = root_square.build_left_square()
        root_square = root_square.build_right_square()
        root_square = root_square.build_left_square()
        super().__init__(root_square)

    def get_boundary(self, square):
        return -square.get_topmost_coordinate()

class PythagoreanBottommostTree(PythagoreanTree):
    def __init__(self):
        root_square = Square(Decimal(0), Decimal(0), Decimal(0), Decimal(1), Decimal(1))
        root_square = root_square.build_left_square()
        root_square = root_square.build_left_square()
        root_square = root_square.build_left_square()
        root_square = root_square.build_left_square()
        root_square = root_square.build_left_square()
        super().__init__(root_square)

    def get_boundary(self, square):
        return square.get_bottommost_coordinate()

class Problem():
    def solve(self):
        getcontext().prec = 20
        min_x = PythagoreanLeftmostTree().get_boundary_coordinate()
        max_x = -PythagoreanRightmostTree().get_boundary_coordinate()
        min_y = PythagoreanBottommostTree().get_boundary_coordinate()
        max_y = -PythagoreanTopmostTree().get_boundary_coordinate()
        print('min_x =>', min_x)
        print('max_x =>', max_x)
        print('min_y =>', min_y)
        print('max_y =>', max_y)
        print('area =>', (max_x - min_x) * (max_y - min_y))

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
