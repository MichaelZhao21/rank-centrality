# Rank Centrality

Based on Negahban et al.'s paper ["Rank centrality: Ranking from pair-wise comparisons"](https://arxiv.org/abs/1209.1688).

## Execution

Create a virtual environment and install the required packages:

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

Then, simply run the python test files: `python3 nascar.py`.

To check if the algorithm is correct, you can reference the actual rankings for the 2002 NASCAR season: https://www.driveraverages.com/nascar/year.php?yr_id=2002.

### Custom Dataset

To use your own dataset, prepare a python file similar to `nascar.py`. Note the format that we want the input rankings or pairwise comparison data in (see `rc.py`). Then, simply import the functions from `rc.py`. You will need to adjust the regularization parameter (`init` parameter of `rank_centrality` function). This is because when the graph is less connected, the stable distribution will not be as accurate. There are cases where the ranking order is flipped, but that is fixable by adjusting the `init` parameter. Generally, the less connected the graph, the higher the regularization parameter will need to be. Note that the default for this value is $10e-5$.

## Dataset

The test dataset here is the same 2002 Nascar dataset used in Hunter 2002:

> Hunter, David R. 2004. Mm algorithms for generalized bradley-terry models. *Annals of Statistics* 384–406.

The dataset was fetched using the R library [PlackettLuce](https://hturner.github.io/PlackettLuce). Although I couldn't download the library, I was able to get the data from Github (https://github.com/hturner/PlackettLuce/blob/532a93381b9b6d72bb6af6b6eabd8547a5801099/data/nascar.rda). After downloading the `nascar.rda` file, I ran the following commands in R:

```R
load(file='nascar.rda')
write.csv(nascar, file='races.csv')
write.csv(attr(nascar, 'drivers'), file='drivers.csv')
```

I then joined the data into `nascar.txt` using `extract.py`. This file contains all races, with each race on its own line. The order follows first place, second place, etc.

I do not own any of the data presented and can remove the data uploaded to this repository upon request.

# Citations

[1] S. Negahban, S. Oh, and D. Shah, “Rank centrality: Ranking from pair-wise comparisons,” arXiv.org, https://arxiv.org/abs/1209.1688 (accessed Dec. 29, 2024).
