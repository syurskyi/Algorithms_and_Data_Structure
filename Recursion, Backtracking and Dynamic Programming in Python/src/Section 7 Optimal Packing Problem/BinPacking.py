
def first_fit_decreasing_algorithm(capacities, bin_max_capacity):

    # bins are created run-time - as many bins will be created as needed
    solution_bins = []

    item_names = list(capacities.keys())
    sorted_items = sorted(item_names, key=lambda x: capacities[x], reverse=True)
    print(sorted_items)

    for item in sorted_items:
        bin_found = False
        item_capacity = capacities[item]

        # consider all the bins (this is why the final running time complexity of quadratic)
        for index, actual_bin in enumerate(solution_bins):
            # sum of items' capacity so far in the actual_bin
            actual_bin_summed_size = sum([capacities[key] for key in actual_bin])

            # if there is room for this object in the bin, put it in this bin:
            if item_capacity <= (bin_max_capacity - actual_bin_summed_size):
                solution_bins[index].append(item)
                bin_found = True
                break

        # there is no space for the item in the bins already created
        # so create a new bin for the item
        if not bin_found:
            solution_bins.append([item])

    return solution_bins


if __name__ == '__main__':

    items = {'item#1': 4, 'item#2': 2, 'item#3': 7, 'item#4': 5, 'item#5': 6, 'item#6': 3}

    print(first_fit_decreasing_algorithm(items, 8))




