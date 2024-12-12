import numpy as np
from scipy.ndimage import label

DIRECTIONS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]


def read_input(input_data):
    return np.array(list(np.array(list(line)) for line in input_data.splitlines()))


def is_within_bounds(arr, x, y):
    return (0 <= x < arr.shape[0]) & (0 <= y < arr.shape[1])


class Garden:
    def __init__(self, garden_data: np.ndarray):
        self.grid = garden_data
        self.plants = np.unique(garden_data)
        self.rows, self.columns = self.grid.shape
        self.regions = dict()
        self.areas = dict()
        self.perimeters = dict()
        self.sides = dict()
        self.total_cost = None
        self.total_discounted_cost = None

        for plant in self.plants:
            binary_array = (garden_data == plant)
            labeled_array, num_features = label(binary_array)
            self.regions[plant] = {
                "NrComponents": num_features,
                "Components": labeled_array
            }

    def compute_areas(self):
        for plant, regions in self.regions.items():
            areas = [
                np.sum(np.sum(regions["Components"] == component+1)) for component in range(regions["NrComponents"])
            ]
            self.areas[plant] = areas

    def _compute_perimeter(self, component):
        component_index = np.argwhere(component)
        perimeter = 0
        for x, y in component_index:
            for dx, dy in DIRECTIONS:
                if not ((0 <= x+dx < self.rows) & (0 <= y+dy < self.columns)):
                    perimeter += 1
                else:
                    if not component[x+dx, y+dy]:
                        perimeter += 1
        return perimeter

    def compute_perimeters(self):
        for plant, regions in self.regions.items():
            perimeters = [
                self._compute_perimeter(regions["Components"] == component+1)
                for component in range(regions["NrComponents"])
            ]
            self.perimeters[plant] = perimeters

    @staticmethod
    def _compute_sides(component):

        padded_component = np.pad(
            component, pad_width=1, mode='constant', constant_values=False
        ).astype(int)

        sides = int((np.abs(np.diff(np.diff(padded_component, axis=0), axis=1)).sum() + np.abs(
            np.diff(np.diff(padded_component, axis=1), axis=0)).sum()) / 2)

        return sides

    def compute_sides(self):
        for plant, regions in self.regions.items():
            sides = [
                self._compute_sides(regions["Components"] == component+1)
                for component in range(regions["NrComponents"])
            ]
            self.sides[plant] = sides

    def compute_total_cost(self):
        total_cost = 0
        for plant, regions in self.regions.items():
            for component in range(regions["NrComponents"]):
                total_cost += self.areas[plant][component] * self.perimeters[plant][component]
        self.total_cost = total_cost

    def compute_total_discounted_cost(self):
        total_cost = 0
        for plant, regions in self.regions.items():
            for component in range(regions["NrComponents"]):
                total_cost += self.areas[plant][component] * self.sides[plant][component]
        self.total_discounted_cost = total_cost

    def compute_all(self):
        self.compute_areas()
        self.compute_perimeters()
        self.compute_sides()
        self.compute_total_cost()
        self.compute_total_discounted_cost()


def part_1(garden):
    return garden.total_cost


def part_2(garden):
    return garden.total_discounted_cost


if __name__ == "__main__":

    from aoc.initialize_day import load_input
    data = load_input(__file__)
    garden_ = Garden(read_input(data))
    garden_.compute_all()
    print("Part 1:", part_1(garden_))
    print("Part 2:", part_2(garden_))
