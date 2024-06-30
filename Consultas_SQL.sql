-- Usar base de datos Dynamics_Dine
USE Dynamics_Dine;


-- Desactivar SQL Safe para las actualizaciones (pruebas)
SET SQL_SAFE_UPDATES= 0;


-- Actualizar detalles de pedidos al pedido 2 (Comportamiento en la aplicacion de escritorio)
UPDATE Detalles_Pedido SET Estatus = 0 WHERE FK_PK_NUM_PEDIDO = 2;


-- Actualizar el estatus de todos los pedidos registrados (Prueba de comportamiento en la aplicacion de esritorio)
UPDATE Detalles_Pedido SET Estatus = 1;


-- Actualizar todos las entregas (Prueba en aplicacion movil)
UPDATE Detalles_Pedido SET Entregado = 1;


-- Consulta de tablas para visualizar los datos
SELECT * FROM Detalles_Pedido;
select * FROm Pedidos;


-- Consulta para ver pedidos pendientes
SELECT DP.FK_PK_Num_Pedido, P.Platillos, DP.Cantidad, DP.Estatus 
FROM Detalles_Pedido DP 
JOIN Platillos P ON DP.FK_PK_Platillo = P.FK_Platillo
WHERE DP.FK_PK_Num_Pedido IN (SELECT FK_PK_Num_Pedido FROM Detalles_Pedido WHERE Estatus = 0);


-- Ordenar platillos con tipo de platillo
SELECT P.FK_Platillo, P.Platillos, P.Precios, TP.Tipo_Platillo
FROM Platillos P
JOIN Tipo_Platillo TP ON P.FK_Tipo_Platillo = TP.PK_Tipo_Platillo;


-- Comenzar una transacción
START TRANSACTION;

-- Insertar datos en la tabla Pedidos y obtener el ID generado
INSERT INTO Pedidos (Mesa, Total)
VALUES (1, 250);

-- Obtener el ID generado en Pedidos
SET @id_generado = LAST_INSERT_ID();

-- Insertar en Detalles_Pedido usando el ID generado de Pedidos
INSERT INTO Detalles_Pedido (FK_PK_Num_Pedido, FK_PK_Platillo, Cantidad, Estatus)
VALUES (@id_generado, 'COCA', 2, 0);

-- Confirmar la transacción
COMMIT;


-- Consulta para ver los pedidos activos en una mesa
SELECT PD.PK_Num_Pedido, P.Platillos, PD.Mesa, DP.Estatus, P.FK_Platillo
FROM Pedidos PD
JOIN Detalles_Pedido DP ON PD.PK_Num_Pedido = DP.FK_PK_Num_Pedido
JOIN Platillos P ON DP.FK_PK_Platillo = P.FK_Platillo
WHERE PD.Mesa = 3 AND DP.Entregado = 0;


-- Actualizar datos en entregado a los que tienen estatus 1
UPDATE Detalles_Pedido AS DP 
JOIN Pedidos AS P ON DP.FK_PK_Num_Pedido = P.PK_Num_Pedido
SET DP.Entregado = 1 
WHERE DP.Estatus = 1 AND P.Mesa = 3;