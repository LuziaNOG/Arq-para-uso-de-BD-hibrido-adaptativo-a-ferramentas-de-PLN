-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Tempo de geração: 02-Nov-2021 às 20:11
-- Versão do servidor: 8.0.27-0ubuntu0.20.04.1
-- versão do PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `company`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `department`
--

CREATE TABLE `department` (
  `dname` varchar(15) NOT NULL,
  `dnumber` int NOT NULL,
  `cpf_manager` char(11) DEFAULT NULL,
  `start_date_manager` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `department`
--

INSERT INTO `department` (`dname`, `dnumber`, `cpf_manager`, `start_date_manager`) VALUES
('Matriz', 1, '88866555576', '1981-06-19'),
('Administracao', 4, '98765432168', '1995-01-01'),
('Pesquisa', 5, '33344555587', '1988-05-22');

-- --------------------------------------------------------

--
-- Estrutura da tabela `dependent`
--

CREATE TABLE `dependent` (
  `fcpf` char(11) NOT NULL,
  `name_dependent` varchar(15) NOT NULL,
  `sexo` char(1) DEFAULT NULL,
  `date_birth` date DEFAULT NULL,
  `parentage` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `dependent`
--

INSERT INTO `dependent` (`fcpf`, `name_dependent`, `sexo`, `date_birth`, `parentage`) VALUES
('12345678966', 'Alice', 'F', '1988-12-30', 'Filha'),
('12345678966', 'Elizabeth', 'F', '1967-05-05', 'Esposa'),
('12345678966', 'Michael', 'M', '1988-01-04', 'Filho'),
('33344555587', 'Alicia', 'F', '1986-04-05', 'Filha'),
('33344555587', 'Janaina', 'F', '1958-05-03', 'Esposa'),
('33344555587', 'Tiago', 'M', '1983-10-25', 'Filho'),
('98765432168', 'Antonio', 'M', '1942-02-28', 'Marido');

-- --------------------------------------------------------

--
-- Estrutura da tabela `employee`
--

CREATE TABLE `employee` (
  `pname` varchar(15) NOT NULL,
  `minicial` char(1) DEFAULT NULL,
  `uname` varchar(15) NOT NULL,
  `cpf` char(11) NOT NULL,
  `date_birth` date NOT NULL,
  `address` varchar(40) DEFAULT NULL,
  `sexo` char(1) DEFAULT NULL,
  `salary` decimal(10,2) DEFAULT NULL,
  `cpf_supervisor` char(11) DEFAULT NULL,
  `dnr` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `employee`
--

INSERT INTO `employee` (`pname`, `minicial`, `uname`, `cpf`, `date_birth`, `address`, `sexo`, `salary`, `cpf_supervisor`, `dnr`) VALUES
('João', 'B', 'Silva', '12345678966', '1965-01-09', 'Rua das flores, 751, São Paulo, SP', 'M', '30000.00', '33344555587', 5),
('Fernando', 'T', 'Wong', '33344555587', '1955-12-08', 'Rua da lapa, 34, Sao Paulo, SP', 'M', '40000.00', '88866555576', 5),
('Joice', 'A', 'Leite', '45345345376', '1972-07-31', 'Av. Lucas Obes, 74,São Paulo, SP', 'F', '25000.00', '33344555587', NULL),
('Ronaldo', 'K', 'Lima', '66688444476', '1962-09-15', 'Rua Rebouças,65, Piracicaba, SP', 'M', '38000.00', '33344555587', 5),
('Jorge', 'E', 'Brito', '88866555576', '1937-11-10', 'Rua do Horto, 35,São Paulo, SP', 'M', '55000.00', NULL, 1),
('Jennifer', 'S', 'Souza', '98765432168', '1941-06-20', 'Av. Arthur de Lima, 54, Santo Andre, SP', 'F', '43000.00', '88866555576', 4),
('André', 'V', 'Pereira', '98798798733', '1969-03-29', 'Rua Timbira, 35,São Paulo, SP', 'M', '25000.00', '98765432168', NULL),
('Alice', 'J', 'Zelaya', '99988777767', '1968-01-19', 'Rua Souza Lima, 35, Curitiba, PR', 'F', '25000.00', '98765432168', 4);

-- --------------------------------------------------------

--
-- Estrutura da tabela `location_dep`
--

CREATE TABLE `location_dep` (
  `dnumber` int NOT NULL,
  `dlocal` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `location_dep`
--

INSERT INTO `location_dep` (`dnumber`, `dlocal`) VALUES
(1, 'São Paulo'),
(4, 'Mauá'),
(5, 'Itú'),
(5, 'Santo Andre'),
(5, 'São Paulo');

-- --------------------------------------------------------

--
-- Estrutura da tabela `project`
--

CREATE TABLE `project` (
  `projname` varchar(15) NOT NULL,
  `projnumber` int NOT NULL,
  `projlocal` varchar(15) DEFAULT NULL,
  `dnum` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `project`
--

INSERT INTO `project` (`projname`, `projnumber`, `projlocal`, `dnum`) VALUES
('ProdutoX', 1, 'Santo Andre', 5),
('ProdutoY', 2, 'Itu', 5),
('ProdutoZ', 3, 'São Paulo', 5),
('Informatizacao', 10, 'Maua', 4),
('Reorganizacao', 20, 'Sao Paulo', 1),
('NovosBeneficios', 30, 'Maua', 4);

-- --------------------------------------------------------

--
-- Estrutura da tabela `works_in`
--

CREATE TABLE `works_in` (
  `fcpf` char(11) NOT NULL,
  `pnr` int NOT NULL,
  `hours` decimal(3,1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `works_in`
--

INSERT INTO `works_in` (`fcpf`, `pnr`, `hours`) VALUES
('12345678966', 1, '32.5'),
('12345678966', 2, '7.5'),
('33344555587', 2, '10.0'),
('33344555587', 3, '10.0'),
('33344555587', 10, '10.0'),
('33344555587', 20, '10.0'),
('45345345376', 1, '20.0'),
('45345345376', 2, '20.0'),
('66688444476', 3, '40.0'),
('88866555576', 20, '10.0'),
('98765432168', 20, '15.0'),
('98765432168', 30, '20.0'),
('98798798733', 10, '35.0'),
('98798798733', 30, '5.0'),
('99988777767', 10, '10.0'),
('99988777767', 30, '30.0');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`dnumber`),
  ADD UNIQUE KEY `dname` (`dname`),
  ADD KEY `cpf_manager` (`cpf_manager`);

--
-- Índices para tabela `dependent`
--
ALTER TABLE `dependent`
  ADD PRIMARY KEY (`fcpf`,`name_dependent`);

--
-- Índices para tabela `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`cpf`),
  ADD KEY `cpf_supervisor` (`cpf_supervisor`),
  ADD KEY `dnr` (`dnr`);

--
-- Índices para tabela `location_dep`
--
ALTER TABLE `location_dep`
  ADD PRIMARY KEY (`dnumber`,`dlocal`);

--
-- Índices para tabela `project`
--
ALTER TABLE `project`
  ADD PRIMARY KEY (`projnumber`),
  ADD UNIQUE KEY `projname` (`projname`),
  ADD KEY `dnum` (`dnum`);

--
-- Índices para tabela `works_in`
--
ALTER TABLE `works_in`
  ADD PRIMARY KEY (`fcpf`,`pnr`),
  ADD KEY `pnr` (`pnr`);

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `department`
--
ALTER TABLE `department`
  ADD CONSTRAINT `department_ibfk_1` FOREIGN KEY (`cpf_manager`) REFERENCES `employee` (`cpf`);

--
-- Limitadores para a tabela `dependent`
--
ALTER TABLE `dependent`
  ADD CONSTRAINT `dependent_ibfk_1` FOREIGN KEY (`fcpf`) REFERENCES `employee` (`cpf`);

--
-- Limitadores para a tabela `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`cpf_supervisor`) REFERENCES `employee` (`cpf`),
  ADD CONSTRAINT `employee_ibfk_2` FOREIGN KEY (`dnr`) REFERENCES `department` (`dnumber`);

--
-- Limitadores para a tabela `location_dep`
--
ALTER TABLE `location_dep`
  ADD CONSTRAINT `location_dep_ibfk_1` FOREIGN KEY (`dnumber`) REFERENCES `department` (`dnumber`);

--
-- Limitadores para a tabela `project`
--
ALTER TABLE `project`
  ADD CONSTRAINT `project_ibfk_1` FOREIGN KEY (`dnum`) REFERENCES `department` (`dnumber`);

--
-- Limitadores para a tabela `works_in`
--
ALTER TABLE `works_in`
  ADD CONSTRAINT `works_in_ibfk_1` FOREIGN KEY (`pnr`) REFERENCES `project` (`projnumber`),
  ADD CONSTRAINT `works_in_ibfk_2` FOREIGN KEY (`fcpf`) REFERENCES `employee` (`cpf`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;