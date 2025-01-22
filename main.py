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
        for char in file_contents:
            num_chars[char]=num_chars.setdefault(char, 0)+1
            print(num_chars)


main()
count_words()
count_chars()