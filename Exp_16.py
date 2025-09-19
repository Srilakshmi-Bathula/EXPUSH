def replace_character_in_file(source_file, dest_file, char_to_replace, replacement_char):
    with open(source_file, 'r') as src:
        contents = src.read()
        modified_contents = contents.replace(char_to_replace, replacement_char)
        modified_contents = contents.replace('H', replacement_char)
        
    with open(dest_file, 'w') as dest:
        dest.write(modified_contents)
    print(f"Contents of '{source_file}' have been written to '{dest_file}' with '{char_to_replace}' replaced by '{replacement_char}'.")

def count_character_in_file(source_file, char_to_count):
    with open(source_file, 'r') as src:
        contents = src.read()
        count = contents.count(char_to_count)
    print(f"The character '{char_to_count}' occurs {count} times in the file '{source_file}'.")
    
if __name__ == "__main__":
    source_file = 'source.txt'  # Replace with your source file
    dest_file = 'destination.txt'  # Replace with your destination file
    char_to_replace = 'h'
    replacement_char = 'x'
    
    replace_character_in_file(source_file, dest_file, char_to_replace, replacement_char)
    count_character_in_file(source_file, 'a')
