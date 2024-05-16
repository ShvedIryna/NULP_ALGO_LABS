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


with open("wchain.in", "r") as file:
    N = int(file.readline().strip())
    words = [file.readline().strip() for _ in range(N)]

max_chain_length = longest_chain(words)

with open("wchain.out", "w") as file:
    file.write(str(max_chain_length))