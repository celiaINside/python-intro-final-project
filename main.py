import requests
import matplotlib.pyplot as plt
import os

API_URL = "https://openlibrary.org/search.json"


def fetch_data(author):
    """Fetch data from the API. Returns the raw JSON response, or an empty list on failure."""
    try:
        response = requests.get(API_URL, params={"author": author})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: could not fetch data. {e}")
        return []


def process_data(data):
    """Extract and transform the fields you need. Returns a list of dictionaries."""
    if not isinstance(data, dict):
        return []
    books = data.get("docs", [])
    records = []
    for book in books:
        authors = book.get("author_name", [])
        records.append({
            "title": book.get("title", "Unknown"),
            "author": authors[0] if authors else "Unknown",
            "year": book.get("first_publish_year")
        })
    return records


def display_results(results):
    """Print results to the terminal in a readable format."""
    if not results:
        print("No results found.")
        return

    print(f"\n{len(results)} result(s) found:")
    print("-" * 40)

    for r in results:
        print(f"  Author:     {r.get('author')}")
        print(f"  Title:      {r.get('title')}")
        print(f"  Year:       {r.get('year') if r.get('year') is not None else 'Unknown'}")
        print("-" * 40)

def create_visualization(records):
    """Create a bar chart showing titles published by decade."""
    decade_counts = {}

    for record in records:
        year = record["year"]
        if year is None:
            continue

        decade = (year // 10) * 10

        if decade not in decade_counts:
            decade_counts[decade] = 0

        decade_counts[decade] += 1

    labels = sorted(decade_counts.keys())
    values = [decade_counts[decade] for decade in labels]

    plt.bar(labels, values)
    plt.xlabel("Decade")
    plt.ylabel("Titles Published")
    plt.title("Titles Published per Decade")
    plt.tight_layout()
    plt.savefig("sample_chart.png")
    plt.show()

def main():
    home = os.getenv("HOME")
    print(f"Home directory: {home}")
    author = input("Enter an author: ").strip()

    if not author:
        print("Please enter an author.")
        return

    data = fetch_data(author)

    if not data:
        return

    records = process_data(data)

    if not records:
        print(f"No books found for '{author}'.")
        return

    while True:
        query = input("Enter a title search term: ").strip().lower()
        if not query:
            print("Please enter a value.")
            continue

        results = [r for r in records if query in r["title"].lower()]

        if not results:
            print(f"No results found for '{query}'.")
            continue

        break
    
    display_results(results)
    create_visualization(records)

if __name__ == "__main__":
    main()
