CREATE DATABASE sdss;

\connect sdss;

CREATE TABLE specobj (
    specobjid bigint,
    bestobjid bigint,
    fluxobjid bigint,
    ra float(8),
    dec float(8),
    class varchar(32),
    subclass varchar(32),
    z real,
    class_noqso varchar(32),
    z_noqso real,
    spectroflux_u real,
    spectroflux_g real,
    spectroflux_r real,
    spectroflux_i real,
    spectroflux_z real
);

COPY specobj FROM '/home/ubuntu/specobj.csv' DELIMITER ',' CSV;

CREATE TABLE photoprimary (
    objid bigint,
    specobjid bigint,
    run smallint,
    camcol smallint,
    field smallint,
    type smallint,
    ra float(8),
    dec float(8),
    u real,
    g real,
    r real,
    i real,
    z real
);

COPY photoprimary FROM '/home/ubuntu/photoprimary.csv' DELIMITER ',' CSV;

CREATE TABLE zoospec (
    specobjid bigint,
    objid bigint,
    dr7objid bigint,
    ra real,
    dec real,
    rastring varchar(11),
    decstring varchar(11),
    nvote int,
    p_el float(8),
    p_cw float(8),
    p_acw float(8),
    p_edge float(8),
    p_dk float(8),
    p_mg float(8),
    p_cs float(8),
    p_el_debiased float(8),
    p_cs_debiased float(8),
    spiral int,
    elliptical int,
    uncertain int
);

COPY zoospec FROM '/home/ubuntu/zoospec.csv' DELIMITER ',' CSV;