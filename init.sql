SELECT 'CREATE DATABASE backend'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'backend')\gexec

SELECT 'CREATE DATABASE backend_test'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'backend_test')\gexec
