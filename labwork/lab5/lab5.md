# Lab 5: Python programming and LS routing

## Objectives

1. To become familiar with the syntax and key data structures of Python, for use in Assignment 2.
2. To reinforce our discussion of the routing algorithms discussed in the slides and via programming and exposure to relevant APIs:
  - The NetJSON data interchange format
  - The NetworkX library for network algorithms and visualization
3. To become acquainted with a function that we'll extend as part of Assignment 2.

To receive credit for completing the worksheet, please complete the [Lab 5 Quiz](https://canvas.auckland.ac.nz/courses/31482/quizzes/24192) on Canvas. You'll receive feedback immediately afterwards, and may choose to redo the quiz if you wish.

> The labs' contributions reflect that completion implies engagement with the associated exercises and course material: Please tackle the questions mindfully and independently, as you would for a written assignment.

> Several activities on the lab worksheet are framed as "questions", but responses needn't be submitted (i.e. the on-line quiz is the only submission required). Please don't hesitate to speak to a member of the 364 team if you are unsure of what a suitable response might be.

---

## Preparation

The software we need this week is installed in the Engineering computer lab. If you're working on your own PC, please install [`Anaconda`](https://www.anaconda.com) and [`git`](https://git-scm.com/downloads).

1. Activate a new Python 3.6 environment using `conda`.

```powershell
> conda create -n softeng364python3 python=3.6
> activate softeng364python3
```

2. Install the Python modules [`gevent`](http://www.gevent.org) and [`networkx`](https://networkx.github.io) that we'll require.

```powershell
> conda install gevent networkx
```

> You may like to make a new Git repository in which to track your SOFTENG 364 lab- and assignment work.

3. Create a new text file called e.g. `softeng364lab5.py` and open it in `Spyder` - the Python IDE shipped with Anaconda.

As you proceed through the worksheet, you can append new code snippets and re/execute them by clicking `Run file (F5)` or by typings `%run softeng364lab5.py` at Spyder's IPython command prompt.

---

## Graph representation in JSON and Python

NetJSON is a proposed [serialization](https://en.wikipedia.org/wiki/Serialization) format for network entities.

- Visit [netjson.org](http://netjson.org/) and briefly (<3 minutes) consider the following questions:
  - What is JSON?
  - Which primitive types does JSON support? Which data structures?
  - What types of network-related entities does NetJSON support? Which one is used to encode network graphs?
  - What identifiers are available for nodes?
  - How are attributes associated with nodes and links?

- Encode the network on Slide `5-15`, say, in NetJSON format, including its link costs and the following node coordinates. Save your file as e.g. `KuroseRoss5-15.json`. If you have problems, an example is available [here](https://github.com/softeng364/resources/blob/master/labwork/lab5/).

```json
{
    "u": [0.0, 0.0],
    "v": [1.0, -1.0],
    "w": [1.0, 0.0],
    "x": [1.0, 1.0],
    "y": [2.0, 0.0],
    "z": [3.0, 0.0]
}
```

The Python Standard Library includes a module, [`json`](https://docs.python.org/3/library/json.html) that provides functions (`json.load` and `json.dump`) for de/serialization of JSON to/from Python data structures.

- Use the following snippet of code to deserialize your NetJSON file:

```python
import json
import os
from pprint import pprint  # "pretty print"

filename = os.path.join('.', 'KuroseRoss5-15.json')
with open(filename) as stream:  # ensures stream will be closed
    netjson = json.load(stream)
pprint(netjson)
```

- The resulting value is a Python [`dict`](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)ionary: Python's analog of `HashMap` in Java or `std::map` in C++.

```python
>>> print(type(netjson))
<class 'dict'>
```

- Execute each of the following commands and speak to a 364 team member if you have any queries.

```python
>>> netjson['type']  # retrieves value associated with field 'type'
'NetworkGraph'

>>> pprint(netjson['nodes'])  # this field is a list of dicts
[{'id': 'u', 'properties': {'name': 'u', 'pos': [0.0, 0.0]}},
 {'id': 'v', 'properties': {'name': 'v', 'pos': [1.0, -1.0]}},
 {'id': 'w', 'properties': {'name': 'w', 'pos': [1.0, 0.0]}},
 {'id': 'x', 'properties': {'name': 'x', 'pos': [1.0, 1.0]}},
 {'id': 'y', 'properties': {'name': 'y', 'pos': [2.0, 0.0]}},
 {'id': 'z', 'properties': {'name': 'z', 'pos': [3.0, 0.0]}}]

>>> netjson['nodes'][1]['properties']['name']  # "Do we expect 'u' or 'v'?"
'v'
```

While this `dict` allows us full programmatic access to the graph, many of the things we'd want to do are already available in [NetworkX](https://networkx.github.io): A comprehensive package of Python classes and function for computing with graphs.

## Network representation with NetworkX

- The following code snippet converts our [`dict`](https://docs.python.org/3/library/stdtypes.html?highlight=dict#dict) representation into a [`networkx.Graph`](https://networkx.github.io/documentation/stable/reference/classes/index.html#basic-graph-types) with the original node- and edge attributes. Spend a few minutes (<5) investigating the sub-expressions in this snippet and discuss them with your neighbour.

```python
import networkx as nx  # saves some typing
graph = nx.Graph()
graph.add_nodes_from((
    (node['id'], node['properties'])
        for node in netjson['nodes']))
graph.add_edges_from((
    (link['source'], link['target'], {'cost': link['cost']})
        for link in netjson['links']))  # nodes & attributes

for node, data in graph.nodes(data=True):
    pprint((node, data))

for source, target, data in graph.edges(data=True):
    pprint((source, target, data))  # edges & attributes

for node in graph:
    pprint((node, dict(graph[node])))  # neighbours
```

The resulting `networkx.Graph` contains the same information as the original struct, but all of NetworkX's functions are now directly applicable.

- Replace `graph = nx.Graph()` with `graph = nx.DiGraph()` and re-execute the snippets above.
  - What is the impact on node neighbours?
  - Are twice as many edges actually stored in `Graph`?
  - Are link attributes duplicated in `Graph`?

## Network visualization with NetworkX

- Visualize the graph and its node- and edge attributes, using the specified node coordinates:

```python
node_positions = nx.get_node_attributes(graph, name='pos')
edge_label_positions = nx.draw_networkx_edge_labels(
        graph,
        pos=node_positions,
        node_labels=nx.get_node_attributes(graph, name='name'),
        edge_labels=nx.get_edge_attributes(graph, name='cost'))
draw_networkx(graph, pos=node_positions)
```

When node coordinates are not available, one can employ automatic [graph drawing](https://en.wikipedia.org/wiki/Graph_drawing) algorithms.

- Duplicate the preceding snippet and use  [`spring_layout`](https://networkx.github.io/documentation/stable/reference/generated/networkx.drawing.layout.spring_layout.html#networkx.drawing.layout.spring_layout) as follows.

```python
node_positions = nx.spring_layout(graph)
# Copy snippet as above
```

Before you continue, have a quick look at some of the other algorithms available in NetworkX's [drawing layout](https://networkx.github.io/documentation/stable/reference/drawing.html#module-networkx.drawing.layout) module and their parameters.

## Least-cost paths with NetworkX

NetworkX provides a number of different algorithms and interfaces relating to network algorithms.

- Scan the list of functions in NetworkX's [Algorithms](https://networkx.github.io/documentation/stable/reference/algorithms/index.html) module and briefly (<3 minutes) discuss any that look familiar or interesting - especially if you've met them outside of the context of SOFTENG 250.

We're presently concerned with least-cost paths.

> While Kurose & Ross distinguish between **least-cost** paths and **shortest** paths, NetworkX does not.

- Scan the [list of algorithms](https://networkx.github.io/documentation/stable/reference/algorithms/shortest_paths.html#module-networkx.algorithms.shortest_paths.unweighted) provided for least-cost paths and contrast the following interfaces with your neighbour: Why are they all provided? Which is the minimal interface that we'd need to compute a forwarding table?

| Interface |
|-|
| `*path*()` |
| `*paths*()` |
| `*length*()` |
| `*distance*()` |
| `*predecessor*()` |

- Use one of NetworkX's functions compute the **predecessor** map and the **distances** of the least-cost paths for our network `KuroseRoss5-15`. Satisfy yourself that the outputs match those that we computed on `Slide 5-15` i.e.

```python
>>> pprint(D)  # distances from source 'u'
{'u': 0, 'v': 6, 'w': 3, 'x': 5, 'y': 10, 'z': 12}

>>> pprint(p)  # predecessor list
{'u': [], 'v': ['w'], 'w': ['u'], 'x': ['u'], 'y': ['v'], 'z': ['y']}
```

- Use [`networkx.convert.from_dict_of_lists()`](https://networkx.github.io/documentation/stable/reference/generated/networkx.convert.from_dict_of_lists.html) to generate the least-cost path tree from your predecessor list. Ensure that the edge list is consistent with Slide `5-15`.

```python
>> networkx.convert.from_dict_of_lists(p).edges()
EdgeView([('u', 'w'), ('u', 'x'), ('v', 'w'), ('v', 'y'), ('y', 'z')])
```

- Visualize the least-cost path tree (on top of the original graph) using [`nx.draw_networkx_edges`](https://networkx.github.io/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw_networkx_edges.html). This function has many optional parameters: We need only specify `edgelist`, `edge_color`, and perhaps `width`. Again, ensure that the result is consistent with Slide `5-15`.

- **[Extra]** NetworkX provides implementations of the Dijkstra, Bellman-Ford, Johnson, Floyd-Warshall, and A* algorithms. Contrast these in terms of generality, efficiency, and dependence on network structure.

## Implementation of Dijkstra's algorithm

The pseudocode on Slide `5-14` might be translated into Python as follows:

```python
def dijkstra_5_14(graph, source, weight='weight'):
    """
    Shortest paths via Dijkstra's algorithm,
    consistent with pseudocode on Slide 5-14.
    """
    import math

    # Definitions consistent with Kurose & Ross
    u = source
    def c(x, y):
        return graph[x][y][weight]
    N = frozenset(graph.nodes())
    NPrime = {u}  # i.e. "set([u])"
    D = dict.fromkeys(N, math.inf)

    # Initialization
    for v in N:
        if graph.has_edge(u, v):
            D[v] = c(u, v)
    D[u] = 0  # over-write inf entry for source

    # Loop
    while NPrime != N:
        candidates = {w: D[w] for w in N if w not in NPrime}
        w, Dw = min(candidates.items(), key=lambda item: item[1])
        NPrime.add(w)
        for v in graph[w]:
            if v not in NPrime:
                DvNew = D[w] + c(w, v)
                if DvNew < D[v]:
                    D[v] = DvNew
    return D
```

- Compare each line to the original pseudocode and discuss the following new constructs with your neighbour; trust your intuition and consult the documentation (or a 364 team member) if you are still unsure.
  - Initialization of `D` using [`dict.fromkeys()`](https://docs.python.org/3/library/stdtypes.html#dict.fromkeys) and [`math.inf`](https://docs.python.org/3/library/math.html?math.inf#math.inf)
  - Initialization of the set of nodes `N` as a [`set`/`frozenset`](https://docs.python.org/3/library/stdtypes.html#set). (Why is this necessary? "Isn't `graph.nodes()` already a set?").
  - Initialization of `NPrime` as a [`set`](https://docs.python.org/3/library/stdtypes.html#set).
  - Initialization of `candidates` using familiar [set-builder notation](https://en.wikipedia.org/wiki/Set-builder_notation).
  - Using an [anonymous function](https://en.wikipedia.org/wiki/Anonymous_function) ([`lambda` expression](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)) to map each key-value pair to its value.
  - Using the built-in function [`min`](https://docs.python.org/3/library/functions.html?highlight=min#min) to find a key-value pair with the smallest value.

Two components of **Assignment 2** relate to this function:

1. Make the (small) modifications necessary to compute the predecessor list, which was not considered in the pseudocode.
2. Write a function to compute a forwarding table for the `source` node from the predecessor list.
3. Discuss possible changes that could improve efficiency.
4. Generalize the implementation to support [widest-path- and minimax](https://en.wikipedia.org/wiki/Widest_path_problem) routing problems.

> More information about these and other parts of the assignment will be made available. For now, please complete the lab quiz.
