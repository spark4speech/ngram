#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import string

# Regex pattern to remove most common emojis.
emoji_pattern = re.compile(
    "[" 
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "]+", flags=re.UNICODE
)

def preprocess_text(text):
    """
    Clean and tokenize text.
    - Convert text to lowercase.
    - Remove URLs, mentions, and hashtags.
    - Remove punctuation.
    - Split text into tokens (words).
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\.\S+', '', text)
    
    # Remove Twitter/X mentions and hashtags
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    
    # Remove emojis
    text = emoji_pattern.sub(r'', text)
    
    # Remove punctuation using translation table
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Tokenize: split by whitespace
    tokens = text.split()
    return tokens

def process_file(input_file, output_file):
    """
    Process each line of the input file and write the tokenized tweets to the output file.
    Each line in the output file is a space-separated list of tokens.
    """
    with open(input_file, 'r', encoding='utf-8') as f_in, \
         open(output_file, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            # Remove newline and leading/trailing whitespace
            tweet = line.strip()
            if tweet:  # Process non-empty lines
                tokens = preprocess_text(tweet)
                # Write the tokens as a space-separated string
                f_out.write(' '.join(tokens) + '\n')

if __name__ == '__main__':
    input_file = "./corpus/raw/en_US.twitter.txt"
    output_file = "./corpus/en_US.twitter.tok.txt"
    
    process_file(input_file, output_file)
    print(f"Processed tweets written to {output_file}")
