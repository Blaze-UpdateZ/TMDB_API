from api.movie_posters import app
from api.config import PORT

def main():
    # Initialize the test client
    client = app.test_client()
    
    # Define the query
    query = "your name 2016"
    print(f"--- Searching for: {query} ---")

    # Make the request
    response = client.get(f'/api/movie-posters?query={query}')
    
    # Print the results
    if response.status_code == 200:
        data = response.get_json()
        print(json.dumps(data, indent=2))
    else:
        print(f"Error: {response.status_code}")
        print(response.get_data(as_text=True))

if __name__ == "__main__":
    main()
