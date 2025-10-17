import sys


def minimize_extraction(query_volumes: list, initial_trust: int, max_trust: int) -> int:
    """
    Determines the minimum information leaked while keeping trust above 0.

    Args:
        query_volumes: A list of integers representing information that would leak at each time period if no defense is applied
        initial_trust: An integer representing the starting user trust score
        max_trust: An integer representing the maximum possible trust score

    Returns:
        An integer representing the minimum information that must be leaked

    Raises:
        ValueError: If inputs are invalid.
    """
    # WRITE YOUR CODE HERE
    if not all(isinstance(i, int) for i in [initial_trust, max_trust]):
        raise ValueError("initial_trust and max_trust must be integers.")
    if not isinstance(query_volumes, list) or not all(
        isinstance(q, int) for q in query_volumes
    ):
        raise ValueError("query_volumes must be a list of integers.")

    memo = {}

    def solve(t, current_trust):
        # base case, all queries processed
        if t == len(query_volumes):
            return 0

        # try to hit the memoized result
        if (t, current_trust) in memo:
            return memo[(t, current_trust)]

        # add noise case, only if trust remains positive
        leakage_noise = float("inf")
        trust_after_noise = current_trust - query_volumes[t]
        if trust_after_noise > 0:
            # no leakage, so we just inherit future leakage
            leakage_noise = solve(t + 1, trust_after_noise)

        # clean response case
        trust_after_clean = min(current_trust * 2, max_trust)
        # leakage occurs proportionally to the query volume
        leakage_clean = query_volumes[t] + solve(t + 1, trust_after_clean)

        # pick the best option and memoize it
        result = min(leakage_noise, leakage_clean)
        memo[(t, current_trust)] = result
        return result

    return solve(0, initial_trust)


# --- Main execution block. DO NOT MODIFY ---
if __name__ == "__main__":
    try:
        # 1. Read input from stdin
        query_volumes_str = input().strip()
        initial_trust_str = input().strip()
        max_trust_str = input().strip()
        
        # 2. Convert inputs to appropriate types
        query_volumes = list(map(int, query_volumes_str.split()))
        initial_trust = int(initial_trust_str)
        max_trust = int(max_trust_str)
        
        # 3. Call the minimize_extraction function
        result = minimize_extraction(query_volumes, initial_trust, max_trust)
        
        # 4. Print the result to stdout
        print(result)
        
    except ValueError as e:
        print(f"Input Error or Validation Failed: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
