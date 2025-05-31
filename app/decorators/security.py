from functools import wraps
from flask import current_app, jsonify, request
import logging
import hashlib
import hmac

def validate_signature(payload, signature):
    """
    Validate the incoming payload's signature against our expected signature
    """
    app_secret = current_app.config.get("APP_SECRET")
    if not app_secret:
        logging.error("APP_SECRET not found in Flask config")
        return False

    expected_signature = hmac.new(
        key=app_secret.encode("utf-8"),
        msg=payload,
        digestmod=hashlib.sha256,
    ).hexdigest()

    return hmac.compare_digest(expected_signature, signature)


def signature_required(f):
    """
    Decorator to ensure that the incoming requests to our webhook are valid and signed with the correct signature.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        signature_header = request.headers.get("X-Hub-Signature-256", "")
        signature = signature_header.replace("sha256=", "")

        logging.info(f"Received Signature: {signature}")
        logging.info(f"APP_SECRET from config: {current_app.config.get('APP_SECRET')}")

        if not validate_signature(request.get_data(), signature):
            logging.info("Signature verification failed!")
            return jsonify({"status": "error", "message": "Invalid signature"}), 403

        return f(*args, **kwargs)

    return decorated_function
