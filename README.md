# CS2520_project: Flash Card Program (Nebula)

## Overview
This repository contains the code for my flashcard program named `Nebula`. This project aims to explore the nuances 
behind the PyQt6 library. A library focused on building graphical user interfaces via Python. By 
combining fundamental princicples behind widgets, layouts and signals I was able to create a basic
flashcard program as not only a project for learning, but as a tool for personal use.

## Goals
The primary Goals of this project are as follows:
- Explore basic graphic user interface conventions in PyQt6
- To familiarize one self with file operations
- Learn to create basic flexible widgets
- To ditch and replace my physical flashcards

# How it works:
1) First you'll have the option to open existing flashcards or create new flashcards
2) If you open existing flashcards you must open a txt file containing lines in this format:
   `Question^Answer`
3) If you create a new set of flashcards, the program will look for a `decks` folder that holds your flashcards
4) If the `deck` folder is not found, then it will create it for you in your current working directory
5) Finally once a deck is opened or created, you'll be able to see the question and click on it to reveal the answer!
6) From here, you can look for specific flashcards or hit the `next`/`previous` buttons to continue

## Features used
- TODO

## Libraries used
- PyQt6 (GUI)
    - QtCore
    - QtWidgets
- tkinter (built-in)
    - filedialog
- os (built-in)
    - Used for creating a directory
      in working directory named: 'decks' 

Before running the program, ensure (`PyQt`) is installed.
