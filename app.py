from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>🏠 Home</h2>
    <p>Welcome to the Flask Gateway Demo App</p>
    <ul>
        <li><a href="/products">Products</a></li>
        <li><a href="/orders">Orders</a></li>
        <li><a href="/support">Support</a></li>
    </ul>
    """

@app.route("/products")
def products():
    return """
    <h2>🛒 Products</h2>
    <ul>
        <li>Laptop – ₹70,000</li>
        <li>Headphones – ₹3,000</li>
        <li>Mouse – ₹1,200</li>
    </ul>
    """

@app.route("/orders")
def orders():
    return """
    <h2>📦 Orders</h2>
    <ul>
        <li>Order #101 – Delivered</li>
        <li>Order #102 – In Transit</li>
        <li>Order #103 – Processing</li>
    </ul>
    """

@app.route("/support")
def support():
    return """
    <h2>🎧 Support</h2>
    <p>Email: support@example.com</p>
    """

@app.route("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

