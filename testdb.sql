-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.1.31-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win32
-- HeidiSQL Version:             9.5.0.5196
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for testdb
DROP DATABASE IF EXISTS `testdb`;
CREATE DATABASE IF NOT EXISTS `testdb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `testdb`;

-- Dumping structure for table testdb.roles
DROP TABLE IF EXISTS `roles`;
CREATE TABLE IF NOT EXISTS `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- Dumping data for table testdb.roles: ~3 rows (approximately)
DELETE FROM `roles`;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` (`id`, `name`) VALUES
	(1, 'Global Admin'),
	(2, 'Admin'),
	(3, 'User');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;

-- Dumping structure for table testdb.users
DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) COLLATE utf8_general_ci NOT NULL,
  `password` varchar(40) COLLATE utf8_general_ci NOT NULL,
  `email` varchar(255) COLLATE utf8_general_ci NOT NULL,
  `firstname` varchar(255) COLLATE utf8_general_ci DEFAULT NULL,
  `lastname` varchar(255) COLLATE utf8_general_ci DEFAULT NULL,
  `active` int(1) NOT NULL,
  `newsletter` int(1) NOT NULL COMMENT 'if set to 1 send emails :)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- Dumping data for table testdb.users: ~16 rows (approximately)
DELETE FROM `users`;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
--INSERT INTO `users` (`id`, `username`, `password`, `email`, `firstname`, `lastname`, `active`, `newsletter`) VALUES
--	(1, 'mance', 'e10adc3949ba59abbe56e057f20f883e', 'dj.mancovic@gmail.com', 'Djordje', 'Mancovic', 1, 1),
--	(4, 'john', 'e10adc3949ba59abbe56e057f20f883e', 'john.doe@gmail.com', 'john', 'doe', 1, 0),
--	(5, 'john2', 'e10adc3949ba59abbe56e057f20f883e', 'john2.doe@gmail.com', 'john', 'doe', 1, 0),
--	(6, '', '', '', '', '', 0, 0),
--	(7, 'test', 'test', 'test', 'test', 'test', 1, 1),
--	(8, 'test', 'test', 'test', 'test', 'test', 1, 1),
--	(9, 'john3', 'e10adc3949ba59abbe56e057f20f883e', 'john3.doe@gmail.com', 'john', 'doe', 1, 0),
--	(10, 'john4', 'e10adc3949ba59abbe56e057f20f883e', 'john4.doe@gmail.com', 'john', 'doe', 1, 0),
--	(11, 'john5', 'e10adc3949ba59abbe56e057f20f883e', 'john5.doe@gmail.com', 'john', 'doe', 1, 0),
--	(18, 'john7', 'e10adc3949ba59abbe56e057f20f883e', 'john7.doe@gmail.com', 'john', 'doe', 1, 0),
--	(19, 'john8', 'e10adc3949ba59abbe56e057f20f883e', 'john8.doe@gmail.com', 'john', 'doe', 1, 0),
--	(20, 'john9', 'e10adc3949ba59abbe56e057f20f883e', 'john9.doe@gmail.com', 'john', 'doe', 1, 0),
--	(21, 'john11', 'e10adc3949ba59abbe56e057f20f883e', 'john11.doe@gmail.com', 'john', 'doe', 1, 0),
--	(22, 'john12', 'e10adc3949ba59abbe56e057f20f883e', 'john12.doe@gmail.com', 'john', 'doe', 1, 0),
--	(23, 'john13', 'e10adc3949ba59abbe56e057f20f883e', 'john13.doe@gmail.com', 'john', 'doe', 1, 0),
--	(24, 'john14', 'e10adc3949ba59abbe56e057f20f883e', 'john14.doe@gmail.com', 'john', 'doe', 1, 0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

-- Dumping structure for table testdb.user_roles
DROP TABLE IF EXISTS `user_roles`;
CREATE TABLE IF NOT EXISTS `user_roles` (
  `user_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`,`role_id`),
  KEY `user_roles_to_roles_idx` (`role_id`),
  CONSTRAINT `user_roles_to_roles` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `user_roles_to_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='Connecdt tables users and roles';

-- Dumping data for table testdb.user_roles: ~6 rows (approximately)
DELETE FROM `user_roles`;
/*!40000 ALTER TABLE `user_roles` DISABLE KEYS */;
--INSERT INTO `user_roles` (`user_id`, `role_id`) VALUES
--	(1, 1),
--	(1, 2),
--	(1, 3),
--	(4, 2),
--	(23, 3),
--	(24, 3);
/*!40000 ALTER TABLE `user_roles` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
