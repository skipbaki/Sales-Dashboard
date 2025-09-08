DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
  customer_id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  city TEXT,
  email TEXT
);

CREATE TABLE products (
  product_id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  category TEXT,
  price REAL
);

CREATE TABLE orders (
  order_id SERIAL PRIMARY KEY,
  customer_id INTEGER,
  order_date TEXT,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
  order_item_id SERIAL PRIMARY KEY,
  order_id INTEGER,
  product_id INTEGER,
  quantity INTEGER,
  unit_price REAL,
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE payments (
  payment_id SERIAL PRIMARY KEY,
  order_id INTEGER,
  amount REAL,
  payment_date TEXT,
  method TEXT,
  FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

INSERT INTO customers (name, city, email) VALUES ('Baki', 'Bengaluru', 'baki@example.com');
INSERT INTO customers (name, city, email) VALUES ('Partha', 'Assam', 'partha@example.com');
INSERT INTO customers (name, city, email) VALUES ('Anurag', 'Bengaluru', 'anurag@example.com');
INSERT INTO customers (name, city, email) VALUES ('Aravind', 'Hyderabad', 'aravind@example.com');
INSERT INTO customers (name, city, email) VALUES ('Abdur', 'Mumbai', 'abdur@example.com');

INSERT INTO products (name, category, price) VALUES ('Keyboard', 'Accessories', 29.99);
INSERT INTO products (name, category, price) VALUES ('Mouse', 'Accessories', 12.50);
INSERT INTO products (name, category, price) VALUES ('Monitor', 'Electronics', 149.99);
INSERT INTO products (name, category, price) VALUES ('USB-C Cable', 'Accessories', 9.99);
INSERT INTO products (name, category, price) VALUES ('Webcam', 'Electronics', 59.99);

INSERT INTO orders (customer_id, order_date) VALUES (1, '2025-06-20');
INSERT INTO orders (customer_id, order_date) VALUES (2, '2025-06-21');
INSERT INTO orders (customer_id, order_date) VALUES (1, '2025-07-01');
INSERT INTO orders (customer_id, order_date) VALUES (3, '2025-07-15');
INSERT INTO orders (customer_id, order_date) VALUES (4, '2025-08-05');
INSERT INTO orders (customer_id, order_date) VALUES (5, '2025-08-20');
INSERT INTO orders (customer_id, order_date) VALUES (1, '2025-09-01');

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (1,1,1,29.99);
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (1,2,2,12.50);
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (2,3,1,149.99);
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (3,2,1,12.50);
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (3,4,3,9.99);
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (4,5,1,59.99);
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (5,1,2,29.99);
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (6,3,1,149.99);
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (7,2,1,12.50);

INSERT INTO payments (order_id, amount, payment_date, method) VALUES (1, 54.99, '2025-06-20', 'card');
INSERT INTO payments (order_id, amount, payment_date, method) VALUES (2, 149.99, '2025-06-21', 'netbanking');
INSERT INTO payments (order_id, amount, payment_date, method) VALUES (3, 42.47, '2025-07-01', 'card');
INSERT INTO payments (order_id, amount, payment_date, method) VALUES (4, 59.99, '2025-07-15', 'upi');
INSERT INTO payments (order_id, amount, payment_date, method) VALUES (5, 59.98, '2025-08-05', 'cash');
INSERT INTO payments (order_id, amount, payment_date, method) VALUES (6, 149.99, '2025-08-20', 'cash');
INSERT INTO payments (order_id, amount, payment_date, method) VALUES (7, 12.50, '2025-09-01', 'upi');
