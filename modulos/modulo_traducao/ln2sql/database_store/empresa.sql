-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Tempo de geração: 08-Nov-2021 às 19:53
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
-- Banco de dados: `empresa`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `DEPARTAMENTO`
--

CREATE TABLE `DEPARTAMENTO` (
  `Dnome` varchar(15) NOT NULL,
  `Dnumero` int NOT NULL,
  `Cpf_gerente` char(11) DEFAULT NULL,
  `Data_inicio_gerente` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `DEPARTAMENTO`
--

INSERT INTO `DEPARTAMENTO` (`Dnome`, `Dnumero`, `Cpf_gerente`, `Data_inicio_gerente`) VALUES
('Matriz', 1, '88866555576', '1981-06-19'),
('Administracao', 4, '98765432168', '1995-01-01'),
('Pesquisa', 5, '33344555587', '1988-05-22');

-- --------------------------------------------------------

--
-- Estrutura da tabela `DEPENDENTE`
--

CREATE TABLE `DEPENDENTE` (
  `Fcpf` char(11) NOT NULL,
  `Nome_dependente` varchar(15) NOT NULL,
  `Sexo` char(1) DEFAULT NULL,
  `Datanasc` date DEFAULT NULL,
  `Parentesco` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `DEPENDENTE`
--

INSERT INTO `DEPENDENTE` (`Fcpf`, `Nome_dependente`, `Sexo`, `Datanasc`, `Parentesco`) VALUES
('12345678966', 'Alice', 'F', '1988-12-30', 'Filha'),
('12345678966', 'Elizabeth', 'F', '1967-05-05', 'Esposa'),
('12345678966', 'Michael', 'M', '1988-01-04', 'Filho'),
('33344555587', 'Alicia', 'F', '1986-04-05', 'Filha'),
('33344555587', 'Janaina', 'F', '1958-05-03', 'Esposa'),
('33344555587', 'Tiago', 'M', '1983-10-25', 'Filho'),
('98765432168', 'Antonio', 'M', '1942-02-28', 'Marido');

-- --------------------------------------------------------

--
-- Estrutura da tabela `FUNCIONARIO`
--

CREATE TABLE `FUNCIONARIO` (
  `Pnome` varchar(15) NOT NULL,
  `Minicial` char(1) DEFAULT NULL,
  `Unome` varchar(15) NOT NULL,
  `Cpf` char(11) NOT NULL,
  `Datanasc` date NOT NULL,
  `Endereco` varchar(40) DEFAULT NULL,
  `Sexo` char(1) DEFAULT NULL,
  `Salario` decimal(10,2) DEFAULT NULL,
  `Cpf_supervisor` char(11) DEFAULT NULL,
  `Dnr` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `FUNCIONARIO`
--

INSERT INTO `FUNCIONARIO` (`Pnome`, `Minicial`, `Unome`, `Cpf`, `Datanasc`, `Endereco`, `Sexo`, `Salario`, `Cpf_supervisor`, `Dnr`) VALUES
('João', 'B', 'Silva', '12345678966', '1965-01-09', 'Rua das flores, 751, São Paulo, SP', 'M', '30000.00', '33344555587', 5),
('Fernando', 'T', 'Wong', '33344555587', '1955-12-08', 'Rua da lapa, 34, Sao Paulo, SP', 'M', '40000.00', '88866555576', 5),
('Joice', 'A', 'Leite', '45345345376', '1972-07-31', 'Av. Lucas Obes, 74,São Paulo, SP', 'F', '25000.00', '33344555587', 4),
('Ronaldo', 'K', 'Lima', '66688444476', '1962-09-15', 'Rua Rebouças,65, Piracicaba, SP', 'M', '38000.00', '33344555587', 5),
('Jorge', 'E', 'Brito', '88866555576', '1937-11-10', 'Rua do Horto, 35,São Paulo, SP', 'M', '55000.00', NULL, 1),
('Jennifer', 'S', 'Souza', '98765432168', '1941-06-20', 'Av. Arthur de Lima, 54, Santo Andre, SP', 'F', '43000.00', '88866555576', 4),
('André', 'V', 'Pereira', '98798798733', '1969-03-29', 'Rua Timbira, 35,São Paulo, SP', 'M', '25000.00', '98765432168', 4),
('Alice', 'J', 'Zelaya', '99988777767', '1968-01-19', 'Rua Souza Lima, 35, Curitiba, PR', 'F', '25000.00', '98765432168', 4);

-- --------------------------------------------------------

--
-- Estrutura da tabela `LOCALIZACAO_DEP`
--

CREATE TABLE `LOCALIZACAO_DEP` (
  `Dnumero` int NOT NULL,
  `Dlocal` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `LOCALIZACAO_DEP`
--

INSERT INTO `LOCALIZACAO_DEP` (`Dnumero`, `Dlocal`) VALUES
(1, 'São Paulo'),
(4, 'Mauá'),
(5, 'Itú'),
(5, 'Santo Andre'),
(5, 'São Paulo');

-- --------------------------------------------------------

--
-- Estrutura da tabela `PROJETO`
--

CREATE TABLE `PROJETO` (
  `Projnome` varchar(15) NOT NULL,
  `Projnumero` int NOT NULL,
  `Projlocal` varchar(15) DEFAULT NULL,
  `Dnum` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `PROJETO`
--

INSERT INTO `PROJETO` (`Projnome`, `Projnumero`, `Projlocal`, `Dnum`) VALUES
('ProdutoX', 1, 'Santo Andre', 5),
('ProdutoY', 2, 'Itu', 5),
('ProdutoZ', 3, 'São Paulo', 5),
('Informatizacao', 10, 'Maua', 4),
('Reorganizacao', 20, 'Sao Paulo', 1),
('NovosBeneficios', 30, 'Maua', 4);

-- --------------------------------------------------------

--
-- Estrutura da tabela `TRABALHA_EM`
--

CREATE TABLE `TRABALHA_EM` (
  `Fcpf` char(11) NOT NULL,
  `Pnr` int NOT NULL,
  `Horas` decimal(3,1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `TRABALHA_EM`
--

INSERT INTO `TRABALHA_EM` (`Fcpf`, `Pnr`, `Horas`) VALUES
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
-- Índices para tabela `DEPARTAMENTO`
--
ALTER TABLE `DEPARTAMENTO`
  ADD PRIMARY KEY (`Dnumero`),
  ADD UNIQUE KEY `Dnome` (`Dnome`),
  ADD KEY `Cpf_gerente` (`Cpf_gerente`);

--
-- Índices para tabela `DEPENDENTE`
--
ALTER TABLE `DEPENDENTE`
  ADD PRIMARY KEY (`Fcpf`,`Nome_dependente`);

--
-- Índices para tabela `FUNCIONARIO`
--
ALTER TABLE `FUNCIONARIO`
  ADD PRIMARY KEY (`Cpf`),
  ADD KEY `Cpf_supervisor` (`Cpf_supervisor`),
  ADD KEY `Dnr` (`Dnr`);

--
-- Índices para tabela `LOCALIZACAO_DEP`
--
ALTER TABLE `LOCALIZACAO_DEP`
  ADD PRIMARY KEY (`Dnumero`,`Dlocal`);

--
-- Índices para tabela `PROJETO`
--
ALTER TABLE `PROJETO`
  ADD PRIMARY KEY (`Projnumero`),
  ADD UNIQUE KEY `Projnome` (`Projnome`),
  ADD KEY `Dnum` (`Dnum`);

--
-- Índices para tabela `TRABALHA_EM`
--
ALTER TABLE `TRABALHA_EM`
  ADD PRIMARY KEY (`Fcpf`,`Pnr`),
  ADD KEY `Pnr` (`Pnr`);

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `DEPARTAMENTO`
--
ALTER TABLE `DEPARTAMENTO`
  ADD CONSTRAINT `DEPARTAMENTO_ibfk_1` FOREIGN KEY (`Cpf_gerente`) REFERENCES `FUNCIONARIO` (`Cpf`);

--
-- Limitadores para a tabela `DEPENDENTE`
--
ALTER TABLE `DEPENDENTE`
  ADD CONSTRAINT `DEPENDENTE_ibfk_1` FOREIGN KEY (`Fcpf`) REFERENCES `FUNCIONARIO` (`Cpf`);

--
-- Limitadores para a tabela `FUNCIONARIO`
--
ALTER TABLE `FUNCIONARIO`
  ADD CONSTRAINT `FUNCIONARIO_ibfk_1` FOREIGN KEY (`Cpf_supervisor`) REFERENCES `FUNCIONARIO` (`Cpf`),
  ADD CONSTRAINT `FUNCIONARIO_ibfk_2` FOREIGN KEY (`Dnr`) REFERENCES `DEPARTAMENTO` (`Dnumero`);

--
-- Limitadores para a tabela `LOCALIZACAO_DEP`
--
ALTER TABLE `LOCALIZACAO_DEP`
  ADD CONSTRAINT `LOCALIZACAO_DEP_ibfk_1` FOREIGN KEY (`Dnumero`) REFERENCES `DEPARTAMENTO` (`Dnumero`);

--
-- Limitadores para a tabela `PROJETO`
--
ALTER TABLE `PROJETO`
  ADD CONSTRAINT `PROJETO_ibfk_1` FOREIGN KEY (`Dnum`) REFERENCES `DEPARTAMENTO` (`Dnumero`);

--
-- Limitadores para a tabela `TRABALHA_EM`
--
ALTER TABLE `TRABALHA_EM`
  ADD CONSTRAINT `TRABALHA_EM_ibfk_1` FOREIGN KEY (`Pnr`) REFERENCES `PROJETO` (`Projnumero`),
  ADD CONSTRAINT `TRABALHA_EM_ibfk_2` FOREIGN KEY (`Fcpf`) REFERENCES `FUNCIONARIO` (`Cpf`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;