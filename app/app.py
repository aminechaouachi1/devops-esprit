from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUESTS = Counter(
    "app_http_requests_total",
    "Nombre de requetes HTTP vers l'application"
)

@app.get("/")
def home():
    REQUESTS.inc()
    return {"status": "ok", "message": "Application DevOps ESPRIT"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
