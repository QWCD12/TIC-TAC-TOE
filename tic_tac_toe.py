# Set up environment
board = [a1:'', a2:'', a3:'', b1:'', b2:'', b3:'', c1:'', c2:'', c3:'']
# Winner variable used to stop the program
winner = 0
# Set up winning environments
def win():
    if board[a1] == board[b2] and board[b2] == board[c3]:
        print( str(board[a1]) + "'s wins.")
        winner += 1
        return winner
    elif board[a1] == board[a2] and board[a2] == board[a3]:
        print( str(board[a1]) + "'s wins.")
        winner += 1
        return winner
    elif board[b1] == board[b2] and board[b2] == board[b3]:
        print( str(board[b1]) + "'s wins.")
        winner += 1
        return winner
    elif board[c1] == board[c2] and board[c2] == board[c3]:
        print( str(board[c1]) + "'s wins.")
        winner += 1
        return winner
    elif board[a1] == board[b1] and board[b1] == board[c1]:
        print( str(board[a1]) + "'s wins.")
        winner += 1
        return winner
    elif board[a2] == board[b2] and board[b2] == board[c2]:
        print( str(board[a2]) + "'s wins.")
        winner += 1
        return winner
    elif board[a3] == board[b3] and board[b3] == board[c3]:
        print( str(board[a3]) + "'s wins.")
        winner += 1
        return winner

# Player inputs
def move():
    next_move = input("What is your next move")
    # Convert next_move value to the certain board position
    if current_player == 'o':
        # Replace current value with o
        board[next_move] = 'o'
    elif current_player == 'x':
        # Replace current value with x
        board[next_move] = 'x'
