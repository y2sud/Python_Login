CREATE TABLE `user` (
  `email_id` varchar(30) NOT NULL,
  `username` varchar(15) NOT NULL,
  `password` varchar(64) NOT NULL,
  `fullname` varchar(45) NOT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `email_id_UNIQUE` (`email_id`),
  UNIQUE KEY `user_id_UNIQUE` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
