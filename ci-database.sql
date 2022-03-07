CREATE TABLE `user` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `fetched_at` datetime DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `pull_request` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `number` int,
  `repository_id` int,
  `status` varchar(255),
  `created_at` datetime,
  `fetched_at` datetime DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `commit` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `hash` varchar(255),
  `author_id` int,
  `modified_lines` int,
  `modified_files` json,
  `order_number` int,
  `pull_request_id` int,
  `created_at` datetime,
  `fetched_at` datetime DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `repository` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `owner_id` int,
  `created_at` datetime,
  `language` varchar(255),
  `topics` JSON,
  `fetching_finished` bool DEFAULT false,
  `fetched_at` datetime DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `check_run` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `github_id` bigint,
  `name` varchar(255),
  `commit_id` int,
  `check_suit_id` varchar(255),
  `status` varchar(255),
  `conclusion` varchar(255),
  `started_at` datetime,
  `finished_at` datetime,
  `order_number` int,
  `total_count` int,
  `fetched_at` datetime DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE `pull_request` ADD FOREIGN KEY (`repository_id`) REFERENCES `repository` (`id`);

ALTER TABLE `commit` ADD FOREIGN KEY (`author_id`) REFERENCES `user` (`id`);

ALTER TABLE `commit` ADD FOREIGN KEY (`pull_request_id`) REFERENCES `pull_request` (`id`);

ALTER TABLE `repository` ADD FOREIGN KEY (`owner_id`) REFERENCES `user` (`id`);

ALTER TABLE `check_run` ADD FOREIGN KEY (`commit_id`) REFERENCES `commit` (`id`);
