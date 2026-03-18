from constraint import *

def edge_key(u, v):
    if u <= v:
        return u, v
    else:
        return v, u

def solve_with_k(graph, k):
    problem = Problem()

    node_vars = list(graph.nodes())
    edge_vars = [edge_key(u, v) for u, v in graph.edges()]

    for v in node_vars:
        problem.addVariable(("v", v), range(k))
    for e in edge_vars:
        problem.addVariable(("e", e), range(k))

    for u, v in graph.edges():
        problem.addConstraint(lambda a, b: a != b,
                              (("v", u), ("v", v)))

    for u, v in graph.edges():
        e = edge_key(u, v)
        problem.addConstraint(lambda e_col, u_col: e_col != u_col,
                              (("e", e), ("v", u)))
        problem.addConstraint(lambda e_col, v_col: e_col != v_col,
                              (("e", e), ("v", v)))

    for u in graph.nodes():
        incident_edges = [edge_key(u, v) for v in graph.neighbors(u)]
        for i in range(len(incident_edges)):
            for j in range(i + 1, len(incident_edges)):
                problem.addConstraint(lambda a, b: a != b,
                                      (("e", incident_edges[i]), ("e", incident_edges[j])))

    return problem.getSolution()


def total_coloring(graph):
    max_degree = max(dict(graph.degree()).values()) if graph.number_of_nodes() > 0 else 0

    for k in range(max_degree + 1, max_degree + 3):
        solution = solve_with_k(graph, k)
        if solution is not None:
            for u in graph.nodes():
                graph.nodes[u]["color"] = solution[("v", u)]
            for u, v in graph.edges():
                e = edge_key(u, v)
                graph.edges[u, v]["color"] = solution[("e", e)]
            return k

    k = max_degree + 3
    solution = solve_with_k(graph, k)
    if solution is not None:
        for u in graph.nodes():
            graph.nodes[u]["color"] = solution[("v", u)]
        for u, v in graph.edges():
            e = edge_key(u, v)
            graph.edges[u, v]["color"] = solution[("e", e)]
        return k

    raise Exception("No total coloring found")