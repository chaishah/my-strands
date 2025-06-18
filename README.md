# Strands Game

This project is a simple implementation of a **Strands**-style puzzle game inspired by the New York Times Strands. Each puzzle consists of a spanagram that uses every letter on the board and other theme-related words.

## Usage

1. Install dependencies (preferably in a virtual environment):
   ```bash
   pip install Flask
   ```

2. Update `puzzles.csv` with your puzzles. The CSV format is:

   ```csv
   date,theme,spanagram,words
   2024-01-01,Fruits,APPLEORANGE,"apple|orange|pear|grape"
   ```

   - `date` should be in `YYYY-MM-DD` format.
   - `spanagram` is the special word containing all letters on the board.
   - `words` lists other theme words, separated by `|`.

3. Run the server:

   ```bash
   python app.py
   ```

   The game will be available at `http://localhost:8000/`. You can request a specific puzzle by passing the date as a query parameter: `http://localhost:8000/?date=2024-01-01`.

4. Host the application on your preferred platform (e.g., a cloud server or platform-as-a-service) to make it accessible from anywhere.

## Updating Puzzles

Add a new line to `puzzles.csv` for each day with the theme, spanagram, and other words. The application reads from the CSV on startup, so restart the server after updating the file.

