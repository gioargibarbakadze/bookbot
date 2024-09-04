def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #num_words = word_count(text)
    letters_dict = count_letters(text)
    print(letters_dict)
    #print(f"{num_words} words")
    #print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def count_letters(text):
    lowered_string = text.lower()
    dic = {}
    for char in lowered_string:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    return dic





main()
