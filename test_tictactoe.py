from functions import check_winner

def test_check_winner():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    assert check_winner(board, 'X') == False
    board = [' ', 'X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
    assert check_winner(board, 'X') == True
    board = [' ', 'X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
    assert check_winner(board, 'X') == True


