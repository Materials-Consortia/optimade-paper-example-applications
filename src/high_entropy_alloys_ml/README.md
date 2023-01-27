# High entropy alloys example

This folder contains scripts and results from querying OPTIMADE APIs for high
entropy alloy materials (HEA).

The client implemented in the
[optimade-python-tools](https://github.com/Materials-Consortia/optimade-python-tools) library was used to execute the following query:

```
elements HAS ANY
    "Mn", "Cr", "Fe", "Co", "Ni", "Cu", "Ag", "W", "Mo", "Nb", "Al", "Cd", "Sn", "Pb", "Bi", "Zn", "Ge", "Si", "Sb", "Mg"
AND NOT
    elements HAS ANY "B", "Br", "C", "Cl", "F", "H", "N", "O", "S", "Se"
AND
    nelements >= 5
```

The number of matching entries from each database are given in
[`results_count_table.md`](./results_count_table.md) (reproduced below):

|                                                                    |   count |
|:-------------------------------------------------------------------|--------:|
| http://aflow.org/API/optimade/                                     |       2 |
| https://www.crystallography.net/cod/optimade                       |      42 |
| https://aiida.materialscloud.org/mc3d/optimade                     |       2 |
| https://aiida.materialscloud.org/mc2d/optimade                     |       0 |
| https://aiida.materialscloud.org/2dtopo/optimade                   |       0 |
| https://aiida.materialscloud.org/tc-applicability/optimade         |       0 |
| https://aiida.materialscloud.org/pyrene-mofs/optimade              |       0 |
| https://aiida.materialscloud.org/curated-cofs/optimade             |       0 |
| https://aiida.materialscloud.org/stoceriaitf/optimade              |       0 |
| https://aiida.materialscloud.org/autowannier/optimade              |       0 |
| https://aiida.materialscloud.org/tin-antimony-sulfoiodide/optimade |       0 |
| https://optimade.materialsproject.org                              |       8 |
| https://api.mpds.io                                                |     nan |
| https://nomad-lab.eu/prod/rae/optimade/                            |      21 |
| https://optimade.odbx.science                                      |       0 |
| https://optimade-misc.odbx.science                                 |      10 |
| http://optimade.openmaterialsdb.se                                 |       0 |
| http://oqmd.org/optimade/                                          |    7772 |
| https://www.crystallography.net/tcod/optimade                      |       0 |
| http://optimade.2dmatpedia.org                                     |       0 |
| Total                                                              |    7857 |

The structures returned are available in
[`./data/hea_structures.json`](./data/hea_structures.json).

These results can be reproduced with:

```shell
pip install -r requirements.txt
python queries.py
```
