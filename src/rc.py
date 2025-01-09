from scipy.linalg import eig
import numpy as np

def print_matrix(matrix: list[list[float]]) -> None:
    """
    Prints the float matrix in a nice format, with 2 decimal places.
    """

    for row in matrix:
        for i in row:
            print("{:.2f}".format(i), end=" ")
        print()
        

def ranks_to_comparisons(rankings: list[tuple]) -> dict[tuple, int]:
    """
    Converts a list of rankings to a dictionary of comparisons. The input is a list of rankings,
    where each ranking is a list of items. The output is a dictionary with keys (i, j), where i
    beats j, and the value is the number of times i beats j.
    """

    # Initialize the comparisons dictionary
    comparisons = {}

    # Iterate over each ranking
    for ranking in rankings:
        # Iterate over each pair of items in the ranking
        for i in range(len(ranking)):
            for j in range(i + 1, len(ranking)):
                # Get the items
                win = ranking[i]
                lose = ranking[j]

                # Update the comparisons dictionary
                if (win, lose) in comparisons:
                    comparisons[(win, lose)] += 1
                else:
                    comparisons[(win, lose)] = 1
                if (lose, win) not in comparisons:
                    comparisons[(lose, win)] = 0

    return comparisons


def to_indexed_comparisons(comparisons: dict[tuple, int]) -> tuple[dict, dict, dict[tuple[int, int], int]]:
    """
    Converts a dictionary of comparisons to a dictionary of items and a dictionary of indexes
    and returns that dictionary.
    """

    # Get all items
    items = set()
    for key in comparisons.keys():
        items.add(key[0])
        items.add(key[1])

    # Create a dictionary of items to indexes
    item_to_index = {}
    index_to_item = {}
    for i, item in enumerate(sorted(items)):
        item_to_index[item] = i
        index_to_item[i] = item

    # Create a dictionary of indexed comparisons
    indexed_comparisons = {}
    for key, value in comparisons.items():
        indexed_comparisons[(item_to_index[key[0]], item_to_index[key[1]])] = value

    return index_to_item, indexed_comparisons


def unindex_dict_keys(d: dict[int, float], index: dict) -> dict[any, float]:
    """
    Converts a dictionary with integer keys to a dictionary with the keys in the map.
    """

    # Create a new dictionary
    new_dict = {}
    for key, value in d.items():
        new_key = index[key]
        new_dict[new_key] = value

    return new_dict


def borda_count(comparisons: dict[tuple, int]) -> dict[any, float]:
    """
    Computes the Borda count scores of all items passed in. The comparisons dictionary
    contains key (i, j), where i beats j and value is the number of times i beats j. The
    output dictionary is a mapping from item to its Borda count score.
    """

    # Initialize the Borda count dictionary
    borda_counts = {}

    # Iterate over each comparison
    for key, value in comparisons.items():
        win, lose = key

        # Update the Borda count dictionary
        if win in borda_counts:
            borda_counts[win] += value
        else:
            borda_counts[win] = value

        if lose not in borda_counts:
            borda_counts[lose] = 0

    return borda_counts


def rank_centrality(comparisons: dict[tuple, int]) -> dict[any, float]:
    """
    Computes the rank centrality scores of all items passed in. The comparisons dictionary
    contains key (i, j), where i beats j and value is the number of times i beats j. The
    output dictionary is a mapping from item to its rank centrality score.
    """

    # Make sure all comparisons are valid (keys have to be tuples of length 2)
    for key in comparisons.keys():
        if not isinstance(key, tuple) or len(key) != 2:
            raise ValueError("Invalid comparison key: {}".format(key))
    
    # Calculate out-degree of each item and get max
    out_degree = {}
    for key in comparisons.keys():
        i, j = key
        if i in out_degree:
            out_degree[i] += 1
        else:
            out_degree[i] = 1
    d = max(out_degree.values())
    n = len(out_degree)
    
    # Create probability transition matrix
    p = [[10e-5 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if (i, j) in comparisons:
                p[i][j] = comparisons[(i, j)] / (comparisons[(i, j)] + comparisons[(j, i)]) / d
    for i in range(n):
        p[i][i] = 1 - sum(p[i]) - 10e-5

    # Get left eigenvector of p
    w, v = eig(p, left=True, right=False)

    # Get the leading eigenvector
    max_index = np.argmax(w)
    leading_eigenvector = v[:, max_index]

    # Normalize the leading eigenvector
    leading_eigenvector = (leading_eigenvector - min(leading_eigenvector)) / (max(leading_eigenvector) - min(leading_eigenvector)) * 100

    # Map the leading eigenvector to the items
    scores = {i: v for i, v in enumerate(leading_eigenvector)}

    return scores

    
if __name__ == "__main__":
    # Test the function
    rankings = [('b', 'c', 'a', 'd', 'e'), ('a', 'b', 'c', 'd', 'e'), ('b', 'c', 'a', 'e', 'd'), ('c', 'b', 'a', 'e', 'd'), ('b', 'c', 'd', 'e', 'a'), ('c', 'b', 'e', 'a', 'd')]
    comps = ranks_to_comparisons(rankings)
    item_index, comps = to_indexed_comparisons(comps)

    bc_scores = borda_count(comps)
    rc_scores = rank_centrality(comps)
    sorted_bc_scores = sorted(bc_scores.items(), key=lambda x: x[1], reverse=True)
    sorted_rc_scores = sorted(rc_scores.items(), key=lambda x: x[1], reverse=True)

    print("Borda count scores:")
    print(sorted_bc_scores)

    print("Rank centrality scores:")
    print(sorted_rc_scores)

