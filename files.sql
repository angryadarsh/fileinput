-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 16, 2022 at 07:31 PM
-- Server version: 10.2.18-MariaDB-log
-- PHP Version: 5.5.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `FileInput`
--

-- --------------------------------------------------------

--
-- Table structure for table `files`
--

CREATE TABLE `files` (
  `id` int(11) NOT NULL,
  `FileName` varchar(255) DEFAULT NULL,
  `FilePath` varchar(255) DEFAULT NULL,
  `ExecutionTime` double DEFAULT NULL,
  `DateTime` datetime DEFAULT current_timestamp(),
  `Exe_Status` int(20) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `files`
--

INSERT INTO `files` (`id`, `FileName`, `FilePath`, `ExecutionTime`, `DateTime`, `Exe_Status`) VALUES
(1, 'text.text', 'var/html/www/text.text', 1660629063.1407351, '2022-08-16 15:06:22', 1),
(2, 'text1.text', 'var/html/www/text1.text', 1660629063.1407459, '2022-08-16 15:07:46', 1),
(3, 'text2.text', 'var/html/www/text2.text', 1660644445.002622, '2022-08-16 15:37:25', 1),
(4, '1660646165.75425_.txt', 'C:\\Users\\3014\\1660646165.75425_.txt', 1660646165.75425, '2022-08-16 16:06:05', 1),
(5, 'temp.txt', 'C:\\Users\\3014\\temp.txt', 1660648123.0981655, '2022-08-16 16:38:43', 1),
(6, 'temp.txt', 'C:\\Users\\3014\\temp.txt', 1660649132.097978, '2022-08-16 16:55:32', 1),
(7, 'temp.txt', 'C:\\Users\\3014\\temp.txt', 2022, '2022-08-16 18:52:59', 1),
(8, 'temp.txt', 'C:\\Users\\3014\\temp.txt', 50.048226, '2022-08-16 18:59:50', 1),
(9, 'temp.txt', 'C:\\Users\\3014\\temp.txt', 2022, '2022-08-16 19:06:41', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `files`
--
ALTER TABLE `files`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `files`
--
ALTER TABLE `files`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
