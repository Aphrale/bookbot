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
        for key in num_chars:
            print(f"The", key, "character was found", num_chars[key], "times")
            
main()
count_words()
count_chars()