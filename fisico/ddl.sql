-- ENUM correto no PostgreSQL
CREATE TYPE status_reserva_enum AS ENUM ('Ativa', 'Concluida', 'Vencida');

CREATE TABLE autor (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  data_nascimento DATE NOT NULL,
  nacionalidade VARCHAR(255) NOT NULL
);

CREATE TABLE categoria (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  descricao VARCHAR(255) NOT NULL
);

CREATE TABLE editora (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  endereco VARCHAR(255) NOT NULL
);

CREATE TABLE livro (
  id SERIAL PRIMARY KEY,
  titulo VARCHAR(255) NOT NULL,
  ano_publicacao INT NOT NULL,
  genero VARCHAR(255) NOT NULL,
  id_autor INT NOT NULL,
  id_categoria INT NOT NULL,
  id_editora INT NOT NULL,

  FOREIGN KEY (id_autor) REFERENCES autor(id) ON DELETE CASCADE,
  FOREIGN KEY (id_categoria) REFERENCES categoria(id) ON DELETE CASCADE,
  FOREIGN KEY (id_editora) REFERENCES editora(id) ON DELETE CASCADE
);

CREATE TABLE usuario (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  data_registro DATE DEFAULT CURRENT_DATE
);

CREATE TABLE multa (
  id SERIAL PRIMARY KEY,
  valor NUMERIC(10,2) NOT NULL,
  data_aplicacao DATE NOT NULL,
  data_pagamento DATE,
  id_usuario INT NOT NULL,

  FOREIGN KEY (id_usuario) REFERENCES usuario(id) ON DELETE CASCADE
);

CREATE TABLE reserva (
  id SERIAL PRIMARY KEY,
  data_reserva DATE DEFAULT CURRENT_DATE,
  status_reserva status_reserva_enum NOT NULL,
  id_livro INT NOT NULL,
  id_usuario INT NOT NULL,

  FOREIGN KEY (id_livro) REFERENCES livro(id) ON DELETE CASCADE,
  FOREIGN KEY (id_usuario) REFERENCES usuario(id) ON DELETE CASCADE
);

CREATE TABLE emprestimo (
  id SERIAL PRIMARY KEY,
  data_emprestimo DATE DEFAULT CURRENT_DATE,
  data_devolucao DATE,
  id_usuario INT NOT NULL,
  id_livro INT NOT NULL,

  FOREIGN KEY (id_livro) REFERENCES livro(id) ON DELETE CASCADE,
  FOREIGN KEY (id_usuario) REFERENCES usuario(id) ON DELETE CASCADE
);