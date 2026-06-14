#!/bin/usr/python3



from flask_jwt_extended import JWTManager

  app = Flask(__name__)
  jwt = JWTManager(app)


  @jwt.unauthorized_loader
  def handle_unauthorized_error(err):
      return jsonify({"error": "Missing or invalid token"}), 401

  @jwt.invalid_token_loader
  def handle_invalid_token_error(err):
      return jsonify({"error": "Invalid token"}), 401

  @jwt.expired_token_loader
  def handle_expired_token_error(err):
      return jsonify({"error": "Token has expired"}), 401

  @jwt.revoked_token_loader
  def handle_revoked_token_error(err):
      return jsonify({"error": "Token has been revoked"}), 401

  @jwt.needs_fresh_token_loader
  def handle_needs_fresh_token_error(err):
      return jsonify({"error": "Fresh token required"}), 401

if __name__ == "main":
    app.run()
