promt:
sql to create a database called 
blogphp with table blog 
and insert several articles in spanish

-- Crear la base de datos
CREATE DATABASE blogphp;
USE blogphp;

-- Crear la tabla de artículos del blog
CREATE TABLE blog (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    contenido TEXT NOT NULL,
    fecha_publicacion DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insertar varios artículos en español
INSERT INTO blog (titulo, contenido) VALUES
('Cómo empezar con PHP desde cero', 
 'En este artículo aprenderás los conceptos básicos de PHP, cómo instalarlo, cómo ejecutar tu primer script y las mejores prácticas para comenzar en el desarrollo web.'),

('Las mejores prácticas para organizar tu código en PHP', 
 'Mantener tu código limpio y organizado es fundamental. Aquí te mostramos patrones de diseño, estructuras de carpetas recomendadas y trucos que harán tu proyecto más escalable.'),

('Guía para conectar PHP con MySQL', 
 'Explicamos cómo usar PDO y MySQLi para establecer conexiones seguras a bases de datos MySQL desde PHP, con ejemplos prácticos.'),

('Cómo crear un sistema de login seguro en PHP', 
 'Aprende a implementar un sistema de autenticación utilizando hashing de contraseñas, sesiones seguras y validación del lado del servidor.'),

('Errores comunes en PHP y cómo solucionarlos', 
 'En este artículo recopilamos los errores más frecuentes que comenten los principiantes al programar en PHP y te explicamos cómo evitarlos o resolverlos de forma sencilla.');
