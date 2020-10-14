#!/usr/local/bin/python3

from string import punctuation

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]

# ALL RAISES SHOULD BE Deleted, can be treated like pass

def ispunct(s):
    if s == "":
        return False
    for c in s:
        if c not in punctuation:
            return False

    return True        

class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        with open(self.filename) as wordsfile:
            return wordsfile.read()

class WordList:
    def __init__(self, text):
        self.text = text


    def extract_words(self):
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        filtered_text = self.text.lower()        

        for p in punctuation:
            filtered_text = filtered_text.replace(p, '')

        self.extracted_words = filtered_text.split()    

        # for (i, word in enumerate(self.extract_words)):
        #     filtered_letters = []

        #     for letter in word:
        #         if letter not in punctuation:
        #             filtered_letters.append(letter)

        #     filtered_word = "".join(filtered_letters)
        #     self.extracted_words[i] = "".join(filtered_letters)



    def remove_stop_words(self):
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
        extracted_words = self.extracted_words

        for s_w in STOP_WORDS:
            while s_w in extracted_words:
                self.stops_removed = extracted_words.remove(s_w)
                

    def get_freqs(self):
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """

        word_counts =  {}
        for w in self.extracted_words:
            if w in word_counts:
                word_counts[w] += 1
            else:
                word_counts[w] = 1  
        return word_counts          


class FreqPrinter:
    def __init__(self, freqs):
        self.freqs = freqs


    def print_freqs(self):
        """
        Prints out a frequency chart of the top 10 items
        in our frequencies data structure.

        Example:
          her | 33   *********************************
        which | 12   ************
          all | 12   ************
         they | 7    *******
        their | 7    *******
          she | 7    *******
         them | 6    ******
         such | 6    ******
       rights | 6    ******
        right | 6    ******
        """

        

        print(self.freqs)


if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
