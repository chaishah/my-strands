import csv
from datetime import datetime
from flask import Flask, render_template, request, abort

app = Flask(__name__)

PUZZLE_FILE = 'puzzles.csv'

# Load puzzles from CSV
def load_puzzles():
    puzzles = {}
    with open(PUZZLE_FILE, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = row['date']
            puzzles[date] = {
                'theme': row['theme'],
                'spanagram': row['spanagram'].strip(),
                'words': [w.strip() for w in row['words'].split('|')]
            }
    return puzzles

# Arrange letters into a 6x6 board (fills with random letters)
import random
import string

def make_board(spanagram, words):
    letters = list(spanagram.upper())
    for word in words:
        letters.extend(list(word.upper()))
    # fill with random letters up to 36
    while len(letters) < 36:
        letters.append(random.choice(string.ascii_uppercase))
    random.shuffle(letters)
    board = [letters[i*6:(i+1)*6] for i in range(6)]
    return board

Puzzles = load_puzzles()

@app.route('/')
def index():
    # get puzzle by ?date=YYYY-MM-DD or today's puzzle
    date = request.args.get('date')
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    puzzle = Puzzles.get(date)
    if not puzzle:
        abort(404, f'Puzzle for {date} not found.')
    board = make_board(puzzle['spanagram'], puzzle['words'])
    return render_template('index.html', date=date, puzzle=puzzle, board=board)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
