# Setting thresholds
rel_min_sup = 0.01
abs_min_sup = 771

# Initializing single item dictionary
single_item_dict = {}

# Reading the input file and mining frequent single items
with open('input_file.txt', 'r') as input:
    for line in input:
        items = line.strip().split(';')
        for item in items:
            if item in single_item_dict:
                single_item_dict[item] += 1
            else:
                single_item_dict[item] = 1

# Filtering by minimum support threshold
frequent_single_item_dict = {key: value for key, value in single_item_dict.items() if value > abs_min_sup}

# Writing the frequent single items
with open('patterns_single.txt', 'w') as output_single:
    for key, value in frequent_single_item_dict.items():
        output_single.write(f'{value}:{key}\n')
