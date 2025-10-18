import pathlib
import pytest
from mujopy import MuJoPyModel
from mujopy import RobotGraph


@pytest.fixture
def go1_mujopy_model():
    xml_path = pathlib.Path("./tests/data/unitree_go1/go1.xml")
    model = MuJoPyModel(
        xml_path=str(xml_path), include_world_body=True, include_free_joints=True
    )
    model.register_default_properties()
    return model


@pytest.fixture
def go1_robot_graph():
    xml_path = pathlib.Path("./tests/data/unitree_go1/go1.xml")
    feature_config_path = pathlib.Path("./tests/data/test_feature_conf.yml")
    graph = RobotGraph(xml_path=str(xml_path), feature_config_path=feature_config_path)
    return graph
