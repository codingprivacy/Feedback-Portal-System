-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: datahouse
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
-- Table structure for table `fdbck_resp_training`
--

DROP TABLE IF EXISTS `fdbck_resp_training`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fdbck_resp_training` (
  `enrollment_number` bigint(20) NOT NULL,
  `resp1` varchar(300) DEFAULT NULL,
  `resp2` varchar(300) DEFAULT NULL,
  `resp3` varchar(300) DEFAULT NULL,
  `resp4` varchar(300) DEFAULT NULL,
  `resp5` varchar(300) DEFAULT NULL,
  `resp6` varchar(300) DEFAULT NULL,
  `resp7` varchar(300) DEFAULT NULL,
  `resp8` varchar(300) DEFAULT NULL,
  `resp9` varchar(300) DEFAULT NULL,
  `resp10` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`enrollment_number`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fdbck_resp_training`
--

LOCK TABLES `fdbck_resp_training` WRITE;
/*!40000 ALTER TABLE `fdbck_resp_training` DISABLE KEYS */;
INSERT INTO `fdbck_resp_training` VALUES (150303105011,'Mostly they do, but sometimes they might not..','','','','','','','','',''),(150303105055,'He does complete the course in time, but not in the pace we expect them to. Usually, the last chapters are not comprehensible at all.','I find him to have a very little knowledge on the subject he is teaching. ','He responds to the questions well, yet he does not always provide the correct explanations/answers to the doubts. ','There has always been a situation of chaos in the classroom. He can not manage the classroom at all.','He needs to work on that.','There is chaos all around. Students busy in their on work and life.','No, nothing that I can recall. I believe he should guide the students a bit more.','Well, he tries to conduct tests, not regular though. Students don\'t show up and that doesn\'t seem to bother him much.','He is fair while evaluating. I don\'t sense any partiality.','I would really appreciate , if he can gain more in depth knowledge about the subject. Also, I would want him to emphasize more on practical aspect.'),(150303105086,'No, he doesnot. Because when he starts a topic he includes much more than just the course given by the college.','As I wrote in my previous answer he teaches more than the course. He has a vast knowledge about the subject.','Very well. If he doesnot know the answer to the asked question he researches and tells it the next day.','Ofcourse in a class chaos does happen at times but he handles it well.','Average communication skills.','Faculty\'s interest towards students interaction makes student take interest in his teaching.','Yes, he has always been there for students.','He knows students are already giving a lot of tests so he doesnot conduct tests but seminaars and presentations by students are conducted more often.','He is not partial for average or toppers but doesnot always treat well the students who donot attend his class regularly.','Mr. Wilkinson is a good teacher and i am comfortable with his teaching.'),(150303105103,'Yes','Not so good','Not very well','Yes','Good','He is good at maintaining the class','Yes','Yesss','No','Yes'),(150303105111,'Mostly yes , and if not than the reason is that the syllabus is too large and more theoretical than practical.','I\'d say about 8/10 for most of the faculties. Some know it about average.','They do take interest in it and try their best to solve it. ','Yep a lot of times. Mostly they handle it by scolding but there must be a better way.','About 70% have average or below average communication skills but the rest rest have really good communication skills.','It can be described as a quiet classroom most of the times but not sure about how many students actuallget what he says.','Yes mostly. And i feel each teacher should reach out personally or respond well when the student does the same.','There are not much tests but we do have quizzes once or twice in a semester by some teachers. The frequency can be increased.','Pretty fair i don\'t see any biased markings.','I\'m quite comfortable but maybe the teaching methods can be less theoretical or less ppts and more practical or hands on.'),(150303105170,'Yes, He does complete it on time.','Really good.','He is very much happy to solve doubts.','Yes, He stops teaching in the class in such case.','Execellent','Sometime it\'s noisy and other time it\'s silent.','Yes He did in many instances.','No','No, He is not partial about evaluating answer sheets.','Yes, comfortable!'),(150303105178,'No because faculty is alloted some tasks other than teaching which affects the course completion','Good knowledge of subject','Faculty is always available any kind of doubts and if one asks the same doubt again the faculty tries to explain in different way ','No','The faculty is able to interact with us very well .Good communication skills.','All students except a few are attentive during his lecture','Yes','Yes he conducts some fun quizes in interactive way rather than pen- paper based test. Also, arranges expert lectures for important topics','He has never done partiality while evaluation','Yes'),(160303105185,'No,they just focus on no. of lecture not on syllabus portion','New faculty doesn\'t know there subject well.','Some faculty doesn\'t not have enough knowledge of subject which alloted to them so they are not able to clear doubts','Some faculty cant handel the situation well.','They give us good mentoring session.','Classroom scence are worst during his teaching.','She helped student on more personal level and guided them for further studies.','No there is no such things like class test or something.','He/she  is fair while evaluating amswer sheets.','No i am not comfortable with his teaching.he should prepare the topic which he is gonna teach us.'),(160303105212,'No. Lack of time.','Not sure.','Pretty good.','Yes there is chaos sometimes but that\'s just to have some fun so we don\'t feel bored in lectures','Not to good and not to bad as their English might not be proper but they still try to communicate and explain','I don\'t know this faculty','Nil','Nil','Nil','Nil');
/*!40000 ALTER TABLE `fdbck_resp_training` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-05 16:10:01
