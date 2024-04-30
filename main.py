def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_letter_count(text)
    sorted_list = letters_dict_to_sorted_list(letter_count)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words was found in the document")
    print()
    for item in sorted_list:
        if not item["letter"].isalpha():
            continue
        print(f"{item['letter']} was found {item['count']} times")
    print("--- End of report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def sort_on(d):
    return d["count"]
    
def letters_dict_to_sorted_list(letters_dict):
    sorted_list = []
    for letter in letters_dict:
        sorted_list.append({"letter": letter, "count": letters_dict[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_letter_count(text):
    letter_count = {}
    for letter in text:
        lowered = letter.lower()
        if lowered not in letter_count:
            letter_count[lowered] = 1
        else:
            letter_count[lowered] += 1
    return letter_count


main()