def test_children(go1_mujopy_model):

    # Test for first body
    first_body = go1_mujopy_model.body(0)
    children = first_body.children
    first_child = children[0]

    assert len(children) == 1
    assert first_child == go1_mujopy_model.body(1)

    # Test for second body
    children = first_child.children

    assert len(children) == 4
    assert children[0] == go1_mujopy_model.body(2)
    assert children[1] == go1_mujopy_model.body(5)
    assert children[2] == go1_mujopy_model.body(8)
    assert children[3] == go1_mujopy_model.body(11)


def test_joints(go1_mujopy_model):

    # Test for first body
    first_body = go1_mujopy_model.body(0)
    joints = first_body.joints
    assert len(joints) == 0

    # Test for third body
    third_body = go1_mujopy_model.body(2)
    joints = third_body.joints
    assert len(joints) == 1
    assert joints[0] == go1_mujopy_model.joint(1)


def test_geoms(go1_mujopy_model):

    # Test for first body
    first_body = go1_mujopy_model.body(0)
    geoms = first_body.geoms
    assert len(geoms) == 0

    # Test for second body
    second_body = go1_mujopy_model.body(1)
    geoms = second_body.geoms
    assert len(geoms) == 9
    assert geoms[0] == go1_mujopy_model.geom(0)
    assert geoms[-1] == go1_mujopy_model.geom(8)
