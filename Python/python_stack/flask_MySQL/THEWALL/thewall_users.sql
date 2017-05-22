-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: 127.0.0.1    Database: thewall
-- ------------------------------------------------------
-- Server version	5.6.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'Refayat','Haque','refayathaque@gmail.com','5f4dcc3b5aa765d61d8327deb882cf99','2017-05-19 21:14:21','2017-05-19 21:14:21'),(3,'Johnny','Capitula','johnny@email.com','5f4dcc3b5aa765d61d8327deb882cf99','2017-05-20 10:54:02','2017-05-20 10:54:02'),(4,'Patrick','Starfish','patrick@email.com','5f4dcc3b5aa765d61d8327deb882cf99','2017-05-20 11:26:13','2017-05-20 11:26:13'),(5,'Honda','Civic','honda@email.com','5f4dcc3b5aa765d61d8327deb882cf99','2017-05-20 13:31:58','2017-05-20 13:31:58'),(6,'Frank','Munoz','frank@email.com','5f4dcc3b5aa765d61d8327deb882cf99','2017-05-20 14:59:49','2017-05-20 14:59:49'),(7,'Jeffrey','Wright','jeffrey@email.com','5f4dcc3b5aa765d61d8327deb882cf99','2017-05-20 15:02:33','2017-05-20 15:02:33'),(8,'George','Lopez','lopez@email.com','5f4dcc3b5aa765d61d8327deb882cf99','2017-05-20 15:03:15','2017-05-20 15:03:15'),(9,'George','Lopez','lopez@email.com','5f4dcc3b5aa765d61d8327deb882cf99','2017-05-20 15:04:44','2017-05-20 15:04:44'),(10,'Micahel','Curreri','curreri@email.com','5f4dcc3b5aa765d61d8327deb882cf99','2017-05-20 15:05:24','2017-05-20 15:05:24'),(11,'Daniel','Maramis','dmaramis@email.com','5f4dcc3b5aa765d61d8327deb882cf99','2017-05-20 15:51:08','2017-05-20 15:51:08');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-05-22 11:54:33
