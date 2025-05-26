import requests
from bs4 import BeautifulSoup

def fetch_page_content(url):
    """
    Fetches the content of a given URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The text content of the page, or None if an error occurs.
    """
    headers = {'User-Agent': 'MyGameOfThronesScraper/1.0'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

def parse_episodes(html_content):
    """
    Parses the HTML content to extract Game of Thrones episode details and
    returns them as a list of dictionaries.

    Args:
        html_content (str): The HTML content of the page.

    Returns:
        list: A list of dictionaries, where each dictionary represents an episode.
              Returns an empty list if no content is parsed or no episodes are found.
    """
    all_episodes_data = []
    if not html_content:
        # This message is useful if fetch_page_content succeeded but html_content was empty for some reason.
        # If fetch_page_content failed, it prints its own error.
        print("No HTML content provided to parse_episodes.")
        return all_episodes_data

    soup = BeautifulSoup(html_content, 'html.parser')

    temporadas_headings = soup.find_all('div', class_='mw-heading mw-heading3')

    if not temporadas_headings:
        print("Warning: No season headings found on the page.")
        return all_episodes_data

    for temporada_heading_div in temporadas_headings:
        num_temporada_tag = temporada_heading_div.find('h3')
        if not num_temporada_tag:
            print("Warning: Found a season heading div without an h3 title. Skipping this season.")
            continue
        current_season_title = num_temporada_tag.get_text().strip()
        
        siguiente_div = temporada_heading_div.find_next_sibling('div')
        if not siguiente_div:
            print(f"Warning: Could not find content div for {current_season_title}. Skipping this season.")
            continue
        
        tabla = siguiente_div.find('table', class_='wikitable')
        if not tabla:
            print(f"Warning: Could not find episode table for {current_season_title}. Skipping this season.")
            continue
            
        episodios_rows = tabla.find_all('tr', class_='vevent')
        if not episodios_rows:
            print(f"Warning: No episode rows found in the table for {current_season_title}.")
            continue

        for episodio_row in episodios_rows:
            celdas = episodio_row.find_all('td')
            if len(celdas) < 5:
                print(f"Warning: Episode row in {current_season_title} has only {len(celdas)} cells. Expected 5. Skipping this episode.")
                continue
            
            num_episodio = celdas[0].get_text(strip=True)
            titulo = celdas[1].get_text(strip=True).strip('«»')
            dir_por = celdas[2].get_text(strip=True)
            escrito_por = celdas[3].get_text(strip=True)
            emision = celdas[4].get_text(strip=True)
            
            episode_data = {
                "season_title": current_season_title,
                "episode_number_in_season": num_episodio,
                "title": titulo,
                "directed_by": dir_por,
                "written_by": escrito_por,
                "original_air_date": emision
            }
            all_episodes_data.append(episode_data)
            
    return all_episodes_data

if __name__ == '__main__':
    WIKIPEDIA_URL = 'https://es.wikipedia.org/wiki/Anexo:Episodios_de_Game_of_Thrones'
    
    print(f"Fetching content from: {WIKIPEDIA_URL}")
    html_content = fetch_page_content(WIKIPEDIA_URL)
    
    # parse_episodes is designed to return an empty list if html_content is None or if parsing fails.
    episodes_data = parse_episodes(html_content)
    
    if episodes_data: # Check if the list is not empty
        print(f"\nFound {len(episodes_data)} episodes. Details:\n")
        for episode in episodes_data:
            print(f"Season: {episode['season_title']}")
            print(f"  Episode Number: {episode['episode_number_in_season']}")
            print(f"  Title: {episode['title']}")
            print(f"  Directed by: {episode['directed_by']}")
            print(f"  Written by: {episode['written_by']}")
            print(f"  Air Date: {episode['original_air_date']}")
            print("---")
    else:
        # This message covers cases where html_content was None (fetch failed)
        # or where parsing found no episodes.
        print("\nNo episodes were found. This could be due to a failure in fetching page content or no episodes being parsed from the page.")
