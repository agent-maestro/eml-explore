"""Shim sanity test — verify the deprecation re-export works."""
import pytest


def test_shim_imports_with_deprecation_warning():
    with pytest.warns(DeprecationWarning, match="eml-explore is deprecated"):
        import eml_explore
    assert hasattr(eml_explore, "__version__")
    assert eml_explore.__version__ == "0.2.0"
