"""Contract tests for the minimal Rti-Tek STHZB identification Quirk."""

import importlib.util
import sys
from pathlib import Path
from types import ModuleType


MODULE_PATH = Path(__file__).parents[1] / "rti_tek_sthzb.py"


def _load_with_quirk_builder_stub(monkeypatch) -> list[tuple[object, ...]]:
    calls: list[tuple[object, ...]] = []

    class QuirkBuilder:
        def __init__(self, manufacturer: str, model: str) -> None:
            calls.append(("create", manufacturer, model))

        def add_to_registry(self) -> None:
            calls.append(("register",))

    package = ModuleType("zhaquirks")
    builder_module = ModuleType("zhaquirks.builder")
    builder_module.QuirkBuilder = QuirkBuilder
    monkeypatch.setitem(sys.modules, "zhaquirks", package)
    monkeypatch.setitem(sys.modules, "zhaquirks.builder", builder_module)

    spec = importlib.util.spec_from_file_location("rti_tek_sthzb", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return calls


def test_import_registers_only_the_exact_device_match(monkeypatch) -> None:
    """The identification package must not add capabilities or entity mappings."""
    calls = _load_with_quirk_builder_stub(monkeypatch)

    assert calls == [
        ("create", "Rti-Tek", "STHZB"),
        ("register",),
    ]
