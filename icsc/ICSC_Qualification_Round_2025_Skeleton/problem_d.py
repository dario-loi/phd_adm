import sys
import random


def create_crossword(words: list) -> list:
    """
    Generate a 10x10 word search puzzle containing the given words.
    
    Args:
        words: A list of words to include in the puzzle.
        
    Returns:
        A 2D array (list of lists) representing the word search puzzle.
    """
    
    import string
    random.seed(42)
    
    # WRITE YOUR CODE HERE
    GRID_SIZE = 10
    base = [w.upper() for w in words]
    # generate distractors by removing the last character of each word longer than 4 letters
    # we only want at most 3 distractors
    distractors = [w[:-1].upper() for w in base if len(w) > 4][:3]
    full_map = {
        d: [f for f in base if f.startswith(d) and len(f) == len(d) + 1]
        for d in distractors
    }  # map distractor to its full word
    seq = sorted(base + distractors, key=len, reverse=True)
    g = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]

    # easily extendable to generate reverse words by adding (0, -1), (-1, 0), (-1, -1)
    DIRS = ((0, 1), (1, 0), (1, 1))
    for wi, w in enumerate(seq):
        is_distractor = w in full_map
        best = None
        best_i = -1
        placements = []
        L = len(w)
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                for dr, dc in DIRS:
                    # skip trivial placement (first row, first column, horizontal)
                    # a bit hardcoded, but necessary for aesthetics
                    if wi == 0 and r == 0 and c == 0 and dr == 0 and dc == 1:
                        continue
                    rr, cc = r + (L - 1) * dr, c + (L - 1) * dc
                    # ensure within bounds
                    if not (0 <= rr < GRID_SIZE and 0 <= cc < GRID_SIZE):
                        continue
                    inter = 0
                    new_cells = 0
                    ok = True
                    for i, ch in enumerate(w):
                        R, C = r + i * dr, c + i * dc
                        cell = g[R][C]

                        # if already taken by different char, skip
                        if cell and cell != ch and not cell.islower():
                            ok = False
                            break
                        # if already taken by same char, intersect
                        if cell == ch:
                            inter += 1
                        # overwrite constraint with different character
                        if (
                            cell is None
                            or cell.islower()
                            and not cell.upper() == ch
                        ):
                            new_cells += 1
                    if not ok:
                        continue
                    # skip fully embedded distractor (no new cells added)
                    if is_distractor and new_cells == 0:
                        continue
                    # mark placement as best one, maximizing intersections
                    if inter > best_i:
                        best_i, best = inter, (r, c, dr, dc)
                    placements.append((r, c, dr, dc))
        if not best:
            if not placements:
                continue
            # pick random best placement
            best = random.choice(placements)
        r, c, dr, dc = best
        for i, ch in enumerate(w):
            # write the word into the grid
            g[r + i * dr][c + i * dc] = ch
        # mark forbidden extension letters after distractor to avoid forming full word
        if is_distractor:
            rr, cc = r + L * dr, c + L * dc
            if (
                0 <= rr < GRID_SIZE
                and 0 <= cc < GRID_SIZE
                and g[rr][cc] is None
            ):
                forb = "".join({f[-1].lower() for f in full_map[w]})
                g[rr][cc] = forb
    # fill remaining with random letters avoiding lowercase-forbidden markers
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            cell = g[r][c]
            if cell is None or cell.islower():
                # extract constraint
                banned = set(cell.upper()) if cell else set()
                choices = set(string.ascii_uppercase) - banned
                g[r][c] = random.choice(list(choices))
    return g




# --- Main execution block. DO NOT MODIFY.  ---
if __name__ == "__main__":
    try:
        # Read words from first line (comma-separated)
        words_input = input().strip()
        words = [word.strip() for word in words_input.split(',')]
        
        # Generate the word search puzzle
        puzzle = create_crossword(words)
        
        # Print the result as a 2D grid
        for row in puzzle:
            print(''.join(row))
            
    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)