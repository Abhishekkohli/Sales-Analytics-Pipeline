-- Fact table for sales
CREATE TABLE fact_sales (
    order_id SERIAL PRIMARY KEY,
    order_date DATE,
    customer_id INT,
    product_id INT,
    quantity INT,
    total_price DECIMAL
);

-- Dimension tables
CREATE TABLE dim_customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255),
    customer_region VARCHAR(100)
);

CREATE TABLE dim_product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
    product_category VARCHAR(100),
    unit_price DECIMAL
);

CREATE TABLE dim_time (
    date DATE PRIMARY KEY,
    year INT,
    month INT,
    day INT,
    weekday VARCHAR(50)
);
