-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 24, 2023 at 06:51 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `interview_app`
--

-- --------------------------------------------------------

--
-- Table structure for table `ap_category`
--

CREATE TABLE `ap_category` (
  `id` int(11) NOT NULL,
  `category` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ap_category`
--

INSERT INTO `ap_category` (`id`, `category`) VALUES
(1, 'General Aptitude'),
(2, 'Programming');

-- --------------------------------------------------------

--
-- Table structure for table `ap_exam`
--

CREATE TABLE `ap_exam` (
  `id` int(11) NOT NULL,
  `sid` int(11) NOT NULL,
  `num_question` int(11) NOT NULL,
  `mark` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ap_exam`
--

INSERT INTO `ap_exam` (`id`, `sid`, `num_question`, `mark`) VALUES
(1, 1, 5, 1);

-- --------------------------------------------------------

--
-- Table structure for table `ap_exam_attend`
--

CREATE TABLE `ap_exam_attend` (
  `id` int(11) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `eid` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  `attend` int(11) NOT NULL,
  `correct` int(11) NOT NULL,
  `mark` int(11) NOT NULL,
  `percent` double NOT NULL,
  `status` int(11) NOT NULL,
  `qid` int(11) NOT NULL,
  `sid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ap_exam_attend`
--


-- --------------------------------------------------------

--
-- Table structure for table `ap_files`
--

CREATE TABLE `ap_files` (
  `id` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `sid` int(11) NOT NULL,
  `filename` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ap_files`
--

INSERT INTO `ap_files` (`id`, `cid`, `sid`, `filename`) VALUES
(1, 2, 1, 'F1a.txt');

-- --------------------------------------------------------

--
-- Table structure for table `ap_hr`
--

CREATE TABLE `ap_hr` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `company` varchar(30) NOT NULL,
  `address` varchar(50) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ap_hr`
--

INSERT INTO `ap_hr` (`id`, `name`, `company`, `address`, `mobile`, `email`, `uname`, `pass`) VALUES
(1, 'Rahul', 'HCL', 'Chennai', 8954545121, 'rahul@gmail.com', 'rahul', '123456');

-- --------------------------------------------------------

--
-- Table structure for table `ap_login`
--

CREATE TABLE `ap_login` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ap_login`
--

INSERT INTO `ap_login` (`username`, `password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `ap_subcat`
--

CREATE TABLE `ap_subcat` (
  `id` int(11) NOT NULL,
  `cat_id` int(11) NOT NULL,
  `subcat` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ap_subcat`
--

INSERT INTO `ap_subcat` (`id`, `cat_id`, `subcat`) VALUES
(1, 2, 'Java Programming');

-- --------------------------------------------------------

--
-- Table structure for table `ap_test_question`
--

CREATE TABLE `ap_test_question` (
  `id` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `sid` int(11) NOT NULL,
  `question` varchar(200) NOT NULL,
  `option1` varchar(100) NOT NULL,
  `option2` varchar(100) NOT NULL,
  `option3` varchar(100) NOT NULL,
  `option4` varchar(100) NOT NULL,
  `answer` int(11) NOT NULL,
  `details` text NOT NULL,
  `filename` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ap_test_question`
--

INSERT INTO `ap_test_question` (`id`, `cid`, `sid`, `question`, `option1`, `option2`, `option3`, `option4`, `answer`, `details`, `filename`) VALUES
(1, 2, 1, 'Which one of these lists contains only Java programming language keywords?', 'class, if, void, long, Int, continue', ' goto, instanceof, native, finally, default, throws', 'try, virtual, throw, final, volatile, transient', ' strictfp, constant, super, implements, do', 2, 'All the words in option B are among the 49 Java keywords. Although goto reserved as a keyword in Java, goto is not used and has no function.\r\n\r\nOption A is wrong because the keyword for the primitive int starts with a lowercase i.\r\n\r\nOption C is wrong because "virtual" is a keyword in C++, but not Java.\r\n\r\nOption D is wrong because "constant" is not a keyword. Constants in Java are marked static and final.\r\n\r\nOption E is wrong because "include" is a keyword in C, but not in Java.', ''),
(2, 2, 1, 'Which is a reserved word in the Java programming language?', 'method', 'native', 'subclasses', 'reference', 2, 'The word "native" is a valid keyword, used to modify a method declaration.\r\n\r\nOption A, D and E are not keywords. Option C is wrong because the keyword for subclassing in Java is extends, not ''subclasses''.', ''),
(3, 2, 1, 'Which is a valid keyword in java?', 'interface', 'string', 'Float', 'unsigned', 1, 'interface is a valid keyword.\r\n\r\nOption B is wrong because although "String" is a class type in Java, "string" is not a keyword.\r\n\r\nOption C is wrong because "Float" is a class type. The keyword for the Java primitive is float.\r\n\r\nOption D is wrong because "unsigned" is a keyword in C/C++ but not in Java.', ''),
(4, 2, 1, 'Which one of the following will declare an array and initialize it with five numbers?', 'Array a = new Array(5);', 'int [] a = {23,22,21,20,19};', ' int a [] = new int[5];', ' int [5] array;', 2, '', ''),
(5, 2, 1, 'Which is the valid declarations within an interface definition?', 'public double methoda();', ' public final double methoda();', 'static void methoda(double d1);', 'protected void methoda(double d1);', 1, '', '');

-- --------------------------------------------------------

--
-- Table structure for table `ap_time`
--

CREATE TABLE `ap_time` (
  `id` int(11) NOT NULL,
  `user` varchar(20) NOT NULL,
  `t1` varchar(20) NOT NULL,
  `t2` varchar(20) NOT NULL,
  `t3` varchar(20) NOT NULL,
  `t4` varchar(20) NOT NULL,
  `tdate` varchar(20) NOT NULL,
  `rdate` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ap_time`
--

INSERT INTO `ap_time` (`id`, `user`, `t1`, `t2`, `t3`, `t4`, `tdate`, `rdate`) VALUES
(1, 'pravin', '12', '5', '13', '30', '24-04-2023', '24-04-2023');

-- --------------------------------------------------------

--
-- Table structure for table `ap_train_question`
--

CREATE TABLE `ap_train_question` (
  `id` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `sid` int(11) NOT NULL,
  `question` varchar(200) NOT NULL,
  `option1` varchar(100) NOT NULL,
  `option2` varchar(100) NOT NULL,
  `option3` varchar(100) NOT NULL,
  `option4` varchar(100) NOT NULL,
  `answer` int(11) NOT NULL,
  `details` text NOT NULL,
  `filename` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ap_train_question`
--

INSERT INTO `ap_train_question` (`id`, `cid`, `sid`, `question`, `option1`, `option2`, `option3`, `option4`, `answer`, `details`, `filename`) VALUES
(1, 2, 1, 'Which one of these lists contains only Java programming language keywords?', 'class, if, void, long, Int, continue', ' goto, instanceof, native, finally, default, throws', 'try, virtual, throw, final, volatile, transient', ' strictfp, constant, super, implements, do', 2, 'All the words in option B are among the 49 Java keywords. Although goto reserved as a keyword in Java, goto is not used and has no function.\r\n\r\nOption A is wrong because the keyword for the primitive int starts with a lowercase i.\r\n\r\nOption C is wrong because "virtual" is a keyword in C++, but not Java.\r\n\r\nOption D is wrong because "constant" is not a keyword. Constants in Java are marked static and final.\r\n\r\nOption E is wrong because "include" is a keyword in C, but not in Java.', 'F1dd.txt'),
(2, 2, 1, 'Which is a reserved word in the Java programming language?', 'method', 'native', 'subclasses', 'reference', 2, 'The word "native" is a valid keyword, used to modify a method declaration.\r\n\r\nOption A, D and E are not keywords. Option C is wrong because the keyword for subclassing in Java is extends, not ''subclasses''.', ''),
(3, 2, 1, 'Which is a valid keyword in java?', 'interface', 'string', 'Float', 'unsigned', 1, 'interface is a valid keyword.\r\n\r\nOption B is wrong because although "String" is a class type in Java, "string" is not a keyword.\r\n\r\nOption C is wrong because "Float" is a class type. The keyword for the Java primitive is float.\r\n\r\nOption D is wrong because "unsigned" is a keyword in C/C++ but not in Java.', ''),
(4, 2, 1, 'Which is true about a method-local inner class?', 'It must be marked final.', ' It can be marked abstract.', 'It can be marked public.', ' It can be marked static.', 2, 'Option B is correct because a method-local inner class can be abstract, although it means a subclass of the inner class must be created if the abstract class is to be used (so an abstract method-local inner class is probably not useful).\r\n\r\nOption A is incorrect because a method-local inner class does not have to be declared final (although it is legal to do so).\r\n\r\nC and D are incorrect because a method-local inner class cannot be made public (remember-you cannot mark any local variables as public), or static.', ''),
(5, 2, 1, 'Which statement is true about a static nested class?', 'You must have a reference to an instance of the enclosing class in order to instantiate it.', ' It does not have access to nonstatic members of the enclosing class.', ' It''s variables and methods must be static.', 'It must extend the enclosing class.', 2, 'Option B is correct because a static nested class is not tied to an instance of the enclosing class, and thus can''t access the nonstatic members of the class (just as a static method can''t access nonstatic members of a class).', ''),
(6, 2, 1, 'Which constructs an anonymous inner class instance?', ' Runnable r = new Runnable() { };', ' Runnable r = new Runnable(public void run() { });', ' Runnable r = new Runnable { public void run(){}};', ' System.out.println(new Runnable() {public void run() { }});', 4, 'D is correct. It defines an anonymous inner class instance, which also means it creates an instance of that new anonymous class at the same time. The anonymous class is an implementer of the Runnable interface, so it must override the run() method of Runnable.', '');

-- --------------------------------------------------------

--
-- Table structure for table `ap_user`
--

CREATE TABLE `ap_user` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(20) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL,
  `create_date` varchar(20) NOT NULL,
  `questions` varchar(200) NOT NULL,
  `eid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ap_user`
--

INSERT INTO `ap_user` (`id`, `name`, `gender`, `dob`, `address`, `city`, `mobile`, `email`, `uname`, `pass`, `create_date`, `questions`, `eid`) VALUES
(1, 'Pravin', 'Male', '2000-03-23', '56, GD Nagar', 'Karur', 8856545584, 'pravin@gmail.com', 'pravin', '123456', '12-03-2023', '6,2,5,3,4', 1),
(2, 'Ram', 'Male', '1999-06-05', '44,GG', 'Madurai', 9638527415, 'ram@gmail.com', 'ram', '1234', '19-04-2023', '', 0);
