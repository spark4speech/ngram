#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

MIN_FREQUENCY = 10

def load_model(input_path):
    with open(input_path, "r", encoding="utf-8") as f:
        return json.load(f)

def filter_model(model, min_freq):
    return {
        context: {
            word: freq
            for word, freq in predictions.items()
            if freq >= min_freq
        }
        for context, predictions in model.items()
        if any(freq >= min_freq for freq in predictions.values())
    }

def save_model(output_path, model):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(model, f, ensure_ascii=False, indent=2)

def main():
    input_file = "./corpus/en_US.twitter.clean.trigrams.json"
    output_file = "./corpus/en_US.clean.trigrams.min.json"

    print("Loading model...")
    model = load_model(input_file)

    print("Filtering model...")
    minimized_model = filter_model(model, MIN_FREQUENCY)

    print("Saving minimized model...")
    save_model(output_file, minimized_model)

    print(f"Model reduced from {len(model)} to {len(minimized_model)} contexts.")

if __name__ == "__main__":
    main()
