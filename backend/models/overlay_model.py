from bson import ObjectId

def serialize_overlay(overlay):
    """Convert MongoDB overlay document into JSON-serializable format."""
    if not overlay:
        return {}

    return {
        "id": str(overlay.get("_id", "")),
        "type": overlay.get("type", "text"),
        "content": overlay.get("content", ""),
        "position": overlay.get("position", {"x": 0, "y": 0}),
        "size": overlay.get("size", {"width": 100, "height": 50})
    }
