"""eml-explore — DEPRECATED.

This package has been consolidated into ``eml-cost`` as the
:mod:`eml_cost.explore` subpackage. The standalone distribution
will receive no further updates.

Migration:

    pip uninstall eml-explore
    pip install "eml-cost[explore]>=0.15.0"

    # then change your imports:
    # OLD:  from eml_explore import X
    # NEW:  from eml_cost.explore import X

This shim re-exports the public API from ``eml_cost.explore`` so
existing code keeps working while you migrate.
"""
from __future__ import annotations

import warnings as _warnings

_warnings.warn(
    "eml-explore is deprecated. Use `pip install \"eml-cost[explore]\"` "
    "instead. The functionality is now available at eml_cost.explore. "
    "This package will receive no further updates.",
    DeprecationWarning,
    stacklevel=2,
)

from eml_cost import explore as _impl  # noqa: E402

# Mirror the upstream public API so `from eml_explore import X` keeps
# working. We deliberately avoid `from eml_cost.explore import *`
# to keep `__all__` faithful to whatever the new home declares.
__all__ = list(getattr(_impl, "__all__", []))
for _name in __all__:
    globals()[_name] = getattr(_impl, _name)
del _name, _impl

# Override any upstream __version__ — this shim has its own version line.
__version__ = "0.2.0"
