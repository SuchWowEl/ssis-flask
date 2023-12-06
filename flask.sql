CREATE DATABASE  IF NOT EXISTS `ssis` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `ssis`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: ssis
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `college`
--

DROP TABLE IF EXISTS `college`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `college` (
  `code` varchar(10) NOT NULL,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college`
--

LOCK TABLES `college` WRITE;
/*!40000 ALTER TABLE `college` DISABLE KEYS */;
INSERT INTO `college` VALUES ('CASS','College Of Arts And Social Sciences'),('CCS','College of Computer Science'),('CEBA','College of Business Administration & Accountancy'),('COE','College of Education'),('COET','College of Engineering and Technology'),('CON','College of Nursing');
/*!40000 ALTER TABLE `college` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course` (
  `code` varchar(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  `college` varchar(10) NOT NULL,
  PRIMARY KEY (`code`),
  KEY `course_FK` (`college`),
  CONSTRAINT `course_FK` FOREIGN KEY (`college`) REFERENCES `college` (`code`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES ('BS Psych','Bachelor of Science in Psychology','CASS'),('BSCA','Bachelor of Science in Computer Applications','CCS'),('BSChE','Bachelor of Science in Chemical Engineering','COET'),('BSCS','Bachelor of Science in Computer Science','CCS'),('BSECE','Bachelor of Science in Electrical and Communications Engineering','COET'),('BSIS','Bachelor of Science in Information Systems','CCS');
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `id` varchar(9) NOT NULL,
  `firstname` varchar(30) NOT NULL,
  `lastname` varchar(20) NOT NULL,
  `course` varchar(10) NOT NULL,
  `year` int NOT NULL,
  `gender` varchar(6) NOT NULL,
  `profile_pic` text,
  `time_updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `student_FK` (`course`),
  CONSTRAINT `student_FK` FOREIGN KEY (`course`) REFERENCES `course` (`code`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('1111-1111','Chet','Holmgren','BSCA',3,'Others','','2023-12-06 14:16:28'),('2021-0440','Albert','Einsten','BSECE',2,'Others','','2023-12-06 10:45:48'),('2021-0441','Kobe','Bryant','BSCS',3,'Male',NULL,'2023-12-06 10:30:39'),('2021-1201','John','Doe','BS Psych',1,'Male',NULL,'2023-12-06 10:30:39'),('2021-4513','Johnny','Bravo','BSIS',3,'Female',NULL,'2023-12-06 10:30:39'),('2022-0028','Sophia','Anderson','BSCA',2,'Female',NULL,'2023-12-06 10:30:39'),('2022-0057','Daniel','Martinez','BS Psych',1,'Male',NULL,'2023-12-06 10:30:39'),('2022-0118','Ava','Johnson','BSIS',3,'Female',NULL,'2023-12-06 10:30:39'),('2022-0122','Olivia','Harris','BSCS',1,'Female',NULL,'2023-12-06 10:30:39'),('2022-0141','Matthew','Smith','BSECE',2,'Male',NULL,'2023-12-06 10:30:39'),('2022-0202','Jane','Smith','BSCA',2,'Female',NULL,'2023-12-06 10:30:39'),('2022-0219','Oliver','Lee','BS Psych',1,'Male',NULL,'2023-12-06 10:30:39'),('2022-0230','Alexander','Brown','BS Psych',1,'Male',NULL,'2023-12-06 10:30:39'),('2022-0234','Olivia','Harris','BSCS',1,'Female',NULL,'2023-12-06 10:30:39'),('2022-0236','Mia','Rodriguez','BSIS',3,'Female',NULL,'2023-12-06 10:30:39'),('2022-0238','Avery','Taylor','BSCA',2,'Female',NULL,'2023-12-06 10:30:39'),('2022-0243','Michael','Johnson','BSChE',3,'Male',NULL,'2023-12-06 10:30:39'),('2022-0306','Emily','Lee','BSIS',3,'Female',NULL,'2023-12-06 10:30:39'),('2022-0314','Isabella','Taylor','BSCA',2,'Female',NULL,'2023-12-06 10:30:39'),('2022-0316','Sophia','Garcia','BSCS',1,'Female',NULL,'2023-12-06 10:30:39'),('2022-0343','Ethan','White','BS Psych',1,'Male',NULL,'2023-12-06 10:30:39'),('2022-0428','Sophia','Garcia','BSCS',1,'Female',NULL,'2023-12-06 10:30:39'),('2022-0513','Liam','Brown','BS Psych',1,'Male',NULL,'2023-12-06 10:30:39'),('2022-0539','Daniel','Moore','BSChE',3,'Male',NULL,'2023-12-06 10:30:39'),('2022-0544','Alice','Wilson','BSCS',1,'Female',NULL,'2023-12-06 10:30:39'),('2022-0642','Scarlett','Brown','BSIS',3,'Others',NULL,'2023-12-06 10:30:39'),('2022-0820','Emma','White','BSCA',2,'Female',NULL,'2023-12-06 10:30:39'),('2022-1009','Noah','Harris','BSChE',3,'Male',NULL,'2023-12-06 10:30:39'),('2022-1015','Mason','Moore','BSChE',3,'Male',NULL,'2023-12-06 10:30:39'),('2022-1017','Elijah','Smith','BSECE',2,'Male',NULL,'2023-12-06 10:30:39'),('2022-1033','Jack','Martinez','BSChE',3,'Male',NULL,'2023-12-06 10:30:39'),('2022-1044','Chloe','Martinez','BSCA',2,'Female',NULL,'2023-12-06 10:30:39'),('2022-1226','Mia','Smith','BSCA',2,'Female',NULL,'2023-12-06 10:30:39'),('2022-2023','James','Gonzalez','BSECE',2,'Others',NULL,'2023-12-06 10:30:39'),('2022-2024','Charlotte','Rodriguez','BSIS',3,'Female',NULL,'2023-12-06 10:30:39'),('2022-2037','Samuel','Smith','BS Psych',1,'Male',NULL,'2023-12-06 10:30:39'),('2022-3010','Olivia','Gonzalez','BSCS',1,'Female',NULL,'2023-12-06 10:30:39'),('2022-3011','Ethan','Rodriguez','BSECE',2,'Male',NULL,'2023-12-06 10:30:39'),('2022-3032','Ella','Johnson','BSCA',2,'Female',NULL,'2023-12-06 10:30:39'),('2022-4019','Ava','Smith','BSIS',3,'Female',NULL,'2023-12-06 10:30:39'),('2022-4225','Benjamin','Brown','BS Psych',1,'Male',NULL,'2023-12-06 10:30:39'),('2022-5035','Jackson','Gonzalez','BSECE',2,'Others',NULL,'2023-12-06 10:30:39'),('2022-7027','Lucas','Moore','BSChE',3,'Male',NULL,'2023-12-06 10:30:39'),('2022-7040','Ava','Garcia','BSCS',1,'Female',NULL,'2023-12-06 10:30:39'),('2022-8029','Henry','White','BSECE',2,'Male',NULL,'2023-12-06 10:30:39'),('2022-8030','Amelia','Smith','BSIS',3,'Others',NULL,'2023-12-06 10:30:39'),('2022-9021','William','Martinez','BSChE',3,'Male',NULL,'2023-12-06 10:30:39'),('2022-9205','David','Brown','BSECE',2,'Male',NULL,'2023-12-06 10:30:39'),('2321-3213','bert','hellow','BS Psych',2,'Male',NULL,'2023-12-06 10:30:39'),('3123-6593','aaaaaaaa','sa','BS Psych',2,'Male',NULL,'2023-12-06 10:30:39');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-20 23:18:27
