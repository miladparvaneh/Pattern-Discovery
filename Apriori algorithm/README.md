## Apriori algorithm

The Apriori algorithm is capable of extracting frequently occurring category sets from provided data. Here, the input file is in the form of a text file consisting of category lists. Each line corresponds to one category list, where the list consists of a number of category instances separated by semicolons.

In **single_item_mining.py**, all frequent categories of length-1, along with their absolute support counts, are mined and written to a text file titled "patterns.txt". Each line in this file represents a single frequent category and follows the format: `support:category`.

In **itemset_mining.py**, the program generates a text file named "patterns.txt", where it records each set of frequent categories together with their respective absolute support counts. Each line in the file represents a unique set of frequent categories, formatted as follows: `support:category_1;category_2;category_3;...`.
