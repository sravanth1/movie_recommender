import json
import pprint

#######for our convinience most of the times the data is changed to lowercase 

#####reading json file##################
with open("input.json") as main_file:
	data=json.load(main_file)

###########production of different genres############
distinct_genres=[]
for movie in data:
	for genre in movie['genre']:
		distinct_genres.append(genre.lower())

distinct_genres=sorted(list(set(distinct_genres)))

pprint.pprint(len(distinct_genres))

#######################production of different directors#############
distinct_directors=[]

for movie in data:
	distinct_directors.append(movie['director'].lower())

distinct_directors=sorted(list(set(distinct_directors)))

pprint.pprint(distinct_directors)


#######################production of feature vectors where keys are movie titles and 
#######################values are feature vectors of their genre indicating 1 at that position
genre_feature_vectors={}

for movie in data:
	genre_feature_vectors[movie['title'].lower()]=[0]*(len(distinct_genres)+2)#####first two indices are for imdb_rating and metascore
	genre_feature_vectors[movie['title'].lower()][0]=float(movie['rating'])
	genre_feature_vectors[movie['title'].lower()][1]=float(movie['metascore'])
	for genre in movie['genre']:
		genre_feature_vectors[movie['title'].lower()][distinct_genres.index(genre.lower())+2]=1


#############production od feature vectors where  keys are movie titles and values are 
#############feature vectors of which director directed that movie...indicated by 1 at that position
director_feature_vectors={}

for movie in data:
	director_feature_vectors[movie['title'].lower()]=[0]*len(distinct_directors)
	director_feature_vectors[movie['title'].lower()][distinct_directors.index(movie['director'].lower())]=1

pprint.pprint(director_feature_vectors)

