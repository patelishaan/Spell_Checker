Simple Python Spell Checker
This repository contains a simple spell checker application built using Python. It leverages a large text corpus to calculate word frequencies and suggests corrections based on common typographical errors (deletions, insertions, swaps, and replacements). The application includes a backend logic for spell checking and a Flask-based web interface for user interaction.

Features
Frequency-based Spell Checking: Utilizes a pre-calculated frequency distribution of words from a large text corpus (big.txt) to determine the most probable correct spellings.

Edit Distance 1 Corrections: Generates possible corrections by applying single-character edits (deletions, insertions, swaps, replacements) to the input word.

Flask Web Interface: Provides a user-friendly web interface to input words and view spell check suggestions.

Modular Design: Separates concerns into data processing (main.py), spell checking logic (spell_check_backend_logic.py), and web application (app.py).

How it Works
The spell checker operates in three main stages:

Corpus Processing (main.py):

Reads a large text file (big.txt).

Extracts all words and creates a vocabulary.

Calculates the frequency of each word in the corpus.

Saves the word frequency distribution as a Python pickle file (sherlock.pkl). This file is crucial for the spell-checking logic.

Backend Spell Checking Logic (spell_check_backend_logic.py):

Loads the word frequency distribution from sherlock.pkl.

Implements functions to generate possible corrected words based on:

Splits: Dividing a word into two parts.

Deletions: Removing one character.

Swaps: Swapping two adjacent characters.

Replacements: Replacing one character with another.

Insertions: Inserting an additional character.

The edit() function combines these operations to generate all possible words with one edit distance from the input word.

The spell_check_edit_1() function filters these generated words against the loaded vocabulary and returns the top suggestions sorted by their probability in the corpus.

There's also a spell_check_edit_2() function for two-level edits, though the current app.py primarily uses spell_check_edit_1().

Flask Web Application (app.py):

Sets up a Flask web server.

Defines a single route (/) for the home page.

Handles GET requests to display the input form.

Handles POST requests when a user submits a word:

It takes the input word.

Calls the spell_check_edit_1() function from spell_check_backend_logic.py to get corrections.

Renders an HTML template (index.html) to display the original word and the suggested corrections
