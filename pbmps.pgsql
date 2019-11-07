--
-- PostgreSQL database dump
--

-- Dumped from database version 10.10
-- Dumped by pg_dump version 10.10

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: detail_beasiswa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.detail_beasiswa (
    id_penyedia integer,
    nama character varying(50),
    waktu_buka integer,
    waktu_tutup integer,
    fakultas character varying(50),
    jurusan character varying(50),
    semester integer,
    min_gpa real,
    deskripsi character varying(500),
    batas_semester integer
);


ALTER TABLE public.detail_beasiswa OWNER TO postgres;

--
-- Name: mahasiswa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mahasiswa (
    nim character varying(10) NOT NULL,
    email character varying(50),
    password character varying(50),
    nama character varying(150),
    no_telepon character varying(20),
    usia integer,
    jurusan character varying(50),
    semester integer,
    gpa numeric(3,2),
    pendapatan integer,
    berkas character varying(400)
);


ALTER TABLE public.mahasiswa OWNER TO postgres;

--
-- Name: penyedia_beasiswa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.penyedia_beasiswa (
    id_penyedia integer NOT NULL,
    nama character varying(50),
    email character varying(50),
    no_telepon character varying(50),
    alamat character varying(50),
    website character varying(50)
);


ALTER TABLE public.penyedia_beasiswa OWNER TO postgres;

--
-- Name: penyedia_beasiswa_id_penyedia_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.penyedia_beasiswa_id_penyedia_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.penyedia_beasiswa_id_penyedia_seq OWNER TO postgres;

--
-- Name: penyedia_beasiswa_id_penyedia_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.penyedia_beasiswa_id_penyedia_seq OWNED BY public.penyedia_beasiswa.id_penyedia;


--
-- Name: pilihan_beasiswa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pilihan_beasiswa (
    id_penyedia integer NOT NULL,
    nim character varying(10) NOT NULL,
    status_seleksi character varying(20),
    waktu_submit timestamp without time zone
);


ALTER TABLE public.pilihan_beasiswa OWNER TO postgres;

--
-- Name: penyedia_beasiswa id_penyedia; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.penyedia_beasiswa ALTER COLUMN id_penyedia SET DEFAULT nextval('public.penyedia_beasiswa_id_penyedia_seq'::regclass);


--
-- Data for Name: detail_beasiswa; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.detail_beasiswa (id_penyedia, nama, waktu_buka, waktu_tutup, fakultas, jurusan, semester, min_gpa, deskripsi, batas_semester) FROM stdin;
1	Beasiswa Unggulan	20191106	20191206	STEI	STI	5	3.0999999	Test	7
2	Beasiswa Pemberdayaan	20191106	20191206	STEI	STI	5	2.0999999	Test	7
\.


--
-- Data for Name: mahasiswa; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mahasiswa (nim, email, password, nama, no_telepon, usia, jurusan, semester, gpa, pendapatan, berkas) FROM stdin;
\.


--
-- Data for Name: penyedia_beasiswa; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.penyedia_beasiswa (id_penyedia, nama, email, no_telepon, alamat, website) FROM stdin;
1	Bank Indonesia	BI@gmail.com	123456	ITB	www.bi.id
2	Kemdikbud	kemdikbud@gmail.com	12345678	Indonesia	www.kemdikbud.id
5	GDP	gdplabs@gmail.com	082929292	Mega Kuningan	gdplabs.id
6	LOL	lols@gmail.com	082929292	Mega Kuningan	gdplabs.id
\.


--
-- Data for Name: pilihan_beasiswa; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pilihan_beasiswa (id_penyedia, nim, status_seleksi, waktu_submit) FROM stdin;
\.


--
-- Name: penyedia_beasiswa_id_penyedia_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.penyedia_beasiswa_id_penyedia_seq', 6, true);


--
-- Name: mahasiswa mahasiswa_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mahasiswa
    ADD CONSTRAINT mahasiswa_pkey PRIMARY KEY (nim);


--
-- Name: penyedia_beasiswa penyedia_beasiswa_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.penyedia_beasiswa
    ADD CONSTRAINT penyedia_beasiswa_pkey PRIMARY KEY (id_penyedia);


--
-- Name: pilihan_beasiswa pilihan_beasiswa_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pilihan_beasiswa
    ADD CONSTRAINT pilihan_beasiswa_pkey PRIMARY KEY (id_penyedia, nim);


--
-- Name: detail_beasiswa detail_beasiswa_id_penyedia_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detail_beasiswa
    ADD CONSTRAINT detail_beasiswa_id_penyedia_fkey FOREIGN KEY (id_penyedia) REFERENCES public.penyedia_beasiswa(id_penyedia);


--
-- Name: pilihan_beasiswa pilihan_beasiswa_id_penyedia_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pilihan_beasiswa
    ADD CONSTRAINT pilihan_beasiswa_id_penyedia_fkey FOREIGN KEY (id_penyedia) REFERENCES public.penyedia_beasiswa(id_penyedia);


--
-- Name: pilihan_beasiswa pilihan_beasiswa_nim_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pilihan_beasiswa
    ADD CONSTRAINT pilihan_beasiswa_nim_fkey FOREIGN KEY (nim) REFERENCES public.mahasiswa(nim);


--
-- PostgreSQL database dump complete
--

