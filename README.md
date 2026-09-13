Project Title: Search books by keyword on Open Library

This program allows the user to search through Open Library's Tolkien works by keyword, including partial matches. It provides the user with author, title, and year published for each result. 

## API

This project uses the Open Library API: (https://openlibrary.org/search.json?author=tolkien) API.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/python-intro-final-project.git
   cd python-intro-final-project
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   # .venv\Scripts\activate       # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python main.py
```

Run the program to be meet with a prompt: Enter a title search term. The program will search the Open Library Tolkien database for any titles that match your search term, and report matches out in an easily readable, organized format.

## CLI Interactions

- **Filter by title keyword** — enter a keyword to see all matching records

