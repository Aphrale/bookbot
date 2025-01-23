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
        file_contents = "".join(file_contents.split())
        for char in file_contents:
            if  if char == " " or char == "'" or char == "," or char == "(" or char == ")" or char == " " or char == "." or char == "-" or char == ":" or char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9" or char == "0" or char == "[" or char == "]" or char == "#" or char == "*" or char == "?" or char == ";" or char == "!" or char == '"' or char == "_" or char == "/" or char == "%" or char == "@" or char == "$": 
                del char
            elif char in num_chars:
                num_chars[char] = num_chars[char] + 1
            else:
                num_chars[char] = 1
        for key in num_chars:
            print(f"The '" + key + "' character was found", num_chars[key], "times")
            
main()
count_words()
count_chars()