# Test inputs:
#NUM_MARBLES, NUM_PLAYERS = 25, 9 -> 32
#NUM_MARBLES, NUM_PLAYERS = 1618, 10 -> 8317

# Consider larger index to be clockwise.
# lower index is counter-clockwise.

def marbleGame(marbles, players):
    marbles = [0]
    current_index = 0
    player = 0
    scores = {i: 0 for i in range(NUM_PLAYERS)}
    for i in range(1, NUM_MARBLES+1):

        if i % 23 == 0:
            scores[player] += i
            scores[player] += marbles.pop((current_index - 7) % len(marbles))
            current_index = (current_index - 7) % (len(marbles) + 1)
        
        else:
            current_index = (current_index + 1) % len(marbles)+1
            marbles.insert(current_index, i)

        player = (player + 1) % NUM_PLAYERS
    
    return max(scores.values())

print("Part 1: ", marbleGame(71058, 491))
print("Part 1: ", marbleGame(7105800, 491))
