def test_body(go1_mujopy_model):

    # Test for last geom
    first_geom = go1_mujopy_model.geom(1)
    body = first_geom.body
    assert body == go1_mujopy_model.body(1)

    # Test for last geom
    last_geom = go1_mujopy_model.geom(54)
    body = last_geom.body
    assert body == go1_mujopy_model.body(13)
