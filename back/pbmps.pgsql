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
-- Name: login_mahasiswa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.login_mahasiswa (
    username character varying(50) NOT NULL,
    password character varying(50) NOT NULL
);


ALTER TABLE public.login_mahasiswa OWNER TO postgres;

--
-- Name: login_mapping_mahasiswa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.login_mapping_mahasiswa (
    nim character varying(10),
    username character varying(50) NOT NULL
);


ALTER TABLE public.login_mapping_mahasiswa OWNER TO postgres;

--
-- Name: login_mapping_penyedia; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.login_mapping_penyedia (
    id_penyedia integer,
    username character varying(50) NOT NULL
);


ALTER TABLE public.login_mapping_penyedia OWNER TO postgres;

--
-- Name: login_penyedia; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.login_penyedia (
    username character varying(50) NOT NULL,
    password character varying(50) NOT NULL
);


ALTER TABLE public.login_penyedia OWNER TO postgres;

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
    gpa real,
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
    waktu_submit integer
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
2	Beasiswa Pemberdayaan	20191106	20191206	STEI	STI	5	2.0999999	Test	7
5	Beasiswa dengan Magang	22032020	22032021	STEI	EL	3	3.5	Ada kesempatan ke luar negeri	5
1	Beasiswa Unggulan	20191106	20191107	STEI	STI	5	3.0999999	Test	7
\.


--
-- Data for Name: login_mahasiswa; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.login_mahasiswa (username, password) FROM stdin;
nicho	nicho
wealth	wealth
\.


--
-- Data for Name: login_mapping_mahasiswa; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.login_mapping_mahasiswa (nim, username) FROM stdin;
18217041	wealth
\.


--
-- Data for Name: login_mapping_penyedia; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.login_mapping_penyedia (id_penyedia, username) FROM stdin;
32	tanoto
33	kemenristek
\.


--
-- Data for Name: login_penyedia; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.login_penyedia (username, password) FROM stdin;
tanoto	tanoto
kemenristek	kemenristek
\.


--
-- Data for Name: mahasiswa; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mahasiswa (nim, email, password, nama, no_telepon, usia, jurusan, semester, gpa, pendapatan, berkas) FROM stdin;
18217028	18217028@std.stei.itb.ac.id	swordbeach	Nicholaus	08989259809	21	STI	5	3.5	2000000	shfsbjhbfsjbfshdbf
18217022	18217022@std.stei.itb.ac.id	abc	Alfin	08232323	21	STI	6	4	20000000	jjbdvhxjvbhxjcv
18217030	18217030@std.stei.itb.ac.id	abcd	Feby	085656454	21	STI	6	4	50000000	jjbdvsdsdhxjvbhxjcv
18217051	18217051@std.stei.itb.ac.id	abcde	Johnnie Walker	08565553454	21	STI	7	2.79999995	50000000	jjbdvsddfdfsdhxjvbhxjcv
18217041	182@gmail.com	test	wealthtan	081234567890	20	STI	5	3.79999995	99999999	lengkap
\.


--
-- Data for Name: penyedia_beasiswa; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.penyedia_beasiswa (id_penyedia, nama, email, no_telepon, alamat, website) FROM stdin;
1	Bank Indonesia	BI@gmail.com	123456	ITB	www.bi.id
2	Kemdikbud	kemdikbud@gmail.com	12345678	Indonesia	www.kemdikbud.id
5	GDP	gdplabs@gmail.com	082929292	Mega Kuningan	gdplabs.id
6	LOL	lols@gmail.com	082929292	Mega Kuningan	gdplabs.id
8	Mekari	mekari@gmail.com	08008080	Taman Lawang	het.co.id
9	Mekari2	mekari@gmail.com	08008080	Taman Lawang	het.co.id
10	Bank BRI	BRI@gmail.com	08343434	BRI HQ	www.bri.co.id
11	Bank BCA	BCA@gmail.com	0833434434	BCA HQ	www.bca.co.id
16	Crypton Media	crypton_media@gmail.com	08338347334	Tokyo	www.crypton.co.jp
19	whentai	nhentai@gmail.com	08923434	Osaka	www.nhentai.co.jp
21	DY	dy@gmail.com	081234567890	venetian	ph.com
22	DY	dy@gmail.com	081234567890	venetian	ph.com
25	DY	dy@gmail.com	081234567890	venetian	ph.com
26	DY	dy@gmail.com	081234567890	venetian	ph.com
28	DY	dy@gmail.com	081234567890	venetian	ph.com
30	DY	dy@gmail.com	081234567890	venetian	ph.com
31	DY	dy@gmail.com	081234567890	venetian	ph.com
32	DY	dy@gmail.com	081234567890	venetian	ph.com
33	Kemenristek	kemenristek@gmail.com	0898988	ITB	www.kemenristek.com
\.


--
-- Data for Name: pilihan_beasiswa; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pilihan_beasiswa (id_penyedia, nim, status_seleksi, waktu_submit) FROM stdin;
5	18217030	Diterima	20190324
5	18217051	Ditolak	20190324
2	18217028	Diterima	20190322
2	18217022	Diterima	20190324
\.


--
-- Name: penyedia_beasiswa_id_penyedia_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.penyedia_beasiswa_id_penyedia_seq', 33, true);


--
-- Name: login_mahasiswa login_mahasiswa_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_mahasiswa
    ADD CONSTRAINT login_mahasiswa_pkey PRIMARY KEY (username);


--
-- Name: login_mapping_mahasiswa login_mapping_mahasiswa_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_mapping_mahasiswa
    ADD CONSTRAINT login_mapping_mahasiswa_username_key UNIQUE (username);


--
-- Name: login_mapping_penyedia login_mapping_penyedia_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_mapping_penyedia
    ADD CONSTRAINT login_mapping_penyedia_username_key UNIQUE (username);


--
-- Name: login_penyedia login_penyedia_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_penyedia
    ADD CONSTRAINT login_penyedia_pkey PRIMARY KEY (username);


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
-- Name: login_mapping_mahasiswa login_mapping_mahasiswa_nim_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_mapping_mahasiswa
    ADD CONSTRAINT login_mapping_mahasiswa_nim_fkey FOREIGN KEY (nim) REFERENCES public.mahasiswa(nim);


--
-- Name: login_mapping_mahasiswa login_mapping_mahasiswa_username_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_mapping_mahasiswa
    ADD CONSTRAINT login_mapping_mahasiswa_username_fkey FOREIGN KEY (username) REFERENCES public.login_mahasiswa(username);


--
-- Name: login_mapping_penyedia login_mapping_penyedia_id_penyedia_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_mapping_penyedia
    ADD CONSTRAINT login_mapping_penyedia_id_penyedia_fkey FOREIGN KEY (id_penyedia) REFERENCES public.penyedia_beasiswa(id_penyedia);


--
-- Name: login_mapping_penyedia login_mapping_penyedia_username_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_mapping_penyedia
    ADD CONSTRAINT login_mapping_penyedia_username_fkey FOREIGN KEY (username) REFERENCES public.login_penyedia(username);


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

