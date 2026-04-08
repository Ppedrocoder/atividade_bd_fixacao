-- =========================
-- AUTORES
-- =========================
INSERT INTO autor (nome, data_nascimento, nacionalidade) VALUES
('Machado de Assis', '1839-06-21', 'Brasileiro'),
('Clarice Lispector', '1920-12-10', 'Brasileira'),
('George Orwell', '1903-06-25', 'Britânico'),
('J.K. Rowling', '1965-07-31', 'Britânica'),
('J.R.R. Tolkien', '1892-01-03', 'Britânico');

-- =========================
-- CATEGORIAS
-- =========================
INSERT INTO categoria (nome, descricao) VALUES
('Romance', 'Histórias focadas em relacionamentos'),
('Ficção', 'Narrativas imaginárias'),
('Fantasia', 'Mundos fictícios e mágicos'),
('Tecnologia', 'Livros técnicos'),
('Clássico', 'Obras clássicas');

-- =========================
-- EDITORAS
-- =========================
INSERT INTO editora (nome, endereco) VALUES
('Companhia das Letras', 'São Paulo'),
('Record', 'Rio de Janeiro'),
('Penguin Books', 'Londres'),
('HarperCollins', 'Nova York'),
('Bloomsbury', 'Londres');

-- =========================
-- LIVROS
-- =========================
INSERT INTO livro (titulo, ano_publicacao, genero, id_autor, id_categoria, id_editora) VALUES
('Dom Casmurro', 1899, 'Romance', 1, 5, 1),
('A Hora da Estrela', 1977, 'Romance', 2, 1, 2),
('1984', 1949, 'Ficção', 3, 2, 3),
('Harry Potter', 1997, 'Fantasia', 4, 3, 5),
('O Hobbit', 1937, 'Fantasia', 5, 3, 3);

-- =========================
-- USUÁRIOS
-- =========================
INSERT INTO usuario (nome, email, data_registro) VALUES
('Carlos Silva', 'carlos@email.com', '2024-01-10'),
('Ana Souza', 'ana@email.com', '2024-02-15'),
('Pedro Lima', 'pedro@email.com', '2024-03-20'),
('Mariana Alves', 'mariana@email.com', '2024-04-05'),
('Lucas Pereira', 'lucas@email.com', '2024-05-01');

-- =========================
-- MULTAS
-- =========================
INSERT INTO multa (valor, data_aplicacao, data_pagamento, id_usuario) VALUES
(10.50, '2024-03-01', NULL, 1),
(5.00, '2024-03-10', '2024-03-15', 2),
(7.25, '2024-04-01', NULL, 3),
(12.00, '2024-04-10', '2024-04-12', 4),
(3.75, '2024-05-01', NULL, 5);

-- =========================
-- RESERVAS
-- =========================
INSERT INTO reserva (data_reserva, status_reserva, id_livro, id_usuario) VALUES
('2024-05-01', 'Ativa', 1, 1),
('2024-05-02', 'Concluida', 2, 2),
('2024-05-03', 'Vencida', 3, 3),
('2024-05-04', 'Ativa', 4, 4),
('2024-05-05', 'Ativa', 5, 5);

-- =========================
-- EMPRESTIMOS
-- =========================
INSERT INTO emprestimo (data_emprestimo, data_devolucao, id_usuario, id_livro) VALUES
('2024-04-01', '2024-04-10', 1, 1),
('2024-04-05', '2024-04-15', 2, 2),
('2024-04-10', NULL, 3, 3),
('2024-04-12', '2024-04-20', 4, 4),
('2024-04-15', NULL, 5, 5);