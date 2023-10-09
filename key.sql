CREATE TABLE IF NOT EXISTS food (
    idFood INT AUTO_INCREMENT PRIMARY KEY,
    nameFood VARCHAR(50) NOT NULL,
    priceFood DECIMAL(10, 2) NOT NULL,
    descriptionFood VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS orders (
    idOrder INT AUTO_INCREMENT PRIMARY KEY,
    buyerName VARCHAR(100),
    tableNumber INT NOT NULL,
    idFood INT NOT NULL,
    quantity INT NOT NULL,
    descFood VARCHAR(255) NOT NULL,
    served BOOLEAN NOT NULL,
    FOREIGN KEY (idFood) REFERENCES food(idFood)
);


