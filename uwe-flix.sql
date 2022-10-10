-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 10, 2022 at 11:37 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.3.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `uwe-flix`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$320000$q8QodJCwhKqlsCZRXgsFk0$IgJGpbwwPygyhtcd9AQEGPjOEgJVd+ya0DgqrIKK1GI=', '2022-10-10 09:08:47.983323', 1, 'admin', '', '', 'radiela.y@abv.bg', 1, 1, '2022-10-09 16:33:17.597298');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-10-09 16:31:18.223888'),
(2, 'auth', '0001_initial', '2022-10-09 16:31:18.606239'),
(3, 'admin', '0001_initial', '2022-10-09 16:31:18.695096'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-10-09 16:31:18.702565'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-10-09 16:31:18.710568'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-10-09 16:31:18.769629'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-10-09 16:31:18.809725'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-10-09 16:31:18.825794'),
(9, 'auth', '0004_alter_user_username_opts', '2022-10-09 16:31:18.832665'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-10-09 16:31:18.880537'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-10-09 16:31:18.883529'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-10-09 16:31:18.891508'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-10-09 16:31:18.904472'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-10-09 16:31:18.920461'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-10-09 16:31:18.940381'),
(16, 'auth', '0011_update_proxy_permissions', '2022-10-09 16:31:18.949307'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-10-09 16:31:18.966365'),
(18, 'sessions', '0001_initial', '2022-10-09 16:31:18.999277'),
(19, 'user_page', '0001_initial', '2022-10-09 16:31:19.644478'),
(20, 'user_page', '0002_alter_student_club', '2022-10-09 16:31:19.865297'),
(21, 'user_page', '0003_student_in_club', '2022-10-09 16:31:19.888276'),
(22, 'user_page', '0004_remove_student_in_club', '2022-10-09 16:31:19.902237'),
(23, 'user_page', '0005_student_in_club', '2022-10-09 16:31:19.923222'),
(24, 'user_page', '0006_alter_student_in_club', '2022-10-09 16:31:19.930241'),
(25, 'user_page', '0007_alter_club_contact_number_alter_club_landline_number', '2022-10-09 16:31:20.004224'),
(26, 'user_page', '0008_removescreendetails', '2022-10-09 16:31:20.059537'),
(27, 'user_page', '0009_removeshowingdetails', '2022-10-09 16:31:20.111406'),
(28, 'user_page', '0010_removemoviedetails', '2022-10-09 16:31:20.176589'),
(29, 'user_page', '0011_removeclubdetails', '2022-10-09 16:31:20.235506'),
(30, 'user_page', '0012_removeuserdetails', '2022-10-09 16:31:20.294655'),
(31, 'user_page', '0013_removestaffdetails_remove_club_representatives_and_more', '2022-10-09 16:31:20.437216'),
(32, 'user_page', '0014_alter_orderdetails_screen', '2022-10-09 16:31:20.608938'),
(33, 'user_page', '0015_alter_orderdetails_screen', '2022-10-09 16:31:20.716254'),
(34, 'user_page', '0016_alter_showingdetails_films', '2022-10-09 16:31:20.723239'),
(35, 'user_page', '0017_paidorderdetails', '2022-10-09 16:31:20.782930'),
(36, 'user_page', '0018_remove_paidorderdetails_order_paidorderdetails_date_and_more', '2022-10-09 16:31:20.913512'),
(37, 'user_page', '0019_remove_paidorderdetails_screen_type_and_more', '2022-10-09 16:31:20.934041'),
(38, 'user_page', '0020_remove_paidorderdetails_selected_seats', '2022-10-09 16:31:20.945976'),
(39, 'user_page', '0021_rename_usename_paidorderdetails_username', '2022-10-09 16:31:20.956947'),
(40, 'user_page', '0022_alter_paidorderdetails_price', '2022-10-09 16:31:21.036779'),
(41, 'user_page', '0002_alter_filmdetails_id_alter_screendetails_id_and_more', '2022-10-09 16:31:21.054710');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `movies`
--

CREATE TABLE `movies` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `img` varchar(100) NOT NULL,
  `age_rating` varchar(10) NOT NULL,
  `duration` varchar(10) NOT NULL,
  `description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `movies`
--

INSERT INTO `movies` (`id`, `title`, `img`, `age_rating`, `duration`, `description`) VALUES
(1, 'Spiderman', 'media/spiderman_BF3pkja.jpg', '12+', '2h 37min', 'New Spiderman Movie'),
(2, 'Batman', 'media/batman_t0NehrV.jpg', '12+', '2h 58min', 'Batman Movie'),
(3, 'Uncharted', 'media/uncharted_g2Hrv7Z.jpg', '12+', '1h 58min', 'Uncharted 2022'),
(4, 'RedNotice', 'media/red_notice_0pP6AXW.jpg', '12+', '1h 52min', 'Red Notice');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `id` bigint(20) NOT NULL,
  `title` varchar(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time(6) DEFAULT NULL,
  `screen_type` varchar(5) NOT NULL,
  `selected_seats` int(10) UNSIGNED NOT NULL CHECK (`selected_seats` >= 0),
  `price` bigint(20) UNSIGNED NOT NULL CHECK (`price` >= 0),
  `screen_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `id` bigint(20) NOT NULL,
  `username` varchar(8) NOT NULL,
  `date` date DEFAULT NULL,
  `price` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `screens`
--

CREATE TABLE `screens` (
  `id` bigint(20) NOT NULL,
  `seats_available` int(10) UNSIGNED NOT NULL CHECK (`seats_available` >= 0),
  `screen_type` varchar(2) NOT NULL,
  `Showings_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `screens`
--

INSERT INTO `screens` (`id`, `seats_available`, `screen_type`, `Showings_id`) VALUES
(1, 20, '1', 1),
(2, 30, '2', 2),
(3, 20, '1', 3),
(4, 30, '1', 4);

-- --------------------------------------------------------

--
-- Table structure for table `showings`
--

CREATE TABLE `showings` (
  `id` bigint(20) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `Films_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `showings`
--

INSERT INTO `showings` (`id`, `date`, `time`, `Films_id`) VALUES
(1, '2022-09-12', '20:30:00.000000', 1),
(2, '2022-09-12', '20:00:00.000000', 2),
(3, '2022-09-12', '21:00:00.000000', 3),
(4, '2022-09-12', '21:30:00.000000', 4);

-- --------------------------------------------------------

--
-- Table structure for table `upcoming_movies`
--

CREATE TABLE `upcoming_movies` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `img` varchar(100) NOT NULL,
  `age_rating` varchar(10) NOT NULL,
  `duration` varchar(10) NOT NULL,
  `description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `upcoming_movies`
--

INSERT INTO `upcoming_movies` (`id`, `title`, `img`, `age_rating`, `duration`, `description`) VALUES
(1, 'Dog', 'media/dog_HNzXV4p.jpg', '12+', '1h 58min', 'Dog 2 Movie'),
(3, 'Sing2', 'media/sing2.jpg', 'Kids', '1h 52min', 'Animated movie suitable for children.');

-- --------------------------------------------------------

--
-- Table structure for table `user_page_club`
--

CREATE TABLE `user_page_club` (
  `id` bigint(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `address` varchar(50) NOT NULL,
  `address2` varchar(50) NOT NULL,
  `city` varchar(30) NOT NULL,
  `postcode` varchar(7) NOT NULL,
  `contact_number` varchar(20) NOT NULL,
  `landline_number` varchar(20) DEFAULT NULL,
  `description` longtext NOT NULL,
  `rep_email` varchar(254) NOT NULL,
  `rep_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user_page_removeclubdetails`
--

CREATE TABLE `user_page_removeclubdetails` (
  `id` bigint(20) NOT NULL,
  `choose_club_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user_page_removemoviedetails`
--

CREATE TABLE `user_page_removemoviedetails` (
  `id` bigint(20) NOT NULL,
  `choose_movie_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user_page_removeorderdetails`
--

CREATE TABLE `user_page_removeorderdetails` (
  `id` bigint(20) NOT NULL,
  `choose_item_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user_page_removescreendetails`
--

CREATE TABLE `user_page_removescreendetails` (
  `id` bigint(20) NOT NULL,
  `choose_screen_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user_page_removeshowingdetails`
--

CREATE TABLE `user_page_removeshowingdetails` (
  `id` bigint(20) NOT NULL,
  `choose_showing_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user_page_removestaffdetails`
--

CREATE TABLE `user_page_removestaffdetails` (
  `id` bigint(20) NOT NULL,
  `choose_member_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user_page_removeupcomingdetails`
--

CREATE TABLE `user_page_removeupcomingdetails` (
  `id` bigint(20) NOT NULL,
  `choose_item_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user_page_removeuserdetails`
--

CREATE TABLE `user_page_removeuserdetails` (
  `id` bigint(20) NOT NULL,
  `choose_user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user_page_student`
--

CREATE TABLE `user_page_student` (
  `id` bigint(20) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `id_number` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `credits` int(10) UNSIGNED NOT NULL CHECK (`credits` >= 0),
  `Club_id` bigint(20) DEFAULT NULL,
  `in_club` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_page_student`
--

INSERT INTO `user_page_student` (`id`, `first_name`, `last_name`, `email`, `id_number`, `password`, `credits`, `Club_id`, `in_club`) VALUES
(2, 'Radiela', 'Yorgova', 'radiela.y@abv.bg', '9913450', '883beb59e50c0c9b1abee20d7138141fca1962393b6f2d8d28f583fb045c5c35', 20, NULL, 'no');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `movies`
--
ALTER TABLE `movies`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Orders_screen_id_d83c7ac4_fk_Screens_id` (`screen_id`);

--
-- Indexes for table `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `screens`
--
ALTER TABLE `screens`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Screens_Showings_id_d2999ab1_fk_Showings_id` (`Showings_id`);

--
-- Indexes for table `showings`
--
ALTER TABLE `showings`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Showings_Films_id_11ebb141_fk_Movies_id` (`Films_id`);

--
-- Indexes for table `upcoming_movies`
--
ALTER TABLE `upcoming_movies`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_page_club`
--
ALTER TABLE `user_page_club`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_page_removeclubdetails`
--
ALTER TABLE `user_page_removeclubdetails`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_page_removeclub_choose_club_id_ad93d638_fk_user_page` (`choose_club_id`);

--
-- Indexes for table `user_page_removemoviedetails`
--
ALTER TABLE `user_page_removemoviedetails`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_page_removemovi_choose_movie_id_9e3abda3_fk_Movies_id` (`choose_movie_id`);

--
-- Indexes for table `user_page_removeorderdetails`
--
ALTER TABLE `user_page_removeorderdetails`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_page_removeorde_choose_item_id_425662b1_fk_Orders_id` (`choose_item_id`);

--
-- Indexes for table `user_page_removescreendetails`
--
ALTER TABLE `user_page_removescreendetails`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_page_removescre_choose_screen_id_7b850021_fk_Screens_i` (`choose_screen_id`);

--
-- Indexes for table `user_page_removeshowingdetails`
--
ALTER TABLE `user_page_removeshowingdetails`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_page_removeshow_choose_showing_id_52123a85_fk_Showings_` (`choose_showing_id`);

--
-- Indexes for table `user_page_removestaffdetails`
--
ALTER TABLE `user_page_removestaffdetails`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_page_removestaf_choose_member_id_8b4048d8_fk_auth_user` (`choose_member_id`);

--
-- Indexes for table `user_page_removeupcomingdetails`
--
ALTER TABLE `user_page_removeupcomingdetails`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_page_removeupco_choose_item_id_af0b0da9_fk_Upcoming_` (`choose_item_id`);

--
-- Indexes for table `user_page_removeuserdetails`
--
ALTER TABLE `user_page_removeuserdetails`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_page_removeuser_choose_user_id_b0b17f02_fk_user_page` (`choose_user_id`);

--
-- Indexes for table `user_page_student`
--
ALTER TABLE `user_page_student`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_page_student_Club_id_12510546_fk_user_page_club_id` (`Club_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `movies`
--
ALTER TABLE `movies`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `screens`
--
ALTER TABLE `screens`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `showings`
--
ALTER TABLE `showings`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `upcoming_movies`
--
ALTER TABLE `upcoming_movies`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user_page_club`
--
ALTER TABLE `user_page_club`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_page_removeclubdetails`
--
ALTER TABLE `user_page_removeclubdetails`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_page_removemoviedetails`
--
ALTER TABLE `user_page_removemoviedetails`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_page_removeorderdetails`
--
ALTER TABLE `user_page_removeorderdetails`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_page_removescreendetails`
--
ALTER TABLE `user_page_removescreendetails`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_page_removeshowingdetails`
--
ALTER TABLE `user_page_removeshowingdetails`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_page_removestaffdetails`
--
ALTER TABLE `user_page_removestaffdetails`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_page_removeupcomingdetails`
--
ALTER TABLE `user_page_removeupcomingdetails`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_page_removeuserdetails`
--
ALTER TABLE `user_page_removeuserdetails`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_page_student`
--
ALTER TABLE `user_page_student`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `Orders_screen_id_d83c7ac4_fk_Screens_id` FOREIGN KEY (`screen_id`) REFERENCES `screens` (`id`);

--
-- Constraints for table `screens`
--
ALTER TABLE `screens`
  ADD CONSTRAINT `Screens_Showings_id_d2999ab1_fk_Showings_id` FOREIGN KEY (`Showings_id`) REFERENCES `showings` (`id`);

--
-- Constraints for table `showings`
--
ALTER TABLE `showings`
  ADD CONSTRAINT `Showings_Films_id_11ebb141_fk_Movies_id` FOREIGN KEY (`Films_id`) REFERENCES `movies` (`id`);

--
-- Constraints for table `user_page_removeclubdetails`
--
ALTER TABLE `user_page_removeclubdetails`
  ADD CONSTRAINT `user_page_removeclub_choose_club_id_ad93d638_fk_user_page` FOREIGN KEY (`choose_club_id`) REFERENCES `user_page_club` (`id`);

--
-- Constraints for table `user_page_removemoviedetails`
--
ALTER TABLE `user_page_removemoviedetails`
  ADD CONSTRAINT `user_page_removemovi_choose_movie_id_9e3abda3_fk_Movies_id` FOREIGN KEY (`choose_movie_id`) REFERENCES `movies` (`id`);

--
-- Constraints for table `user_page_removeorderdetails`
--
ALTER TABLE `user_page_removeorderdetails`
  ADD CONSTRAINT `user_page_removeorde_choose_item_id_425662b1_fk_Orders_id` FOREIGN KEY (`choose_item_id`) REFERENCES `orders` (`id`);

--
-- Constraints for table `user_page_removescreendetails`
--
ALTER TABLE `user_page_removescreendetails`
  ADD CONSTRAINT `user_page_removescre_choose_screen_id_7b850021_fk_Screens_i` FOREIGN KEY (`choose_screen_id`) REFERENCES `screens` (`id`);

--
-- Constraints for table `user_page_removeshowingdetails`
--
ALTER TABLE `user_page_removeshowingdetails`
  ADD CONSTRAINT `user_page_removeshow_choose_showing_id_52123a85_fk_Showings_` FOREIGN KEY (`choose_showing_id`) REFERENCES `showings` (`id`);

--
-- Constraints for table `user_page_removestaffdetails`
--
ALTER TABLE `user_page_removestaffdetails`
  ADD CONSTRAINT `user_page_removestaf_choose_member_id_8b4048d8_fk_auth_user` FOREIGN KEY (`choose_member_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `user_page_removeupcomingdetails`
--
ALTER TABLE `user_page_removeupcomingdetails`
  ADD CONSTRAINT `user_page_removeupco_choose_item_id_af0b0da9_fk_Upcoming_` FOREIGN KEY (`choose_item_id`) REFERENCES `upcoming_movies` (`id`);

--
-- Constraints for table `user_page_removeuserdetails`
--
ALTER TABLE `user_page_removeuserdetails`
  ADD CONSTRAINT `user_page_removeuser_choose_user_id_b0b17f02_fk_user_page` FOREIGN KEY (`choose_user_id`) REFERENCES `user_page_student` (`id`);

--
-- Constraints for table `user_page_student`
--
ALTER TABLE `user_page_student`
  ADD CONSTRAINT `user_page_student_Club_id_12510546_fk_user_page_club_id` FOREIGN KEY (`Club_id`) REFERENCES `user_page_club` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
