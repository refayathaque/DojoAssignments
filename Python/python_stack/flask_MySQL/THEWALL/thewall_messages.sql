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
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` text,
  `created_at` varchar(255) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `created_at_MySQL_form` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_users_idx` (`user_id`),
  CONSTRAINT `fk_messages_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (3,'Test','2017-05-19 22:30:45','2017-05-19 22:30:45',2,NULL),(4,'Test 2','2017-05-19 22:32:01','2017-05-19 22:32:01',2,NULL),(5,'test','2017-05-19 22:33:13','2017-05-19 22:33:13',2,NULL),(6,'Another test message','2017-05-19 22:34:26','2017-05-19 22:34:26',2,NULL),(7,'TestTestTes','2017-05-19 22:51:31','2017-05-19 22:51:31',2,NULL),(8,'JohnnyRockets','2017-05-19 22:53:33','2017-05-19 22:53:33',2,NULL),(9,'hellohellohello','2017-05-19 22:56:18','2017-05-19 22:56:18',2,NULL),(10,'Another test!','2017-05-19 22:57:08','2017-05-19 22:57:08',2,NULL),(11,'Jesus Christ!','2017-05-19 22:57:28','2017-05-19 22:57:28',2,NULL),(12,'What\'s going on?','2017-05-19 22:57:41','2017-05-19 22:57:41',2,NULL),(13,'Shotta!','2017-05-19 22:58:26','2017-05-19 22:58:26',2,NULL),(14,'Check this out Ausar!','2017-05-19 22:58:37','2017-05-19 22:58:37',2,NULL),(15,'What\'s up mayne?','2017-05-19 22:59:00','2017-05-19 22:59:00',2,NULL),(16,'Hello friends!','0000-00-00 00:00:00','2017-05-19 23:01:55',2,NULL),(17,'Hello!','2017-05-19 23:06:10','2017-05-19 23:06:10',2,NULL),(18,'Hi!','2017-05-19 23:16:37','2017-05-19 23:16:37',2,NULL),(19,'Yoooooooo','2017-05-20 08:59:16','2017-05-20 08:59:16',2,NULL),(20,'fsdfdsafkldjgdakjf;dafjsad','2017-05-20 09:35:21','2017-05-20 09:35:21',2,NULL),(21,'hellopooooopfsdfkjldhgda',NULL,'2017-05-20 09:45:02',2,NULL),(22,'fadksfhasdkfhs;adkfjasd',NULL,'2017-05-20 09:46:52',2,NULL),(23,'fkjhsdalkfjas;dkfdsafdsaf','0000-00-00 00:00:00','2017-05-20 10:14:26',2,NULL),(24,'fdsafasdfasdfsadf','0000-00-00 00:00:00','2017-05-20 10:14:31',2,NULL),(25,'fsfdasdfasdfsd','0000-00-00 00:00:00','2017-05-20 10:15:51',2,NULL),(26,'WHY WONT THIS WORK','0000-00-00 00:00:00','2017-05-20 10:16:17',2,NULL),(27,'heloooooooooooo','0000-00-00 00:00:00','2017-05-20 10:16:43',2,NULL),(28,'YOUYOOKNFS','May 20 2017 10:19 AM','2017-05-20 10:19:08',2,NULL),(29,'fsfasdfasdf','May 20 2017 at 10:21 AM','2017-05-20 10:21:11',2,NULL),(30,'fsdafasdfsafds','May 20 2017 at 10:21AM','2017-05-20 10:21:35',2,NULL),(31,'kjfsdklfjasd;kfljasd;klfasf','May 20 2017 at 10:22 AM','2017-05-20 10:22:02',2,NULL),(32,'fskjdfhadslkfjhsad;kfaskfjdasf','May 20 2017 at 10:24 AM','2017-05-20 10:24:40',2,'2017-05-20 10:24:40'),(33,'fkjsdhfksdfsdjfkla;sdfasdfasdf','May 20 2017 at 10:53 AM','2017-05-20 10:53:40',2,'2017-05-20 10:53:40'),(34,'Hello friends!','May 20 2017 at 10:54 AM','2017-05-20 10:54:09',3,'2017-05-20 10:54:09'),(35,'gobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of textgobs of text','May 20 2017 at 10:54 AM','2017-05-20 10:54:54',3,'2017-05-20 10:54:54'),(36,'hey man!','May 20 2017 at 11:02 AM','2017-05-20 11:02:28',3,'2017-05-20 11:02:28'),(37,'fsdfasdfasdf','May 20 2017 at 11:02 AM','2017-05-20 11:02:39',3,'2017-05-20 11:02:39'),(38,'Hey man!','May 20 2017 at 11:03 AM','2017-05-20 11:03:06',3,'2017-05-20 11:03:06'),(39,'hello!','May 20 2017 at 11:03 AM','2017-05-20 11:03:34',3,'2017-05-20 11:03:34'),(40,'Testing!','May 20 2017 at 11:04 AM','2017-05-20 11:04:55',3,'2017-05-20 11:04:55'),(41,'hello!','May 20 2017 at 11:26 AM','2017-05-20 11:26:17',4,'2017-05-20 11:26:17'),(42,'Hi I\'m Honda Civic!','May 20 2017 at 01:32 PM','2017-05-20 13:32:06',5,'2017-05-20 13:32:06'),(43,'hello!','May 20 2017 at 03:06 PM','2017-05-20 15:06:25',10,'2017-05-20 15:06:25'),(44,'HelloHelloPleaseWork:(','May 20 2017 at 03:42 PM','2017-05-20 15:42:48',2,'2017-05-20 15:42:48'),(45,'Hello!','May 20 2017 at 03:44 PM','2017-05-20 15:44:53',5,'2017-05-20 15:44:53'),(46,'Hi I\'m MO!','May 20 2017 at 03:49 PM','2017-05-20 15:49:25',10,'2017-05-20 15:49:25'),(47,'HAHAHAHAHA YESSSS YOURE MO!!!!!','May 20 2017 at 03:49 PM','2017-05-20 15:49:45',2,'2017-05-20 15:49:45'),(48,'Hi Raf! Glad to see you on THEWALL!','May 20 2017 at 03:51 PM','2017-05-20 15:51:20',11,'2017-05-20 15:51:20');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
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
