-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: pumis
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

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
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `department_name` varchar(20) DEFAULT NULL,
  `teacher_name` varchar(20) DEFAULT NULL,
  `teacher_abb` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institute`
--

DROP TABLE IF EXISTS `institute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `institute` (
  `institute_name` varchar(20) DEFAULT NULL,
  `department_name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institute`
--

LOCK TABLES `institute` WRITE;
/*!40000 ALTER TABLE `institute` DISABLE KEYS */;
/*!40000 ALTER TABLE `institute` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `enrollment_number` bigint(20) NOT NULL,
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(20) DEFAULT NULL,
  `institute_name` varchar(20) DEFAULT NULL,
  `department_name` varchar(20) DEFAULT NULL,
  `semester` varchar(5) DEFAULT NULL,
  `student_class` varchar(20) DEFAULT NULL,
  `email_id` varchar(50) DEFAULT NULL,
  `mobile_number` bigint(10) DEFAULT NULL,
  PRIMARY KEY (`enrollment_number`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (150303105011,'Shivam','Bhadauriya','PIET','CSE','8','A1','bhadauriyashivam91@gmail.com',9753847810),(150303105028,'Bharat','Choudhary','PIET','CSE','8','B1','choudharybharat969@gmail.com',9998533833),(150303105055,'Anindita','Guha','PIET','CSE','8','B1','aninditaguha9@gmail.com',7567550604),(150303105062,'Harshil','Joshi','PIET','CSE','8','B1','harshilhjoshi@gmail.com',9825057339),(150303105071,'Nitin','Lalwani','PIET','CSE','8','B1','nitindlalwani@gmail.com',9408341126),(150303105086,'Jahnvi','Mehta','PIET','CSE','8','B1','jahnvimehta20@gmail.com',9428392188),(150303105090,'Vatsal','Mistry','PIET','CSE','8','B1','mistryvatsal11@gmail.com',7203051703),(150303105111,'Prarthana ','Parmar','PIET','CSE','8','B2','prarthana273@gmail.com',7227838348),(150303105127,'Harsh','Patel','PIET','CSE','8','B2','HARSHGP44@GMAIL.COM',9978779967),(150303105130,'Krupa','Patel','PIET','CSE','8','B2','krupapatel1005@gmail.com',9586581212),(150303105135,'Mohit','Patel','PIET','CSE','8','B4','pmohit47@gmail.com',7566022611),(150303105170,'Jaydeep','Rajpurohit','PIET','CSE','8','B2','jaydeeppurohit1996@gmail.com',9426861425),(150303105178,'Sumit','Saini','PIET','CSE','8','B2','150303105178@paruluniversity.ac.in',9586173119),(150303105191,'Riti','Sharma','PIET','CSE','8','B2','150303105191@paruluniversity.ac.in',8980629266),(160303105177,'Riya','Ora','PIET','CSE','6','B2','riyaora27@gmail.com',9407184218),(160303105185,'PRAGYA','PANCHOLI','PIET','CSE','6','B3','pragyapancholi21@gmail.com',7283923009),(160303105212,'Dhruv','Patel','PIET','CSE','6','B2','pateldhruv333@gmail.com',7874445544),(160303105353,'Bhavini','Suthar','PIET','CSE','6','B3','sutharsweety27@gmail.com',8980055865),(160303105737,'Kunj','Thakor','PIET','CSE','8','B3','kunjkumarthakor@icloud.com',7874804043),(160303105901,'Piyush','Jain','PIET','CSE','8','B3','piyushj728@gmail.com',9675297708),(170303105324,'Shivanshi','Singh','PIET','CSE','4','B4','shivanshis816@gmail.com',7007943867),(180303105321,'Sanskriti','Shukla','PIET','CSE','2','B5','sanskritishukla94001@gmail.com',9426789975);
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

-- Dump completed on 2019-03-05 16:01:26
