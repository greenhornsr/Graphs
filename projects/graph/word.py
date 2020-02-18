# PROBLEM
'''
Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.
Sample:
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']
begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
beginWord = "hungry"
endWord = "happy"
None
'''

# attributes of problem
    # undirected, cyclic, sparse
    # nodes are words, edges/neighbors are words that differ by one and only one letter

# 1. Translate the problem into graph terminology
# 2. Build your graph
# 3. Traverse your graph

# Imports
from util import Stack, Queue

f = open('words.txt', 'r')
words = f.read().split('\n')
f.close()

word_set = set([w.lower() for w in words])


def get_neighbors(w):
    '''
    Return all words in word_set that have 1 and only 1 letter different
    '''
    # For each letter in the word:
        # For each letter in alphabet:
            # Replace the word letter with the alphabet letter
            # Check if the resulting word is in the word_set
            # Ignore if equal to the original word
            # if so, add to the neighbor list
    neighbors = []
    letter_list = list(w)
    alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    print(alphabet)
    for i in range(len(letter_list)):
        for letter in alphabet:
            temp_word = list(letter_list)
            temp_word[i] = letter
            new_word = ''.join(temp_word)
            print(new_word)
            if new_word in word_set and new_word is not w:
                neighbors.append(new_word)
    return neighbors

def find_ladders(begin_word, end_word):
    '''
    Find a word transformation between begin and end word
    use Breadth First Search
    '''
    q = Queue()
    q.enqueue([begin_word])

    visited = set()

    while q.size() > 0:
        path = q.dequeue()
        w = path[-1]
        if w == end_word:
            return path
        if w not in visited:
            visited.add(w)
            for neighbor in get_neighbors(w):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)
