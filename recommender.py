import json
import pprint
import numpy as np
import random
import collections
from operator import itemgetter
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

############################production of different actors####################
distinct_stars=[]
for movie in data:
	for star in movie['stars']:
		distinct_stars.append(star.lower())

distinct_stars=sorted(list(set(distinct_stars)))

#######################production of feature vectors where keys are movie titles and 
#######################values are feature vectors of their genre indicating 1 at that position
genre_feature_vectors={}

for movie in data:
	genre_feature_vectors[movie['title'].lower()]=[0]*(len(distinct_genres)+2)#####first two indices are for imdb_rating and metascore
	genre_feature_vectors[movie['title'].lower()][0]=float(movie['rating'])

	###########some of the metascores are not given...they are NULL so we have to predict it
	if len(movie['metascore']) > 0:
		genre_feature_vectors[movie['title'].lower()][1]=float(movie['metascore'])
	else:
		genre_feature_vectors[movie['title'].lower()][1]=0

	for genre in movie['genre']:
		genre_feature_vectors[movie['title'].lower()][distinct_genres.index(genre.lower())+2]=1


#############production od feature vectors where  keys are movie titles and values are 
#############feature vectors of which director directed that movie...indicated by 1 at that position
director_feature_vectors={}

for movie in data:
	director_feature_vectors[movie['title'].lower()]=[0]*len(distinct_directors)
	director_feature_vectors[movie['title'].lower()][distinct_directors.index(movie['director'].lower())]=1

#pprint.pprint(director_feature_vectors)

#############production od feature vectors where  keys are movie titles and values are 
#############feature vectors of which actors acted in that movie...indicated by 1 at that position

actor_feature_vectors={}

for movie in data:
	actor_feature_vectors[movie['title'].lower()]=[0]*len(distinct_stars)
	for star in movie['stars']:
		actor_feature_vectors[movie['title'].lower()][distinct_stars.index(star.lower())]=1

#pprint.pprint(actor_feature_vectors)

################Combining all the feature vectors to make a single feature vector as the keys in all the dicts are same ...i.e; the movies

all_feature_vectors={}

for key in genre_feature_vectors:
	all_feature_vectors[key]=genre_feature_vectors[key]+director_feature_vectors[key]+actor_feature_vectors[key]

print(all_feature_vectors)

test_movie=data[random.randint(0,len(data)-1)]

pprint.pprint(test_movie['title'])
test_feature_vector=all_feature_vectors[test_movie['title'].lower()]

results={}
for key in all_feature_vectors:
	results[key]=np.dot(np.array(test_feature_vector),np.array(all_feature_vectors[key]))/(np.linalg.norm(np.array(test_feature_vector))*np.linalg.norm(np.array(all_feature_vectors[key])))

od=collections.OrderedDict(sorted(results.items(),key=itemgetter(1)))
print (type(od))
pprint.pprint(od)

####################consider last 11 and i printed the selected movie also at first(test_movie)