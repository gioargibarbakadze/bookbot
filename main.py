def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    print(f"{num_words} words")
    #print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)



main()
