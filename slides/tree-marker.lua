-- Expand a slide's tree-marker attribute with the existing Python renderer.

local filter_directory = pandoc.path.directory(PANDOC_SCRIPT_FILE)
local renderer = pandoc.path.join({ filter_directory, "tree_markers.py" })

function Header(header)
  local marker_name = header.attributes["tree-marker"]
  if marker_name == nil then
    return nil
  end

  local ok, marker_html = pcall(
    pandoc.pipe,
    "python",
    { renderer, marker_name },
    ""
  )
  if not ok then
    error(
      "Could not render tree marker "
        .. string.format("%q", marker_name)
        .. " from slides/tree-markers.yml:\n"
        .. tostring(marker_html),
      0
    )
  end

  return {
    header,
    pandoc.RawBlock("html", marker_html),
  }
end
