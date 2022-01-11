CREATE TABLE `user` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255)
);

CREATE TABLE `pull_request` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `hash` varchar(255),
  `repository_id` int,
  `status` varchar(255),
  `created_at` datetime
);

CREATE TABLE `commit` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `hash` varchar(255),
  `author_id` int,
  `modified_lines` int,
  `modified_files` json,
  `order_number` int,
  `pull_request_id` int,
  `created_at` datetime
);

CREATE TABLE `repository` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `status` varchar(255)
);

CREATE TABLE `check_run` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `hash` varchar(255),
  `name` int,
  `commit_id` int,
  `status` varchar(255),
  `created_at` datetime,
  `order_number` int
);

ALTER TABLE `pull_request` ADD FOREIGN KEY (`repository_id`) REFERENCES `repository` (`id`);

ALTER TABLE `commit` ADD FOREIGN KEY (`author_id`) REFERENCES `user` (`id`);

ALTER TABLE `commit` ADD FOREIGN KEY (`pull_request_id`) REFERENCES `pull_request` (`id`);

ALTER TABLE `check_run` ADD FOREIGN KEY (`commit_id`) REFERENCES `commit` (`id`);