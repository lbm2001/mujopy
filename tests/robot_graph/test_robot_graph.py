def test_robo_graph(go1_robot_graph):

    # Test number of nodes and edges
    num_nodes = go1_robot_graph.number_of_nodes()
    num_edges = go1_robot_graph.number_of_edges()
    assert num_nodes == 25
    assert num_edges == 24

    # Test feature matrix shape
    feature_matrix = go1_robot_graph.feature_matrix
    assert go1_robot_graph.BODY_DIM == 13
    assert go1_robot_graph.JOINT_DIM == 3
    assert feature_matrix.shape == (25, 16)
