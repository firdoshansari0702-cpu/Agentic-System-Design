import sqlite3

conn = sqlite3.connect('foodrush.db')
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id   INTEGER PRIMARY KEY,
    customer_name TEXT,
    city          TEXT
);

CREATE TABLE IF NOT EXISTS restaurants (
    restaurant_id   INTEGER PRIMARY KEY,
    restaurant_name TEXT,
    city            TEXT,
    cuisine         TEXT
);

CREATE TABLE IF NOT EXISTS orders (
    order_id      INTEGER PRIMARY KEY,
    customer_id   INTEGER,
    restaurant_id INTEGER,
    order_amount  REAL,
    order_date    TEXT,
    status        TEXT,
    FOREIGN KEY (customer_id)   REFERENCES customers(customer_id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
);

INSERT OR IGNORE INTO customers VALUES
(1, 'Arjun Sharma',  'Delhi'),
(2, 'Priya Mehta',   'Mumbai'),
(3, 'Kiran Rao',     'Delhi'),
(4, 'Sneha Patel',   'Bangalore'),
(5, 'Rahul Nair',    'Mumbai'),
(6, 'Aisha Khan',    'Delhi');

INSERT OR IGNORE INTO restaurants VALUES
(1, 'Spice Garden', 'Delhi',     'Indian'),
(2, 'Burger Hub',   'Delhi',     'Fast Food'),
(3, 'Pizza Palace', 'Mumbai',    'Italian'),
(4, 'Dosa Corner',  'Bangalore', 'South Indian'),
(5, 'Wok Express',  'Delhi',     'Chinese');

INSERT OR IGNORE INTO orders VALUES
(1,  1, 1, 450.0, '2024-01-10', 'delivered'),
(2,  1, 2, 320.0, '2024-01-15', 'delivered'),
(3,  1, 5, 580.0, '2024-02-01', 'delivered'),
(4,  2, 3, 900.0, '2024-01-20', 'delivered'),
(5,  2, 3, 750.0, '2024-02-05', 'cancelled'),
(6,  3, 1, 400.0, '2024-01-25', 'delivered'),
(7,  3, 2, 280.0, '2024-02-10', 'delivered'),
(8,  3, 1, 500.0, '2024-02-15', 'delivered'),
(9,  4, 4, 350.0, '2024-01-30', 'delivered'),
(10, 5, 3, 620.0, '2024-02-20', 'pending'),
(11, 1, 1, 410.0, '2024-03-01', 'delivered'),
(12, 3, 5, 680.0, '2024-03-05', 'delivered');
""")

conn.commit()
print("Database setup complete.")
# Task 1: Restaurant Revenue Report
print("\n--- Task 1: Restaurant Revenue Report ---")
cursor.execute("""
SELECT r.restaurant_name, COUNT(o.order_id), SUM(o.order_amount)
FROM restaurants r
JOIN orders o ON r.restaurant_id = o.restaurant_id
WHERE o.status = 'delivered'
GROUP BY r.restaurant_id
HAVING COUNT(o.order_id) > 2
ORDER BY SUM(o.order_amount) DESC;
""")
for row in cursor.fetchall():
    print(row)

# Task 2: Full Customer Order Summary
print("\n--- Task 2: Full Customer Order Summary ---")
cursor.execute("""
SELECT c.customer_name, c.city, COUNT(o.order_id), COALESCE(SUM(o.order_amount), 0.0)
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY SUM(o.order_amount) DESC;
""")
for row in cursor.fetchall():
    print(row)

# Task 3: Delhi High-Spenders
print("\n--- Task 3: Delhi High-Spenders ---")
cursor.execute("""
SELECT c.customer_name, COUNT(o.order_id), SUM(o.order_amount)
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE c.city = 'Delhi'
GROUP BY c.customer_id
HAVING COUNT(o.order_id) > 1 AND SUM(o.order_amount) > 1000
ORDER BY SUM(o.order_amount) DESC;
""")
for row in cursor.fetchall():
    print(row)

# Task 4: Multi-Table Spend Breakdown
print("\n--- Task 4: Multi-Table Spend Breakdown ---")
cursor.execute("""
SELECT c.customer_name, r.restaurant_name, COUNT(o.order_id), SUM(o.order_amount)
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN restaurants r ON o.restaurant_id = r.restaurant_id
GROUP BY c.customer_id, r.restaurant_id
HAVING SUM(o.order_amount) > 500
ORDER BY c.customer_name ASC, SUM(o.order_amount) DESC;
""")
for row in cursor.fetchall():
    print(row)

conn.close()


