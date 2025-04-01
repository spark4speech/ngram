#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

def load_model(model_path):
    """Load the n-gram model from a JSON file."""
    with open(model_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def predict_next_words(model, context, top_n=5):
    """
    Given a context (string of the last n-1 words), returns a sorted list of predictions.
    Each prediction is a tuple (word, frequency).
    """
    if context in model:
        predictions = model[context]
        # Sort the predictions by frequency in descending order
        sorted_predictions = sorted(predictions.items(), key=lambda x: x[1], reverse=True)
        return sorted_predictions[:top_n]
    return []

def main():
    model_path = "./corpus/en_US.clean.trigrams.min.json"
    print("Loading n-gram model...")
    model = load_model(model_path)
    print("Model loaded successfully!")
    print("Enter a sentence (at least 2 words) to predict the next word(s):")
        
    try:
        while True:
            text = input("\n").strip().lower()
            tokens = text.split()
            if len(tokens) < 2:
                print("Enter at least 2 words for prediction (trigram model requires 2-word context)")
                continue

            # Trigram model so context is the last 2 words
            context = " ".join(tokens[-2:])
            predictions = predict_next_words(model, context)

            if predictions:
                print("predictions:")
                for word, count in predictions:
                    print(f"  {word} (frequency: {count})")
            else:
                print("No predictions available for this context.")
    except KeyboardInterrupt:
        print("exiting...")

if __name__ == "__main__":
    main()
