## Apriori algorithm for frequent itemset mining

This implementation of the Apriori algorithm is capable of extracting frequently occurring category sets from provided data. The input file should be in the form of a text file consisting of category lists. Each line should correspond to one category list, where the list consists of a number of category instances separated by semicolons.

In **single_item_mining.py**, all frequent categories of length-1, along with their absolute support counts, are mined and written to a text file titled "patterns_single.txt". Each line in this file represents a single frequent category and follows the format: `support:category`.

In **itemset_mining.py**, the program generates a text file named "patterns_all.txt", where it records each set of frequent categories together with their respective absolute support counts. Each line in the file represents a unique set of frequent categories, formatted as follows: `support:category_1;category_2;category_3;...`.
