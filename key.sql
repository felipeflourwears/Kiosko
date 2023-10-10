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


