def main():
    def format_word(word):
        word = word.lower()
        new_word = word.capitalize()
        return new_word

    def convert_to_pascal_case(text):
        text = text + " "
        current_word = ""
        final_text = ""
        length = 0
        for l in text:
            if l != " ":
                current_word += l
            else:
                final_text += format_word(current_word)
                current_word = ""
            length += 1
            if length == len(text):
                break
        return final_text



    word = input("Enter a string: ")
    print(f"Pascal Case: {convert_to_pascal_case(word)}")
if __name__ == '__main__':
    main()