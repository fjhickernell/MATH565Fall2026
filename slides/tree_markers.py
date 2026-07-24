"""Render named, course-specific tree-marker presets."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml


def _add_tree_components_to_path() -> None:
    search_roots = (
        Path(__file__).resolve().parent.parent,
        Path.cwd(),
        *Path.cwd().parents,
    )
    for repository_root in search_roots:
        components = (
            repository_root
            / "classlib"
            / "classlib"
            / "quarto"
            / "components"
        )
        if (components / "trees" / "__init__.py").is_file():
            component_path = str(components.resolve())
            if component_path not in sys.path:
                sys.path.insert(0, component_path)
            return
    raise FileNotFoundError("Cannot find the classlib tree components")


_add_tree_components_to_path()

from trees import render_tree  # noqa: E402


_PRESET_FILE = Path(__file__).with_name("tree-markers.yml")
_TOP_LEVEL_KEYS = {"version", "defaults", "markers"}
_RENDER_KEYS = {
    "tree",
    "groups",
    "labels",
    "group_headings",
    "show_group_headings",
    "mask",
    "width",
    "font_scale",
    "classes",
    "asset_base_url",
}


class TreeMarkerPresetError(ValueError):
    """Raised when the course tree-marker registry is invalid."""


def _mapping(value: Any, *, field: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise TreeMarkerPresetError(f"{field} must be a mapping")
    return value


def _render_options(value: Any, *, field: str) -> dict[str, Any]:
    options = _mapping(value, field=field)
    unknown = set(options) - _RENDER_KEYS
    if unknown:
        names = ", ".join(sorted(unknown))
        raise TreeMarkerPresetError(f"{field} has unknown fields: {names}")
    return options


def load_tree_marker_presets(
    path: str | Path = _PRESET_FILE,
) -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    """Load and validate the versioned course marker registry."""

    preset_path = Path(path)
    data = yaml.safe_load(preset_path.read_text(encoding="utf-8"))
    root = _mapping(data, field="tree-marker registry")

    unknown = set(root) - _TOP_LEVEL_KEYS
    if unknown:
        names = ", ".join(sorted(unknown))
        raise TreeMarkerPresetError(
            f"tree-marker registry has unknown fields: {names}"
        )
    if root.get("version") != 1:
        raise TreeMarkerPresetError("tree-marker registry version must be 1")

    defaults = _render_options(root.get("defaults"), field="defaults")
    markers_data = _mapping(root.get("markers"), field="markers")
    markers: dict[str, dict[str, Any]] = {}
    for name, options in markers_data.items():
        if not isinstance(name, str) or not name:
            raise TreeMarkerPresetError(
                "marker names must be nonempty strings"
            )
        markers[name] = _render_options(
            options,
            field=f"markers.{name}",
        )

    return defaults, markers


def render_tree_marker(name: str, **overrides: Any) -> str:
    """Render one named marker, optionally overriding its saved settings."""

    defaults, markers = load_tree_marker_presets()
    if name not in markers:
        raise TreeMarkerPresetError(f"undefined tree marker {name!r}")

    unknown = set(overrides) - _RENDER_KEYS
    if unknown:
        names = ", ".join(sorted(unknown))
        raise TreeMarkerPresetError(f"overrides have unknown fields: {names}")

    options = {**defaults, **markers[name], **overrides}
    try:
        tree = options.pop("tree")
    except KeyError as error:
        raise TreeMarkerPresetError(
            f"tree marker {name!r} does not define a tree"
        ) from error

    return render_tree(tree, **options)
