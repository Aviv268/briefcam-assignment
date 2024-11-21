# BriefCam(Rick and Morty) Assignment
This project involves both API interaction and frontend automation using Selenium.

## API Interaction: Rick and Morty Characters

The backend script interacts with the Rick and Morty API to fetch character data.

### Features

- Fetches all episodes from the Rick and Morty API.
- Selects a random episode with at least 30 characters.
- Randomly selects two characters from that episode.
- Generates character introductions and saves them to characters_introduction.txt
- Saves character data needed for UI automation to data/character_data.json.

### How to Run

1. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   
2. **Run the Script**
   ```bash
   python api_interaction.py
Or run from the pycharm GUI by right-clicking the api_interaction.py 

3. **Check the Output**

-   Character introductions will be saved in characters_introduction.txt.
- Character data will be saved in data/character_data.json.

## Frontend Automation: Google Images Search

The frontend automation uses Selenium and PyTest to interact with Google Images
### Features

- Opens Google in Chrome browser maximized and in English.
- Navigates to Google Images using the link on the homepage.
- Searches for "Rick and Moty" followed by the first character's name.
- Calculates image position based on character ID and clicks on it.
- Captures screenshots of both characters' images.
- Verifies if both characters are from the same location.
- Saves screenshots with specific filenames in the screenshots directory.
- Uses the Page Object Model (POM) design pattern.
