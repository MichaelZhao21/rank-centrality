# Run Rank Centrality on the nascar dataset.
from src import rc

if __name__ == '__main__':
    f = open('data/nascar.txt', 'r')
    rankings = [tuple(line.strip().split('|')) for line in f]
    comps = rc.ranks_to_comparisons(rankings)
    item_index, comps = rc.to_indexed_comparisons(comps)

    bc_scores = rc.unindex_dict_keys(rc.borda_count(comps), item_index)
    rc_scores = rc.unindex_dict_keys(rc.rank_centrality(comps, init=0.5), item_index)
    sorted_bc_scores = sorted(bc_scores.items(), key=lambda x: x[1], reverse=True)
    sorted_rc_scores = sorted(rc_scores.items(), key=lambda x: x[1], reverse=True)

    print("Borda count scores:")
    for i in sorted_bc_scores:
        print(f'{i[0]:<20}', i[1])
    print()

    print("Rank centrality scores:")
    for i in sorted_rc_scores:
        print(f'{i[0]:<20}', i[1])
