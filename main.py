lowercase_alphabet = {"a" : "1", "b" : "2", "c" : "3", "d" : "4", "e" : "5",
                "f" : "6", "g" : "7", "h" : "8", "i" : "9", "j" : "10", 
                "k" : "11", "l" : "12", "m" : "13", "n" : "14", "o" : "15", 
                "p" : "16", "q" : "17", "r" : "18", "s" : "19", "t" : "20", 
                "u" : "21", "v" : "22", "w" : "23", "x" : "24", "y" : "25", 
                "z" : "26", }

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_words_count(text)
    char_count = get_char_count(text)
    report = get_report(word_count, char_count, book_path)
    print(report)

def get_report(word_count, char_count, book_path):
    report = f"--- Begin report of {book_path} ---\n{word_count} words found in the document\n\n"
    for char, count in char_count.items():
        report += f"The character {char} was found {count} number of times \n"
    report += "--- End of report ---"
    return report

def get_char_count(text):
    lowercase_text = text.lower()
    chars_with_count = {}
    for letter in lowercase_alphabet:
        chars_with_count[letter] = get_count_for_specific_char(lowercase_text, letter)
    return chars_with_count

def get_count_for_specific_char(text, letter):
    return text.count(letter)

def get_words_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()