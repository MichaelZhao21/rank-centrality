# Run Rank Centrality on the nascar dataset.
from src import rc

if __name__ == '__main__':
    f = open('data/nascar.txt', 'r')
    rankings = [tuple(line.strip().split(',')) for line in f]
    comps = rc.ranks_to_comparisons(rankings)
    item_index, comps = rc.to_indexed_comparisons(comps)

    bc_scores = rc.borda_count(comps)
    rc_scores = rc.rank_centrality(comps)
    sorted_bc_scores = sorted(bc_scores.items(), key=lambda x: x[1], reverse=True)
    sorted_rc_scores = sorted(rc_scores.items(), key=lambda x: x[1], reverse=True)

    print("Borda count scores:")
    print(sorted_bc_scores)

    print("Rank centrality scores:")
    print(sorted_rc_scores)