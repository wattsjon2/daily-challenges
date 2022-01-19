#Consider the following scenario:
#Imagine you are on a flight and want to watch 2 movies while you are in the air.
#You are given a list of integers (movie_durations) which includes the duration of all available 
#movies (in minutes) you have to choose from. You are also given an input d which represents the total 
#duration of the flight in minutes.
#In order to watch 2 movies on the flgiht, you must find 2 movies whose total duration is less than
#or equal to (d - 30 minutes). If multiple pairs are found, choose the pair with the longest total duration.
#Return the indices of the 2 movies you find.
#Input: movie_durations = [90, 85, 75, 60, 120, 150, 125], d = 250
#Output: [0, 6]
#Explanation: movieDurations[0] + movieDurations[6] = 90 + 125 = 215 is the maximum number within 220 (250min - 30min)


def inFlightMovies(movie_durations, d):
    pairs = set()
    for i in range(len(movie_durations)):
        for j in range(len(movie_durations)):
            if i == j:
                pass
            elif movie_durations[i] + movie_durations[j] < d - 30:
                pairs.add(tuple(sorted([i,j,movie_durations[i] + movie_durations[j]])))

    final = sorted(pairs, key = lambda i: i[2])
    return final[-1][0:2]
    

print(inFlightMovies([90, 85, 75, 60, 120, 150, 125],250))