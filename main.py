import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sample_path = r"C:\Users\Fawzaan\Documents\Programming Studies\AI_DS\Videos\Recommendation System\Building a movie recommendation system\movie_dataset.csv"
important_column = ['Actors', 'Director', 'Genre', 'Title']


class Recommender:
    def __init__(self, file_path, important_columns=[]):
        self.__file_path = file_path
        self.__df = pd.read_csv(self.__file_path)
        self.__df['Recommender_id'] = range(0, self.__df.shape[0])
        # Create a list of important columns for the recommendation engine
        self.__important_columns = important_columns
        self.__cosine_sim = self.__create_similarity_matrix()

    # Create a function to convert the values of the important columns into a single string
    def __get_important_features(self, data):
        important_features = []
        for i in range(0, data.shape[0]):
            important_features.append(
                data[self.__important_columns[0]][i] + ' ' + data[self.__important_columns[1]][i] + ' ' +
                data[self.__important_columns[2]][i] + ' ' + data[self.__important_columns[3]][i])
        return important_features

    # Tokenize the texts
    def __tokenize_texts(self):
        # Convert the text to a matrix of token counts
        cm = CountVectorizer().fit_transform(self.__get_important_features(self.__df))
        return cm

    def __create_similarity_matrix(self):
        # Get the cosine similiarity matrix from the count matrix
        # This creates a list of how similar other element/data are to the one
        # at the current position, thus the shape is cs.shape = (m x m)
        cs = cosine_similarity(self.__tokenize_texts())
        return cs

    def __get_sorted_program_similarity(self, movie_id):
        # Create a list of enumerations for the similarity scores
        scores = list(enumerate(self.__cosine_sim[movie_id]))
        # Sort the list
        sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
        # Remove itself since it will make the top of the list
        sorted_scores = sorted_scores[1:]
        return sorted_scores

    def get_sim_topk_info(self, movie_id, k=10):
        # Create a loop to  print the first 7 similar movies
        sorted_scores = self.__get_sorted_program_similarity(movie_id)
        sim_list = []
        recommended_objs = []
        j = 0
        # print('The 7 most recommended movie ', title, 'are:\n')
        for item in sorted_scores:
            recommended_obj = self.__df[self.__df.Recommender_id == item[0]]
            movie_title = recommended_obj['Title'].values[0]
            print((j + 1, movie_title))
            sim_list.append({"id": item[0], "name": movie_title})
            recommended_objs.append(recommended_obj.values)
            j = j + 1
            if j == k:
                break
        return sim_list, recommended_objs


recommender = Recommender(sample_path, important_columns=important_column)
print("DONE INIT")
recommender.get_sim_topk_info(368, k=5)
