USE CupcakeDeliveryDB;

CREATE TABLE clientes
(
    id INT PRIMARY KEY IDENTITY(1,1),
    nome_completo NVARCHAR(255) NOT NULL,
    data_nascimento DATE NOT NULL,
    cpf NVARCHAR(14) NOT NULL,
    endereco NVARCHAR(255) NOT NULL,
    numero NVARCHAR(10) NOT NULL,
    bairro NVARCHAR(255) NOT NULL,
    complemento NVARCHAR(255),
    cidade NVARCHAR(255) NOT NULL,
    estado NVARCHAR(2) NOT NULL,
    cep NVARCHAR(10) NOT NULL,
    celular NVARCHAR(15) NOT NULL
);
