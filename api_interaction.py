import json
import os

import requests
import random


base_url = 'https://rickandmortyapi.com/api'


class Character:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.status = data['status']
        self.species = data['species']
        self.type = data['type']
        self.gender = data['gender']
        self.origin = data['origin']['name']
        self.location = data['location']['name']
        self.image = data['image']

    def introduce(self):
        return (f"Hi! I'm {self.name}, My ID is {self.id}, I'm from {self.location}, "
                f"I'm a {self.species} and I'm {self.status}.")


def fetch_all_episodes():
    episodes = []
    next_url = f"{base_url}/episode"

    while next_url:
        response = requests.get(next_url)
        data = response.json()
        episodes.extend(data['results'])
        next_url = data['info']['next']

    return episodes


def select_random_episode_with_min_characters(episodes, min_characters=30):
    characters_episodes = [episode for episode in episodes if len(episode['characters']) >= min_characters]
    if not characters_episodes:
        raise ValueError(f"There is no episode with at least {min_characters} characters.")
    selected_episode = random.choice(characters_episodes)
    return selected_episode


def print_episode_name_and_characters(episode):
    episode_name = episode['name']
    num_characters = len(episode['characters'])
    print(f"At episode: {episode_name} there are {num_characters} characters")


def select_characters(episode, num_characters=2):
    characters_urls = episode['characters']
    selected_urls = random.sample(characters_urls, num_characters)
    return selected_urls


def fetch_multiple_characters(character_urls):
    character_ids = [url.split('/')[-1] for url in character_urls]
    response = requests.get(f"{base_url}/character/{','.join(character_ids)}")
    data = response.json()
    if isinstance(data, dict):
        characters_data = [data]
    else:
        characters_data = data

    characters = [Character(char_data) for char_data in characters_data]
    return characters


def introductions_writer(characters, filename='characters_introduction.txt'):
    with open(filename, 'w') as file:
        for character in characters:
            introduction = character.introduce()
            file.write(introduction + '\n')
            print(introduction)


# **************************
def save_characters_data(characters, filename='data/character_data.json'):
    character_list = []
    for character in characters:
        character_info = {
            'id': character.id,
            'name': character.name,
            'status': character.status,
            'species': character.species,
            'location': character.location,
            'image': character.image
        }
        character_list.append(character_info)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as file:
        json.dump(character_list, file)
# **************************


if __name__ == '__main__':
    all_episodes = fetch_all_episodes()
    selected_episode = select_random_episode_with_min_characters(all_episodes)

    print_episode_name_and_characters(selected_episode)
    selected_urls = select_characters(selected_episode)

    characters = fetch_multiple_characters(selected_urls)
    introductions_writer(characters)

    save_characters_data(characters)
