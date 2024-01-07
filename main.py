import difflib

def load_text_files(file_path1, file_path2):
    try:
        with open(file_path1, 'r', encoding='utf-8') as file1, open(file_path2, 'r', encoding='utf-8') as file2:
            text1 = file1.read()
            text2 = file2.read()
        return text1, text2
    except FileNotFoundError:
        print("File not found.")
        return None, None

def check_plagiarism(text1, text2):
    if text1 is None or text2 is None:
        return None

    # Calculate the similarity ratio between the two texts
    similarity_ratio = difflib.SequenceMatcher(None, text1, text2).ratio()
    return similarity_ratio

def main():
    print("Welcome to the Plagiarism Checker Program!")

    file_path1 = input("Enter the path of the first text file: ")
    file_path2 = input("Enter the path of the second text file: ")

    text1, text2 = load_text_files(file_path1, file_path2)

    if text1 is not None and text2 is not None:
        similarity_ratio = check_plagiarism(text1, text2)
        if similarity_ratio is not None:
            print(f"Similarity ratio between the two texts: {similarity_ratio:.2%}")
            if similarity_ratio > 0.8:
                print("High similarity detected. Possible plagiarism.")
            else:
                print("Low similarity. Likely not plagiarism.")
    else:
        print("Exiting the Plagiarism Checker Program.")

if __name__ == "__main__":
    main()
