import os

cwd_path = os.getcwd()

def read_data(file_name, custom_idx):
    """
    Function reads file and makes list of words from concrete sentence in file.
    :param file_name: (str) name of file which should be read
    :param custom_idx: (int) number of sentence in read file which should be used
    :return: (list) list of words of read sentence
    """
    list_of_lines = []
    file_path = os.path.join(cwd_path, file_name)
    if os.path.exists(file_path):
        with open(file_path) as txt_file:
            for line in txt_file.readlines():
                list_of_lines.append(line.strip())
            if custom_idx >= len(list_of_lines):
                return None
            my_line = list_of_lines[custom_idx]
            my_line = my_line.lower()
            my_line = my_line.strip(".!?")
            list_of_words = my_line.split(" ")
        return list_of_words

    else:
        return None

def tokenize(list_of_words):
    """
    Function converts first characters of words to tokens.
    :param list_of_words: (list) list of words
    :return: (list) list of numbers(tokens of characters)
    """
    list_of_numbers = []
    for word in list_of_words:
        char = word[0]
        number = ord(char)
        list_of_numbers.append(number)
    return list_of_numbers

def counting_sort(list_of_words):
    """
    Function sorts words by their tokens using counting sort.
    :param list_of_words: (list) list of words which should be sorted
    :return: (dict) dict of sorted sequence of words and frequency of items
    """
    my_dict = dict()
    list_of_numbers = tokenize(list_of_words)
    list_of_numbers.reverse()
    list_of_words.reverse()
    count_of_items = []
    sorted_words = []
    for i in range(0, 256):
        count_of_items.append(0)
    for i in range(len(list_of_numbers)):
        sorted_words.append(0)
    for token in list_of_numbers:
        count_of_items[token] += 1
    for i in range(len(count_of_items)):
        count_of_items[i] += count_of_items[i - 1]
    for i, token in enumerate(list_of_numbers):
        cf = count_of_items[token]
        cf_minus = count_of_items[token] - 1
        sorted_words[cf_minus] = list_of_words[i]
        count_of_items[token] = cf - 1

    my_dict['sorted_sequence'] = sorted_words
    my_dict['frequency'] = count_of_items

    return my_dict

def main():
    """
    Driver function.
    :return:
    """
    # read data
    data = read_data("famous_quotes.txt", custom_idx=1)
    # sort sequence
    sequence = counting_sort(data)


if __name__ == "__main__":
    main()
