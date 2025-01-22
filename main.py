def main():
    path = "books/frankenstein.txt"
    text = book_text(path) # text in string form
    num_words = get_num_words(text) #total number of words in text
    char_count = get_num_character(text) #dictionary of character: occurences
    lowered = text.lower() # text converted to all lower case
    char_list = chars_dict_to_sorted_list(char_count) #a list ontaning multiple dictionaries + sorting
    #char_list.sort(reverse=True, key=sort_on) # sorts the list for highest occurences

    
    print(f" --- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    for dict in char_list:
        print(f"The '{dict["key"]}' character was found '{dict["value"]}' times")
    print("--- End report ---")
    
def book_text(path): #reads the path into a string
    with open(path) as f:
        return f.read()

def get_num_words(text): #Makes a list from the text and gives out the length of the list
    words = text.split()
    return len(words)

from collections import Counter #draws from collection to Count occurences and append to a dictionary
def get_num_character(text):
    return dict(Counter(text.lower()))

""""" #old code that got redundant by the next function, but would achieve the same
def char_count_list(char_count):
    filtered_list = [{"key": key, "value": value} for key, value in char_count.items() if key.isalpha()]
    return filtered_list


def sort_on(dict): # sort logic to sort vor Value
    return dict["value"]
"""""
def chars_dict_to_sorted_list(num_chars_dict):
    # Convert dictionary to list of dictionaries and sort it by the "num" value
    sorted_list = [
        {"key": ch, "value": num_chars_dict[ch]}
        for ch in num_chars_dict if ch.isalpha()  # Filtering out non-alphabetic characters
    ]
    sorted_list.sort(reverse=True, key=lambda item: item["value"])  # Sort by frequency (Value)
    return sorted_list

if __name__ == "__main__":
    main()
