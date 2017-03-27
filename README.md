A basic robotic clone to recommend movies using cosine simulator.



APPROACH:

1.Find the attributes which are sparse and fill the sparse places with the median of all the similar kind of attributes.Though there are many efficient ways to fill them I opted median for simplicity.

2.Find distinct number of actors , directors , genres to make their feature vectors for all the films.

3.Feature Vector : It is a vector where 1 is stored in every place corresponding to the attribiutes which are related to them.I.e..; for "DARK KNIGHT" movies the column corresponding to christopher nolan is '1' in director feature vectors.

4.Combine all the feature vectors into single array and add IMDB_ratign , runlength etc.. all the factors needed to the feature vector

5.Now we have a dictionary with movie titles as keys and feature vectors as values.

6.Mean Normalization.....i.e..; subtract mean of all the feature vectors from every feature vector and divide it by standard deviation of the same.

7.Use Cosine Similarity to get the top 10 similar movies as shown in the code.