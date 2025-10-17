import sys


def optimal_cakes(flour: int, sugar: int, eggs: int) -> int:
    """
    Determines the optimal combination of cakes from two recipes that maximizes
    total cakes and minimizes waste.

    Recipe 1: 100 flour, 50 sugar, 20 eggs
    Recipe 2: 50 flour, 100 sugar, 30 eggs

    Args:
        flour: An integer larger than 0 specifying the amount of available flour.
        sugar: An integer larger than 0 specifying the amount of available sugar.
        eggs: An integer larger than 0 specifying the amount of available eggs.

    Returns:
        An integer representing the total waste (sum of leftover ingredients)

    Raises:
        ValueError: If inputs are not positive.
    """
    # WRITE YOUR CODE HERE
    if not (
        isinstance(flour, int) and isinstance(sugar, int) and isinstance(eggs, int)
    ):
        raise ValueError("Inputs must be integers.")
    if flour <= 0 or sugar <= 0 or eggs <= 0:
        raise ValueError("Inputs must be positive integers.")

    total_available = flour + sugar + eggs

    # Calculate the bounds for Recipe A cakes
    max_x = min(flour // 100, sugar // 50, eggs // 20)

    best_usage = -1

    for x in range(max_x + 1):

        # Use the x-dependent bounds to calculate the maximum possible Recipe B cakes
        # under the currently considered Recipe A cake amount (x)
        y_by_flour = (flour - 100 * x) // 50
        y_by_sugar = (sugar - 50 * x) // 100
        y_by_eggs = (eggs - 20 * x) // 30

        # Select the minimum among the three constraints (worst case is the feasibility limit)
        ymax = min(y_by_flour, y_by_sugar, y_by_eggs)
        if ymax < 0:
            continue

        # Maximize usage function
        usage = 170 * x + 180 * ymax
        if usage > best_usage:
            best_usage = usage

    final_waste = total_available - best_usage
    return final_waste


# --- Main execution block. DO NOT MODIFY  ---
if __name__ == "__main__":
    try:
        # 1. Read input from stdin
        flour_str = input().strip()
        sugar_str = input().strip()
        eggs_str = input().strip()
        
        # 2. Convert inputs to appropriate types
        flour = int(flour_str)
        sugar = int(sugar_str)
        eggs = int(eggs_str)
        
        # 3. Call the optimal cakes function
        result = optimal_cakes(flour, sugar, eggs)
        
        # 4. Print the result to stdout in the required format
        print(result)
        
    except ValueError as e:
        # Handle errors during input conversion or validation
        print(f"Input Error or Validation Failed: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        # Handle cases where not enough input lines were provided
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
