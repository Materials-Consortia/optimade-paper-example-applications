# High entropy alloys example

This folder contains scripts and results from querying OPTIMADE APIs for high
entropy alloy materials (HEA).

The client implemented in the
[optimade-python-tools](https://github.com/Materials-Consortia/optimade-python-tools) library was used to execute the following query:

```
elements HAS ANY
    "Mn", "Cr", "Fe", "Co", "Ni", "Cu", "Ag", "W", "Mo", "Nb", "Al", "Cd", "Sn", "Pb", "Bi", "Zn", "Ge", "Si", "Sb", "Mg"
AND NOT
    elements HAS ANY "B", "Br", "C", "Cl", "F", "H", "I", "N", "O", "P", "S", "Se"
AND
    nelements >= 4
```

The number of matching entries from each database are given in
[`results_count_table.md`](./results_count_table.md) (reproduced below):

|                                                                    |   count |
|:-------------------------------------------------------------------|--------:|
| http://aflow.org/API/optimade/                                     |     nan |
| https://www.crystallography.net/cod/optimade                       |    1297 |
| https://aiida.materialscloud.org/mc3d/optimade                     |     234 |
| https://aiida.materialscloud.org/mc2d/optimade                     |     191 |
| https://aiida.materialscloud.org/2dtopo/optimade                   |       0 |
| https://aiida.materialscloud.org/tc-applicability/optimade         |       0 |
| https://aiida.materialscloud.org/pyrene-mofs/optimade              |       0 |
| https://aiida.materialscloud.org/curated-cofs/optimade             |       0 |
| https://aiida.materialscloud.org/stoceriaitf/optimade              |       0 |
| https://aiida.materialscloud.org/autowannier/optimade              |       0 |
| https://aiida.materialscloud.org/tin-antimony-sulfoiodide/optimade |       0 |
| https://optimade.materialsproject.org                              |    1197 |
| https://api.mpds.io                                                |     nan |
| https://nomad-lab.eu/prod/rae/optimade/                            |      18 |
| https://optimade.odbx.science                                      |       0 |
| https://optimade-misc.odbx.science                                 |      12 |
| http://optimade.openmaterialsdb.se                                 |       0 |
| http://oqmd.org/optimade/                                          |    7555 |
| https://www.crystallography.net/tcod/optimade                      |       0 |
| http://optimade.2dmatpedia.org                                     |       0 |
| Total                                                              |    7634 |

The structures returned are available in
[`./data/hea_structures.json`](./data/hea_structures.json).

These results can be reproduced with:

```shell
pip install -r requirements.txt
python queries.py
```

Additionally, see the results of this query on the [web-client](https://optimade.science/?filter=elements%20HAS%20ANY%20%22Mn%22,%20%22Cr%22,%20%22Fe%22,%20%22Co%22,%20%22Ni%22,%20%22Cu%22,%20%22Ag%22,%20%22W%22,%20%22Mo%22,%20%22Nb%22,%20%22Al%22,%20%22Cd%22,%20%22Sn%22,%20%22Pb%22,%20%22Bi%22,%20%22Zn%22,%20%22Ge%22,%20%22Si%22,%20%22Sb%22,%20%22Mg%22%20AND%20NOT%20elements%20HAS%20ANY%20%22B%22,%20%22C%22,%20%22Cl%22,%20%22F%22,%20%22H%22,%20%22N%22,%20%22O%22,%20%22S%22,%20%22Se%22%20AND%20nelements%20%3E=%205).
