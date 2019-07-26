-- 1.0.0
-- Para ejecurar desde la consola de Postgresql usamos
-- C:\Users\JSM>psql -h localhost -U postgres
-- Contraseña para usuario postgres:
-- postgres=# \i C:/python-01/crea_bd.sql
--
-- Database: bd_ventas01
DROP DATABASE if exists bd_ventas01; -- Si la BD existe se elimina 
CREATE DATABASE bd_ventas01
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Spain.1252'
    LC_CTYPE = 'Spanish_Spain.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- Creamos la tabla para clientes
DROP TABLE IF EXISTS t_cliente; 
--DROP SEQUENCE IF EXISTS csd_relationship_csd_relationship_id_seq;
CREATE TABLE public.t_cliente
(
    cod_cliente character varying(18)[] COLLATE pg_catalog."default" NOT NULL, --llave
    nom_cliente character varying(150)[] COLLATE pg_catalog."default",
    cl_direccion character varying(200)[] COLLATE pg_catalog."default",
    cl_telefono character varying(15)[] COLLATE pg_catalog."default",
    CONSTRAINT t_cliente_pkey PRIMARY KEY (cod_cliente)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.t_cliente
    OWNER to postgres;

-- Creamos la tabla para productos
CREATE TABLE public.t_productos
(
    cod_producto character varying(10)[] COLLATE pg_catalog."default" NOT NULL, --llave
    nom_producto character varying(150)[] COLLATE pg_catalog."default",
    pr_stock integer[],
    pr_precio real,
    CONSTRAINT t_productos_pkey PRIMARY KEY (cod_producto)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.t_productos
    OWNER to postgres;

-- Creamos la tabla de factura por si la llegamos a usar
-- esta tabla almacena el encabezado de la factura
CREATE TABLE public.t_factura
(
    num_factura integer NOT NULL,
    fecha date,
    cod_cliente character varying(18)[] COLLATE pg_catalog."default",
    nom_cliente character varying(150)[] COLLATE pg_catalog."default",
    sub_total real,
    impuesto real,
    total real,
    CONSTRAINT t_factura_pkey PRIMARY KEY (num_factura)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.t_factura
    OWNER to postgres;

-- Creamos la tabla del detalle de factura por si la llegamos a usar
-- esta tabla almacena el detalle de las facturas
-- no cree el campo Doc_num del enunciado ya que creo q no va a ser necesario 
CREATE TABLE public.t_detalle
(
    num_factura integer,
    cod_producto character varying(15)[] COLLATE pg_catalog."default",
    nom_producto character varying(150)[] COLLATE pg_catalog."default",
    cantidad integer,
    precio real,
    impuesto real,
    tot_linea real
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.t_detalle
    OWNER to postgres;

