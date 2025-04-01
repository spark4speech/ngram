#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from better_profanity import profanity

def load_ngram_model(input_path):
    """Load the n-gram model from a JSON file."""
    with open(input_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def clean_ngram_model(model):
    """
    Remove explicit words from the n-gram model.
    If the nth word in the n-gram is profane, remove it from the dictionary.
    """
    cleaned_model = {}

    for context, words in model.items():
        cleaned_words = {word: count for word, count in words.items() if not profanity.contains_profanity(word)}

        if cleaned_words:
            cleaned_model[context] = cleaned_words

    return cleaned_model

def save_cleaned_model(output_path, cleaned_model):
    """Save the cleaned n-gram model to a JSON file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(cleaned_model, f, ensure_ascii=False, indent=4)

def main():
    input_path = "./corpus/en_US.twitter.trigrams.json"
    output_path = "./corpus/en_US.twitter.clean.trigrams.json"

    print("Loading n-gram model...")
    model = load_ngram_model(input_path)

    print("Cleaning explicit words...")
    cleaned_model = clean_ngram_model(model)

    print(f"Saving cleaned model to {output_path}...")
    save_cleaned_model(output_path, cleaned_model)

    print("Cleaning complete!")

if __name__ == "__main__":
    main()
