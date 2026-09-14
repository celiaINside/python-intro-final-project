Project Title: Open Library Book Search (Author & Title)

This program allows the user to first search for an author through Open Library's vast database by entering a name. Then, the user is prompted to search for Titles by that author via a title search term. The program then provides the user with author, title, and year published for each result. 

## API

This project uses the Open Library API: https://openlibrary.org/search.json

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

Run the program to be met with a prompt: Enter an author name. The program fetches all works by that author. Then, one more prompt: Enter a title search term. The program will search the Open Library database for any titles by your given author name that match your title search term, and report matches out in an easily readable, organized format.

## CLI Interactions

- **Filter by author search term** — enter a keyword to see all matching records
- **Filter by title search term** — enter a keyword to see all matching records
