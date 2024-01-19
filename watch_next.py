import spacy

nlp1 = spacy.load('en_core_web_sm')
nlp2 = spacy.load('en_core_web_md')

movies = []

with open("movies.txt", "r+") as file:
	for line in file:
		movies.append(line)

planet_hulk_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

model = nlp2(planet_hulk_description)

similar = []
modifieds = []

for movie in movies:
	movie_description = movie.replace(movie[0:9], "")
	modify_description = nlp1(movie_description)
	modified_description = [token.orth_ for token in modify_description if not token.is_punct | token.is_space]
	modifieds.append(modified_description)
	
for description in modifieds:
	jo = " ".join(description)
	similarity = nlp2(jo).similarity(model)
	similar.append(similarity)

most_similar = max(similar)

get_index = similar.index(most_similar)

get_movie = movies[get_index]

movie_title = get_movie.replace(get_movie[8:], "")
print(f"{movie_title} - is the most similar movie to planet hulk that the user may watch next.")