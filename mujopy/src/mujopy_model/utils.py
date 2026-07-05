class MuJoPyModelItem:
    """Base wrapper that forwards attribute access to the underlying MuJoCo view."""

    def __init__(self, mujoco_view):
        self.mujoco_view = mujoco_view

    def __getattr__(self, attr):
        try:
            return getattr(self.mujoco_view, attr)
        except AttributeError as exc:
            raise AttributeError(
                f"{type(self).__name__} has no attribute {attr!r}"
            ) from exc
