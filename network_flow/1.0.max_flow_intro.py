 """
 
 how much flow can we push through a flow graph the edges of which have a  certain capacity without exceeding the capacity of each edge?
 this is the max flow problem.
 there is always a source node and a sink node the latter of which is the terminal node in the graph.
 flow graph: each edge has a certain capacity that must not be exceeded.

 a common algorithm for solving this problem is the Ford-Fulkerson method.
 Here we find augmenting paths throught the RESIDUAL GRAPH and augment the flow till no more augmenting paths are found.
 Here residual graph means the graph with the current flow indicated along with additional possible flow.

 and augmenting path is a path from source to sink with unused capacity > 0. That is, some edges might be occupied already but every edge on the path
 must have space for additional flow.
 Every augmenting path has a bottleneck value and this is equal to the smallest edge
 capacity on the path.
 since the flow through that path cannot be greater than the bottleneck we automatically 
 assume the flow through that path to be the bottleneck value and update all the edges 
 accordingly. This is called augmenting the path.

 The path back from the sink to the source tracing along the augmenting path is called
 the residual path, the members of which are called residual edges. We would also
 """