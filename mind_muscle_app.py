from app import app
import os

if __name__ == "__main__":
    port = os.environ.get("PORT") or 5000
    app.run(host="0.0.0.0", port=port)
