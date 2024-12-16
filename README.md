# Movie-Recommender-System


Movie Recommendation System
This document provides an overview of our Movie Recommendation System, detailing the strategy, techniques, and processes used in building the model.

Overview
To develop an effective recommendation system, we employ Natural Language Processing (NLP) techniques to process and analyze textual data. Below is a step-by-step explanation of our approach:

1. Feature Engineering
Column Cleanup:
We begin by removing unnecessary columns from the dataset. Since the focus is on textual data (tags), numeric or unrelated columns are not required.

Data Preprocessing:- 

Remove unwanted data, spaces, and inconsistencies.
Extract only important terms for each row to create meaningful data.

2. Creating the Tag Feature
We combine relevant columns or features into a single "Tag" column to provide comprehensive textual input for the recommendation system.
Steps in Text Preprocessing
Lowercasing the Text:- 
All text is converted to lowercase to ensure uniformity (e.g., "Action" and "action" are treated the same).

Removing Stop Words and Punctuations: - 
Unimportant words like "is," "and," or "the" are removed, along with punctuations, to retain meaningful content.


Vectorization:- 
Since textual data cannot be processed directly, words are converted into vectors (numerical representations).
Example: For a dataset of 5000 movies with 500,000 total words, the words are transformed into vectors.
Using these vectors, we calculate the 5-10 most similar vectors for each movie to identify relationships between movies based on common features.

Stemming:-
Words are reduced to their root form to avoid redundancy.
Examples:
"Running," "runs," and "ran" → run
"Activity" and "activities" → activity


Similarity Calculation:- 
To calculate the similarity between movie vectors, we use the Cosine Distance Formula instead of the Euclidean Distance Formula.

Why Cosine Distance?
Cosine distance measures the angle between vectors, which is more effective for high-dimensional data (e.g., 5000-10,000 vectors).
Euclidean distance is less effective in higher dimensions due to issues like the "curse of dimensionality."


Conclusion:- 
This system enables us to build a robust movie recommendation model by efficiently identifying movies with similar features. By combining NLP techniques, preprocessing steps, and vector-based similarity calculations, we ensure accurate and meaningful recommendations.
