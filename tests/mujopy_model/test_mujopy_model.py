import numpy as np
import mujoco

from mujopy import MuJoPyModel
from mujopy.src.mujopy_model import Body, Joint, Geom


def test_body(go1_mujopy_model):

    # Get data
    first_body = go1_mujopy_model.body(0)
    last_body = go1_mujopy_model.body(13)

    # Assert
    assert isinstance(first_body, Body)
    assert first_body.id == 0
    assert last_body.id == 13


def test_joint(go1_mujopy_model):

    # Get data
    first_joint = go1_mujopy_model.joint(0)
    last_joint = go1_mujopy_model.joint(12)

    # Assert
    assert isinstance(first_joint, Joint)
    assert first_joint.id == 0
    assert last_joint.id == 12


def test_geom(go1_mujopy_model):

    # Get data
    first_geom = go1_mujopy_model.geom(0)
    last_geom = go1_mujopy_model.geom(54)

    # Assert
    assert isinstance(first_geom, Geom)
    assert first_geom.id == 0
    assert last_geom.id == 54


def test_bodies(go1_mujopy_model):

    # Get data
    bodies = go1_mujopy_model.bodies
    first_body = bodies[0]
    last_body = bodies[-1]

    # Assert
    assert isinstance(bodies, tuple)
    assert isinstance(first_body, Body)

    assert len(bodies) == 14
    assert first_body.id == 0
    assert last_body.id == 13


def test_joints(go1_mujopy_model):

    # Get data
    joints = go1_mujopy_model.joints
    first_joint = joints[0]
    last_joint = joints[-1]

    # Assert
    assert isinstance(joints, tuple)
    assert isinstance(first_joint, Joint)
    assert isinstance(last_joint, Joint)

    assert len(joints) == 13
    assert first_joint.id == 0
    assert last_joint.id == 12


def test_geoms(go1_mujopy_model):

    # Get data
    geoms = go1_mujopy_model.geoms
    first_geom = geoms[0]
    last_geom = geoms[-1]

    # Assert
    assert isinstance(geoms, tuple)
    assert isinstance(first_geom, Geom)
    assert isinstance(last_geom, Geom)

    assert len(geoms) == 55
    assert first_geom.id == 0
    assert last_geom.id == 54


def test_register_body_property(go1_mujopy_model):

    def _body_is_not_root(body: Body) -> bool:
        return int(np.asarray(body.mujoco_view.parentid).item()) != body.id

    MuJoPyModel.register_body_property("body_is_not_root", _body_is_not_root)

    root_body = go1_mujopy_model.body(0)
    not_root_body = go1_mujopy_model.body(1)

    assert not root_body.body_is_not_root
    assert not_root_body.body_is_not_root


def test_register_joint_property(go1_mujopy_model):

    def _name(joint: Joint) -> str:
        raw_name = joint.mujoco_view.name
        name = raw_name if raw_name and raw_name.strip() else "notset"
        return name

    MuJoPyModel.register_joint_property("name", _name)

    second_joint = go1_mujopy_model.joint(1)

    assert second_joint.name == "FR_hip_joint"


def test_register_geom_property(go1_mujopy_model):

    def _geom_is_not_mesh(geom: Geom) -> bool:
        geom_type = mujoco.mjtGeom(int(np.asarray(geom.mujoco_view.type).item()))
        return geom_type != mujoco.mjtGeom.mjGEOM_MESH

    MuJoPyModel.register_geom_property("geom_is_not_mesh", _geom_is_not_mesh)

    mesh_geom = go1_mujopy_model.geom(9)
    not_mesh_geom = go1_mujopy_model.geom(10)

    assert not mesh_geom.geom_is_not_mesh
    assert not_mesh_geom.geom_is_not_mesh
