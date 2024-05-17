def longest_chain(words):
    """
    Determine the length of the maximum chain that can be achieved in this game at given words.
    :param words: list of words
    :return: the length of the maximum chain
    """
    chain_len = {}
    words.sort(key=len)
    max_chain = 0
    for word in words:
        chain_len[word] = 1

        for index in range(len(word)):
            next_word = word[:index] + word[index + 1:]
            if next_word in chain_len:
                chain_len[word] = max(chain_len[word], chain_len[next_word] + 1)

        max_chain = max(max_chain, chain_len[word])

    return max_chain


def write_and_read_file(input_file, output_file):
    """
    Reads words from the input file and writes the result to the output file.
    Args:
        input_file (str): Path to the file containing words.
        output_file (str): Path to the file for writing the result.
    Returns:
        None
    """
    with open(input_file, "r") as file:
        words = [line.strip() for line in file.readlines()]
    max_chain = longest_chain(words)

    with open(output_file, "w") as file:
        file.write(str(max_chain))
