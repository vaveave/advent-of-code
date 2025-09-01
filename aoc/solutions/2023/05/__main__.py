def parse_input(input_data):
    input_pre = input_data.split("\n\n")
    seeds = list(map(int, input_pre[0].replace("seeds: ", "").split()))
    map_dict = dict()

    for i, str_map in enumerate(input_pre[1:]):
        level_map = [list(map(int, m.split())) for m in str_map.split("\n")[1:]]
        level_map = sorted(level_map, key=lambda x: x[1])

        for j, [_, src_st, range_len] in enumerate(level_map[:-1]):
            if (src_st + range_len) < level_map[j + 1][1]:
                insertion_point = j + 1
                level_map.insert(
                    insertion_point,
                    [
                        (src_st + range_len),
                        (src_st + range_len),
                        level_map[j + 1][1] - (src_st + range_len),
                    ],
                )
        map_dict[i] = level_map

    return seeds, map_dict


def follow_seed_path(seed, map_dict):
    pos = seed

    for map_ in map_dict.values():
        if not (pos < map_[0][1] or pos > map_[-1][1] + map_[-1][2] - 1):
            for coord in map_:
                if coord[1] <= pos < coord[1] + coord[2]:
                    pos += coord[0] - coord[1]
                    break

    return pos


def read_input(data):
    return data


def part_1(input_data):
    seeds, map_dict = parse_input(input_data)
    return min(follow_seed_path(seed, map_dict) for seed in seeds)


def follow_seed_range_path(min_seed, max_seed, map_dict):
    ranges = [[min_seed, max_seed]]

    for map_ in map_dict.values():
        next_level_ranges = []

        for a, b in ranges:
            if b < map_[0][1] or a > map_[-1][1] + map_[-1][2] - 1:
                next_level_ranges.append([a, b])
            else:
                if a < map_[0][1]:
                    next_level_ranges.append([a, map_[0][1] - 1])
                if b > map_[-1][1] + map_[-1][2] - 1:
                    next_level_ranges.append([map_[-1][1] + map_[-1][2], b])

                for dest_st, src_st, range_len in map_:
                    if a <= src_st and b >= src_st + range_len - 1:
                        next_level_ranges.append([dest_st, dest_st + range_len - 1])

                for dest_st, src_st, range_len in map_:
                    if src_st <= a < src_st + range_len:
                        next_level_ranges.append(
                            [
                                a + dest_st - src_st,
                                min(b + dest_st - src_st, dest_st + range_len - 1),
                            ]
                        )
                        break

                for dest_st, src_st, range_len in map_:
                    if src_st <= b < src_st + range_len:
                        next_level_ranges.append(
                            [max(a + dest_st - src_st, dest_st), b + dest_st - src_st]
                        )
                        break

        ranges = next_level_ranges.copy()

    return ranges


def part_2(input_data):
    seeds, map_dict = parse_input(input_data)
    locations = []

    for i in range(0, len(seeds), 2):
        locations += follow_seed_range_path(
            seeds[i], seeds[i] + seeds[i + 1] - 1, map_dict
        )

    return min(location[0] for location in locations)


def main():
    from aoc.cli.utils import load_input
    data = load_input(__file__)
    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))


if __name__ == "__main__":
    main()
