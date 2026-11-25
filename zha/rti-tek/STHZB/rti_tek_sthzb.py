"""Minimal ZHA identification Quirk for Rti-Tek STHZB."""

from zhaquirks.builder import QuirkBuilder


(
    QuirkBuilder("Rti-Tek", "STHZB")
    .add_to_registry()
)
