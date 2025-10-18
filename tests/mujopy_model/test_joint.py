def test_body(go1_mujopy_model):

    # Test for second joint
    second_joint = go1_mujopy_model.joint(1)
    body = second_joint.body
    assert body == go1_mujopy_model.body(2)

    # Test for third joint
    third_joint = go1_mujopy_model.joint(2)
    body = third_joint.body
    assert body == go1_mujopy_model.body(3)
