CREATE TABLE roles (
    idRol SERIAL PRIMARY KEY,
    rol VARCHAR(20) NOT NULL
);

INSERT INTO roles (rol) VALUES
    ('Administrador'),
    ('Vendedor');


CREATE TABLE user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(20),
    password CHAR(102),
    fullname VARCHAR(50),
    idRol INT,
    FOREIGN KEY (idRol) REFERENCES roles(idRol)
);


INSERT INTO user (username, password, fullname, idRol) VALUES ('admin', 'pbkdf2:sha256:600000$1BuUwwsYKWlllAYx$2a864776cd5c5bb2e007cd6f95da1a422cb9e5a57f1faa4e6c4078d11964e280', 'Administrador LF', 1);
INSERT INTO user (username, password, fullname, idRol) VALUES ('admin', 'pbkdf2:sha256:600000$1BuUwwsYKWlllAYx$2a864776cd5c5bb2e007cd6f95da1a422cb9e5a57f1faa4e6c4078d11964e280', 'Vendedor LF', 2);

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
    numberTable VARCHAR(5) NOT NULL,
    userCode VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    idOrder INT AUTO_INCREMENT PRIMARY KEY,
    idFood INT NOT NULL,
    quantity INT NOT NULL,
    descriptionOrd VARCHAR(255) NOT NULL,
    dateDay DATE NOT NULL,
    total DECIMAL(20, 2) NOT NULL,
    served BOOLEAN NOT NULL,
    userCode VARCHAR(50) NOT NULL,
    FOREIGN KEY (idFood) REFERENCES foodMenu(idFood),
    FOREIGN KEY (userCode) REFERENCES client(userCode)
);


INSERT INTO `categoryfood` (`idCategory`, `nameCategory`) VALUES
(1, 'Chicken'),
(2, 'Beef'),
(3, 'Pork'),
(4, 'Seafood'),
(5, 'Appetizers'),
(6, 'Salads'),
(7, 'Soups'),
(9, 'Vegetarian'),
(10, 'Soft Drinks'),
(11, 'Hot Drinks '),
(12, 'Beer');

--
-- Disparadores `categoryfood`
--
DELIMITER $$
CREATE TRIGGER `delete category` BEFORE DELETE ON `categoryfood` FOR EACH ROW DELETE FROM foodmenu WHERE idCategory = OLD.idCategory
$$
DELIMITER ;

--
-- Disparadores `client`
--
DELIMITER $$
CREATE TRIGGER `delete client` BEFORE DELETE ON `client` FOR EACH ROW DELETE FROM orders WHERE idClient = OLD.idClient
$$
DELIMITER ;

INSERT INTO `foodmenu` (`idFood`, `nameFood`, `priceFood`, `imageUrl`, `descriptionFood`, `available`, `idCategory`) VALUES
(1, 'Grilled Chicken Breast', 15.99, 'http://192.168.0.155/media/img/pop.jpg', 'Succulent grilled chicken breast seasoned to perfection, served with a choice of sides', 1, 1),
(2, 'Chicken Alfredo Pasta', 17.99, 'http://192.168.0.155/media/img/pop.jpg', 'Creamy Alfredo pasta with tender pieces of grilled chicken, garnished with fresh parsley', 1, 1),
(3, 'Spicy Buffalo Wings', 12.99, 'http://192.168.0.155/media/img/pop.jpg', 'Crispy chicken wings coated in a tangy and spicy buffalo sauce, served with blue cheese dressing.', 1, 1),
(4, 'Filet Mignon', 24.99, 'http://192.168.0.155/media/img/pop.jpg', 'Juicy and tender filet mignon cooked to your liking, served with garlic mashed potatoes and seasonal vegetables.', 1, 2),
(5, 'Beef Stir-Fry', 18.99, 'http://192.168.0.155/media/img/pop.jpg', 'Sliced beef stir-fried with colorful vegetables in a savory sauce, served over steamed rice.', 1, 2),
(6, 'Beef Tacos', 14.99, 'http://192.168.0.155/media/img/pop.jpg', 'Flavorful shredded beef seasoned with Mexican spices, served in warm tortillas with salsa and guacamole.', 1, 2),
(7, 'Pork Ribs', 19.99, 'http://192.168.0.155/media/img/pop.jpg', 'Tender and succulent pork ribs slow-cooked to perfection, glazed with a smoky barbecue sauce.', 1, 3),
(8, 'Pork Chops', 16.99, 'http://192.168.0.155/media/img/pop.jpg', 'Grilled pork chops seasoned with a blend of herbs and spices, served with sweet potato wedges and steamed vegetables.', 1, 3),
(9, 'Pulled Pork Sandwich', 13.99, 'http://192.168.0.155/media/img/pop.jpg', 'Slow-cooked pulled pork seasoned with a special barbecue rub, served in a bun with coleslaw.', 1, 3),
(10, 'Grilled Salmon', 20.99, 'http://192.168.0.155/media/img/pop.jpg', 'Fresh Atlantic salmon fillet grilled to perfection, accompanied by lemon-butter sauce and steamed asparagus.', 1, 4),
(11, 'Shrimp Scampi', 19.99, 'http://192.168.0.155/media/img/pop.jpg', 'Succulent shrimp sautéed in garlic, butter, and white wine, served over a bed of linguine.', 1, 4),
(12, 'Seafood Paella', 22.99, 'http://192.168.0.155/media/img/pop.jpg', ' Spanish-style paella with a medley of seafood, including shrimp, mussels, and clams, infused with aromatic saffron rice.', 1, 4),
(13, 'Stuffed Mushrooms', 9.99, 'http://192.168.0.155/media/img/pop.jpg', 'Mushrooms filled with a mixture of seasoned breadcrumbs, cheese, and herbs, baked to a golden perfection.', 1, 5),
(15, 'Bruschetta', 7.99, 'http://192.168.0.155/media/img/pop.jpg', 'Toasted baguette slices topped with diced tomatoes, fresh basil, garlic, and a drizzle of balsamic glaze.', 1, 5),
(16, 'Caesar Salad', 10.99, 'http://192.168.0.155/media/img/pop.jpg', 'Crisp romaine lettuce, croutons, and parmesan cheese tossed in Caesar dressing.', 1, 6),
(17, 'Greek Salad', 11.99, 'http://192.168.0.155/media/img/pop.jpg', 'A refreshing salad with tomatoes, cucumbers, olives, feta cheese, and a zesty Greek dressing.', 1, 6),
(18, 'Cobb Salad', 12.99, 'http://192.168.0.155/media/img/pop.jpg', 'A hearty salad with grilled chicken, bacon, avocado, blue cheese, eggs, and tomatoes on a bed of mixed greens.', 1, 6),
(19, 'Cream of Mushroom Soup', 6.99, 'http://192.168.0.155/media/img/pop.jpg', 'Creamy soup made with fresh mushrooms, onions, and a hint of thyme.', 1, 7),
(20, 'Lobster Bisque', 8.99, 'http://192.168.0.155/media/img/pop.jpg', 'Rich and velvety soup made with lobster, cream, and a touch of brandy.', 1, 7),
(21, 'Minestrone Soup', 6.99, 'http://192.168.0.155/media/img/pop.jpg', 'A hearty Italian vegetable soup with beans, pasta, and seasonal vegetables.', 1, 7),
(25, 'Eggplant Parmesan', 16.99, 'http://192.168.0.155/media/img/pop.jpg', 'Breaded and fried eggplant slices layered with marinara sauce and melted cheese.', 1, 9),
(26, 'Vegetarian Stir-Fry', 15.99, 'http://192.168.0.155/media/img/pop.jpg', 'A mix of colorful vegetables stir-fried in a savory sauce, served over steamed rice.', 1, 9),
(27, 'Quinoa Stuffed Bell Peppers', 14.99, 'http://192.168.0.155/media/img/pop.jpg', 'Bell peppers stuffed with a delicious mixture of quinoa, black beans, corn, and spices.', 1, 9),
(28, 'Cola', 2.50, 'http://192.168.0.155/media/img/pop.jpg', 'Classic carbonated cola soft drink.', 1, 10),
(29, 'Lemonade', 2.50, 'http://192.168.0.155/media/img/pop.jpg', 'Freshly squeezed lemonade, sweet and tangy.', 1, 10),
(30, 'Iced Tea', 2.50, 'http://192.168.0.155/media/img/pop.jpg', 'Refreshing iced tea served sweetened or unsweetened.', 1, 10),
(31, 'Cappuccino', 3.50, 'http://192.168.0.155/media/img/pop.jpg', 'A rich, strong espresso coffee topped with creamy froth, perfect for coffee enthusiasts.', 1, 11),
(32, 'Chai Latte', 4.00, 'http://192.168.0.155/media/img/pop.jpg', 'A spiced tea blend mixed with steamed milk, offering a delightful balance of flavors.', 1, 11),
(33, 'Hot Chocolate', 3.00, 'http://192.168.0.155/media/img/pop.jpg', 'A comforting and indulgent beverage made with rich cocoa and topped with whipped cream.', 1, 11),
(34, 'Pale Ale', 5.00, 'http://192.168.0.155/media/img/pop.jpg', 'A light and hoppy beer with a refreshing taste and a hint of citrus notes.', 1, 12),
(35, 'Stout', 6.00, 'http://192.168.0.155/media/img/pop.jpg', 'A dark and robust beer with flavors of roasted malt, chocolate, and coffee.', 1, 12),
(36, 'Lager', 4.50, 'http://192.168.0.155/media/img/pop.jpg', 'A classic, crisp beer with a smooth, clean taste, perfect for any occasion.', 1, 12);

--
-- Disparadores `foodmenu`
--
DELIMITER $$
CREATE TRIGGER `delete foodmenu` BEFORE DELETE ON `foodmenu` FOR EACH ROW DELETE FROM orders WHERE idFood = OLD.idFood
$$
DELIMITER ;


INSERT INTO client (nameClient, numberTable, userCode)
VALUES
    ('Client1', 'Table1', 'UserCode1'),
    ('Client2', 'Table2', 'UserCode2'),
    ('Client3', 'Table3', 'UserCode3'),
    ('Client4', 'Table4', 'UserCode4'),
    ('Client5', 'Table5', 'UserCode5'),
    ('Client6', 'Table6', 'UserCode6'),
    ('Client7', 'Table7', 'UserCode7'),
    ('Client8', 'Table8', 'UserCode8'),
    ('Client9', 'Table9', 'UserCode9'),
    ('Client10', 'Table10', 'UserCode10');