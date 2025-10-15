from flask import Blueprint, request, jsonify
from bson import ObjectId, errors as bson_errors
from config import db
from models.overlay_model import serialize_overlay

overlay_bp = Blueprint("overlay_bp", __name__, url_prefix="/api/overlays")

# Helper: validate overlay payload
def _validate_overlay_payload(data):
    if not isinstance(data, dict):
        return False, "Invalid JSON payload"
    # You can add more schema checks here
    return True, None

# 🟢 CREATE
@overlay_bp.route("/", methods=["POST"])
def create_overlay():
    data = request.get_json(silent=True)
    ok, err = _validate_overlay_payload(data)
    if not ok:
        return jsonify({"error": err}), 400

    new_overlay = {
        "type": data.get("type", "text"),        # text / image
        "content": data.get("content", ""),
        "position": data.get("position", {"x": 0, "y": 0}),
        "size": data.get("size", {"width": 100, "height": 50})
    }
    try:
        result = db.overlays.insert_one(new_overlay)
        return jsonify({"id": str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({"error": "Database insert failed", "details": str(e)}), 500

# 🟡 READ (all overlays)
@overlay_bp.route("/", methods=["GET"])
def get_overlays():
    try:
        overlays = list(db.overlays.find())
        return jsonify([serialize_overlay(o) for o in overlays])
    except Exception as e:
        return jsonify({"error": "Failed to fetch overlays", "details": str(e)}), 500

# 🔵 READ single overlay
@overlay_bp.route("/<overlay_id>", methods=["GET"])
def get_overlay(overlay_id):
    try:
        obj_id = ObjectId(overlay_id)
    except bson_errors.InvalidId:
        return jsonify({"error": "Invalid overlay id"}), 400

    overlay = db.overlays.find_one({"_id": obj_id})
    if not overlay:
        return jsonify({"error": "Overlay not found"}), 404
    return jsonify(serialize_overlay(overlay))

# 🔵 UPDATE
@overlay_bp.route("/<overlay_id>", methods=["PUT"])
def update_overlay(overlay_id):
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid or missing JSON body"}), 400

    # Build update dict only with provided keys to avoid setting fields to null
    allowed_keys = {"type", "content", "position", "size"}
    update_fields = {k: data[k] for k in data if k in allowed_keys}

    if not update_fields:
        return jsonify({"error": "No updatable fields provided"}), 400

    try:
        obj_id = ObjectId(overlay_id)
    except bson_errors.InvalidId:
        return jsonify({"error": "Invalid overlay id"}), 400

    try:
        result = db.overlays.update_one({"_id": obj_id}, {"$set": update_fields})
        if result.matched_count == 0:
            return jsonify({"error": "Overlay not found"}), 404
        return jsonify({"message": "Overlay updated successfully"})
    except Exception as e:
        return jsonify({"error": "Database update failed", "details": str(e)}), 500

# 🔴 DELETE
@overlay_bp.route("/<overlay_id>", methods=["DELETE"])
def delete_overlay(overlay_id):
    try:
        obj_id = ObjectId(overlay_id)
    except bson_errors.InvalidId:
        return jsonify({"error": "Invalid overlay id"}), 400

    try:
        result = db.overlays.delete_one({"_id": obj_id})
        if result.deleted_count == 0:
            return jsonify({"error": "Overlay not found"}), 404
        return jsonify({"message": "Overlay deleted successfully"})
    except Exception as e:
        return jsonify({"error": "Database delete failed", "details": str(e)}), 500
