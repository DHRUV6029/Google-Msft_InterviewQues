# I had a google phone screen which was fairly easy, however, I screwed up the time complexity because I was not as prepared + nervous. Said time complexity was O(N) instead of O(V+E) lol, so whatever. I clearly was not prepared since the interviewer didn't ask any follow up questions (this simple one took majority of time).

# It was a standard graph problem. Given a unidirectional graph, print all nodes in whichever order you want in an array. So, essentially you are flattening the graph and presenting it as an array. You also choose which data structure input you would like (obviously describe it). I chose to view it as a tree by passing in root node and then recursively traversing through neighbors whilst using a hashset to ensure a previously seen node doesn't get added in again.

#DO A bFS Simple (mighrt be cycles so keep making visirt and print the path )
