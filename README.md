# Rank Centrality

Based on Negahban et al.'s paper ["Rank centrality: Ranking from pair-wise comparisons"](https://arxiv.org/abs/1209.1688).

## Dataset

The test dataset here is the same 2002 Nascar dataset used in Hunter 2002:

> Hunter, David R. 2004. Mm algorithms for generalized bradley-terry models. *Annals of Statistics* 384–406.

The dataset was fetched using the R library [PlackettLuce](https://hturner.github.io/PlackettLuce). Although I couldn't download the library, I was able to get the data from Github (https://github.com/hturner/PlackettLuce/blob/532a93381b9b6d72bb6af6b6eabd8547a5801099/data/nascar.rda). After downloading the `nascar.rda` file, I ran the following commands in R:

```R
load(file='nascar.rda')
write.csv(nascar, file='races.csv')
write.csv(attr(nascar, 'drivers'), file='drivers.csv')
```

Then do the following in python:

```python
# TODO
```

I do not own any of the data presented and can remove the data uploaded to this repository upon request.

# Citations

[1] S. Negahban, S. Oh, and D. Shah, “Rank centrality: Ranking from pair-wise comparisons,” arXiv.org, https://arxiv.org/abs/1209.1688 (accessed Dec. 29, 2024). 