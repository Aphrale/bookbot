def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_list = file_contents.split()
        num_words = len(word_list)
        print(num_words)

def count_chars():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_chars = {}
        file_contents = file_contents.lower()
        for char in file_contents:
            if char in num_chars:
                num_chars[char] = num_chars[char] + 1
            else:
                num_chars[char] = 1
        print(num_chars)

def report():
      with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")
        num_chars = {}
        file_contents = file_contents.lower()
        file_contents = "".join(file_contents.split())
        for char in file_contents:
            if char.isalpha() and char in num_chars:
                    num_chars[char] = num_chars[char] + 1
            elif char.isalpha():
                num_chars[char] = 1
        char_list = []
        for char in num_chars:
            char_list.append({"char": char, "num": num_chars[char]})

        def sort_on(dict):
            return dict["num"]

        char_list.sort(reverse=True, key=sort_on)
        for char_dict in char_list:
            print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
        print("--- End report ---")


main()
count_words()
count_chars()
report()