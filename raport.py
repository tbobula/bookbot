def raport(book_name, num_words, sorted_characters ):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_name}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key,value in sorted_characters.items():
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")