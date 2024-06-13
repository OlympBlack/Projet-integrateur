-- Adminer 4.8.1 MySQL 8.2.0 dump
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

INSERT INTO `zz_langages` (id, name) VALUES
(1, 'Afrikaans'),
(2, 'Albanais'),
(3, 'Amharique'),
(4, 'Anglais'),
(5, 'Arabe'),
(6, 'Arménien'),
(7, 'Aymara'),
(8, 'Azéri'),
(9, 'Bengali'),
(10, 'Birman'),
(11, 'Bosniaque'),
(12, 'Bulgare'),
(13, 'Catalan'),
(14, 'Chichewa'),
(15, 'Chinois (mandarin)'),
(16, 'Coréen'),
(17, 'Croate'),
(18, 'Danois'),
(19, 'Espagnol'),
(20, 'Estonien'),
(21, 'Finnois'),
(22, 'Français'),
(23, 'Géorgien'),
(24, 'Grec'),
(25, 'Hébreu'),
(26, 'Hindi'),
(27, 'Hongrois'),
(28, 'Indonésien'),
(29, 'Irlandais'),
(30, 'Islandais'),
(31, 'Italien'),
(32, 'Japonais'),
(33, 'Kazakh'),
(34, 'Kirghize'),
(35, 'Kiswahili'),
(36, 'Kurde'),
(37, 'Letton'),
(38, 'Lituanien'),
(39, 'Luxembourgeois'),
(40, 'Macédonien'),
(41, 'Malais'),
(42, 'Maltais'),
(43, 'Maori'),
(44, 'Mongol'),
(45, 'Népalais'),
(46, 'Norvégien'),
(47, 'Ourdou'),
(48, 'Ouzbek'),
(49, 'Pachtou'),
(50, 'Persan'),
(51, 'Polonais'),
(52, 'Portugais'),
(53, 'Quechua'),
(54, 'Roumain'),
(55, 'Russe'),
(56, 'Serbe'),
(57, 'Sesotho'),
(58, 'Singhalais'),
(59, 'Slovaque'),
(60, 'Slovène'),
(61, 'Suédois'),
(62, 'Tamoul'),
(63, 'Tchèque'),
(64, 'Télougou'),
(65, 'Thaï'),
(66, 'Tigrigna'),
(67, 'Turc'),
(68, 'Ukrainien'),
(69, 'Vietnamien'),
(70, 'Xhosa'),
(71, 'Yiddish'),
(72, 'Zoulou');

DROP TABLE IF EXISTS `zz_hobbys`;
CREATE TABLE `zz_hobbys` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

INSERT INTO `zz_hobbys` (id, name) VALUES
(1, 'Sport'),
(2, 'Cuisine'),
(3, 'Jardinage'),
(4, 'Randonnée'),
(5, 'Pêche'),
(6, 'Musique'),
(7, 'Musculation'),
(8, 'Danse'),
(9, 'Camping'),
(10, 'Photographie'),
(11, 'Bourse'),
(12, 'Méditation'),
(13, 'Technologie'),
(14, 'Livres'),
(15, 'Politique'),
(16, 'Economie'),
(17, 'Diplomatie'),
(18, 'Mode'),
(19, 'Concert'),
(20, 'Voyage'),
(21, 'Bijoux'),
(22, 'Gaming'),
(23, 'Commerce'),
(24, 'Bricolage'),
(25, 'Langues'),
(26, 'Shopping'),
(27, 'Séries'),
(28, 'Films'),
(29, 'Documentaire'),
(30, 'Spiritualité'),
(31, 'Théatre'),
(32, 'Thé'),
(33, 'Comédie'),
(34, 'Astrologie'),
(35, 'Beer'),
(36, 'Vin'),
(37, 'Cigarette'),
(38, 'Automobile'),
(39, 'Crypto'),
(40, 'Surf'),
(41, 'Informatique');



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
  `hobby` json DEFAULT NULL,
  `pref` json DEFAULT NULL,
  `online` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `pseudo` (`pseudo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

DROP TABLE IF EXISTS `zz_locations`;
CREATE TABLE  `zz_locations`(
    `id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `user_id` INT UNSIGNED NOT NULL,
    `longitude` DOUBLE PRECISION NOT NULL,
    `latitude` DOUBLE PRECISION NOT NULL,
    `city` VARCHAR(255) NOT NULL,
    `country` VARCHAR(255) NOT NULL,
    CONSTRAINT `fk_loc_user` FOREIGN KEY (`user_id`) REFERENCES `zz_users`(`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;



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
