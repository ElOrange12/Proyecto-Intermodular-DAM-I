-- ===============================================
--     TIENDA DE PATOS DE GOMA - INSTALACIÓN SQL
-- ===============================================

-- ====== 1. CREACIÓN DE TABLAS MADRE ======

-- Categorías de patos
CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);

-- Clientes
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(150),
    email VARCHAR(150) UNIQUE,
    direccion VARCHAR(255)
);

-- Productos (patos de goma)
CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    color VARCHAR(50),
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

-- Gestión de stock
CREATE TABLE stock (
    id_stock INT AUTO_INCREMENT PRIMARY KEY,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    ubicacion VARCHAR(100),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- ====== 2. TABLAS HIJAS ======

-- Pedidos
CREATE TABLE pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    fecha DATE NOT NULL,
    total DECIMAL(10,2),
    estado VARCHAR(50),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- Líneas de pedido
CREATE TABLE lineas_pedido (
    id_linea INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- ===============================================
--     3. VISTAS PARA MOSTRAR INFORMACIÓN COMPLETA
-- ===============================================

-- Vista de productos con su categoría
CREATE VIEW vista_productos_categorias AS
SELECT p.id_producto, p.nombre AS producto, p.precio, p.color,
       c.nombre AS categoria
FROM productos p
LEFT JOIN categorias c ON p.id_categoria = c.id_categoria;

-- Vista de stock completo
CREATE VIEW vista_stock AS
SELECT s.id_stock, p.nombre AS producto, s.cantidad, s.ubicacion
FROM stock s
JOIN productos p ON s.id_producto = p.id_producto;

-- Vista de pedidos con datos del cliente
CREATE VIEW vista_pedidos_clientes AS
SELECT pe.id_pedido, pe.fecha, pe.total, pe.estado,
       c.nombre, c.apellidos, c.email
FROM pedidos pe
JOIN clientes c ON pe.id_cliente = c.id_cliente;

-- Vista de líneas de pedido con datos del producto y pedido
CREATE VIEW vista_lineas_detalle AS
SELECT lp.id_linea, pe.id_pedido, c.nombre AS cliente, p.nombre AS producto,
       lp.cantidad, lp.precio_unitario,
       (lp.cantidad * lp.precio_unitario) AS subtotal
FROM lineas_pedido lp
JOIN pedidos pe ON lp.id_pedido = pe.id_pedido
JOIN clientes c ON pe.id_cliente = c.id_cliente
JOIN productos p ON lp.id_producto = p.id_producto;

-- ===============================================
--     4. INSERTAR DATOS (Orden correcto por FK)
-- ===============================================

-- ====== Categorías (MADRE) ======
INSERT INTO categorias (nombre, descripcion) VALUES
('Patos Clásicos', 'Patos de goma tradicionales'),
('Patos Temáticos', 'Patos con disfraces o temas especiales'),
('Patos Gigantes', 'Patos de gran tamaño'),
('Patos Mini', 'Patos pequeños coleccionables');

-- ====== Clientes (MADRE) ======
INSERT INTO clientes (nombre, apellidos, email, direccion) VALUES
('Dani', 'Oliveira Vidal', 'daniel@example.com', 'Calle Naranja 12'),
('Hugo', 'Garcia Lopez', 'hugo@example.com', 'Avenida del Pato 3'),
('Lucia', 'Martinez Ruiz', 'lucia@example.com', 'Calle Río Amarillo 8');

-- ====== Productos (MADRE) ======
INSERT INTO productos (nombre, descripcion, precio, color, id_categoria) VALUES
('Pato Amarillo Clásico', 'El clásico pato de goma', 4.99, 'Amarillo', 1),
('Pato Pirata', 'Pato con parche y sombrero pirata', 7.50, 'Negro', 2),
('Pato Unicornio', 'Pato temático con cuerno mágico', 8.99, 'Multicolor', 2),
('Pato Gigante XXL', 'Pato gigante para piscina', 24.99, 'Amarillo', 3),
('Mini Pato Rosa', 'Pato pequeño en color rosa', 2.49, 'Rosa', 4);

-- ====== Stock (DEPENDE DE PRODUCTOS) ======
INSERT INTO stock (id_producto, cantidad, ubicacion) VALUES
(1, 150, 'Almacén A'),
(2, 80, 'Almacén B'),
(3, 60, 'Almacén B'),
(4, 20, 'Almacén C'),
(5, 300, 'Almacén A');

-- ====== Pedidos (DEPENDE DE CLIENTES) ======
INSERT INTO pedidos (id_cliente, fecha, total, estado) VALUES
(1, '2025-01-10', 17.48, 'Enviado'),
(2, '2025-01-12', 24.99, 'Procesando'),
(3, '2025-01-14', 12.49, 'Entregado');

-- ====== Líneas de pedido (DEPENDE DE PEDIDOS + PRODUCTOS) ======
INSERT INTO lineas_pedido (id_pedido, id_producto, cantidad, precio_unitario) VALUES
(1, 1, 2, 4.99),
(1, 5, 1, 2.49),
(2, 4, 1, 24.99),
(3, 2, 1, 7.50),
(3, 5, 2, 2.49); 

