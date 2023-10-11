CREATE DATABASE kioskopop;
USE kioskopop;

CREATE TABLE IF NOT EXISTS categoryFood (
    idCategory INT AUTO_INCREMENT PRIMARY KEY,
    nameCategory VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS foodMenu (
    idFood INT AUTO_INCREMENT PRIMARY KEY,    
    nameFood VARCHAR(50) NOT NULL,
    priceFood DECIMAL(10, 2) NOT NULL,
    imageUrl VARCHAR(255) NOT NULL,
    descriptionFood VARCHAR(255) NOT NULL,
    available BOOLEAN NOT NULL,
    idCategory INT NOT NULL,
    FOREIGN KEY (idCategory) REFERENCES categoryFood (idCategory)
);

CREATE TABLE IF NOT EXISTS client (
    idClient INT AUTO_INCREMENT PRIMARY KEY,
    nameClient VARCHAR(50) NOT NULL, 
    numberTable VARCHAR(5) NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    idOrder INT AUTO_INCREMENT PRIMARY KEY,
    idClient INT NOT NULL,
    idFood INT NOT NULL,
    quantity INT NOT NULL,
    descriptionOrd VARCHAR(255) NOT NULL,
    dateDay DATE NOT NULL,
    total DECIMAL(20, 2) NOT NULL,
    FOREIGN KEY (idFood) REFERENCES foodMenu(idFood), -- Corrección aquí
    FOREIGN KEY (idClient) REFERENCES client(idClient)
);

CREATE TABLE IF NOT EXISTS user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(20),
    password CHAR(102),
    fullname VARCHAR(50)
);



-- Insertar datos ficticios en la tabla "categoryFood"
INSERT INTO categoryFood (nameCategory)
VALUES
('Marisco'),
('Postres'),
('Refrescos'),
('Helados'),
('Desayunos'),
('Bebidas Calientes'),
('Sopas'),
('Platos Principales'),
('Aperitivos'),
('Especiales del Chef'),
('Bebidas Alcohólicas'),
('Vegetariano'),
('Parrilla'),
('Pescado');

-- Insertar datos ficticios en la tabla "foodMenu"
INSERT INTO foodMenu (nameFood, priceFood, imageUrl, descriptionFood, available, idCategory)
VALUES
('Paella de Marisco', 19.99, 'paella.jpg', 'Deliciosa paella de mariscos con arroz y azafrán', 1, 1),
('Tiramisú', 6.49, 'tiramisu.jpg', 'Postre italiano con capas de café y mascarpone', 1, 2),
('Refresco de Limón', 2.99, 'limon.jpg', 'Refresco de limón fresco y burbujeante', 1, 3),
('Helado de Vainilla', 4.99, 'helado.jpg', 'Helado cremoso de vainilla con jarabe de chocolate', 1, 4),
('Desayuno Continental', 8.99, 'desayuno.jpg', 'Desayuno completo con croissants y café', 1, 5),
('Café Espresso', 2.49, 'cafe.jpg', 'Taza de café espresso fuerte', 1, 6),
('Sopa de Tomate', 5.99, 'sopa.jpg', 'Sopa de tomate casera con crutones', 1, 7),
('Filete a la Parrilla', 14.99, 'filete.jpg', 'Filete de res a la parrilla con papas fritas', 1, 8),
('Aros de Cebolla', 4.49, 'aros.jpg', 'Aros de cebolla crujientes con salsa de mostaza', 1, 9),
('Plato del Chef', 22.99, 'chef.jpg', 'Plato exclusivo del chef con ingredientes de temporada', 1, 10),
('Vino Tinto', 15.99, 'vino.jpg', 'Botella de vino tinto de la casa', 1, 11),
('Ensalada César', 7.49, 'ensalada.jpg', 'Ensalada César clásica con pollo a la parrilla', 1, 12),
('Salmón a la Parrilla', 16.99, 'salmon.jpg', 'Filete de salmón a la parrilla con espárragos', 1, 13);


-- Insertar 10 registros de clientes en la tabla "client"
INSERT INTO client (nameClient, numberTable)
VALUES
('Cliente 1', 'Table 1'),
('Cliente 2', 'Table 2'),
('Cliente 3', 'Table 3'),
('Cliente 4', 'Table 4'),
('Cliente 5', 'Table 5'),
('Cliente 6', 'Table 6'),
('Cliente 7', 'Table 7'),
('Cliente 8', 'Table 8'),
('Cliente 9', 'Table 9'),
('Cliente 10', 'Table 10');

-- Insertar datos de pedidos coherentes en la tabla "orders"
INSERT INTO orders (idClient, idFood, quantity, descriptionOrd, dateDay, total, served)
VALUES
(1, 6, 2, 'Pedido de Paella de Marisco', '2023-10-10', 39.98, 1),
(2, 7, 1, 'Tiramisú de postre', '2023-10-10', 6.49, 1),
(3, 8, 2, 'Refresco de Limón', '2023-10-10', 5.98, 0),
(1, 9, 1, 'Helado de Vainilla', '2023-10-11', 4.99, 1),
(4, 10, 2, 'Desayuno Continental', '2023-10-11', 17.98, 1),
(1, 11, 1, 'Café Espresso', '2023-10-12', 2.49, 0),
(2, 12, 3, 'Sopa de Tomate', '2023-10-12', 17.97, 1),
(3, 13, 1, 'Filete a la Parrilla', '2023-10-13', 14.99, 1),
(4, 14, 2, 'Aros de Cebolla', '2023-10-13', 8.98, 0),
(1, 15, 1, 'Plato del Chef', '2023-10-14', 22.99, 1),
(2, 16, 1, 'Vino Tinto', '2023-10-14', 15.99, 1),
(3, 17, 2, 'Ensalada César', '2023-10-15', 14.98, 0),
(4, 18, 1, 'Salmón a la Parrilla', '2023-10-15', 16.99, 1);

