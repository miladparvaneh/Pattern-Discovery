# Setting relative and absolute support thresholds
rel_min_sup = 0.01
abs_min_sup = 100

# Reading the input file and forming a dictionary of single words
single_words = {}

with open('input_file.txt', 'r') as input:
    for line in input:
        words_list = line.strip().split()
        
        # Initialize count_flag for the current line
        count_flag = {}
        for word in words_list:
            if word not in count_flag:
                count_flag[word] = True  # Mark the word as counted for this line
                
                # Update the count for the word
                if word in single_words:
                    single_words[word] += 1
                else:
                    single_words[word] = 1
                
# Mining the frequent single words
freq_single_words = {key: value for key, value in single_words.items() if value >= abs_min_sup}
print('Number of frequent single words:', len(freq_single_words))

# Writing into the output file
with open('patterns.txt', 'w') as output_length1:
    for key, value in freq_single_words.items():
        output_length1.write(f'{value}:{key}\n')

# Reading the input file and forming a dictionary of length_2 sequences
length2_seq_candids = []
length2_seq = {}

# Forming a list of length-2 sequence candidates
with open('input_file.txt', 'r') as input:
    for line in input:
        words_list = line.strip().split()
        for idx, word in enumerate(words_list):
            if word in freq_single_words and word != words_list[-1]:
                length2_seq_candids.append([words_list[idx], words_list[idx+1]])
                
print('Number of length_2 sequence candidates', len(length2_seq_candids))

# Function to check if the pair appears consecutively
def is_consecutive_pair(pair, lst):
    for i in range(len(lst) - 1):  # Loop through the list until the second last item
        if lst[i] == pair[0] and lst[i + 1] == pair[1]:
            return True
    return False
        
# Forming a dictionary of length_2 sequences with their counts
with open('input_file.txt', 'r') as input:
    for idx, line in enumerate(input):
        if idx % 1000 == 0:
                print('Line #:', idx)
        words_list = line.strip().split()
        
        # Initialize count_flag for the current line
        count_flag = {}
        for candid in length2_seq_candids:
            if tuple(candid) not in count_flag:
                if is_consecutive_pair(candid, words_list):
                    count_flag[tuple(candid)] = True  # Mark the sequence as counted for this line

                    # Update the count for the sequence
                    if tuple(candid) in length2_seq:
                        length2_seq[tuple(candid)] += 1
                    else:
                        length2_seq[tuple(candid)] = 1

# Mining the frequent length_2 sequences
freq_length2_seq = {key: value for key, value in length2_seq.items() if value >= abs_min_sup}
print('Number of frequent length_2 sequences:', len(freq_length2_seq))

# Appending to the output file
with open('patterns.txt', 'a') as output_length2:
    for key, value in freq_length2_seq.items():
        key_string = ';'.join(key)
        output_length2.write(f'{value}:{key_string}\n')
