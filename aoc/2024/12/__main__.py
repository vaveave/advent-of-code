import numpy as np
from scipy.ndimage import label


def read_input(input_data):
    return np.array([list(line) for line in input_data.splitlines()])


class Garden:
    def __init__(self, garden_data: np.ndarray):
        self.grid = garden_data
        self.plants = np.unique(garden_data)
        self.regions = {}
        self.total_cost = 0
        self.total_discounted_cost = 0

        for plant in self.plants:
            binary_array = garden_data == plant
            labeled_array, num_features = label(binary_array)
            self.regions[plant] = {
                "NrComponents": num_features,
                "Components": labeled_array,
            }

        self.compute_all()

    def compute_all(self):
        for plant, regions in self.regions.items():
            for component in range(1, regions["NrComponents"] + 1):
                component_mask = regions["Components"] == component

                area = np.sum(component_mask)

                padded_component = np.pad(
                    component_mask, pad_width=1, mode="constant", constant_values=False
                ).astype(int)
                perimeter = (
                    np.abs(np.diff(padded_component, axis=0)).sum()
                    + np.abs(np.diff(padded_component, axis=1)).sum()
                )

                side_count = (
                    np.abs(np.diff(np.diff(padded_component, axis=0), axis=1)).sum()
                    + np.abs(np.diff(np.diff(padded_component, axis=1), axis=0)).sum()
                ) // 2

                self.total_cost += area * perimeter
                self.total_discounted_cost += area * side_count


def part_1(garden):
    return garden.total_cost


def part_2(garden):
    return garden.total_discounted_cost


if __name__ == "__main__":
    from aoc.initialize_day import load_input

    data = load_input(__file__)
    garden_ = Garden(read_input(data))
    print("Part 1:", part_1(garden_))
    print("Part 2:", part_2(garden_))
