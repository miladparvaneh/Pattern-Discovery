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

# Rewriting the frequent single items into the new output file
with open('patterns_all.txt', 'w') as output_all:
    for key, value in frequent_single_item_dict.items():
        output_all.write(f'{value}:{key}\n')
        
F = frequent_single_item_dict
k = 2

# Mining frequent 2-itemset and longer
while F:
    # Candidate generation
    if k == 2: # 2-itemset
        items_list = []
        for key, value in F.items():
            items_list.append(key)
        
        temp = []
        candids_list = []
        for i in range(len(items_list)):
            for j in range(len(items_list)):
                if i != j:
                    temp = [items_list[i], items_list[j]]
                    candids_list.append(temp[0] + ';' + temp[1])
        
    else: # 3-itemset or longer
        common = k - 2
        items_list = []
        for key, value in F.items():
            items_list.append(key.strip().split(';'))
        
        temp = []
        candids_list = []
        for i in range(len(items_list)):
            for j in range(len(items_list)):
                if i != j:
                    if all(items_list[i][n] == items_list[j][n] for n in range(common)):
                        temp = []
                        for n in range(common):
                            temp.append(items_list[i][n])
                        temp.append(items_list[i][k - 2])
                        temp.append(items_list[j][k - 2])
                        combined = ';'.join(temp)
                        candids_list.append(combined)
                    
        # Pruning
        delete_index = []
        for i in range(len(candids_list)):
            pruned = []
            candid_items = candids_list[i].strip().split(';')
            for j in range(len(candid_items)):
                sub = candid_items[:j] + candid_items[j+1:]
                pruned.append(sub)
            
            # Checking whether all sub-items are frequent
            frequent = [0] * len(pruned)
            for m in range(len(pruned)):
                for key, value in F.items():
                    key_items = key.strip().split(';')
                    if all(item in key_items for item in pruned[m]):
                        frequent[m] = 1
                        break
                
            if not all(item == 1 for item in frequent):
                delete_index.append(i)
                
        candids_list_pruned = [item for idx, item in enumerate(candids_list) if idx not in delete_index]
    
    # Forming the (k+1)-itemset dictionary
    F_update = {}
    with open('input_file.txt', 'r') as input:
        for line in input:
            input_items = line.strip().split(';')
            for candid in candids_list:
                candid_items = candid.strip().split(';')
                if all(item in input_items for item in candid_items):
                    if candid in F_update:
                        F_update[candid] += 1
                    else:
                        F_update[candid] = 1

    # Filtering by minimum support threshold
    frequent_F_update = {key: value for key, value in F_update.items() if value > abs_min_sup}
    
    # Normalizing the keys to eliminate repeated candidates
    normalized_F = {}
    for key, value in frequent_F_update.items():
        normalized_key = ';'.join(sorted(key.split(';')))
        if normalized_key not in normalized_F:
            normalized_F[normalized_key] = value
        else:
            pass
    
    # Updating the itemsets dictionary for next iteration
    F = frequent_F_update
    k += 1
    
    # Appending the new itemsets to the output file (using normalized_F)
    with open('patterns_all.txt', 'a') as output_all:
        for key, value in normalized_F.items():
            output_all.write(f'{value}:{key}\n')
