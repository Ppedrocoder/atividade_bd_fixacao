-- Apaga tudo
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

-- Permissões padrão (importante)
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;