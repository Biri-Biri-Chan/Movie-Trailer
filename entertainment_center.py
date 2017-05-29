import media
import fresh_tomatoes

# The mummy movie: movie title, storyline, poster image and movie trailer
the_mummy = media.Movie(
	"THE MUMMY",
    "A legend that has endured since the dawn of man is reborn in THE MUMMY, "
    "Universal Pictures' all-new epic action-adventure.",
    "https://upload.wikimedia.org/wikipedia/en/a/a2/The_Mummy_%282017%29.jpg",  # NOQA
    "https://www.youtube.com/watch?v=t_Sp2MozCiI"
    )

# Transformers movie: movie title, storyline, poster image and movie trailer
transformers = media.Movie(
    "Transformers",
    "In the absence of Optimus Prime, a war has commenced between "
    "the human race and the Transformers.",
    "https://upload.wikimedia.org/wikipedia/en/2/26/Transformers_The_Last_Knight_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=Fm97e8Ynuzg"
    )

# Alien movie: movie title, storyline, poster image and movie trailer
alien = media.Movie(
    "Alien: Covenant",
    "Weyland tells David that one day they will search for mankind's "
    "creator together.",
    "https://upload.wikimedia.org/wikipedia/en/3/33/Alien_Covenant_Teaser_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=a3H4NevbIMQ"
    )

# King Arthur movie: movie title, storyline, poster image and movie trailer
king_arthur = media.Movie(
    "King Arthur: Legend of the Sword",
    "Arthur grows into a skilled fighter and man of the streets, alongside "
    "his friends Tristan and Backlack.",
    "https://upload.wikimedia.org/wikipedia/en/a/a4/King_Arthur_LotS_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=rmbacnTAESM"
    )

# Baywatch movie: movie title, storyline, poster image and movie trailer
baywatch = media.Movie(
    "Baywatch",
    "Mitch Buchannon, the gung-ho leader of the elite Baywatch lifeguard "
    "squad, clashes with new recruit Matt Brody, a washed-up pro "
    "athlete brought in as the new face of the organization.",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Baywatch_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=A1fZjiOwynM"
    )

# Kingsman movie: movie title, storyline, poster image and movie trailer
kingsman = media.Movie(
    "Kingsman: The Golden Circle",
    "Eggsy, Merlin and Roxy head to the United States to join forces with "
    "Statesman, Kingsman's American counterpart.",
    "https://upload.wikimedia.org/wikipedia/en/7/73/Kingsman_The_Golden_Circle.jpg",  # NOQA
    "https://www.youtube.com/watch?v=oepOtA9SCJA"
    )

movies = [the_mummy, transformers, alien, king_arthur, baywatch, kingsman]

fresh_tomatoes.open_movies_page(movies)
