/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.7.2-MariaDB, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: proj2
-- ------------------------------------------------------
-- Server version	11.7.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `Administrador`
--

DROP TABLE IF EXISTS `Administrador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Administrador` (
  `ID_administrador` int(10) NOT NULL AUTO_INCREMENT,
  `UtilizadorID_utilizador` int(10) NOT NULL,
  PRIMARY KEY (`ID_administrador`),
  KEY `FKAdministra170969` (`UtilizadorID_utilizador`),
  CONSTRAINT `FKAdministra170969` FOREIGN KEY (`UtilizadorID_utilizador`) REFERENCES `Utilizador` (`ID_utilizador`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Administrador`
--

LOCK TABLES `Administrador` WRITE;
/*!40000 ALTER TABLE `Administrador` DISABLE KEYS */;
INSERT INTO `Administrador` VALUES
(1,11),
(2,12);
/*!40000 ALTER TABLE `Administrador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Alerta`
--

DROP TABLE IF EXISTS `Alerta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Alerta` (
  `ID_alerta` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(200) DEFAULT NULL,
  `UtilizadorID_utilizador` int(10) NOT NULL,
  `AdministradorID_administrador` int(10) NOT NULL,
  `Tipo_AlertaID_tipo_alerta` int(10) NOT NULL,
  PRIMARY KEY (`ID_alerta`),
  KEY `FKAlerta757900` (`UtilizadorID_utilizador`),
  KEY `FKAlerta954578` (`AdministradorID_administrador`),
  KEY `FKAlerta6974` (`Tipo_AlertaID_tipo_alerta`),
  CONSTRAINT `FKAlerta6974` FOREIGN KEY (`Tipo_AlertaID_tipo_alerta`) REFERENCES `Tipo_Alerta` (`ID_tipo_alerta`),
  CONSTRAINT `FKAlerta757900` FOREIGN KEY (`UtilizadorID_utilizador`) REFERENCES `Utilizador` (`ID_utilizador`),
  CONSTRAINT `FKAlerta954578` FOREIGN KEY (`AdministradorID_administrador`) REFERENCES `Administrador` (`ID_administrador`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Alerta`
--

LOCK TABLES `Alerta` WRITE;
/*!40000 ALTER TABLE `Alerta` DISABLE KEYS */;
INSERT INTO `Alerta` VALUES
(1,'Teste!',12,1,1),
(2,'Teste2!',11,1,1),
(3,'Teste3!',11,1,1),
(4,'Teste3!',11,1,1),
(5,'Dados da Reserva, 1 alterados.',11,1,1),
(6,'Dados da Reserva, 1 alterados.',11,1,1),
(7,'Viagem confirmada (6).',11,1,1),
(8,'Viagem confirmada (7).',11,1,1);
/*!40000 ALTER TABLE `Alerta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Avaliacao`
--

DROP TABLE IF EXISTS `Avaliacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Avaliacao` (
  `ID_avaliacao` int(10) NOT NULL AUTO_INCREMENT,
  `Nota` int(5) DEFAULT NULL,
  `ViagemID_viagem` int(10) NOT NULL,
  `CondutorID_condutor` int(10) NOT NULL,
  PRIMARY KEY (`ID_avaliacao`),
  KEY `FKAvaliacao526337` (`ViagemID_viagem`),
  KEY `FKAvaliacao223157` (`CondutorID_condutor`),
  CONSTRAINT `FKAvaliacao223157` FOREIGN KEY (`CondutorID_condutor`) REFERENCES `Condutor` (`ID_condutor`),
  CONSTRAINT `FKAvaliacao526337` FOREIGN KEY (`ViagemID_viagem`) REFERENCES `Viagem` (`ID_viagem`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Avaliacao`
--

LOCK TABLES `Avaliacao` WRITE;
/*!40000 ALTER TABLE `Avaliacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `Avaliacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Bandeira_Cartao`
--

DROP TABLE IF EXISTS `Bandeira_Cartao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Bandeira_Cartao` (
  `ID_bandeira_cartao` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`ID_bandeira_cartao`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bandeira_Cartao`
--

LOCK TABLES `Bandeira_Cartao` WRITE;
/*!40000 ALTER TABLE `Bandeira_Cartao` DISABLE KEYS */;
INSERT INTO `Bandeira_Cartao` VALUES
(1,'VISA');
/*!40000 ALTER TABLE `Bandeira_Cartao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Carta_Conducao`
--

DROP TABLE IF EXISTS `Carta_Conducao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Carta_Conducao` (
  `ID_carta_conducao` int(10) NOT NULL AUTO_INCREMENT,
  `Numero` int(12) DEFAULT NULL,
  `Data_emissao` date DEFAULT NULL,
  `Data_validade` date DEFAULT NULL,
  `Status` tinyint(4) DEFAULT NULL,
  `Foto` varbinary(255) DEFAULT NULL,
  `CondutorID_condutor` int(10) NOT NULL,
  `Tipo_CategoriaID_tipo_categoria` int(10) NOT NULL,
  PRIMARY KEY (`ID_carta_conducao`),
  UNIQUE KEY `Numero` (`Numero`),
  KEY `FKCarta_Cond742089` (`CondutorID_condutor`),
  KEY `FKCarta_Cond804823` (`Tipo_CategoriaID_tipo_categoria`),
  CONSTRAINT `FKCarta_Cond742089` FOREIGN KEY (`CondutorID_condutor`) REFERENCES `Condutor` (`ID_condutor`),
  CONSTRAINT `FKCarta_Cond804823` FOREIGN KEY (`Tipo_CategoriaID_tipo_categoria`) REFERENCES `Tipo_Categoria` (`ID_tipo_categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Carta_Conducao`
--

LOCK TABLES `Carta_Conducao` WRITE;
/*!40000 ALTER TABLE `Carta_Conducao` DISABLE KEYS */;
/*!40000 ALTER TABLE `Carta_Conducao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cartao`
--

DROP TABLE IF EXISTS `Cartao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cartao` (
  `ID_cc` int(10) NOT NULL AUTO_INCREMENT,
  `Digito_seguranca` int(4) DEFAULT NULL,
  `Data_validade` date DEFAULT NULL,
  `Token` varchar(200) DEFAULT NULL,
  `Bandeira_CartaoID_bandeira_cartao` int(10) NOT NULL,
  PRIMARY KEY (`ID_cc`),
  UNIQUE KEY `Token` (`Token`),
  KEY `FKCartao223477` (`Bandeira_CartaoID_bandeira_cartao`),
  CONSTRAINT `FKCartao223477` FOREIGN KEY (`Bandeira_CartaoID_bandeira_cartao`) REFERENCES `Bandeira_Cartao` (`ID_bandeira_cartao`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cartao`
--

LOCK TABLES `Cartao` WRITE;
/*!40000 ALTER TABLE `Cartao` DISABLE KEYS */;
INSERT INTO `Cartao` VALUES
(1,1,'2025-01-01','1',1);
/*!40000 ALTER TABLE `Cartao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cartao_Utilizador`
--

DROP TABLE IF EXISTS `Cartao_Utilizador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cartao_Utilizador` (
  `UtilizadorID_utilizador` int(10) NOT NULL,
  `CartaoID_cc` int(10) NOT NULL,
  KEY `FKCartao_Uti238252` (`UtilizadorID_utilizador`),
  KEY `FKCartao_Uti957238` (`CartaoID_cc`),
  CONSTRAINT `FKCartao_Uti238252` FOREIGN KEY (`UtilizadorID_utilizador`) REFERENCES `Utilizador` (`ID_utilizador`),
  CONSTRAINT `FKCartao_Uti957238` FOREIGN KEY (`CartaoID_cc`) REFERENCES `Cartao` (`ID_cc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cartao_Utilizador`
--

LOCK TABLES `Cartao_Utilizador` WRITE;
/*!40000 ALTER TABLE `Cartao_Utilizador` DISABLE KEYS */;
/*!40000 ALTER TABLE `Cartao_Utilizador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Chat_Viagem`
--

DROP TABLE IF EXISTS `Chat_Viagem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Chat_Viagem` (
  `ID_chat_viagem` int(10) NOT NULL AUTO_INCREMENT,
  `ViagemID_viagem` int(10) NOT NULL,
  PRIMARY KEY (`ID_chat_viagem`),
  KEY `FKChat_Viage248310` (`ViagemID_viagem`),
  CONSTRAINT `FKChat_Viage248310` FOREIGN KEY (`ViagemID_viagem`) REFERENCES `Viagem` (`ID_viagem`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Chat_Viagem`
--

LOCK TABLES `Chat_Viagem` WRITE;
/*!40000 ALTER TABLE `Chat_Viagem` DISABLE KEYS */;
INSERT INTO `Chat_Viagem` VALUES
(1,1);
/*!40000 ALTER TABLE `Chat_Viagem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Condutor`
--

DROP TABLE IF EXISTS `Condutor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Condutor` (
  `ID_condutor` int(10) NOT NULL AUTO_INCREMENT,
  `Reputacao` int(5) DEFAULT NULL,
  `Data_criacao` date DEFAULT NULL,
  `UtilizadorID_utilizador` int(10) NOT NULL,
  `Doc_reg_criminal` varchar(255) DEFAULT NULL,
  `Doc_comprov_residencia` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID_condutor`),
  KEY `FKCondutor482216` (`UtilizadorID_utilizador`),
  CONSTRAINT `FKCondutor482216` FOREIGN KEY (`UtilizadorID_utilizador`) REFERENCES `Utilizador` (`ID_utilizador`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Condutor`
--

LOCK TABLES `Condutor` WRITE;
/*!40000 ALTER TABLE `Condutor` DISABLE KEYS */;
INSERT INTO `Condutor` VALUES
(1,NULL,NULL,2,NULL,NULL),
(3,2,NULL,6,'',''),
(23,0,'2025-04-20',11,'docs/condutores/Aula_9_1.pdf','docs/condutores/Aula_9_1_kbt3eY1.pdf'),
(24,0,'2025-04-20',12,NULL,NULL);
/*!40000 ALTER TABLE `Condutor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Condutor_Veiculo`
--

DROP TABLE IF EXISTS `Condutor_Veiculo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Condutor_Veiculo` (
  `ID_condutor_veiculo` int(10) NOT NULL AUTO_INCREMENT,
  `Documento_arquivo` varchar(255) DEFAULT NULL,
  `Data_emissao` date DEFAULT NULL,
  `Data_validade` date DEFAULT NULL,
  `CondutorID_condutor` int(10) NOT NULL,
  `VeiculoID_veiculo` int(10) NOT NULL,
  PRIMARY KEY (`ID_condutor_veiculo`),
  KEY `FKCondutor_V286592` (`CondutorID_condutor`),
  KEY `FKCondutor_V49743` (`VeiculoID_veiculo`),
  CONSTRAINT `FKCondutor_V286592` FOREIGN KEY (`CondutorID_condutor`) REFERENCES `Condutor` (`ID_condutor`),
  CONSTRAINT `FKCondutor_V49743` FOREIGN KEY (`VeiculoID_veiculo`) REFERENCES `Veiculo` (`ID_veiculo`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Condutor_Veiculo`
--

LOCK TABLES `Condutor_Veiculo` WRITE;
/*!40000 ALTER TABLE `Condutor_Veiculo` DISABLE KEYS */;
INSERT INTO `Condutor_Veiculo` VALUES
(2,NULL,NULL,NULL,3,14),
(9,'docs/condutores/PDS_G11_relatorio_10444-23290-24880-26018-26875_qi8HFMD.pdf','2025-04-21','2026-04-21',23,15),
(10,'','2025-04-21','2025-04-21',23,2),
(11,'','2025-04-21','2025-04-21',23,14);
/*!40000 ALTER TABLE `Condutor_Veiculo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Conselho`
--

DROP TABLE IF EXISTS `Conselho`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Conselho` (
  `ID_conselho` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(20) DEFAULT NULL,
  `DistritoID_distrito` int(10) NOT NULL,
  PRIMARY KEY (`ID_conselho`),
  KEY `FKConselho54259` (`DistritoID_distrito`),
  CONSTRAINT `FKConselho54259` FOREIGN KEY (`DistritoID_distrito`) REFERENCES `Distrito` (`ID_distrito`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Conselho`
--

LOCK TABLES `Conselho` WRITE;
/*!40000 ALTER TABLE `Conselho` DISABLE KEYS */;
INSERT INTO `Conselho` VALUES
(1,'Teste',1);
/*!40000 ALTER TABLE `Conselho` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Contacto`
--

DROP TABLE IF EXISTS `Contacto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Contacto` (
  `ID_contacto` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(50) DEFAULT NULL,
  `UtilizadorID_utilizador` int(10) NOT NULL,
  `Tipo_ContactoID_tipo_contacto` int(10) NOT NULL,
  PRIMARY KEY (`ID_contacto`),
  KEY `FKContacto646561` (`UtilizadorID_utilizador`),
  KEY `FKContacto306499` (`Tipo_ContactoID_tipo_contacto`),
  CONSTRAINT `FKContacto306499` FOREIGN KEY (`Tipo_ContactoID_tipo_contacto`) REFERENCES `Tipo_Contacto` (`ID_tipo_contacto`),
  CONSTRAINT `FKContacto646561` FOREIGN KEY (`UtilizadorID_utilizador`) REFERENCES `Utilizador` (`ID_utilizador`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Contacto`
--

LOCK TABLES `Contacto` WRITE;
/*!40000 ALTER TABLE `Contacto` DISABLE KEYS */;
INSERT INTO `Contacto` VALUES
(1,'123345789',11,2);
/*!40000 ALTER TABLE `Contacto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cor_Veiculo`
--

DROP TABLE IF EXISTS `Cor_Veiculo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cor_Veiculo` (
  `ID_cor_veiculo` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`ID_cor_veiculo`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cor_Veiculo`
--

LOCK TABLES `Cor_Veiculo` WRITE;
/*!40000 ALTER TABLE `Cor_Veiculo` DISABLE KEYS */;
INSERT INTO `Cor_Veiculo` VALUES
(1,'Verde');
/*!40000 ALTER TABLE `Cor_Veiculo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Dados_MB`
--

DROP TABLE IF EXISTS `Dados_MB`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Dados_MB` (
  `ID_mb` int(10) NOT NULL AUTO_INCREMENT,
  `Referencia` int(9) DEFAULT NULL,
  `Entidade` int(5) DEFAULT NULL,
  `Data_limite` date DEFAULT NULL,
  PRIMARY KEY (`ID_mb`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dados_MB`
--

LOCK TABLES `Dados_MB` WRITE;
/*!40000 ALTER TABLE `Dados_MB` DISABLE KEYS */;
INSERT INTO `Dados_MB` VALUES
(1,1,1,'2025-01-01');
/*!40000 ALTER TABLE `Dados_MB` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Desvio`
--

DROP TABLE IF EXISTS `Desvio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Desvio` (
  `ID_desvio` int(10) NOT NULL AUTO_INCREMENT,
  `Data_emissao` date DEFAULT NULL,
  `Status_DesvioID_status_desvio` int(10) NOT NULL,
  `ViagemID_viagem` int(10) NOT NULL,
  PRIMARY KEY (`ID_desvio`),
  KEY `FKDesvio848337` (`Status_DesvioID_status_desvio`),
  KEY `FKDesvio108382` (`ViagemID_viagem`),
  CONSTRAINT `FKDesvio108382` FOREIGN KEY (`ViagemID_viagem`) REFERENCES `Viagem` (`ID_viagem`),
  CONSTRAINT `FKDesvio848337` FOREIGN KEY (`Status_DesvioID_status_desvio`) REFERENCES `Status_Desvio` (`ID_status_desvio`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Desvio`
--

LOCK TABLES `Desvio` WRITE;
/*!40000 ALTER TABLE `Desvio` DISABLE KEYS */;
INSERT INTO `Desvio` VALUES
(1,'2025-04-29',1,4),
(2,'2025-04-30',1,4),
(3,'2025-04-29',1,4),
(4,'2025-04-29',2,4);
/*!40000 ALTER TABLE `Desvio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Distrito`
--

DROP TABLE IF EXISTS `Distrito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Distrito` (
  `ID_distrito` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(20) DEFAULT NULL,
  `PaisID_pais` int(10) NOT NULL,
  PRIMARY KEY (`ID_distrito`),
  KEY `FKDistrito57352` (`PaisID_pais`),
  CONSTRAINT `FKDistrito57352` FOREIGN KEY (`PaisID_pais`) REFERENCES `Pais` (`ID_pais`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Distrito`
--

LOCK TABLES `Distrito` WRITE;
/*!40000 ALTER TABLE `Distrito` DISABLE KEYS */;
INSERT INTO `Distrito` VALUES
(1,'teste',1);
/*!40000 ALTER TABLE `Distrito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Estado_Civil`
--

DROP TABLE IF EXISTS `Estado_Civil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Estado_Civil` (
  `ID_estado_civil` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID_estado_civil`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Estado_Civil`
--

LOCK TABLES `Estado_Civil` WRITE;
/*!40000 ALTER TABLE `Estado_Civil` DISABLE KEYS */;
INSERT INTO `Estado_Civil` VALUES
(1,'Casado');
/*!40000 ALTER TABLE `Estado_Civil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Freguesia`
--

DROP TABLE IF EXISTS `Freguesia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Freguesia` (
  `ID_freguesia` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(20) DEFAULT NULL,
  `ConselhoID_conselho` int(10) NOT NULL,
  PRIMARY KEY (`ID_freguesia`),
  KEY `FKFreguesia640070` (`ConselhoID_conselho`),
  CONSTRAINT `FKFreguesia640070` FOREIGN KEY (`ConselhoID_conselho`) REFERENCES `Conselho` (`ID_conselho`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Freguesia`
--

LOCK TABLES `Freguesia` WRITE;
/*!40000 ALTER TABLE `Freguesia` DISABLE KEYS */;
INSERT INTO `Freguesia` VALUES
(1,'Teste',1);
/*!40000 ALTER TABLE `Freguesia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Grupo`
--

DROP TABLE IF EXISTS `Grupo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Grupo` (
  `ID_grupo` int(10) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(50) DEFAULT NULL,
  `Data_criacao` date DEFAULT NULL,
  PRIMARY KEY (`ID_grupo`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Grupo`
--

LOCK TABLES `Grupo` WRITE;
/*!40000 ALTER TABLE `Grupo` DISABLE KEYS */;
INSERT INTO `Grupo` VALUES
(1,'grupo1','2025-04-01'),
(2,'grupo2','2025-04-01');
/*!40000 ALTER TABLE `Grupo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Marca_Veiculo`
--

DROP TABLE IF EXISTS `Marca_Veiculo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Marca_Veiculo` (
  `ID_marca_veiculo` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID_marca_veiculo`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Marca_Veiculo`
--

LOCK TABLES `Marca_Veiculo` WRITE;
/*!40000 ALTER TABLE `Marca_Veiculo` DISABLE KEYS */;
INSERT INTO `Marca_Veiculo` VALUES
(1,'Citroen');
/*!40000 ALTER TABLE `Marca_Veiculo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Mensagem`
--

DROP TABLE IF EXISTS `Mensagem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Mensagem` (
  `ID_mensagem` int(10) NOT NULL AUTO_INCREMENT,
  `Valor` varchar(2000) DEFAULT NULL,
  `Data_envio` date DEFAULT NULL,
  `Lida` tinyint(4) DEFAULT NULL,
  `Chat_ViagemID_chat_viagem` int(10) NOT NULL,
  `UtilizadorID_utilizador` int(10) NOT NULL,
  PRIMARY KEY (`ID_mensagem`),
  KEY `FKMensagem684197` (`Chat_ViagemID_chat_viagem`),
  KEY `FKMensagem858327` (`UtilizadorID_utilizador`),
  CONSTRAINT `FKMensagem684197` FOREIGN KEY (`Chat_ViagemID_chat_viagem`) REFERENCES `Chat_Viagem` (`ID_chat_viagem`),
  CONSTRAINT `FKMensagem858327` FOREIGN KEY (`UtilizadorID_utilizador`) REFERENCES `Utilizador` (`ID_utilizador`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Mensagem`
--

LOCK TABLES `Mensagem` WRITE;
/*!40000 ALTER TABLE `Mensagem` DISABLE KEYS */;
INSERT INTO `Mensagem` VALUES
(1,'Esta é uma nova mensagem no chat.','2025-04-26',0,1,11);
/*!40000 ALTER TABLE `Mensagem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Modelo_Veiculo`
--

DROP TABLE IF EXISTS `Modelo_Veiculo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Modelo_Veiculo` (
  `ID_modelo_veiculo` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(50) DEFAULT NULL,
  `Marca_VeiculoID_marca_veiculo` int(10) NOT NULL,
  PRIMARY KEY (`ID_modelo_veiculo`),
  KEY `FKModelo_Vei610888` (`Marca_VeiculoID_marca_veiculo`),
  CONSTRAINT `FKModelo_Vei610888` FOREIGN KEY (`Marca_VeiculoID_marca_veiculo`) REFERENCES `Marca_Veiculo` (`ID_marca_veiculo`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Modelo_Veiculo`
--

LOCK TABLES `Modelo_Veiculo` WRITE;
/*!40000 ALTER TABLE `Modelo_Veiculo` DISABLE KEYS */;
INSERT INTO `Modelo_Veiculo` VALUES
(1,'Citron Interessante',1);
/*!40000 ALTER TABLE `Modelo_Veiculo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Morada`
--

DROP TABLE IF EXISTS `Morada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Morada` (
  `ID_morada` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(20) DEFAULT NULL,
  `UtilizadorID_utilizador` int(10) NOT NULL,
  `FreguesiaID_freguesia` int(10) NOT NULL,
  PRIMARY KEY (`ID_morada`),
  KEY `FKMorada66729` (`UtilizadorID_utilizador`),
  KEY `FKMorada32036` (`FreguesiaID_freguesia`),
  CONSTRAINT `FKMorada32036` FOREIGN KEY (`FreguesiaID_freguesia`) REFERENCES `Freguesia` (`ID_freguesia`),
  CONSTRAINT `FKMorada66729` FOREIGN KEY (`UtilizadorID_utilizador`) REFERENCES `Utilizador` (`ID_utilizador`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Morada`
--

LOCK TABLES `Morada` WRITE;
/*!40000 ALTER TABLE `Morada` DISABLE KEYS */;
INSERT INTO `Morada` VALUES
(1,'Rua Teste, Ed. Teste',11,1);
/*!40000 ALTER TABLE `Morada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Nacionalidade`
--

DROP TABLE IF EXISTS `Nacionalidade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Nacionalidade` (
  `ID_nacionalidade` int(10) NOT NULL AUTO_INCREMENT,
  `PaisID_pais` int(10) NOT NULL,
  PRIMARY KEY (`ID_nacionalidade`),
  KEY `FKNacionalid615907` (`PaisID_pais`),
  CONSTRAINT `FKNacionalid615907` FOREIGN KEY (`PaisID_pais`) REFERENCES `Pais` (`ID_pais`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Nacionalidade`
--

LOCK TABLES `Nacionalidade` WRITE;
/*!40000 ALTER TABLE `Nacionalidade` DISABLE KEYS */;
INSERT INTO `Nacionalidade` VALUES
(1,1);
/*!40000 ALTER TABLE `Nacionalidade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ocorrencia`
--

DROP TABLE IF EXISTS `Ocorrencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ocorrencia` (
  `ID_ocorrencia` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(2000) DEFAULT NULL,
  `Data_envio` date DEFAULT NULL,
  `Data_lida` date DEFAULT NULL,
  `ViagemID_viagem` int(10) NOT NULL,
  `UtilizadorID_utilizador` int(10) NOT NULL,
  `AdministradorID_administrador` int(10) NOT NULL,
  `Tipo_OcorrenciaID_tipo_ocorrencia` int(10) NOT NULL,
  PRIMARY KEY (`ID_ocorrencia`),
  KEY `FKOcorrencia228312` (`ViagemID_viagem`),
  KEY `FKOcorrencia422270` (`UtilizadorID_utilizador`),
  KEY `FKOcorrencia836840` (`AdministradorID_administrador`),
  KEY `FKOcorrencia766645` (`Tipo_OcorrenciaID_tipo_ocorrencia`),
  CONSTRAINT `FKOcorrencia228312` FOREIGN KEY (`ViagemID_viagem`) REFERENCES `Viagem` (`ID_viagem`),
  CONSTRAINT `FKOcorrencia422270` FOREIGN KEY (`UtilizadorID_utilizador`) REFERENCES `Utilizador` (`ID_utilizador`),
  CONSTRAINT `FKOcorrencia766645` FOREIGN KEY (`Tipo_OcorrenciaID_tipo_ocorrencia`) REFERENCES `Tipo_Ocorrencia` (`ID_tipo_ocorrencia`),
  CONSTRAINT `FKOcorrencia836840` FOREIGN KEY (`AdministradorID_administrador`) REFERENCES `Administrador` (`ID_administrador`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ocorrencia`
--

LOCK TABLES `Ocorrencia` WRITE;
/*!40000 ALTER TABLE `Ocorrencia` DISABLE KEYS */;
INSERT INTO `Ocorrencia` VALUES
(1,'Veículo apresentou problema durante a viagem.','2025-04-26',NULL,1,11,1,1);
/*!40000 ALTER TABLE `Ocorrencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pagamento`
--

DROP TABLE IF EXISTS `Pagamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Pagamento` (
  `ID_pagamento` int(10) NOT NULL AUTO_INCREMENT,
  `Valor` int(10) DEFAULT NULL,
  `Data_pagamento` date DEFAULT NULL,
  `Tipo_PagamentoID_tipo_pagamento` int(10) NOT NULL,
  `ReservaID_reserva` int(10) NOT NULL,
  PRIMARY KEY (`ID_pagamento`),
  KEY `FKPagamento699630` (`Tipo_PagamentoID_tipo_pagamento`),
  KEY `FKPagamento294151` (`ReservaID_reserva`),
  CONSTRAINT `FKPagamento294151` FOREIGN KEY (`ReservaID_reserva`) REFERENCES `Reserva` (`ID_reserva`),
  CONSTRAINT `FKPagamento699630` FOREIGN KEY (`Tipo_PagamentoID_tipo_pagamento`) REFERENCES `Tipo_Pagamento` (`ID_tipo_pagamento`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pagamento`
--

LOCK TABLES `Pagamento` WRITE;
/*!40000 ALTER TABLE `Pagamento` DISABLE KEYS */;
INSERT INTO `Pagamento` VALUES
(1,100,'2025-01-01',1,4),
(2,100,'2025-01-01',1,5),
(3,300,'2025-01-01',1,6),
(4,500,'2025-01-01',1,7);
/*!40000 ALTER TABLE `Pagamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pais`
--

DROP TABLE IF EXISTS `Pais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Pais` (
  `ID_pais` int(10) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID_pais`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pais`
--

LOCK TABLES `Pais` WRITE;
/*!40000 ALTER TABLE `Pais` DISABLE KEYS */;
INSERT INTO `Pais` VALUES
(1,'Portugal');
/*!40000 ALTER TABLE `Pais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Passageiro`
--

DROP TABLE IF EXISTS `Passageiro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Passageiro` (
  `ID_passageiro` int(10) NOT NULL AUTO_INCREMENT,
  `Data_criacao` date DEFAULT NULL,
  `UtilizadorID_utilizador` int(10) NOT NULL,
  PRIMARY KEY (`ID_passageiro`),
  KEY `FKPassageiro451853` (`UtilizadorID_utilizador`),
  CONSTRAINT `FKPassageiro451853` FOREIGN KEY (`UtilizadorID_utilizador`) REFERENCES `Utilizador` (`ID_utilizador`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Passageiro`
--

LOCK TABLES `Passageiro` WRITE;
/*!40000 ALTER TABLE `Passageiro` DISABLE KEYS */;
INSERT INTO `Passageiro` VALUES
(1,NULL,2),
(4,'2025-04-27',11),
(5,'2025-04-28',12);
/*!40000 ALTER TABLE `Passageiro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Passageiro_Viagem`
--

DROP TABLE IF EXISTS `Passageiro_Viagem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Passageiro_Viagem` (
  `ID_passageiro_viagem` int(10) NOT NULL AUTO_INCREMENT,
  `PassageiroID_passageiro` int(10) NOT NULL,
  `ViagemID_viagem` int(10) NOT NULL,
  `ReservaID_reserva` int(10) NOT NULL,
  PRIMARY KEY (`ID_passageiro_viagem`),
  KEY `FKPassageiro635573` (`PassageiroID_passageiro`),
  KEY `FKPassageiro146953` (`ViagemID_viagem`),
  KEY `FKPassageiro360421` (`ReservaID_reserva`),
  CONSTRAINT `FKPassageiro146953` FOREIGN KEY (`ViagemID_viagem`) REFERENCES `Viagem` (`ID_viagem`),
  CONSTRAINT `FKPassageiro360421` FOREIGN KEY (`ReservaID_reserva`) REFERENCES `Reserva` (`ID_reserva`),
  CONSTRAINT `FKPassageiro635573` FOREIGN KEY (`PassageiroID_passageiro`) REFERENCES `Passageiro` (`ID_passageiro`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Passageiro_Viagem`
--

LOCK TABLES `Passageiro_Viagem` WRITE;
/*!40000 ALTER TABLE `Passageiro_Viagem` DISABLE KEYS */;
INSERT INTO `Passageiro_Viagem` VALUES
(1,4,2,4),
(2,4,3,5),
(3,4,4,6),
(4,5,5,7),
(7,4,4,6);
/*!40000 ALTER TABLE `Passageiro_Viagem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ponto`
--

DROP TABLE IF EXISTS `Ponto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ponto` (
  `ID_ponto` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID_ponto`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ponto`
--

LOCK TABLES `Ponto` WRITE;
/*!40000 ALTER TABLE `Ponto` DISABLE KEYS */;
INSERT INTO `Ponto` VALUES
(1,'Teste'),
(2,'Teste2');
/*!40000 ALTER TABLE `Ponto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ponto_Desvio`
--

DROP TABLE IF EXISTS `Ponto_Desvio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ponto_Desvio` (
  `ID_ponto_desvio` int(11) NOT NULL AUTO_INCREMENT,
  `destino` char(255) DEFAULT NULL,
  `desvioid_desvio` int(11) DEFAULT NULL,
  `pontoid_ponto` int(11) DEFAULT NULL,
  `original` char(255) DEFAULT NULL,
  PRIMARY KEY (`ID_ponto_desvio`),
  KEY `desvioid_desvio` (`desvioid_desvio`),
  KEY `pontoid_ponto` (`pontoid_ponto`),
  CONSTRAINT `Ponto_Desvio_ibfk_1` FOREIGN KEY (`desvioid_desvio`) REFERENCES `Desvio` (`ID_desvio`),
  CONSTRAINT `Ponto_Desvio_ibfk_2` FOREIGN KEY (`pontoid_ponto`) REFERENCES `Ponto` (`ID_ponto`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ponto_Desvio`
--

LOCK TABLES `Ponto_Desvio` WRITE;
/*!40000 ALTER TABLE `Ponto_Desvio` DISABLE KEYS */;
INSERT INTO `Ponto_Desvio` VALUES
(1,'0',1,1,'1'),
(2,'1',1,2,'1'),
(3,'0',1,2,'0'),
(4,'1',1,2,'0'),
(5,'0',2,2,'1'),
(6,'1',2,2,'1'),
(7,'0',2,1,'0'),
(8,'1',2,1,'0'),
(9,'0',3,2,'1'),
(10,'1',3,2,'1'),
(11,'0',3,1,'0'),
(12,'1',3,1,'0'),
(13,'0',4,2,'1'),
(14,'1',4,2,'1'),
(15,'0',4,1,'0'),
(16,'1',4,1,'0');
/*!40000 ALTER TABLE `Ponto_Desvio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ponto_Reserva`
--

DROP TABLE IF EXISTS `Ponto_Reserva`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ponto_Reserva` (
  `ID_ponto_reserva` int(11) NOT NULL AUTO_INCREMENT,
  `destino` char(255) DEFAULT NULL,
  `reservaid_reserva` int(11) DEFAULT NULL,
  `pontoid_ponto` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID_ponto_reserva`),
  KEY `reservaid_reserva` (`reservaid_reserva`),
  KEY `pontoid_ponto` (`pontoid_ponto`),
  CONSTRAINT `Ponto_Reserva_ibfk_1` FOREIGN KEY (`reservaid_reserva`) REFERENCES `Reserva` (`ID_reserva`),
  CONSTRAINT `Ponto_Reserva_ibfk_2` FOREIGN KEY (`pontoid_ponto`) REFERENCES `Ponto` (`ID_ponto`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ponto_Reserva`
--

LOCK TABLES `Ponto_Reserva` WRITE;
/*!40000 ALTER TABLE `Ponto_Reserva` DISABLE KEYS */;
INSERT INTO `Ponto_Reserva` VALUES
(7,'0',4,1),
(8,'1',4,1),
(9,'0',5,1),
(10,'1',5,1),
(11,'0',6,1),
(12,'1',6,2),
(13,'0',7,2),
(14,'1',7,1);
/*!40000 ALTER TABLE `Ponto_Reserva` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ponto_Viagem`
--

DROP TABLE IF EXISTS `Ponto_Viagem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ponto_Viagem` (
  `ID_ponto_viagem` int(10) NOT NULL AUTO_INCREMENT,
  `Destino` tinyint(4) DEFAULT NULL,
  `ViagemID_viagem` int(10) NOT NULL,
  `PontoID_ponto` int(10) NOT NULL,
  PRIMARY KEY (`ID_ponto_viagem`),
  KEY `FKPonto_Viag109697` (`ViagemID_viagem`),
  KEY `FKPonto_Viag133463` (`PontoID_ponto`),
  CONSTRAINT `FKPonto_Viag109697` FOREIGN KEY (`ViagemID_viagem`) REFERENCES `Viagem` (`ID_viagem`),
  CONSTRAINT `FKPonto_Viag133463` FOREIGN KEY (`PontoID_ponto`) REFERENCES `Ponto` (`ID_ponto`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ponto_Viagem`
--

LOCK TABLES `Ponto_Viagem` WRITE;
/*!40000 ALTER TABLE `Ponto_Viagem` DISABLE KEYS */;
INSERT INTO `Ponto_Viagem` VALUES
(1,0,2,1),
(2,1,2,1),
(3,0,3,1),
(4,1,3,1),
(5,0,4,2),
(6,1,4,2),
(7,0,5,2),
(8,1,5,1);
/*!40000 ALTER TABLE `Ponto_Viagem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Reserva`
--

DROP TABLE IF EXISTS `Reserva`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Reserva` (
  `ID_reserva` int(10) NOT NULL AUTO_INCREMENT,
  `Data_emissao` date DEFAULT NULL,
  `Valor` int(10) DEFAULT NULL,
  `UtilizadorID_utilizador` int(10) NOT NULL,
  `CondutorID_condutor` int(10) NOT NULL,
  `PassageiroID_passageiro` int(10) NOT NULL,
  `Status_reservaID_status_reserva` int(11) DEFAULT NULL,
  `Data_viagem` date NOT NULL,
  PRIMARY KEY (`ID_reserva`),
  KEY `FKReserva785147` (`UtilizadorID_utilizador`),
  KEY `FKReserva324074` (`CondutorID_condutor`),
  KEY `FKReserva209958` (`PassageiroID_passageiro`),
  KEY `fk_status_reserva` (`Status_reservaID_status_reserva`),
  CONSTRAINT `FKReserva209958` FOREIGN KEY (`PassageiroID_passageiro`) REFERENCES `Passageiro` (`ID_passageiro`),
  CONSTRAINT `FKReserva324074` FOREIGN KEY (`CondutorID_condutor`) REFERENCES `Condutor` (`ID_condutor`),
  CONSTRAINT `FKReserva785147` FOREIGN KEY (`UtilizadorID_utilizador`) REFERENCES `Utilizador` (`ID_utilizador`),
  CONSTRAINT `fk_status_reserva` FOREIGN KEY (`Status_reservaID_status_reserva`) REFERENCES `Status_Reserva` (`ID_status_reserva`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Reserva`
--

LOCK TABLES `Reserva` WRITE;
/*!40000 ALTER TABLE `Reserva` DISABLE KEYS */;
INSERT INTO `Reserva` VALUES
(4,'2025-04-27',100,11,23,4,3,'2025-05-15'),
(5,'2025-04-27',100,11,23,4,3,'2025-05-25'),
(6,'2025-04-28',300,11,23,4,3,'2025-05-05'),
(7,'2025-04-28',500,12,23,5,3,'2025-10-10');
/*!40000 ALTER TABLE `Reserva` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Status_Desvio`
--

DROP TABLE IF EXISTS `Status_Desvio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Status_Desvio` (
  `ID_status_desvio` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID_status_desvio`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Status_Desvio`
--

LOCK TABLES `Status_Desvio` WRITE;
/*!40000 ALTER TABLE `Status_Desvio` DISABLE KEYS */;
INSERT INTO `Status_Desvio` VALUES
(1,'Inativo'),
(2,'Pendente'),
(3,'Ativo');
/*!40000 ALTER TABLE `Status_Desvio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Status_Reserva`
--

DROP TABLE IF EXISTS `Status_Reserva`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Status_Reserva` (
  `ID_status_reserva` int(11) NOT NULL AUTO_INCREMENT,
  `Descricao` char(255) DEFAULT NULL,
  PRIMARY KEY (`ID_status_reserva`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Status_Reserva`
--

LOCK TABLES `Status_Reserva` WRITE;
/*!40000 ALTER TABLE `Status_Reserva` DISABLE KEYS */;
INSERT INTO `Status_Reserva` VALUES
(1,'Pendente'),
(2,'Aceite'),
(3,'Finalizada');
/*!40000 ALTER TABLE `Status_Reserva` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Status_Viagem`
--

DROP TABLE IF EXISTS `Status_Viagem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Status_Viagem` (
  `ID_status_viagem` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID_status_viagem`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Status_Viagem`
--

LOCK TABLES `Status_Viagem` WRITE;
/*!40000 ALTER TABLE `Status_Viagem` DISABLE KEYS */;
INSERT INTO `Status_Viagem` VALUES
(1,'Pendente'),
(2,'Em Andamento'),
(3,'Finalizada');
/*!40000 ALTER TABLE `Status_Viagem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Suspensao`
--

DROP TABLE IF EXISTS `Suspensao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Suspensao` (
  `ID_suspensao` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(2000) DEFAULT NULL,
  `Data_inicio` date DEFAULT NULL,
  `Data_fim` date DEFAULT NULL,
  `AdministradorID_administrador` int(10) NOT NULL,
  `UtilizadorID_utilizador` int(10) NOT NULL,
  PRIMARY KEY (`ID_suspensao`),
  KEY `FKSuspensao450958` (`AdministradorID_administrador`),
  KEY `FKSuspensao808152` (`UtilizadorID_utilizador`),
  CONSTRAINT `FKSuspensao450958` FOREIGN KEY (`AdministradorID_administrador`) REFERENCES `Administrador` (`ID_administrador`),
  CONSTRAINT `FKSuspensao808152` FOREIGN KEY (`UtilizadorID_utilizador`) REFERENCES `Utilizador` (`ID_utilizador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Suspensao`
--

LOCK TABLES `Suspensao` WRITE;
/*!40000 ALTER TABLE `Suspensao` DISABLE KEYS */;
/*!40000 ALTER TABLE `Suspensao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tipo_Alerta`
--

DROP TABLE IF EXISTS `Tipo_Alerta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tipo_Alerta` (
  `ID_tipo_alerta` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`ID_tipo_alerta`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tipo_Alerta`
--

LOCK TABLES `Tipo_Alerta` WRITE;
/*!40000 ALTER TABLE `Tipo_Alerta` DISABLE KEYS */;
INSERT INTO `Tipo_Alerta` VALUES
(1,'Aviso');
/*!40000 ALTER TABLE `Tipo_Alerta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tipo_Categoria`
--

DROP TABLE IF EXISTS `Tipo_Categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tipo_Categoria` (
  `ID_tipo_categoria` int(10) NOT NULL AUTO_INCREMENT,
  `Tipo` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`ID_tipo_categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tipo_Categoria`
--

LOCK TABLES `Tipo_Categoria` WRITE;
/*!40000 ALTER TABLE `Tipo_Categoria` DISABLE KEYS */;
/*!40000 ALTER TABLE `Tipo_Categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tipo_Contacto`
--

DROP TABLE IF EXISTS `Tipo_Contacto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tipo_Contacto` (
  `ID_tipo_contacto` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`ID_tipo_contacto`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tipo_Contacto`
--

LOCK TABLES `Tipo_Contacto` WRITE;
/*!40000 ALTER TABLE `Tipo_Contacto` DISABLE KEYS */;
INSERT INTO `Tipo_Contacto` VALUES
(1,'Email'),
(2,'Telefone');
/*!40000 ALTER TABLE `Tipo_Contacto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tipo_Ocorrencia`
--

DROP TABLE IF EXISTS `Tipo_Ocorrencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tipo_Ocorrencia` (
  `ID_tipo_ocorrencia` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`ID_tipo_ocorrencia`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tipo_Ocorrencia`
--

LOCK TABLES `Tipo_Ocorrencia` WRITE;
/*!40000 ALTER TABLE `Tipo_Ocorrencia` DISABLE KEYS */;
INSERT INTO `Tipo_Ocorrencia` VALUES
(1,'Reclamação'),
(2,'Sugestão');
/*!40000 ALTER TABLE `Tipo_Ocorrencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tipo_Pagamento`
--

DROP TABLE IF EXISTS `Tipo_Pagamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tipo_Pagamento` (
  `ID_tipo_pagamento` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(20) DEFAULT NULL,
  `Dados_MBID_mb` int(10) NOT NULL,
  `CartaoID_cc` int(10) NOT NULL,
  PRIMARY KEY (`ID_tipo_pagamento`),
  KEY `FKTipo_Pagam53601` (`Dados_MBID_mb`),
  KEY `FKTipo_Pagam624493` (`CartaoID_cc`),
  CONSTRAINT `FKTipo_Pagam53601` FOREIGN KEY (`Dados_MBID_mb`) REFERENCES `Dados_MB` (`ID_mb`),
  CONSTRAINT `FKTipo_Pagam624493` FOREIGN KEY (`CartaoID_cc`) REFERENCES `Cartao` (`ID_cc`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tipo_Pagamento`
--

LOCK TABLES `Tipo_Pagamento` WRITE;
/*!40000 ALTER TABLE `Tipo_Pagamento` DISABLE KEYS */;
INSERT INTO `Tipo_Pagamento` VALUES
(1,'100',1,1);
/*!40000 ALTER TABLE `Tipo_Pagamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tipo_Veiculo`
--

DROP TABLE IF EXISTS `Tipo_Veiculo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tipo_Veiculo` (
  `ID_tipo_veiculo` int(10) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`ID_tipo_veiculo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tipo_Veiculo`
--

LOCK TABLES `Tipo_Veiculo` WRITE;
/*!40000 ALTER TABLE `Tipo_Veiculo` DISABLE KEYS */;
INSERT INTO `Tipo_Veiculo` VALUES
(1,'Teste'),
(2,'Teste');
/*!40000 ALTER TABLE `Tipo_Veiculo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Utilizador`
--

DROP TABLE IF EXISTS `Utilizador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Utilizador` (
  `ID_utilizador` int(10) NOT NULL AUTO_INCREMENT,
  `Nome_Primeiro` varchar(30) DEFAULT NULL,
  `Nome_Ultimo` varchar(30) DEFAULT NULL,
  `Data_nasc` date DEFAULT NULL,
  `Genero` char(1) DEFAULT NULL,
  `Numero_CC` int(8) DEFAULT NULL,
  `Data_criacao` date DEFAULT NULL,
  `GrupoID_grupo` int(10) NOT NULL,
  `Estado_CivilID_estado_civil` int(10) NOT NULL,
  `NacionalidadeID_nacionalidade` int(10) NOT NULL,
  `Senha` varchar(128) DEFAULT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) DEFAULT 0,
  `is_active` tinyint(1) DEFAULT 1,
  `is_staff` tinyint(1) DEFAULT 0,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID_utilizador`),
  UNIQUE KEY `email` (`email`),
  KEY `FKUtilizador55567` (`GrupoID_grupo`),
  KEY `FKUtilizador142159` (`Estado_CivilID_estado_civil`),
  KEY `FKUtilizador714821` (`NacionalidadeID_nacionalidade`),
  CONSTRAINT `FKUtilizador142159` FOREIGN KEY (`Estado_CivilID_estado_civil`) REFERENCES `Estado_Civil` (`ID_estado_civil`),
  CONSTRAINT `FKUtilizador55567` FOREIGN KEY (`GrupoID_grupo`) REFERENCES `Grupo` (`ID_grupo`),
  CONSTRAINT `FKUtilizador714821` FOREIGN KEY (`NacionalidadeID_nacionalidade`) REFERENCES `Nacionalidade` (`ID_nacionalidade`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Utilizador`
--

LOCK TABLES `Utilizador` WRITE;
/*!40000 ALTER TABLE `Utilizador` DISABLE KEYS */;
INSERT INTO `Utilizador` VALUES
(2,'Cristiano','Ronaldo','1985-02-05','M',7,'2025-04-01',1,1,1,'1',NULL,0,1,0,'test@email.com'),
(6,'teste1','teste2','1985-02-05','M',7,'2025-04-01',1,1,1,'pbkdf2_sha256$870000$6qPih0tkJjQveD3w7cAcgi$JzJj/xvJBUzUMsH1fsQDvdii4saycShOyonevVzC2wk=',NULL,0,1,0,'0@0.com'),
(7,'1','1','1985-02-05','M',7,'2025-04-01',1,1,1,'pbkdf2_sha256$870000$6J84me0PqS5mVjaj6cPqed$BkxU43QKi2KJYHIw01m4TVfayKdEWDeDwusJwXEJGas=',NULL,0,1,0,'1@1.com'),
(8,'João','Silva','1990-01-01','M',123456789,'2025-04-09',1,1,1,'pbkdf2_sha256$870000$tiRxGVjWpKQpEtvekPlZhz$ReYYlYT5h9tAm2F8l55vzSN4PYybE+ATz4f5v6Y0lsE=',NULL,0,1,0,'jsilva@email.com'),
(9,'João','Silva','1990-01-01','M',123456789,NULL,1,1,1,'123456',NULL,0,1,0,'silva@email.com'),
(10,'João','Silva','1990-01-01','M',123456789,NULL,1,1,1,'pbkdf2_sha256$870000$tRWJnR0PU1c4gIMy3ZZqdc$sGKCYBNULuMwQFfMCEfX88x6Xv/mzvOgRnzAo7RHc0k=',NULL,0,1,0,'joao@email.com'),
(11,'João2','Silva2','1985-02-05','M',7,NULL,1,1,1,'pbkdf2_sha256$870000$gpEiIs37WfuOzrxhp1Gkrl$m3zbzybI6mql6Z7SGGsnKMtvfWYaAJeC7E7kjy9zdRs=','2025-04-27 20:43:01',1,1,1,'joao2@email.com'),
(12,'2','2','1985-02-05','M',7,'2025-04-18',1,1,1,'pbkdf2_sha256$870000$A84beYBuonvwYUacOKK107$Ee1u1VQBdvJnSDLoGTRd8jRFp3Ym5vQCI6/tBYR7458=',NULL,0,1,0,'2@2.com'),
(15,'5','5','1985-02-05','M',7,'2025-04-19',1,1,1,'pbkdf2_sha256$870000$6WBPGIaL5yDreMOevuVwyZ$JLYv4zA8MUl9mRsNNtuM3hbgssfOgzDUjhQg9YcgH7Y=',NULL,0,1,0,'3@3.com'),
(16,'6','6','1985-02-05','M',7,'2025-04-19',1,1,1,'pbkdf2_sha256$870000$Z7cK2X9dpedz8TFqyMhH2Q$El3R3t4CxoHOFJgaAq0jm1Kqv5Xf3cdZnYgNGn5+pGY=',NULL,0,1,0,'4@4.com');
/*!40000 ALTER TABLE `Utilizador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Veiculo`
--

DROP TABLE IF EXISTS `Veiculo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Veiculo` (
  `ID_veiculo` int(10) NOT NULL AUTO_INCREMENT,
  `Matricula` varchar(7) DEFAULT NULL,
  `Data_fabricacao` date DEFAULT NULL,
  `Ativo` tinyint(4) DEFAULT NULL,
  `Tipo_VeiculoID_tipo_veiculo` int(10) NOT NULL,
  `Cor_VeiculoID_cor_veiculo` int(10) NOT NULL,
  `Modelo_VeiculoID_modelo_veiculo` int(10) NOT NULL,
  PRIMARY KEY (`ID_veiculo`),
  UNIQUE KEY `Matricula` (`Matricula`),
  KEY `FKVeiculo861914` (`Tipo_VeiculoID_tipo_veiculo`),
  KEY `FKVeiculo302397` (`Cor_VeiculoID_cor_veiculo`),
  KEY `FKVeiculo453995` (`Modelo_VeiculoID_modelo_veiculo`),
  CONSTRAINT `FKVeiculo302397` FOREIGN KEY (`Cor_VeiculoID_cor_veiculo`) REFERENCES `Cor_Veiculo` (`ID_cor_veiculo`),
  CONSTRAINT `FKVeiculo453995` FOREIGN KEY (`Modelo_VeiculoID_modelo_veiculo`) REFERENCES `Modelo_Veiculo` (`ID_modelo_veiculo`),
  CONSTRAINT `FKVeiculo861914` FOREIGN KEY (`Tipo_VeiculoID_tipo_veiculo`) REFERENCES `Tipo_Veiculo` (`ID_tipo_veiculo`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Veiculo`
--

LOCK TABLES `Veiculo` WRITE;
/*!40000 ALTER TABLE `Veiculo` DISABLE KEYS */;
INSERT INTO `Veiculo` VALUES
(2,'2',NULL,1,1,1,1),
(14,'12345','2022-02-01',0,2,1,1),
(15,'1234567','2022-02-01',0,2,1,1);
/*!40000 ALTER TABLE `Veiculo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Viagem`
--

DROP TABLE IF EXISTS `Viagem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Viagem` (
  `ID_viagem` int(10) NOT NULL AUTO_INCREMENT,
  `Data_viagem` date DEFAULT NULL,
  `Distancia_percorrida` int(10) DEFAULT NULL,
  `Status_ViagemID_status_viagem` int(10) NOT NULL,
  `CondutorID_condutor` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID_viagem`),
  KEY `FKViagem597327` (`Status_ViagemID_status_viagem`),
  KEY `fk_condutor` (`CondutorID_condutor`),
  CONSTRAINT `FKViagem597327` FOREIGN KEY (`Status_ViagemID_status_viagem`) REFERENCES `Status_Viagem` (`ID_status_viagem`),
  CONSTRAINT `fk_condutor` FOREIGN KEY (`CondutorID_condutor`) REFERENCES `Condutor` (`ID_condutor`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Viagem`
--

LOCK TABLES `Viagem` WRITE;
/*!40000 ALTER TABLE `Viagem` DISABLE KEYS */;
INSERT INTO `Viagem` VALUES
(1,NULL,NULL,1,NULL),
(2,'2025-05-15',0,1,23),
(3,'2025-05-25',0,1,23),
(4,'2025-05-05',100,3,23),
(5,'2025-10-10',0,1,23);
/*!40000 ALTER TABLE `Viagem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=537 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add administrador',7,'add_administrador'),
(26,'Can change administrador',7,'change_administrador'),
(27,'Can delete administrador',7,'delete_administrador'),
(28,'Can view administrador',7,'view_administrador'),
(29,'Can add alerta',8,'add_alerta'),
(30,'Can change alerta',8,'change_alerta'),
(31,'Can delete alerta',8,'delete_alerta'),
(32,'Can view alerta',8,'view_alerta'),
(33,'Can add auth group',9,'add_authgroup'),
(34,'Can change auth group',9,'change_authgroup'),
(35,'Can delete auth group',9,'delete_authgroup'),
(36,'Can view auth group',9,'view_authgroup'),
(37,'Can add auth group permissions',10,'add_authgrouppermissions'),
(38,'Can change auth group permissions',10,'change_authgrouppermissions'),
(39,'Can delete auth group permissions',10,'delete_authgrouppermissions'),
(40,'Can view auth group permissions',10,'view_authgrouppermissions'),
(41,'Can add auth permission',11,'add_authpermission'),
(42,'Can change auth permission',11,'change_authpermission'),
(43,'Can delete auth permission',11,'delete_authpermission'),
(44,'Can view auth permission',11,'view_authpermission'),
(45,'Can add auth user',12,'add_authuser'),
(46,'Can change auth user',12,'change_authuser'),
(47,'Can delete auth user',12,'delete_authuser'),
(48,'Can view auth user',12,'view_authuser'),
(49,'Can add auth user groups',13,'add_authusergroups'),
(50,'Can change auth user groups',13,'change_authusergroups'),
(51,'Can delete auth user groups',13,'delete_authusergroups'),
(52,'Can view auth user groups',13,'view_authusergroups'),
(53,'Can add auth user user permissions',14,'add_authuseruserpermissions'),
(54,'Can change auth user user permissions',14,'change_authuseruserpermissions'),
(55,'Can delete auth user user permissions',14,'delete_authuseruserpermissions'),
(56,'Can view auth user user permissions',14,'view_authuseruserpermissions'),
(57,'Can add avaliacao',15,'add_avaliacao'),
(58,'Can change avaliacao',15,'change_avaliacao'),
(59,'Can delete avaliacao',15,'delete_avaliacao'),
(60,'Can view avaliacao',15,'view_avaliacao'),
(61,'Can add bandeira cartao',16,'add_bandeiracartao'),
(62,'Can change bandeira cartao',16,'change_bandeiracartao'),
(63,'Can delete bandeira cartao',16,'delete_bandeiracartao'),
(64,'Can view bandeira cartao',16,'view_bandeiracartao'),
(65,'Can add carta conducao',17,'add_cartaconducao'),
(66,'Can change carta conducao',17,'change_cartaconducao'),
(67,'Can delete carta conducao',17,'delete_cartaconducao'),
(68,'Can view carta conducao',17,'view_cartaconducao'),
(69,'Can add cartao',18,'add_cartao'),
(70,'Can change cartao',18,'change_cartao'),
(71,'Can delete cartao',18,'delete_cartao'),
(72,'Can view cartao',18,'view_cartao'),
(73,'Can add cartao utilizador',19,'add_cartaoutilizador'),
(74,'Can change cartao utilizador',19,'change_cartaoutilizador'),
(75,'Can delete cartao utilizador',19,'delete_cartaoutilizador'),
(76,'Can view cartao utilizador',19,'view_cartaoutilizador'),
(77,'Can add chat viagem',20,'add_chatviagem'),
(78,'Can change chat viagem',20,'change_chatviagem'),
(79,'Can delete chat viagem',20,'delete_chatviagem'),
(80,'Can view chat viagem',20,'view_chatviagem'),
(81,'Can add condutor',21,'add_condutor'),
(82,'Can change condutor',21,'change_condutor'),
(83,'Can delete condutor',21,'delete_condutor'),
(84,'Can view condutor',21,'view_condutor'),
(85,'Can add condutor veiculo',22,'add_condutorveiculo'),
(86,'Can change condutor veiculo',22,'change_condutorveiculo'),
(87,'Can delete condutor veiculo',22,'delete_condutorveiculo'),
(88,'Can view condutor veiculo',22,'view_condutorveiculo'),
(89,'Can add conselho',23,'add_conselho'),
(90,'Can change conselho',23,'change_conselho'),
(91,'Can delete conselho',23,'delete_conselho'),
(92,'Can view conselho',23,'view_conselho'),
(93,'Can add contacto',24,'add_contacto'),
(94,'Can change contacto',24,'change_contacto'),
(95,'Can delete contacto',24,'delete_contacto'),
(96,'Can view contacto',24,'view_contacto'),
(97,'Can add cor veiculo',25,'add_corveiculo'),
(98,'Can change cor veiculo',25,'change_corveiculo'),
(99,'Can delete cor veiculo',25,'delete_corveiculo'),
(100,'Can view cor veiculo',25,'view_corveiculo'),
(101,'Can add dados mb',26,'add_dadosmb'),
(102,'Can change dados mb',26,'change_dadosmb'),
(103,'Can delete dados mb',26,'delete_dadosmb'),
(104,'Can view dados mb',26,'view_dadosmb'),
(105,'Can add desvio',27,'add_desvio'),
(106,'Can change desvio',27,'change_desvio'),
(107,'Can delete desvio',27,'delete_desvio'),
(108,'Can view desvio',27,'view_desvio'),
(109,'Can add distrito',28,'add_distrito'),
(110,'Can change distrito',28,'change_distrito'),
(111,'Can delete distrito',28,'delete_distrito'),
(112,'Can view distrito',28,'view_distrito'),
(113,'Can add django admin log',29,'add_djangoadminlog'),
(114,'Can change django admin log',29,'change_djangoadminlog'),
(115,'Can delete django admin log',29,'delete_djangoadminlog'),
(116,'Can view django admin log',29,'view_djangoadminlog'),
(117,'Can add django content type',30,'add_djangocontenttype'),
(118,'Can change django content type',30,'change_djangocontenttype'),
(119,'Can delete django content type',30,'delete_djangocontenttype'),
(120,'Can view django content type',30,'view_djangocontenttype'),
(121,'Can add django migrations',31,'add_djangomigrations'),
(122,'Can change django migrations',31,'change_djangomigrations'),
(123,'Can delete django migrations',31,'delete_djangomigrations'),
(124,'Can view django migrations',31,'view_djangomigrations'),
(125,'Can add django session',32,'add_djangosession'),
(126,'Can change django session',32,'change_djangosession'),
(127,'Can delete django session',32,'delete_djangosession'),
(128,'Can view django session',32,'view_djangosession'),
(129,'Can add estado civil',33,'add_estadocivil'),
(130,'Can change estado civil',33,'change_estadocivil'),
(131,'Can delete estado civil',33,'delete_estadocivil'),
(132,'Can view estado civil',33,'view_estadocivil'),
(133,'Can add freguesia',34,'add_freguesia'),
(134,'Can change freguesia',34,'change_freguesia'),
(135,'Can delete freguesia',34,'delete_freguesia'),
(136,'Can view freguesia',34,'view_freguesia'),
(137,'Can add grupo',35,'add_grupo'),
(138,'Can change grupo',35,'change_grupo'),
(139,'Can delete grupo',35,'delete_grupo'),
(140,'Can view grupo',35,'view_grupo'),
(141,'Can add marca veiculo',36,'add_marcaveiculo'),
(142,'Can change marca veiculo',36,'change_marcaveiculo'),
(143,'Can delete marca veiculo',36,'delete_marcaveiculo'),
(144,'Can view marca veiculo',36,'view_marcaveiculo'),
(145,'Can add mensagem',37,'add_mensagem'),
(146,'Can change mensagem',37,'change_mensagem'),
(147,'Can delete mensagem',37,'delete_mensagem'),
(148,'Can view mensagem',37,'view_mensagem'),
(149,'Can add modelo veiculo',38,'add_modeloveiculo'),
(150,'Can change modelo veiculo',38,'change_modeloveiculo'),
(151,'Can delete modelo veiculo',38,'delete_modeloveiculo'),
(152,'Can view modelo veiculo',38,'view_modeloveiculo'),
(153,'Can add morada',39,'add_morada'),
(154,'Can change morada',39,'change_morada'),
(155,'Can delete morada',39,'delete_morada'),
(156,'Can view morada',39,'view_morada'),
(157,'Can add nacionalidade',40,'add_nacionalidade'),
(158,'Can change nacionalidade',40,'change_nacionalidade'),
(159,'Can delete nacionalidade',40,'delete_nacionalidade'),
(160,'Can view nacionalidade',40,'view_nacionalidade'),
(161,'Can add ocorrencia',41,'add_ocorrencia'),
(162,'Can change ocorrencia',41,'change_ocorrencia'),
(163,'Can delete ocorrencia',41,'delete_ocorrencia'),
(164,'Can view ocorrencia',41,'view_ocorrencia'),
(165,'Can add pagamento',42,'add_pagamento'),
(166,'Can change pagamento',42,'change_pagamento'),
(167,'Can delete pagamento',42,'delete_pagamento'),
(168,'Can view pagamento',42,'view_pagamento'),
(169,'Can add pais',43,'add_pais'),
(170,'Can change pais',43,'change_pais'),
(171,'Can delete pais',43,'delete_pais'),
(172,'Can view pais',43,'view_pais'),
(173,'Can add passageiro',44,'add_passageiro'),
(174,'Can change passageiro',44,'change_passageiro'),
(175,'Can delete passageiro',44,'delete_passageiro'),
(176,'Can view passageiro',44,'view_passageiro'),
(177,'Can add passageiro viagem',45,'add_passageiroviagem'),
(178,'Can change passageiro viagem',45,'change_passageiroviagem'),
(179,'Can delete passageiro viagem',45,'delete_passageiroviagem'),
(180,'Can view passageiro viagem',45,'view_passageiroviagem'),
(181,'Can add ponto',46,'add_ponto'),
(182,'Can change ponto',46,'change_ponto'),
(183,'Can delete ponto',46,'delete_ponto'),
(184,'Can view ponto',46,'view_ponto'),
(185,'Can add ponto viagem',47,'add_pontoviagem'),
(186,'Can change ponto viagem',47,'change_pontoviagem'),
(187,'Can delete ponto viagem',47,'delete_pontoviagem'),
(188,'Can view ponto viagem',47,'view_pontoviagem'),
(189,'Can add reserva',48,'add_reserva'),
(190,'Can change reserva',48,'change_reserva'),
(191,'Can delete reserva',48,'delete_reserva'),
(192,'Can view reserva',48,'view_reserva'),
(193,'Can add status desvio',49,'add_statusdesvio'),
(194,'Can change status desvio',49,'change_statusdesvio'),
(195,'Can delete status desvio',49,'delete_statusdesvio'),
(196,'Can view status desvio',49,'view_statusdesvio'),
(197,'Can add status viagem',50,'add_statusviagem'),
(198,'Can change status viagem',50,'change_statusviagem'),
(199,'Can delete status viagem',50,'delete_statusviagem'),
(200,'Can view status viagem',50,'view_statusviagem'),
(201,'Can add suspensao',51,'add_suspensao'),
(202,'Can change suspensao',51,'change_suspensao'),
(203,'Can delete suspensao',51,'delete_suspensao'),
(204,'Can view suspensao',51,'view_suspensao'),
(205,'Can add tipo alerta',52,'add_tipoalerta'),
(206,'Can change tipo alerta',52,'change_tipoalerta'),
(207,'Can delete tipo alerta',52,'delete_tipoalerta'),
(208,'Can view tipo alerta',52,'view_tipoalerta'),
(209,'Can add tipo categoria',53,'add_tipocategoria'),
(210,'Can change tipo categoria',53,'change_tipocategoria'),
(211,'Can delete tipo categoria',53,'delete_tipocategoria'),
(212,'Can view tipo categoria',53,'view_tipocategoria'),
(213,'Can add tipo contacto',54,'add_tipocontacto'),
(214,'Can change tipo contacto',54,'change_tipocontacto'),
(215,'Can delete tipo contacto',54,'delete_tipocontacto'),
(216,'Can view tipo contacto',54,'view_tipocontacto'),
(217,'Can add tipo ocorrencia',55,'add_tipoocorrencia'),
(218,'Can change tipo ocorrencia',55,'change_tipoocorrencia'),
(219,'Can delete tipo ocorrencia',55,'delete_tipoocorrencia'),
(220,'Can view tipo ocorrencia',55,'view_tipoocorrencia'),
(221,'Can add tipo pagamento',56,'add_tipopagamento'),
(222,'Can change tipo pagamento',56,'change_tipopagamento'),
(223,'Can delete tipo pagamento',56,'delete_tipopagamento'),
(224,'Can view tipo pagamento',56,'view_tipopagamento'),
(225,'Can add tipo veiculo',57,'add_tipoveiculo'),
(226,'Can change tipo veiculo',57,'change_tipoveiculo'),
(227,'Can delete tipo veiculo',57,'delete_tipoveiculo'),
(228,'Can view tipo veiculo',57,'view_tipoveiculo'),
(229,'Can add utilizador',58,'add_utilizador'),
(230,'Can change utilizador',58,'change_utilizador'),
(231,'Can delete utilizador',58,'delete_utilizador'),
(232,'Can view utilizador',58,'view_utilizador'),
(233,'Can add veiculo',59,'add_veiculo'),
(234,'Can change veiculo',59,'change_veiculo'),
(235,'Can delete veiculo',59,'delete_veiculo'),
(236,'Can view veiculo',59,'view_veiculo'),
(237,'Can add viagem',60,'add_viagem'),
(238,'Can change viagem',60,'change_viagem'),
(239,'Can delete viagem',60,'delete_viagem'),
(240,'Can view viagem',60,'view_viagem'),
(241,'Can add administrador',61,'add_administrador'),
(242,'Can change administrador',61,'change_administrador'),
(243,'Can delete administrador',61,'delete_administrador'),
(244,'Can view administrador',61,'view_administrador'),
(245,'Can add alerta',62,'add_alerta'),
(246,'Can change alerta',62,'change_alerta'),
(247,'Can delete alerta',62,'delete_alerta'),
(248,'Can view alerta',62,'view_alerta'),
(249,'Can add auth group',63,'add_authgroup'),
(250,'Can change auth group',63,'change_authgroup'),
(251,'Can delete auth group',63,'delete_authgroup'),
(252,'Can view auth group',63,'view_authgroup'),
(253,'Can add auth group permissions',64,'add_authgrouppermissions'),
(254,'Can change auth group permissions',64,'change_authgrouppermissions'),
(255,'Can delete auth group permissions',64,'delete_authgrouppermissions'),
(256,'Can view auth group permissions',64,'view_authgrouppermissions'),
(257,'Can add auth permission',65,'add_authpermission'),
(258,'Can change auth permission',65,'change_authpermission'),
(259,'Can delete auth permission',65,'delete_authpermission'),
(260,'Can view auth permission',65,'view_authpermission'),
(261,'Can add auth user',66,'add_authuser'),
(262,'Can change auth user',66,'change_authuser'),
(263,'Can delete auth user',66,'delete_authuser'),
(264,'Can view auth user',66,'view_authuser'),
(265,'Can add auth user groups',67,'add_authusergroups'),
(266,'Can change auth user groups',67,'change_authusergroups'),
(267,'Can delete auth user groups',67,'delete_authusergroups'),
(268,'Can view auth user groups',67,'view_authusergroups'),
(269,'Can add auth user user permissions',68,'add_authuseruserpermissions'),
(270,'Can change auth user user permissions',68,'change_authuseruserpermissions'),
(271,'Can delete auth user user permissions',68,'delete_authuseruserpermissions'),
(272,'Can view auth user user permissions',68,'view_authuseruserpermissions'),
(273,'Can add avaliacao',69,'add_avaliacao'),
(274,'Can change avaliacao',69,'change_avaliacao'),
(275,'Can delete avaliacao',69,'delete_avaliacao'),
(276,'Can view avaliacao',69,'view_avaliacao'),
(277,'Can add bandeira cartao',70,'add_bandeiracartao'),
(278,'Can change bandeira cartao',70,'change_bandeiracartao'),
(279,'Can delete bandeira cartao',70,'delete_bandeiracartao'),
(280,'Can view bandeira cartao',70,'view_bandeiracartao'),
(281,'Can add carta conducao',71,'add_cartaconducao'),
(282,'Can change carta conducao',71,'change_cartaconducao'),
(283,'Can delete carta conducao',71,'delete_cartaconducao'),
(284,'Can view carta conducao',71,'view_cartaconducao'),
(285,'Can add cartao',72,'add_cartao'),
(286,'Can change cartao',72,'change_cartao'),
(287,'Can delete cartao',72,'delete_cartao'),
(288,'Can view cartao',72,'view_cartao'),
(289,'Can add cartao utilizador',73,'add_cartaoutilizador'),
(290,'Can change cartao utilizador',73,'change_cartaoutilizador'),
(291,'Can delete cartao utilizador',73,'delete_cartaoutilizador'),
(292,'Can view cartao utilizador',73,'view_cartaoutilizador'),
(293,'Can add chat viagem',74,'add_chatviagem'),
(294,'Can change chat viagem',74,'change_chatviagem'),
(295,'Can delete chat viagem',74,'delete_chatviagem'),
(296,'Can view chat viagem',74,'view_chatviagem'),
(297,'Can add condutor',75,'add_condutor'),
(298,'Can change condutor',75,'change_condutor'),
(299,'Can delete condutor',75,'delete_condutor'),
(300,'Can view condutor',75,'view_condutor'),
(301,'Can add condutor veiculo',76,'add_condutorveiculo'),
(302,'Can change condutor veiculo',76,'change_condutorveiculo'),
(303,'Can delete condutor veiculo',76,'delete_condutorveiculo'),
(304,'Can view condutor veiculo',76,'view_condutorveiculo'),
(305,'Can add conselho',77,'add_conselho'),
(306,'Can change conselho',77,'change_conselho'),
(307,'Can delete conselho',77,'delete_conselho'),
(308,'Can view conselho',77,'view_conselho'),
(309,'Can add contacto',78,'add_contacto'),
(310,'Can change contacto',78,'change_contacto'),
(311,'Can delete contacto',78,'delete_contacto'),
(312,'Can view contacto',78,'view_contacto'),
(313,'Can add cor veiculo',79,'add_corveiculo'),
(314,'Can change cor veiculo',79,'change_corveiculo'),
(315,'Can delete cor veiculo',79,'delete_corveiculo'),
(316,'Can view cor veiculo',79,'view_corveiculo'),
(317,'Can add dados mb',80,'add_dadosmb'),
(318,'Can change dados mb',80,'change_dadosmb'),
(319,'Can delete dados mb',80,'delete_dadosmb'),
(320,'Can view dados mb',80,'view_dadosmb'),
(321,'Can add desvio',81,'add_desvio'),
(322,'Can change desvio',81,'change_desvio'),
(323,'Can delete desvio',81,'delete_desvio'),
(324,'Can view desvio',81,'view_desvio'),
(325,'Can add distrito',82,'add_distrito'),
(326,'Can change distrito',82,'change_distrito'),
(327,'Can delete distrito',82,'delete_distrito'),
(328,'Can view distrito',82,'view_distrito'),
(329,'Can add django admin log',83,'add_djangoadminlog'),
(330,'Can change django admin log',83,'change_djangoadminlog'),
(331,'Can delete django admin log',83,'delete_djangoadminlog'),
(332,'Can view django admin log',83,'view_djangoadminlog'),
(333,'Can add django content type',84,'add_djangocontenttype'),
(334,'Can change django content type',84,'change_djangocontenttype'),
(335,'Can delete django content type',84,'delete_djangocontenttype'),
(336,'Can view django content type',84,'view_djangocontenttype'),
(337,'Can add django migrations',85,'add_djangomigrations'),
(338,'Can change django migrations',85,'change_djangomigrations'),
(339,'Can delete django migrations',85,'delete_djangomigrations'),
(340,'Can view django migrations',85,'view_djangomigrations'),
(341,'Can add django session',86,'add_djangosession'),
(342,'Can change django session',86,'change_djangosession'),
(343,'Can delete django session',86,'delete_djangosession'),
(344,'Can view django session',86,'view_djangosession'),
(345,'Can add estado civil',87,'add_estadocivil'),
(346,'Can change estado civil',87,'change_estadocivil'),
(347,'Can delete estado civil',87,'delete_estadocivil'),
(348,'Can view estado civil',87,'view_estadocivil'),
(349,'Can add freguesia',88,'add_freguesia'),
(350,'Can change freguesia',88,'change_freguesia'),
(351,'Can delete freguesia',88,'delete_freguesia'),
(352,'Can view freguesia',88,'view_freguesia'),
(353,'Can add grupo',89,'add_grupo'),
(354,'Can change grupo',89,'change_grupo'),
(355,'Can delete grupo',89,'delete_grupo'),
(356,'Can view grupo',89,'view_grupo'),
(357,'Can add marca veiculo',90,'add_marcaveiculo'),
(358,'Can change marca veiculo',90,'change_marcaveiculo'),
(359,'Can delete marca veiculo',90,'delete_marcaveiculo'),
(360,'Can view marca veiculo',90,'view_marcaveiculo'),
(361,'Can add mensagem',91,'add_mensagem'),
(362,'Can change mensagem',91,'change_mensagem'),
(363,'Can delete mensagem',91,'delete_mensagem'),
(364,'Can view mensagem',91,'view_mensagem'),
(365,'Can add modelo veiculo',92,'add_modeloveiculo'),
(366,'Can change modelo veiculo',92,'change_modeloveiculo'),
(367,'Can delete modelo veiculo',92,'delete_modeloveiculo'),
(368,'Can view modelo veiculo',92,'view_modeloveiculo'),
(369,'Can add morada',93,'add_morada'),
(370,'Can change morada',93,'change_morada'),
(371,'Can delete morada',93,'delete_morada'),
(372,'Can view morada',93,'view_morada'),
(373,'Can add nacionalidade',94,'add_nacionalidade'),
(374,'Can change nacionalidade',94,'change_nacionalidade'),
(375,'Can delete nacionalidade',94,'delete_nacionalidade'),
(376,'Can view nacionalidade',94,'view_nacionalidade'),
(377,'Can add ocorrencia',95,'add_ocorrencia'),
(378,'Can change ocorrencia',95,'change_ocorrencia'),
(379,'Can delete ocorrencia',95,'delete_ocorrencia'),
(380,'Can view ocorrencia',95,'view_ocorrencia'),
(381,'Can add pagamento',96,'add_pagamento'),
(382,'Can change pagamento',96,'change_pagamento'),
(383,'Can delete pagamento',96,'delete_pagamento'),
(384,'Can view pagamento',96,'view_pagamento'),
(385,'Can add pais',97,'add_pais'),
(386,'Can change pais',97,'change_pais'),
(387,'Can delete pais',97,'delete_pais'),
(388,'Can view pais',97,'view_pais'),
(389,'Can add passageiro',98,'add_passageiro'),
(390,'Can change passageiro',98,'change_passageiro'),
(391,'Can delete passageiro',98,'delete_passageiro'),
(392,'Can view passageiro',98,'view_passageiro'),
(393,'Can add passageiro viagem',99,'add_passageiroviagem'),
(394,'Can change passageiro viagem',99,'change_passageiroviagem'),
(395,'Can delete passageiro viagem',99,'delete_passageiroviagem'),
(396,'Can view passageiro viagem',99,'view_passageiroviagem'),
(397,'Can add ponto',100,'add_ponto'),
(398,'Can change ponto',100,'change_ponto'),
(399,'Can delete ponto',100,'delete_ponto'),
(400,'Can view ponto',100,'view_ponto'),
(401,'Can add ponto viagem',101,'add_pontoviagem'),
(402,'Can change ponto viagem',101,'change_pontoviagem'),
(403,'Can delete ponto viagem',101,'delete_pontoviagem'),
(404,'Can view ponto viagem',101,'view_pontoviagem'),
(405,'Can add reserva',102,'add_reserva'),
(406,'Can change reserva',102,'change_reserva'),
(407,'Can delete reserva',102,'delete_reserva'),
(408,'Can view reserva',102,'view_reserva'),
(409,'Can add status desvio',103,'add_statusdesvio'),
(410,'Can change status desvio',103,'change_statusdesvio'),
(411,'Can delete status desvio',103,'delete_statusdesvio'),
(412,'Can view status desvio',103,'view_statusdesvio'),
(413,'Can add status viagem',104,'add_statusviagem'),
(414,'Can change status viagem',104,'change_statusviagem'),
(415,'Can delete status viagem',104,'delete_statusviagem'),
(416,'Can view status viagem',104,'view_statusviagem'),
(417,'Can add suspensao',105,'add_suspensao'),
(418,'Can change suspensao',105,'change_suspensao'),
(419,'Can delete suspensao',105,'delete_suspensao'),
(420,'Can view suspensao',105,'view_suspensao'),
(421,'Can add tipo alerta',106,'add_tipoalerta'),
(422,'Can change tipo alerta',106,'change_tipoalerta'),
(423,'Can delete tipo alerta',106,'delete_tipoalerta'),
(424,'Can view tipo alerta',106,'view_tipoalerta'),
(425,'Can add tipo categoria',107,'add_tipocategoria'),
(426,'Can change tipo categoria',107,'change_tipocategoria'),
(427,'Can delete tipo categoria',107,'delete_tipocategoria'),
(428,'Can view tipo categoria',107,'view_tipocategoria'),
(429,'Can add tipo contacto',108,'add_tipocontacto'),
(430,'Can change tipo contacto',108,'change_tipocontacto'),
(431,'Can delete tipo contacto',108,'delete_tipocontacto'),
(432,'Can view tipo contacto',108,'view_tipocontacto'),
(433,'Can add tipo ocorrencia',109,'add_tipoocorrencia'),
(434,'Can change tipo ocorrencia',109,'change_tipoocorrencia'),
(435,'Can delete tipo ocorrencia',109,'delete_tipoocorrencia'),
(436,'Can view tipo ocorrencia',109,'view_tipoocorrencia'),
(437,'Can add tipo pagamento',110,'add_tipopagamento'),
(438,'Can change tipo pagamento',110,'change_tipopagamento'),
(439,'Can delete tipo pagamento',110,'delete_tipopagamento'),
(440,'Can view tipo pagamento',110,'view_tipopagamento'),
(441,'Can add tipo veiculo',111,'add_tipoveiculo'),
(442,'Can change tipo veiculo',111,'change_tipoveiculo'),
(443,'Can delete tipo veiculo',111,'delete_tipoveiculo'),
(444,'Can view tipo veiculo',111,'view_tipoveiculo'),
(445,'Can add utilizador',112,'add_utilizador'),
(446,'Can change utilizador',112,'change_utilizador'),
(447,'Can delete utilizador',112,'delete_utilizador'),
(448,'Can view utilizador',112,'view_utilizador'),
(449,'Can add veiculo',113,'add_veiculo'),
(450,'Can change veiculo',113,'change_veiculo'),
(451,'Can delete veiculo',113,'delete_veiculo'),
(452,'Can view veiculo',113,'view_veiculo'),
(453,'Can add viagem',114,'add_viagem'),
(454,'Can change viagem',114,'change_viagem'),
(455,'Can delete viagem',114,'delete_viagem'),
(456,'Can view viagem',114,'view_viagem'),
(457,'Can add administrador',115,'add_administrador'),
(458,'Can change administrador',115,'change_administrador'),
(459,'Can delete administrador',115,'delete_administrador'),
(460,'Can view administrador',115,'view_administrador'),
(461,'Can add condutor',116,'add_condutor'),
(462,'Can change condutor',116,'change_condutor'),
(463,'Can delete condutor',116,'delete_condutor'),
(464,'Can view condutor',116,'view_condutor'),
(465,'Can add conselho',117,'add_conselho'),
(466,'Can change conselho',117,'change_conselho'),
(467,'Can delete conselho',117,'delete_conselho'),
(468,'Can view conselho',117,'view_conselho'),
(469,'Can add contacto',118,'add_contacto'),
(470,'Can change contacto',118,'change_contacto'),
(471,'Can delete contacto',118,'delete_contacto'),
(472,'Can view contacto',118,'view_contacto'),
(473,'Can add distrito',119,'add_distrito'),
(474,'Can change distrito',119,'change_distrito'),
(475,'Can delete distrito',119,'delete_distrito'),
(476,'Can view distrito',119,'view_distrito'),
(477,'Can add estado civil',120,'add_estadocivil'),
(478,'Can change estado civil',120,'change_estadocivil'),
(479,'Can delete estado civil',120,'delete_estadocivil'),
(480,'Can view estado civil',120,'view_estadocivil'),
(481,'Can add freguesia',121,'add_freguesia'),
(482,'Can change freguesia',121,'change_freguesia'),
(483,'Can delete freguesia',121,'delete_freguesia'),
(484,'Can view freguesia',121,'view_freguesia'),
(485,'Can add grupo',122,'add_grupo'),
(486,'Can change grupo',122,'change_grupo'),
(487,'Can delete grupo',122,'delete_grupo'),
(488,'Can view grupo',122,'view_grupo'),
(489,'Can add morada',123,'add_morada'),
(490,'Can change morada',123,'change_morada'),
(491,'Can delete morada',123,'delete_morada'),
(492,'Can view morada',123,'view_morada'),
(493,'Can add nacionalidade',124,'add_nacionalidade'),
(494,'Can change nacionalidade',124,'change_nacionalidade'),
(495,'Can delete nacionalidade',124,'delete_nacionalidade'),
(496,'Can view nacionalidade',124,'view_nacionalidade'),
(497,'Can add pais',125,'add_pais'),
(498,'Can change pais',125,'change_pais'),
(499,'Can delete pais',125,'delete_pais'),
(500,'Can view pais',125,'view_pais'),
(501,'Can add passageiro',126,'add_passageiro'),
(502,'Can change passageiro',126,'change_passageiro'),
(503,'Can delete passageiro',126,'delete_passageiro'),
(504,'Can view passageiro',126,'view_passageiro'),
(505,'Can add suspensao',127,'add_suspensao'),
(506,'Can change suspensao',127,'change_suspensao'),
(507,'Can delete suspensao',127,'delete_suspensao'),
(508,'Can view suspensao',127,'view_suspensao'),
(509,'Can add tipo contacto',128,'add_tipocontacto'),
(510,'Can change tipo contacto',128,'change_tipocontacto'),
(511,'Can delete tipo contacto',128,'delete_tipocontacto'),
(512,'Can view tipo contacto',128,'view_tipocontacto'),
(513,'Can add utilizador',129,'add_utilizador'),
(514,'Can change utilizador',129,'change_utilizador'),
(515,'Can delete utilizador',129,'delete_utilizador'),
(516,'Can view utilizador',129,'view_utilizador'),
(517,'Can add blacklisted token',130,'add_blacklistedtoken'),
(518,'Can change blacklisted token',130,'change_blacklistedtoken'),
(519,'Can delete blacklisted token',130,'delete_blacklistedtoken'),
(520,'Can view blacklisted token',130,'view_blacklistedtoken'),
(521,'Can add outstanding token',131,'add_outstandingtoken'),
(522,'Can change outstanding token',131,'change_outstandingtoken'),
(523,'Can delete outstanding token',131,'delete_outstandingtoken'),
(524,'Can view outstanding token',131,'view_outstandingtoken'),
(525,'Can add ponto desvio',132,'add_pontodesvio'),
(526,'Can change ponto desvio',132,'change_pontodesvio'),
(527,'Can delete ponto desvio',132,'delete_pontodesvio'),
(528,'Can view ponto desvio',132,'view_pontodesvio'),
(529,'Can add ponto reserva',133,'add_pontoreserva'),
(530,'Can change ponto reserva',133,'change_pontoreserva'),
(531,'Can delete ponto reserva',133,'delete_pontoreserva'),
(532,'Can view ponto reserva',133,'view_pontoreserva'),
(533,'Can add status reserva',134,'add_statusreserva'),
(534,'Can change status reserva',134,'change_statusreserva'),
(535,'Can delete status reserva',134,'delete_statusreserva'),
(536,'Can view status reserva',134,'view_statusreserva');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES
(1,'pbkdf2_sha256$870000$ZWscbjfovoz6sVnnAiA49E$W5ltTmLoN7/1+EClMISzey8cO0kWG5IQqEqSYqJJryM=','2025-04-08 16:10:54.693960',1,'admin','','',1,1,'2025-04-01 16:29:14.926467');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES
(1,'2025-04-01 19:04:07.218938','1','Grupo object (1)',1,'[{\"added\": {}}]',35,1),
(2,'2025-04-01 19:04:51.011165','1','EstadoCivil object (1)',1,'[{\"added\": {}}]',33,1),
(3,'2025-04-01 19:05:31.729206','1','Grupo object (1)',2,'[{\"changed\": {\"fields\": [\"Nome\"]}}]',35,1),
(4,'2025-04-01 19:06:23.310099','1','Pais object (1)',1,'[{\"added\": {}}]',43,1),
(5,'2025-04-01 19:06:39.741776','1','Nacionalidade object (1)',1,'[{\"added\": {}}]',40,1),
(6,'2025-04-01 19:14:55.464247','1','Utilizador object (1)',1,'[{\"added\": {}}]',58,1),
(7,'2025-04-01 19:17:18.282384','3','Utilizador object (3)',1,'[{\"added\": {}}]',58,1),
(8,'2025-04-01 20:40:19.680238','2','Utilizador object (2)',2,'[{\"changed\": {\"fields\": [\"Senha\"]}}]',58,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=135 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES
(1,'admin','logentry'),
(61,'api_auth','administrador'),
(62,'api_auth','alerta'),
(63,'api_auth','authgroup'),
(64,'api_auth','authgrouppermissions'),
(65,'api_auth','authpermission'),
(66,'api_auth','authuser'),
(67,'api_auth','authusergroups'),
(68,'api_auth','authuseruserpermissions'),
(69,'api_auth','avaliacao'),
(70,'api_auth','bandeiracartao'),
(71,'api_auth','cartaconducao'),
(72,'api_auth','cartao'),
(73,'api_auth','cartaoutilizador'),
(74,'api_auth','chatviagem'),
(75,'api_auth','condutor'),
(76,'api_auth','condutorveiculo'),
(77,'api_auth','conselho'),
(78,'api_auth','contacto'),
(79,'api_auth','corveiculo'),
(80,'api_auth','dadosmb'),
(81,'api_auth','desvio'),
(82,'api_auth','distrito'),
(83,'api_auth','djangoadminlog'),
(84,'api_auth','djangocontenttype'),
(85,'api_auth','djangomigrations'),
(86,'api_auth','djangosession'),
(87,'api_auth','estadocivil'),
(88,'api_auth','freguesia'),
(89,'api_auth','grupo'),
(90,'api_auth','marcaveiculo'),
(91,'api_auth','mensagem'),
(92,'api_auth','modeloveiculo'),
(93,'api_auth','morada'),
(94,'api_auth','nacionalidade'),
(95,'api_auth','ocorrencia'),
(96,'api_auth','pagamento'),
(97,'api_auth','pais'),
(98,'api_auth','passageiro'),
(99,'api_auth','passageiroviagem'),
(100,'api_auth','ponto'),
(101,'api_auth','pontoviagem'),
(102,'api_auth','reserva'),
(103,'api_auth','statusdesvio'),
(104,'api_auth','statusviagem'),
(105,'api_auth','suspensao'),
(106,'api_auth','tipoalerta'),
(107,'api_auth','tipocategoria'),
(108,'api_auth','tipocontacto'),
(109,'api_auth','tipoocorrencia'),
(110,'api_auth','tipopagamento'),
(111,'api_auth','tipoveiculo'),
(112,'api_auth','utilizador'),
(113,'api_auth','veiculo'),
(114,'api_auth','viagem'),
(115,'autenticacao','administrador'),
(116,'autenticacao','condutor'),
(117,'autenticacao','conselho'),
(118,'autenticacao','contacto'),
(119,'autenticacao','distrito'),
(120,'autenticacao','estadocivil'),
(121,'autenticacao','freguesia'),
(122,'autenticacao','grupo'),
(123,'autenticacao','morada'),
(124,'autenticacao','nacionalidade'),
(125,'autenticacao','pais'),
(126,'autenticacao','passageiro'),
(127,'autenticacao','suspensao'),
(128,'autenticacao','tipocontacto'),
(129,'autenticacao','utilizador'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(7,'projeto','administrador'),
(8,'projeto','alerta'),
(9,'projeto','authgroup'),
(10,'projeto','authgrouppermissions'),
(11,'projeto','authpermission'),
(12,'projeto','authuser'),
(13,'projeto','authusergroups'),
(14,'projeto','authuseruserpermissions'),
(15,'projeto','avaliacao'),
(16,'projeto','bandeiracartao'),
(17,'projeto','cartaconducao'),
(18,'projeto','cartao'),
(19,'projeto','cartaoutilizador'),
(20,'projeto','chatviagem'),
(21,'projeto','condutor'),
(22,'projeto','condutorveiculo'),
(23,'projeto','conselho'),
(24,'projeto','contacto'),
(25,'projeto','corveiculo'),
(26,'projeto','dadosmb'),
(27,'projeto','desvio'),
(28,'projeto','distrito'),
(29,'projeto','djangoadminlog'),
(30,'projeto','djangocontenttype'),
(31,'projeto','djangomigrations'),
(32,'projeto','djangosession'),
(33,'projeto','estadocivil'),
(34,'projeto','freguesia'),
(35,'projeto','grupo'),
(36,'projeto','marcaveiculo'),
(37,'projeto','mensagem'),
(38,'projeto','modeloveiculo'),
(39,'projeto','morada'),
(40,'projeto','nacionalidade'),
(41,'projeto','ocorrencia'),
(42,'projeto','pagamento'),
(43,'projeto','pais'),
(44,'projeto','passageiro'),
(45,'projeto','passageiroviagem'),
(46,'projeto','ponto'),
(132,'projeto','pontodesvio'),
(133,'projeto','pontoreserva'),
(47,'projeto','pontoviagem'),
(48,'projeto','reserva'),
(49,'projeto','statusdesvio'),
(134,'projeto','statusreserva'),
(50,'projeto','statusviagem'),
(51,'projeto','suspensao'),
(52,'projeto','tipoalerta'),
(53,'projeto','tipocategoria'),
(54,'projeto','tipocontacto'),
(55,'projeto','tipoocorrencia'),
(56,'projeto','tipopagamento'),
(57,'projeto','tipoveiculo'),
(58,'projeto','utilizador'),
(59,'projeto','veiculo'),
(60,'projeto','viagem'),
(6,'sessions','session'),
(130,'token_blacklist','blacklistedtoken'),
(131,'token_blacklist','outstandingtoken');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES
(1,'contenttypes','0001_initial','2025-04-01 15:58:09.825297'),
(2,'auth','0001_initial','2025-04-01 15:58:10.063457'),
(3,'admin','0001_initial','2025-04-01 15:58:10.110954'),
(4,'admin','0002_logentry_remove_auto_add','2025-04-01 15:58:10.115433'),
(5,'admin','0003_logentry_add_action_flag_choices','2025-04-01 15:58:10.120335'),
(6,'contenttypes','0002_remove_content_type_name','2025-04-01 15:58:10.159167'),
(18,'sessions','0001_initial','2025-04-01 15:58:10.314113'),
(19,'projeto','0001_initial','2025-04-01 16:28:14.609771'),
(20,'api_auth','0001_initial','2025-04-02 22:42:36.491507'),
(21,'autenticacao','0001_initial','2025-04-16 18:40:12.402687'),
(22,'token_blacklist','0001_initial','2025-04-17 12:59:48.808606'),
(23,'token_blacklist','0002_outstandingtoken_jti_hex','2025-04-17 12:59:48.825794'),
(24,'token_blacklist','0003_auto_20171017_2007','2025-04-17 12:59:48.841168'),
(25,'token_blacklist','0004_auto_20171017_2013','2025-04-17 12:59:48.880199'),
(26,'token_blacklist','0005_remove_outstandingtoken_jti','2025-04-17 12:59:48.900607'),
(27,'token_blacklist','0006_auto_20171017_2113','2025-04-17 12:59:48.917417'),
(28,'token_blacklist','0007_auto_20171017_2214','2025-04-17 12:59:49.006564'),
(29,'token_blacklist','0008_migrate_to_bigautofield','2025-04-17 12:59:49.107773'),
(30,'token_blacklist','0010_fix_migrate_to_bigautofield','2025-04-17 12:59:49.115800'),
(31,'token_blacklist','0011_linearizes_history','2025-04-17 12:59:49.117260'),
(32,'token_blacklist','0012_alter_outstandingtoken_user','2025-04-17 12:59:49.122926'),
(33,'projeto','0002_alter_utilizador_options','2025-04-18 21:14:37.338544'),
(53,'auth','0002_alter_permission_name_max_length','2025-04-29 18:39:49.458425'),
(54,'auth','0003_alter_user_email_max_length','2025-04-29 18:39:58.874227'),
(55,'auth','0004_alter_user_username_opts','2025-04-29 18:39:58.878132'),
(56,'auth','0005_alter_user_last_login_null','2025-04-29 18:39:58.882070'),
(57,'auth','0006_require_contenttypes_0002','2025-04-29 18:39:58.883470'),
(58,'auth','0007_alter_validators_add_error_messages','2025-04-29 18:39:58.886630'),
(59,'auth','0008_alter_user_username_max_length','2025-04-29 18:39:58.890719'),
(60,'auth','0009_alter_user_last_name_max_length','2025-04-29 18:39:58.893770'),
(61,'auth','0010_alter_group_name_max_length','2025-04-29 18:39:58.909319'),
(62,'auth','0011_update_proxy_permissions','2025-04-29 18:39:58.922375'),
(63,'auth','0012_alter_user_first_name_max_length','2025-04-29 18:39:58.926486'),
(64,'projeto','0002_alter_estadocivil_options_and_more','2025-04-29 20:14:45.568945'),
(65,'projeto','0002_alter_utilizador_grupoid_grupo','2025-04-29 20:32:14.966423'),
(66,'projeto','0003_alter_utilizador_estado_civilid_estado_civil_and_more','2025-04-29 20:39:00.618552'),
(67,'projeto','0004_alter_grupo_options_and_more','2025-04-29 20:43:16.906269');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES
('0s0kzzginhkaxj0bgufwx1vq3fb0vwkg','.eJxVjDsOwyAQBe9CHaEFL2BSpvcZ0PILTiKQjF1FuXtsyUXSvpl5b-ZoW4vbelrcHNmVCXb53TyFZ6oHiA-q98ZDq-sye34o_KSdTy2m1-10_w4K9bLXOknQNns0RpgsEEAhGCCrRgg0kIwQJOQRB_QmJE1K7BjBoh5M0Jl9vq6rNm4:1tzfeH:JXeJJN4edNMqLMxQaTfbauYEtASUKSI_xCXj3beTcp0','2025-04-15 17:43:41.847076'),
('acqgno9qfad8kayr4kbplzek63mg69u1','.eJxVjDsOwyAQBe9CHaEFL2BSpvcZ0PILTiKQjF1FuXtsyUXSvpl5b-ZoW4vbelrcHNmVCXb53TyFZ6oHiA-q98ZDq-sye34o_KSdTy2m1-10_w4K9bLXOknQNns0RpgsEEAhGCCrRgg0kIwQJOQRB_QmJE1K7BjBoh5M0Jl9vq6rNm4:1tzg9v:5Mk_q3s7wmfea8Pn7ipPIhmH78-nd4oNMnzpNlRLTKE','2025-04-15 18:16:23.414282'),
('dg72qclk5ufgvp0jb69aa239mkucc3v2','.eJxVjDsOwyAQBe9CHaEFL2BSpvcZ0PILTiKQjF1FuXtsyUXSvpl5b-ZoW4vbelrcHNmVCXb53TyFZ6oHiA-q98ZDq-sye34o_KSdTy2m1-10_w4K9bLXOknQNns0RpgsEEAhGCCrRgg0kIwQJOQRB_QmJE1K7BjBoh5M0Jl9vq6rNm4:1u2BXK:UI2APUxvPTJqXlZAnuM6_taLXEEX0g8LOWjF8rtJ8qs','2025-04-22 16:10:54.695487'),
('djdp4kz37vkn09kd8aoqgq22kwzzy58h','.eJxVjDsOwjAQBe_iGlneZP0JJT1nsNbeBQeQI8VJhbg7spQC2jcz760i7VuJe5M1zqzOCkCdfsdE-Sm1E35QvS86L3Vb56S7og_a9HVheV0O9--gUCu95hFtMGniMGXLTAkzBkRyIyZxJI49QPDhJmCHZBiM4UGcRweZDKrPFxJKN_g:1u98q5:uulOyK9vxH9BI3OhpuQKy7pD-oSTW9IHaEk9Wjo4aFU','2025-05-11 20:43:01.163605');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token_blacklist_blacklistedtoken`
--

DROP TABLE IF EXISTS `token_blacklist_blacklistedtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `token_blacklist_blacklistedtoken` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `blacklisted_at` datetime(6) NOT NULL,
  `token_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_id` (`token_id`),
  CONSTRAINT `token_blacklist_blacklistedtoken_token_id_3cc7fe56_fk` FOREIGN KEY (`token_id`) REFERENCES `token_blacklist_outstandingtoken` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token_blacklist_blacklistedtoken`
--

LOCK TABLES `token_blacklist_blacklistedtoken` WRITE;
/*!40000 ALTER TABLE `token_blacklist_blacklistedtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `token_blacklist_blacklistedtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token_blacklist_outstandingtoken`
--

DROP TABLE IF EXISTS `token_blacklist_outstandingtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `token_blacklist_outstandingtoken` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `token` longtext NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `expires_at` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `jti` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_blacklist_outstandingtoken_jti_hex_d9bdf6f7_uniq` (`jti`),
  KEY `token_blacklist_outs_user_id_83bc629a_fk_auth_user` (`user_id`),
  CONSTRAINT `token_blacklist_outs_user_id_83bc629a_fk_auth_user` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token_blacklist_outstandingtoken`
--

LOCK TABLES `token_blacklist_outstandingtoken` WRITE;
/*!40000 ALTER TABLE `token_blacklist_outstandingtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `token_blacklist_outstandingtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'proj2'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2025-04-30 19:28:27
