-- Adminer 4.8.1 MySQL 8.2.0 dump
USE ProjectDB;
SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0; 
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `friendship`;
CREATE TABLE `friendship` (
  `liker` int unsigned NOT NULL,
  `liked` int unsigned NOT NULL,
  `lik` int unsigned NOT NULL,
  PRIMARY KEY (`liker`,`liked`,`lik`),
  UNIQUE KEY `liker` (`liker`,`liked`,`lik`),
  KEY `fk_f_medias` (`liked`),
  CONSTRAINT `fk_f_medias` FOREIGN KEY (`liked`) REFERENCES `zz_users` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `fk_f_users` FOREIGN KEY (`liker`) REFERENCES `zz_users` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


DROP TABLE IF EXISTS `zz_discussions`;
CREATE TABLE `zz_discussions` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `last_message_id` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_d_message` (`last_message_id`),
  CONSTRAINT `fk_d_message` FOREIGN KEY (`last_message_id`) REFERENCES `zz_messages` (`id`) ON DELETE SET NULL ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


DROP TABLE IF EXISTS `zz_langages`;
CREATE TABLE `zz_langages` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


DROP TABLE IF EXISTS `zz_medias`;
CREATE TABLE `zz_medias` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `path` varchar(255) NOT NULL,
  `type` enum('0','1','3') DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `path` (`path`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


DROP TABLE IF EXISTS `zz_messages`;
CREATE TABLE `zz_messages` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `content` mediumtext NOT NULL,
  `media_id` int unsigned DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `user_id` int unsigned NOT NULL,
  `discussion_id` int unsigned NOT NULL,
  `message_id` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_m_user` (`user_id`),
  KEY `fk_m_discussion` (`discussion_id`),
  KEY `fk_m_message` (`message_id`),
  KEY `fk_m_images` (`media_id`),
  CONSTRAINT `fk_m_discussion` FOREIGN KEY (`discussion_id`) REFERENCES `zz_discussions` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `fk_m_images` FOREIGN KEY (`media_id`) REFERENCES `zz_medias` (`id`) ON UPDATE RESTRICT,
  CONSTRAINT `fk_m_message` FOREIGN KEY (`message_id`) REFERENCES `zz_messages` (`id`) ON UPDATE RESTRICT,
  CONSTRAINT `fk_m_user` FOREIGN KEY (`user_id`) REFERENCES `zz_users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


DROP TABLE IF EXISTS `zz_users`;
CREATE TABLE `zz_users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `pseudo` varchar(255) DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `last_connect` datetime NOT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `prenom` varchar(255) DEFAULT NULL,
  `birthday` date NOT NULL,
  `bio` mediumtext,
  `sex` enum('Homme','Femme','Non-Binaire','Je préfère ne pas dire') DEFAULT NULL,
  `plage` enum('1','2','3','4','5','6','7','8','9','10') DEFAULT NULL,
  `astre` enum('Bélier','Taureau','Gémeaux','Cancer','Lion','Vierge','Balance','Scorpion','Sagittaire','Capricorne','Verseau','Poissons') DEFAULT NULL,
  `religion` enum('Catholique','Chrétien','Juif','Bouddhiste','Mormon','Musulman','Orthodoxe','Protestant','Hindou','Athée','Chamanique','Spirituel','Autres') DEFAULT NULL,
  `ville` varchar(255) DEFAULT NULL,
  `pays` varchar(255) DEFAULT NULL,
  `pref` json DEFAULT NULL,
  `online` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `pseudo` (`pseudo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


DROP TABLE IF EXISTS `zz_users_discussions`;
CREATE TABLE `zz_users_discussions` (
  `user_id` int unsigned NOT NULL,
  `discussion_id` int unsigned NOT NULL,
  `status` int NOT NULL,
  `lastdate` datetime DEFAULT NULL,
  PRIMARY KEY (`user_id`,`discussion_id`),
  UNIQUE KEY `user_id` (`user_id`,`discussion_id`),
  KEY `fk_ud_discussion` (`discussion_id`),
  CONSTRAINT `fk_ud_discussion` FOREIGN KEY (`discussion_id`) REFERENCES `zz_discussions` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `fk_ud_user` FOREIGN KEY (`user_id`) REFERENCES `zz_users` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


DROP TABLE IF EXISTS `zz_users_langages`;
CREATE TABLE `zz_users_langages` (
  `user_id` int unsigned NOT NULL,
  `langage_id` int unsigned NOT NULL,
  `type` int unsigned NOT NULL,
  PRIMARY KEY (`user_id`,`langage_id`,`type`),
  UNIQUE KEY `user_id` (`user_id`,`langage_id`,`type`),
  KEY `fk_ul_langage` (`langage_id`),
  CONSTRAINT `fk_ul_langage` FOREIGN KEY (`langage_id`) REFERENCES `zz_langages` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `fk_ul_user` FOREIGN KEY (`user_id`) REFERENCES `zz_users` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


DROP TABLE IF EXISTS `zz_users_medias`;
CREATE TABLE `zz_users_medias` (
  `user_id` int unsigned NOT NULL,
  `media_id` int unsigned NOT NULL,
  `principal` int unsigned DEFAULT '0',
  PRIMARY KEY (`user_id`,`media_id`),
  UNIQUE KEY `user_id` (`user_id`,`media_id`),
  KEY `fk_um_medias` (`media_id`),
  CONSTRAINT `fk_um_medias` FOREIGN KEY (`media_id`) REFERENCES `zz_medias` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `fk_um_users` FOREIGN KEY (`user_id`) REFERENCES `zz_users` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


-- 2024-06-11 19:51:13
