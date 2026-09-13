import requests

API_URL = "https://openlibrary.org/search.json?author=hooks"  # Replace with your chosen API endpoint


def fetch_data():
    """Fetch data from the API. Returns the raw JSON response, or an empty list on failure."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: could not fetch data. {e}")
        return []


def process_data(data):
    """Extract and transform the fields you need. Returns a list of dictionaries."""
    records = data.get("docs", [])  # or "results", depending on your API
    result = []
    for record in records:
        result.append({
            "title": record.get("title", "Unknown"),
            "author": record.get("author_name", ["Unknown"])[0] if record.get("author_name") else "Unknown",
            "year": record.get("first_publish_year", "Unknown")
        })
    return result


def display_results(results):
    """Print results to the terminal in a readable format."""
    if not results:
        print("No results found.")
        return

    print(f"\n{len(results)} result(s) found:")
    print("-" * 40)

    for r in results:
        print(f"  Author:     {r.get('author')}")
        print(f"  Title: {r.get('title')}")
        print(f"  Year: {r.get('year')}"),
        print("-" * 40)


def main():
    
    data = fetch_data()
    if not data:
        return
    records = process_data(data)
    # display_results(records)

    if not records:
        print("No data returned.")
        return

    # print(f"Fetched {len(records)} records.")
    # print(records[0])
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

if __name__ == "__main__":
    main()