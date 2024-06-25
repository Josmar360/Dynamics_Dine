CREATE SCHEMA DYNAMICS_DINE;

USE DYNAMICS_DINE;

CREATE TABLE Tipo_Platillo
(
	PK_Tipo_Platillo VARCHAR(6) NOT NULL,
    Tipo_Platillo VARCHAR(50) NOT NULL,
    CONSTRAINT Tipo_Platillo_PK PRIMARY KEY(PK_Tipo_Platillo)
);

CREATE TABLE Platillos
(
	FK_Platillo VARCHAR(10) NOT NULL,
    Platillos VARCHAR(50) NOT NULL,
    FK_Tipo_Platillo VARCHAR(6) NOT NULL,
    Precios FLOAT NOT NULL,
    CONSTRAINT Platillos_PK PRIMARY KEY(FK_Platillo),
    CONSTRAINT Platillos_FK FOREIGN KEY(FK_Tipo_Platillo) REFERENCES Tipo_Platillo(PK_Tipo_Platillo)
);

CREATE TABLE Pedidos
(
	PK_Num_Pedido INT AUTO_INCREMENT NOT NULL,
    Mesa INT NOT NULL,
    Total FLOAT NOT NULL,
    CONSTRAINT Pedidos_PK PRIMARY KEY(PK_Num_Pedido)
);

CREATE TABLE Detalles_Pedido
(
	FK_PK_Num_Pedido INT AUTO_INCREMENT NOT NULL,
    FK_PK_Platillo VARCHAR(10) NOT NULL,
    Cantidad INT NOT NULL, 
    Estatus BOOLEAN NOT NULL,
    CONSTRAINT Detalles_Pedidos_PK PRIMARY KEY(FK_PK_Num_Pedido, FK_PK_Platillo),
    CONSTRAINT Detalles_Pedidos_Pedido_FK FOREIGN KEY(FK_PK_Num_Pedido) REFERENCES Pedidos(PK_Num_Pedido),
    CONSTRAINT Detalles_Pedidos_Platillo_FK FOREIGN KEY(FK_PK_Platillo) REFERENCES Platillos(FK_Platillo)
);