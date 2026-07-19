#!/usr/bin/python3
"""Display product data from JSON or CSV files using Flask."""
import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def read_csv_file(filename):
    products = []
    with open(filename, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"]),
            })
    return products

def read_sql_file(filename):
    conn = sqlite3.connect(filename)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source == "json":
        product_list = read_json_file("products.json")
    elif source == "csv":
        product_list = read_csv_file("products.csv")
    elif source == "sql":
        product_list = read_sql_file("products.db") 
    else:
        return render_template("product_display.html", error="Wrong source", products=[])

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template("product_display.html", error="Product not found", products=[])

        product_list = [p for p in product_list if p["id"] == product_id]
        if not product_list:
            return render_template("product_display.html", error="Product not found", products=[])

    return render_template("product_display.html", products=product_list, error=None)


if __name__ == "__main__":
    app.run(debug=True, port=5000)