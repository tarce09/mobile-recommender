CREATE DATABASE  IF NOT EXISTS `mobile1` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `mobile1`;
-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: mobile1
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `mobile_mobile1`
--

DROP TABLE IF EXISTS `mobile_mobile1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mobile_mobile1` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Brand` varchar(50) NOT NULL,
  `ProductName` varchar(100) NOT NULL,
  `big_img0` varchar(500) NOT NULL,
  `big_img1` varchar(500) NOT NULL,
  `big_img2` varchar(500) NOT NULL,
  `big_img3` varchar(500) NOT NULL,
  `big_img4` varchar(500) NOT NULL,
  `big_img5` varchar(500) NOT NULL,
  `big_img6` varchar(500) NOT NULL,
  `img` varchar(500) NOT NULL,
  `storage_info` varchar(500) NOT NULL,
  `display_info` varchar(500) NOT NULL,
  `cam_info` varchar(500) NOT NULL,
  `battery_info` varchar(500) NOT NULL,
  `processor_info` varchar(500) NOT NULL,
  `display_type` varchar(500) NOT NULL,
  `link` varchar(500) NOT NULL,
  `Product_price` varchar(15) NOT NULL,
  `Product_rating` varchar(5) NOT NULL,
  `about_phone` varchar(1000) NOT NULL,
  `battery_id` int NOT NULL,
  `camera_id` int NOT NULL,
  `display_id` int NOT NULL,
  `processor_id` int NOT NULL,
  `ram_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mobile_mobile1_battery_id_d77bfb75_fk_mobile_battery_id` (`battery_id`),
  KEY `mobile_mobile1_camera_id_273876be_fk_mobile_camera_id` (`camera_id`),
  KEY `mobile_mobile1_display_id_817d8260_fk_mobile_display_id` (`display_id`),
  KEY `mobile_mobile1_processor_id_6b376266_fk_mobile_processor_id` (`processor_id`),
  KEY `mobile_mobile1_ram_id_ca7a5e35_fk_mobile_ram_id` (`ram_id`),
  CONSTRAINT `mobile_mobile1_battery_id_d77bfb75_fk_mobile_battery_id` FOREIGN KEY (`battery_id`) REFERENCES `mobile_battery` (`id`),
  CONSTRAINT `mobile_mobile1_camera_id_273876be_fk_mobile_camera_id` FOREIGN KEY (`camera_id`) REFERENCES `mobile_camera` (`id`),
  CONSTRAINT `mobile_mobile1_display_id_817d8260_fk_mobile_display_id` FOREIGN KEY (`display_id`) REFERENCES `mobile_display` (`id`),
  CONSTRAINT `mobile_mobile1_processor_id_6b376266_fk_mobile_processor_id` FOREIGN KEY (`processor_id`) REFERENCES `mobile_processor` (`id`),
  CONSTRAINT `mobile_mobile1_ram_id_ca7a5e35_fk_mobile_ram_id` FOREIGN KEY (`ram_id`) REFERENCES `mobile_ram` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=117 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-30 21:11:40
