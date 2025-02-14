#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

def extract_ngrams(tokens, n):
    """
    Extract n-grams from a list of tokens.
    Returns a list of tuples, each tuple is an n-gram.
    """
    ngrams = []
    for i in range(len(tokens) - n + 1):
        ngram = tuple(tokens[i:i+n])
        ngrams.append(ngram)
    return ngrams

def build_ngram_table(tokenized_file, n=3):
    """
    Reads a tokenized file (one sentence per line, tokens separated by spaces)
    and builds an n-gram table. For a trigram model, the key is the first n-1 tokens,
    and the value is a dictionary mapping the nth token to its frequency.
    """
    ngram_table = {}
    
    with open(tokenized_file, 'r', encoding='utf-8') as f:
        for line in f:
            tokens = line.strip().split()
            if len(tokens) < n:
                continue  # Skip lines that are too short
            ngrams = extract_ngrams(tokens, n)
            for ngram in ngrams:
                key = " ".join(ngram[:-1])  # First n-1 words
                next_word = ngram[-1]       # nth word
                if key not in ngram_table:
                    ngram_table[key] = {}
                if next_word not in ngram_table[key]:
                    ngram_table[key][next_word] = 0
                ngram_table[key][next_word] += 1
    return ngram_table

if __name__ == '__main__':
    tokenized_file = "./corpus/en_US.twitter.tok.txt"
    output_file = "./corpus/en_US.twitter.trigrams.json"
    
    ngram_table = build_ngram_table(tokenized_file, n=3)
    
    with open(output_file, 'w', encoding='utf-8') as f_out:
        json.dump(ngram_table, f_out, indent=2, ensure_ascii=False)
    
    print(f"N-gram table written to {output_file}")
