"""Skills 1: lists.py

Complete the following functions. To get a better idea of how each function
should behave, see the examples in test_lists.py.
"""


def get_words_by_first_letter(words, letter):
    """Return a list of all words that start with the given letter."""

    # TODO: replace this with your code
    final_word_list = [word for word in words if letter == word[0]]
    return final_word_list


def filter_by_length(items, length):
    """Return a list of all items with the given length."""

    # TODO: replace this with your code
    final_word_list = [word for word in items if length == len(word)]
    return final_word_list


def words_in_common(words1, words2):
    """Return strings that words1 and words2 have in common."""

    # TODO: replace this with your code
    final_words = []
    for i in words1:
        for j in words2:
            if i == j:
                if i in final_words:
                    pass
                else:
                    final_words.append(i)  
    return final_words

def every_other_item(items):
    """Return a list with every other element items (start with index 0)."""

    # TODO: replace this with your code
    final_words = []
    for i in range(0, len(items), 2):
        final_words.append(items[i])
    return final_words


def smallest_n_items(items, n):
    """Return the n smallest values in the given list, in descending order.

    You can assume that `n` will be less than the length of the list.
    """

    # TODO: replace this with your code
    final_items = sorted(items)
    final_items = sorted(final_items[:n], reverse=True)

    return final_items



def get_index(items, value):
    """Search for a value in items and return its index.

    If the value doesn't exist in items, return None. If the value appears more
    than once, return the index of the first occurrence of the value.
    """

    # TODO: replace this with your code
    final_items = sorted(items)
    try:
        return final_items.index(value)
    except ValueError:
        return None


if __name__ == "__main__":
    import sys
    from pathlib import Path

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        try:
            import pytest
            pytest.main([f"test_{Path(__file__).name}"])
        except ModuleNotFoundError:
            print("Unable to run tests because 'pytest' wasn't found :(")
            print("Run the command below to install pytest:")
            print()
            print("    pip3 install pytest")
