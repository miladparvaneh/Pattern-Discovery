## Apriori algorithm for mining contiguous sequential patterns in text

This implementation of the Apriori algorithm mines contiguous sequential patterns in text data. Only length-1 and -2 phrase candidates are explored. The input file should be in the form of a text file consisting of lines of text. Each line is a string separated by spaces, which means the text should have been stemmed (so words with similar semantics can have the same form), and the punctuations removed.

All the frequent contiguous sequential patterns along with their absolute supports are writen into a text file named "patterns.txt".  Every line corresponds to exactly one pattern and is in this format: `support:item_1;item_2;item_3,...`.
