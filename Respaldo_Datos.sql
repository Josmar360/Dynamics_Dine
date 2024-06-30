CREATE DATABASE  IF NOT EXISTS `dynamics_dine` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dynamics_dine`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 192.168.100.4    Database: dynamics_dine
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `detalles_pedido`
--

DROP TABLE IF EXISTS `detalles_pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalles_pedido` (
  `FK_PK_Num_Pedido` int NOT NULL AUTO_INCREMENT,
  `FK_PK_Platillo` varchar(10) NOT NULL,
  `Cantidad` int NOT NULL,
  `Estatus` tinyint(1) NOT NULL,
  `Entregado` tinyint(1) NOT NULL,
  PRIMARY KEY (`FK_PK_Num_Pedido`,`FK_PK_Platillo`),
  KEY `Detalles_Pedidos_Platillo_FK` (`FK_PK_Platillo`),
  CONSTRAINT `Detalles_Pedidos_Pedido_FK` FOREIGN KEY (`FK_PK_Num_Pedido`) REFERENCES `pedidos` (`PK_Num_Pedido`),
  CONSTRAINT `Detalles_Pedidos_Platillo_FK` FOREIGN KEY (`FK_PK_Platillo`) REFERENCES `platillos` (`FK_Platillo`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalles_pedido`
--

LOCK TABLES `detalles_pedido` WRITE;
/*!40000 ALTER TABLE `detalles_pedido` DISABLE KEYS */;
INSERT INTO `detalles_pedido` VALUES (1,'COCA',1,1,1),(1,'FLN',1,1,1),(1,'POZP',1,1,1),(2,'ACL',1,1,1),(2,'CHILP',1,1,1),(3,'BON',1,1,1),(3,'COR',1,1,1),(3,'ENF',1,1,1),(4,'POZM',1,1,1),(4,'VIC',1,1,1),(5,'CF',1,1,1),(6,'COCA',2,1,1),(11,'COCA',2,1,1),(12,'AG',1,1,1),(13,'AG',1,1,1),(13,'COCA',1,1,1),(14,'CF',1,1,1),(15,'ACL',1,1,1),(15,'AG',1,1,1),(15,'CHILC',1,1,1),(15,'ENCHP',1,1,1),(15,'QUS',1,1,1),(16,'CF',1,1,1),(17,'CHILC',1,1,1),(17,'COCA',1,1,1),(17,'FLN',1,1,1),(17,'QUS',1,1,1),(18,'COR',1,1,1),(19,'ACL',1,1,1),(19,'BON',1,0,1),(19,'CHILC',1,0,1),(19,'COCA',1,0,1),(19,'CRM',1,0,1),(19,'POZC',1,0,1),(21,'CF',1,0,1),(22,'CF',1,0,1),(22,'COCA',1,0,1);
/*!40000 ALTER TABLE `detalles_pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedidos`
--

DROP TABLE IF EXISTS `pedidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedidos` (
  `PK_Num_Pedido` int NOT NULL AUTO_INCREMENT,
  `Mesa` int NOT NULL,
  `Total` float NOT NULL,
  PRIMARY KEY (`PK_Num_Pedido`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedidos`
--

LOCK TABLES `pedidos` WRITE;
/*!40000 ALTER TABLE `pedidos` DISABLE KEYS */;
INSERT INTO `pedidos` VALUES (1,1,156),(2,2,125),(3,3,124),(4,4,126),(5,5,38),(6,1,250),(11,7,0),(12,2,0),(13,6,0),(14,7,38),(15,11,243),(16,7,38),(17,4,166),(18,3,37),(19,3,287),(20,1,76),(21,1,38),(22,1,59);
/*!40000 ALTER TABLE `pedidos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `platillos`
--

DROP TABLE IF EXISTS `platillos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `platillos` (
  `FK_Platillo` varchar(10) NOT NULL,
  `Platillos` varchar(50) NOT NULL,
  `FK_Tipo_Platillo` varchar(6) NOT NULL,
  `Precios` float NOT NULL,
  PRIMARY KEY (`FK_Platillo`),
  KEY `Platillos_FK` (`FK_Tipo_Platillo`),
  CONSTRAINT `Platillos_FK` FOREIGN KEY (`FK_Tipo_Platillo`) REFERENCES `tipo_platillo` (`PK_Tipo_Platillo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `platillos`
--

LOCK TABLES `platillos` WRITE;
/*!40000 ALTER TABLE `platillos` DISABLE KEYS */;
INSERT INTO `platillos` VALUES ('ACL','Arroz con leche','PO',49),('AG','Agua','B',19),('BON','Boing','B',21),('CF','Café','B',38),('CHILC','Chilaquiles con carne','P',76),('CHILP','Chilaquiles con pollo','P',76),('COCA','Coca-cola','B',21),('COR','Corona','B',37),('CRM','Crema','E',31),('ENCHP','Enchiladas con pollo','P',76),('ENF','Enfrijoladas','P',76),('FLN','Flan','PO',46),('GUA','Guacamole','E',48),('POZC','Pozole de cabeza','P',89),('POZM','Pozole mixto','P',89),('POZP','Pozole de pollo','P',89),('QUS','Queso','E',23),('SP','Sprite','B',21),('VIC','Victoria','B',37);
/*!40000 ALTER TABLE `platillos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_platillo`
--

DROP TABLE IF EXISTS `tipo_platillo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_platillo` (
  `PK_Tipo_Platillo` varchar(6) NOT NULL,
  `Tipo_Platillo` varchar(50) NOT NULL,
  PRIMARY KEY (`PK_Tipo_Platillo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_platillo`
--

LOCK TABLES `tipo_platillo` WRITE;
/*!40000 ALTER TABLE `tipo_platillo` DISABLE KEYS */;
INSERT INTO `tipo_platillo` VALUES ('B','Bebida'),('E','Extra'),('P','Platillo'),('PO','Postres');
/*!40000 ALTER TABLE `tipo_platillo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'dynamics_dine'
--

--
-- Dumping routines for database 'dynamics_dine'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-30  0:20:44
