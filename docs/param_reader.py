# %%
from itertools import product
import jupytext
import papermill as pm
from nbformat.corpus.words import generate_corpus_id
from copy import deepcopy


def reads(text, fmt):
    conf = jupytext.config.JupytextConfiguration(
        notebook_metadata_filter="kernelspec,jupytext,params"
    )
    nb = jupytext.reads(text, fmt="myst", config=conf)
    for cell in nb.cells:
        if hasattr(cell.metadata, "tags") is False:
            cell.metadata["tags"] = []
        if not hasattr(cell.metadata, "papermill"):
            cell.metadata["papermill"] = dict()

    if hasattr(nb.metadata, "papermill") is False:
        nb.metadata["papermill"] = dict()
    params = combinations(nb.metadata.params)
    new_cells = []
    for i, param in enumerate(params):
        p_nb = pm.parameterize.parameterize_notebook(nb, parameters=param)
        if i == 0:
            first_nb = deepcopy(p_nb)
        else:
            new_cells += _filter_cells(p_nb.cells)
    # removing cell preceding the injected parameters > ie.e remove the item called parameters
    first_nb.cells = _filter_cells(first_nb.cells) + new_cells

    # recompute all cell ids (to avoid unexpected behaviour)
    cells = []
    nbdict = deepcopy(first_nb)
    for cell in nbdict["cells"]:
        cell["id"] = generate_corpus_id()
        cells.append(cell)
    nbdict.cells = cells
    return nbdict


def _filter_cells(cells, value="parameters"):
    return [cell for cell in cells if value not in cell.metadata.tags]


def combinations(params):
    keys = list(params.keys())
    value_combinations = product(*(params[key] for key in keys))
    result = [
        {key: value for key, value in zip(keys, values)}
        for values in value_combinations
    ]
    return result


def test_comb():
    params = {"a": [1, 2], "b": [1]}
    result = combinations(params)
    expected = [{"a": 1, "b": 1}, {"a": 2, "b": 1}]
    assert result == expected


# %%
