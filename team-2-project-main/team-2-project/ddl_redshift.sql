DROP TABLE IF EXISTS cafe_data.customer CASCADE;
CREATE TABLE cafe_data.customer (
    customer_id varchar(255) NOT NULL DEFAULT 0,
    customer_name varchar(255) NOT NULL DEFAULT 0,
    CONSTRAINT customer_pkey PRIMARY KEY (customer_id)
);


DROP TABLE IF EXISTS cafe_data.order_item CASCADE;
CREATE TABLE cafe_data.order_item (
    order_id varchar(255) NOT NULL DEFAULT 0,
    product_id varchar(255) NOT NULL DEFAULT 0,
    quantity int NOT NULL DEFAULT 0,
    order_item_id varchar(255) NOT NULL DEFAULT 0,
    CONSTRAINT order_item_pkey PRIMARY KEY (order_item_id)
);


DROP TABLE IF EXISTS cafe_data.orders CASCADE;
CREATE TABLE cafe_data.orders (
    order_id varchar(255) NOT NULL DEFAULT 0,
    timestamp timestamp NOT NULL DEFAULT SYSDATE,
    store_id varchar(255) NOT NULL DEFAULT 0,
    customer_id varchar(255) NOT NULL DEFAULT 0,
    total_price double precision NOT NULL DEFAULT 0,
    payment_type_id varchar(255) NOT NULL DEFAULT 0,
    CONSTRAINT orders_pkey PRIMARY KEY (order_id)
);


DROP TABLE IF EXISTS cafe_data.payment_type CASCADE;
CREATE TABLE cafe_data.payment_type (
    payment_type_id varchar(255) NOT NULL DEFAULT 0,
    payment_type_name varchar(255) NOT NULL DEFAULT 0,
    CONSTRAINT payment_type_pkey PRIMARY KEY (payment_type_id)
);


DROP TABLE IF EXISTS cafe_data.product CASCADE;
CREATE TABLE cafe_data.product (
    product_id varchar(255) NOT NULL DEFAULT 0,
    product_name varchar(255) NOT NULL DEFAULT 0,
    product_size_id varchar(255) NOT NULL DEFAULT 0,
    product_flavour_id varchar(255) NOT NULL DEFAULT 0,
    product_price double precision NOT NULL DEFAULT 0,
    CONSTRAINT product_pkey PRIMARY KEY (product_id)
);


DROP TABLE IF EXISTS cafe_data.product_flavour CASCADE;
CREATE TABLE cafe_data.product_flavour (
    product_flavour_id varchar(255) NOT NULL DEFAULT 0,
    product_flavour_name varchar(255) NOT NULL DEFAULT 0,
    CONSTRAINT product_flavour_pkey PRIMARY KEY (product_flavour_id)
);


DROP TABLE IF EXISTS cafe_data.product_size CASCADE;
CREATE TABLE cafe_data.product_size (
    product_size_id varchar(255) NOT NULL DEFAULT 0,
    product_size_name varchar(255) NOT NULL DEFAULT 0,
    CONSTRAINT product_size_pkey PRIMARY KEY (product_size_id)
);


DROP TABLE IF EXISTS cafe_data.store CASCADE;
CREATE TABLE cafe_data.store (
    store_id varchar(255) NOT NULL DEFAULT 0,
    store_name varchar(255) NOT NULL DEFAULT 0,
    CONSTRAINT store_pkey PRIMARY KEY (store_id)
);

-- ALTER TABLE cafe_data.customer ADD PRIMARY KEY (customer_id);
-- ALTER TABLE cafe_data.order_item ADD PRIMARY KEY (order_item_id);
-- ALTER TABLE cafe_data.orders ADD PRIMARY KEY (orders_id);
-- ALTER TABLE cafe_data.payment_type ADD PRIMARY KEY (payment_type_id);
-- ALTER TABLE cafe_data.product_flavour ADD PRIMARY KEY (product_flavour_id);
-- ALTER TABLE cafe_data.product_size ADD PRIMARY KEY (product_size_id);
-- ALTER TABLE cafe_data.store ADD PRIMARY KEY (store_id);

ALTER TABLE cafe_data.order_item ADD CONSTRAINT order_id_fk FOREIGN KEY (order_id) REFERENCES cafe_data.orders(order_id) NOT DEFERRABLE;
ALTER TABLE cafe_data.order_item ADD CONSTRAINT product_id_fk FOREIGN KEY (product_id) REFERENCES cafe_data.product(product_id) NOT DEFERRABLE;

ALTER TABLE cafe_data.orders ADD CONSTRAINT customer_id_fk FOREIGN KEY (customer_id) REFERENCES cafe_data.customer(customer_id) NOT DEFERRABLE;
ALTER TABLE cafe_data.orders ADD CONSTRAINT payment_type_id_fk FOREIGN KEY (payment_type_id) REFERENCES cafe_data.payment_type(payment_type_id) NOT DEFERRABLE;
ALTER TABLE cafe_data.orders ADD CONSTRAINT store_id_fk FOREIGN KEY (store_id) REFERENCES cafe_data.store(store_id) NOT DEFERRABLE;

ALTER TABLE cafe_data.product ADD CONSTRAINT product_flavour_id_fk FOREIGN KEY (product_flavour_id) REFERENCES cafe_data.product_flavour(product_flavour_id) NOT DEFERRABLE;
ALTER TABLE cafe_data.product ADD CONSTRAINT product_size_id_fk FOREIGN KEY (product_size_id) REFERENCES cafe_data.product_size(product_size_id) NOT DEFERRABLE;