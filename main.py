def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    letters_dict = count_letters(text)
    print(letters_dict)
    #print(f"{num_words} words")
    #print(text)
    print("bookr report")
    print("============")
    print(f"{num_words} total words")
    for letter in dict_to_list(letters_dict):
        print(f"letter {letter['letter']} is in the text {letter['count']} times")
    print("=============")
    print("end")


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

def dict_to_list(dict):
    dict_to_list = []
    for x in dict:
        new = {}
        if x.isalpha():
            new["letter"] = x
            new["count"] = dict[x]
            dict_to_list.append(new)
    dict_to_list.sort(reverse=True, key=sort)
    return dict_to_list

def sort(dict):
    return dict["count"]







main()
