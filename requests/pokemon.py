import numpy as np
import requests
from PIL import Image
from matplotlib import pyplot as plt


def get_pokemon_image(pokemon_name: str):
    resp = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")

    pokemon = resp.json()

    sprite_url = pokemon['sprites'].get("other", pokemon['sprites']).get("official-artwork", pokemon['sprites'])[
        'front_default']
    stream = requests.get(sprite_url, stream=True).raw
    img = Image.open(requests.get(sprite_url, stream=True).raw)
    img.save("mp_summmingssssss.png")
    #
    # img = Image.open("mp_summmingssssss.png")
    # img = img.convert("RGB")
    plt.imshow(np.asarray(img))
    plt.show()


def get_random_chuck_joke():
    resp = requests.get("https://api.chucknorris.io/jokes/random")

    print(resp.json()["value"])


# get_random_chuck_joke()
get_pokemon_image("charizard")
# resp = requests.get("https://http.cat/300.jpg", stream=True).raw
# img = Image.open(resp)
# img.save("cat.jpg")
# plt.imshow(np.asarray(img))
# plt.show()
# print(resp)
