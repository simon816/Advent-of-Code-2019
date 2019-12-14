#include <stdlib.h>
#include <stdio.h>
int count = 0;
long int residue_ORE = 1000000000000;
void acquire_ORE(int qty) {
    residue_ORE -= qty;
    if (residue_ORE < 0) {
        printf("%d\n", count);
        exit(0);
    }
}
void produce_ZJZRN();
void acquire_ZJZRN(int qty);
void produce_ZKCXK();
void acquire_ZKCXK(int qty);
void produce_ZWQX();
void acquire_ZWQX(int qty);
void produce_TCPN();
void acquire_TCPN(int qty);
void produce_DRWB();
void acquire_DRWB(int qty);
void produce_MBMKZ();
void acquire_MBMKZ(int qty);
void produce_KRTGD();
void acquire_KRTGD(int qty);
void produce_VNFJQ();
void acquire_VNFJQ(int qty);
void produce_TGJP();
void acquire_TGJP(int qty);
void produce_RHJCQ();
void acquire_RHJCQ(int qty);
void produce_QGDSV();
void acquire_QGDSV(int qty);
void produce_CTRH();
void acquire_CTRH(int qty);
void produce_FPZLF();
void acquire_FPZLF(int qty);
void produce_QBDQ();
void acquire_QBDQ(int qty);
void produce_GDJGV();
void acquire_GDJGV(int qty);
void produce_MBFK();
void acquire_MBFK(int qty);
void produce_LZKJZ();
void acquire_LZKJZ(int qty);
void produce_WFSV();
void acquire_WFSV(int qty);
void produce_GZLHP();
void acquire_GZLHP(int qty);
void produce_XSRWM();
void acquire_XSRWM(int qty);
void produce_SKBV();
void acquire_SKBV(int qty);
void produce_VSRMJ();
void acquire_VSRMJ(int qty);
void produce_CVJQG();
void acquire_CVJQG(int qty);
void produce_BVFPF();
void acquire_BVFPF(int qty);
void produce_XHTJF();
void acquire_XHTJF(int qty);
void produce_DFCT();
void acquire_DFCT(int qty);
void produce_RGZDK();
void acquire_RGZDK(int qty);
void produce_DXBZJ();
void acquire_DXBZJ(int qty);
void produce_RXSZS();
void acquire_RXSZS(int qty);
void produce_SZDWB();
void acquire_SZDWB(int qty);
void produce_BPNVK();
void acquire_BPNVK(int qty);
void produce_RBFX();
void acquire_RBFX(int qty);
void produce_HJDB();
void acquire_HJDB(int qty);
void produce_GHQPH();
void acquire_GHQPH(int qty);
void produce_GCBR();
void acquire_GCBR(int qty);
void produce_BZFH();
void acquire_BZFH(int qty);
void produce_TFQH();
void acquire_TFQH(int qty);
void produce_QNXC();
void acquire_QNXC(int qty);
void produce_JRXQ();
void acquire_JRXQ(int qty);
void produce_ZJHKP();
void acquire_ZJHKP(int qty);
void produce_PRMR();
void acquire_PRMR(int qty);
void produce_JBHKV();
void acquire_JBHKV(int qty);
void produce_BKNQT();
void acquire_BKNQT(int qty);
void produce_QLSVN();
void acquire_QLSVN(int qty);
void produce_FUEL();
void acquire_FUEL(int qty);
void produce_BQGP();
void acquire_BQGP(int qty);
void produce_LQGC();
void acquire_LQGC(int qty);
void produce_NZVL();
void acquire_NZVL(int qty);
void produce_VLJWQ();
void acquire_VLJWQ(int qty);
void produce_BRXLV();
void acquire_BRXLV(int qty);
void produce_MCQS();
void acquire_MCQS(int qty);
void produce_NJFXK();
void acquire_NJFXK(int qty);
void produce_XKTMK();
void acquire_XKTMK(int qty);
void produce_HKCVW();
void acquire_HKCVW(int qty);
void produce_WBKQ();
void acquire_WBKQ(int qty);
void produce_VBHVQ();
void acquire_VBHVQ(int qty);
void produce_JZQJ();
void acquire_JZQJ(int qty);
void produce_WMCD();
void acquire_WMCD(int qty);
void produce_XFNPT();
void acquire_XFNPT(int qty);
void produce_VHFCR();
void acquire_VHFCR(int qty);
int residue_ZJZRN = 0;
void produce_ZJZRN() {
    acquire_HKCVW(1);
    acquire_DFCT(2);
    residue_ZJZRN += 5;
}

void acquire_ZJZRN(int qty) {
    while (residue_ZJZRN < qty) {
        produce_ZJZRN();
    }
    residue_ZJZRN -= qty;
}

int residue_ZKCXK = 0;
void produce_ZKCXK() {
    acquire_TCPN(8);
    acquire_XHTJF(7);
    acquire_DFCT(3);
    residue_ZKCXK += 8;
}

void acquire_ZKCXK(int qty) {
    while (residue_ZKCXK < qty) {
        produce_ZKCXK();
    }
    residue_ZKCXK -= qty;
}

int residue_ZWQX = 0;
void produce_ZWQX() {
    acquire_ZJZRN(1);
    acquire_NZVL(4);
    acquire_NJFXK(1);
    acquire_RHJCQ(7);
    acquire_MCQS(32);
    acquire_XFNPT(1);
    residue_ZWQX += 5;
}

void acquire_ZWQX(int qty) {
    while (residue_ZWQX < qty) {
        produce_ZWQX();
    }
    residue_ZWQX -= qty;
}

int residue_TCPN = 0;
void produce_TCPN() {
    acquire_DRWB(10);
    acquire_JBHKV(16);
    residue_TCPN += 6;
}

void acquire_TCPN(int qty) {
    while (residue_TCPN < qty) {
        produce_TCPN();
    }
    residue_TCPN -= qty;
}

int residue_DRWB = 0;
void produce_DRWB() {
    acquire_MBFK(3);
    residue_DRWB += 7;
}

void acquire_DRWB(int qty) {
    while (residue_DRWB < qty) {
        produce_DRWB();
    }
    residue_DRWB -= qty;
}

int residue_MBMKZ = 0;
void produce_MBMKZ() {
    acquire_RHJCQ(9);
    residue_MBMKZ += 6;
}

void acquire_MBMKZ(int qty) {
    while (residue_MBMKZ < qty) {
        produce_MBMKZ();
    }
    residue_MBMKZ -= qty;
}

int residue_KRTGD = 0;
void produce_KRTGD() {
    acquire_BVFPF(1);
    residue_KRTGD += 2;
}

void acquire_KRTGD(int qty) {
    while (residue_KRTGD < qty) {
        produce_KRTGD();
    }
    residue_KRTGD -= qty;
}

int residue_VNFJQ = 0;
void produce_VNFJQ() {
    acquire_QNXC(1);
    acquire_BKNQT(7);
    acquire_XFNPT(1);
    residue_VNFJQ += 4;
}

void acquire_VNFJQ(int qty) {
    while (residue_VNFJQ < qty) {
        produce_VNFJQ();
    }
    residue_VNFJQ -= qty;
}

int residue_TGJP = 0;
void produce_TGJP() {
    acquire_TCPN(2);
    acquire_WFSV(1);
    residue_TGJP += 2;
}

void acquire_TGJP(int qty) {
    while (residue_TGJP < qty) {
        produce_TGJP();
    }
    residue_TGJP -= qty;
}

int residue_RHJCQ = 0;
void produce_RHJCQ() {
    acquire_DFCT(35);
    residue_RHJCQ += 2;
}

void acquire_RHJCQ(int qty) {
    while (residue_RHJCQ < qty) {
        produce_RHJCQ();
    }
    residue_RHJCQ -= qty;
}

int residue_QGDSV = 0;
void produce_QGDSV() {
    acquire_SKBV(1);
    acquire_CTRH(7);
    residue_QGDSV += 8;
}

void acquire_QGDSV(int qty) {
    while (residue_QGDSV < qty) {
        produce_QGDSV();
    }
    residue_QGDSV -= qty;
}

int residue_CTRH = 0;
void produce_CTRH() {
    acquire_VSRMJ(8);
    acquire_BVFPF(1);
    residue_CTRH += 4;
}

void acquire_CTRH(int qty) {
    while (residue_CTRH < qty) {
        produce_CTRH();
    }
    residue_CTRH -= qty;
}

int residue_FPZLF = 0;
void produce_FPZLF() {
    acquire_WMCD(1);
    residue_FPZLF += 3;
}

void acquire_FPZLF(int qty) {
    while (residue_FPZLF < qty) {
        produce_FPZLF();
    }
    residue_FPZLF -= qty;
}

int residue_QBDQ = 0;
void produce_QBDQ() {
    acquire_CVJQG(13);
    acquire_DXBZJ(8);
    residue_QBDQ += 9;
}

void acquire_QBDQ(int qty) {
    while (residue_QBDQ < qty) {
        produce_QBDQ();
    }
    residue_QBDQ -= qty;
}

int residue_GDJGV = 0;
void produce_GDJGV() {
    acquire_XSRWM(1);
    residue_GDJGV += 5;
}

void acquire_GDJGV(int qty) {
    while (residue_GDJGV < qty) {
        produce_GDJGV();
    }
    residue_GDJGV -= qty;
}

int residue_MBFK = 0;
void produce_MBFK() {
    acquire_ORE(132);
    residue_MBFK += 3;
}

void acquire_MBFK(int qty) {
    while (residue_MBFK < qty) {
        produce_MBFK();
    }
    residue_MBFK -= qty;
}

int residue_LZKJZ = 0;
void produce_LZKJZ() {
    acquire_BQGP(2);
    residue_LZKJZ += 9;
}

void acquire_LZKJZ(int qty) {
    while (residue_LZKJZ < qty) {
        produce_LZKJZ();
    }
    residue_LZKJZ -= qty;
}

int residue_WFSV = 0;
void produce_WFSV() {
    acquire_GZLHP(5);
    residue_WFSV += 7;
}

void acquire_WFSV(int qty) {
    while (residue_WFSV < qty) {
        produce_WFSV();
    }
    residue_WFSV -= qty;
}

int residue_GZLHP = 0;
void produce_GZLHP() {
    acquire_RXSZS(2);
    acquire_MBFK(10);
    acquire_BPNVK(1);
    residue_GZLHP += 2;
}

void acquire_GZLHP(int qty) {
    while (residue_GZLHP < qty) {
        produce_GZLHP();
    }
    residue_GZLHP -= qty;
}

int residue_XSRWM = 0;
void produce_XSRWM() {
    acquire_BZFH(13);
    residue_XSRWM += 8;
}

void acquire_XSRWM(int qty) {
    while (residue_XSRWM < qty) {
        produce_XSRWM();
    }
    residue_XSRWM -= qty;
}

int residue_SKBV = 0;
void produce_SKBV() {
    acquire_QLSVN(3);
    residue_SKBV += 3;
}

void acquire_SKBV(int qty) {
    while (residue_SKBV < qty) {
        produce_SKBV();
    }
    residue_SKBV -= qty;
}

int residue_VSRMJ = 0;
void produce_VSRMJ() {
    acquire_QBDQ(8);
    residue_VSRMJ += 4;
}

void acquire_VSRMJ(int qty) {
    while (residue_VSRMJ < qty) {
        produce_VSRMJ();
    }
    residue_VSRMJ -= qty;
}

int residue_CVJQG = 0;
void produce_CVJQG() {
    acquire_RXSZS(1);
    residue_CVJQG += 9;
}

void acquire_CVJQG(int qty) {
    while (residue_CVJQG < qty) {
        produce_CVJQG();
    }
    residue_CVJQG -= qty;
}

int residue_BVFPF = 0;
void produce_BVFPF() {
    acquire_MBFK(3);
    residue_BVFPF += 3;
}

void acquire_BVFPF(int qty) {
    while (residue_BVFPF < qty) {
        produce_BVFPF();
    }
    residue_BVFPF -= qty;
}

int residue_XHTJF = 0;
void produce_XHTJF() {
    acquire_GZLHP(7);
    acquire_MBFK(4);
    acquire_CVJQG(5);
    residue_XHTJF += 8;
}

void acquire_XHTJF(int qty) {
    while (residue_XHTJF < qty) {
        produce_XHTJF();
    }
    residue_XHTJF -= qty;
}

int residue_DFCT = 0;
void produce_DFCT() {
    acquire_GZLHP(1);
    residue_DFCT += 2;
}

void acquire_DFCT(int qty) {
    while (residue_DFCT < qty) {
        produce_DFCT();
    }
    residue_DFCT -= qty;
}

int residue_RGZDK = 0;
void produce_RGZDK() {
    acquire_SZDWB(4);
    acquire_RHJCQ(4);
    acquire_WMCD(1);
    residue_RGZDK += 3;
}

void acquire_RGZDK(int qty) {
    while (residue_RGZDK < qty) {
        produce_RGZDK();
    }
    residue_RGZDK -= qty;
}

int residue_DXBZJ = 0;
void produce_DXBZJ() {
    acquire_BRXLV(2);
    residue_DXBZJ += 8;
}

void acquire_DXBZJ(int qty) {
    while (residue_DXBZJ < qty) {
        produce_DXBZJ();
    }
    residue_DXBZJ -= qty;
}

int residue_RXSZS = 0;
void produce_RXSZS() {
    acquire_ORE(192);
    residue_RXSZS += 7;
}

void acquire_RXSZS(int qty) {
    while (residue_RXSZS < qty) {
        produce_RXSZS();
    }
    residue_RXSZS -= qty;
}

int residue_SZDWB = 0;
void produce_SZDWB() {
    acquire_PRMR(1);
    acquire_DFCT(6);
    residue_SZDWB += 5;
}

void acquire_SZDWB(int qty) {
    while (residue_SZDWB < qty) {
        produce_SZDWB();
    }
    residue_SZDWB -= qty;
}

int residue_BPNVK = 0;
void produce_BPNVK() {
    acquire_ORE(104);
    residue_BPNVK += 9;
}

void acquire_BPNVK(int qty) {
    while (residue_BPNVK < qty) {
        produce_BPNVK();
    }
    residue_BPNVK -= qty;
}

int residue_RBFX = 0;
void produce_RBFX() {
    acquire_VLJWQ(6);
    acquire_ZKCXK(8);
    acquire_BKNQT(6);
    acquire_JRXQ(26);
    acquire_FPZLF(7);
    acquire_HKCVW(6);
    acquire_KRTGD(18);
    residue_RBFX += 4;
}

void acquire_RBFX(int qty) {
    while (residue_RBFX < qty) {
        produce_RBFX();
    }
    residue_RBFX -= qty;
}

int residue_HJDB = 0;
void produce_HJDB() {
    acquire_XFNPT(7);
    acquire_GDJGV(1);
    residue_HJDB += 2;
}

void acquire_HJDB(int qty) {
    while (residue_HJDB < qty) {
        produce_HJDB();
    }
    residue_HJDB -= qty;
}

int residue_GHQPH = 0;
void produce_GHQPH() {
    acquire_SKBV(15);
    acquire_DRWB(8);
    acquire_RXSZS(12);
    residue_GHQPH += 3;
}

void acquire_GHQPH(int qty) {
    while (residue_GHQPH < qty) {
        produce_GHQPH();
    }
    residue_GHQPH -= qty;
}

int residue_GCBR = 0;
void produce_GCBR() {
    acquire_BZFH(1);
    residue_GCBR += 5;
}

void acquire_GCBR(int qty) {
    while (residue_GCBR < qty) {
        produce_GCBR();
    }
    residue_GCBR -= qty;
}

int residue_BZFH = 0;
void produce_BZFH() {
    acquire_TGJP(1);
    acquire_SKBV(6);
    residue_BZFH += 1;
}

void acquire_BZFH(int qty) {
    while (residue_BZFH < qty) {
        produce_BZFH();
    }
    residue_BZFH -= qty;
}

int residue_TFQH = 0;
void produce_TFQH() {
    acquire_KRTGD(4);
    acquire_ZJHKP(1);
    acquire_LZKJZ(1);
    acquire_VNFJQ(1);
    acquire_QBDQ(6);
    acquire_PRMR(1);
    acquire_NJFXK(1);
    acquire_HJDB(1);
    residue_TFQH += 8;
}

void acquire_TFQH(int qty) {
    while (residue_TFQH < qty) {
        produce_TFQH();
    }
    residue_TFQH -= qty;
}

int residue_QNXC = 0;
void produce_QNXC() {
    acquire_BVFPF(10);
    acquire_RGZDK(1);
    residue_QNXC += 8;
}

void acquire_QNXC(int qty) {
    while (residue_QNXC < qty) {
        produce_QNXC();
    }
    residue_QNXC -= qty;
}

int residue_JRXQ = 0;
void produce_JRXQ() {
    acquire_XHTJF(1);
    residue_JRXQ += 5;
}

void acquire_JRXQ(int qty) {
    while (residue_JRXQ < qty) {
        produce_JRXQ();
    }
    residue_JRXQ -= qty;
}

int residue_ZJHKP = 0;
void produce_ZJHKP() {
    acquire_XKTMK(3);
    acquire_QGDSV(4);
    residue_ZJHKP += 3;
}

void acquire_ZJHKP(int qty) {
    while (residue_ZJHKP < qty) {
        produce_ZJHKP();
    }
    residue_ZJHKP -= qty;
}

int residue_PRMR = 0;
void produce_PRMR() {
    acquire_BZFH(2);
    residue_PRMR += 7;
}

void acquire_PRMR(int qty) {
    while (residue_PRMR < qty) {
        produce_PRMR();
    }
    residue_PRMR -= qty;
}

int residue_JBHKV = 0;
void produce_JBHKV() {
    acquire_BPNVK(1);
    acquire_RXSZS(1);
    residue_JBHKV += 5;
}

void acquire_JBHKV(int qty) {
    while (residue_JBHKV < qty) {
        produce_JBHKV();
    }
    residue_JBHKV -= qty;
}

int residue_BKNQT = 0;
void produce_BKNQT() {
    acquire_XHTJF(10);
    residue_BKNQT += 9;
}

void acquire_BKNQT(int qty) {
    while (residue_BKNQT < qty) {
        produce_BKNQT();
    }
    residue_BKNQT -= qty;
}

int residue_QLSVN = 0;
void produce_QLSVN() {
    acquire_JBHKV(1);
    acquire_XHTJF(2);
    residue_QLSVN += 8;
}

void acquire_QLSVN(int qty) {
    while (residue_QLSVN < qty) {
        produce_QLSVN();
    }
    residue_QLSVN -= qty;
}

int residue_FUEL = 0;
void produce_FUEL() {
    acquire_VNFJQ(24);
    acquire_TFQH(42);
    acquire_RBFX(39);
    acquire_ZWQX(1);
    acquire_VBHVQ(7);
    acquire_DRWB(26);
    acquire_NJFXK(21);
    residue_FUEL += 1;
}

void acquire_FUEL(int qty) {
    while (residue_FUEL < qty) {
        produce_FUEL();
    }
    residue_FUEL -= qty;
}

int residue_BQGP = 0;
void produce_BQGP() {
    acquire_WBKQ(26);
    acquire_XHTJF(14);
    residue_BQGP += 5;
}

void acquire_BQGP(int qty) {
    while (residue_BQGP < qty) {
        produce_BQGP();
    }
    residue_BQGP -= qty;
}

int residue_LQGC = 0;
void produce_LQGC() {
    acquire_WBKQ(5);
    acquire_MBMKZ(7);
    residue_LQGC += 3;
}

void acquire_LQGC(int qty) {
    while (residue_LQGC < qty) {
        produce_LQGC();
    }
    residue_LQGC -= qty;
}

int residue_NZVL = 0;
void produce_NZVL() {
    acquire_LQGC(6);
    residue_NZVL += 5;
}

void acquire_NZVL(int qty) {
    while (residue_NZVL < qty) {
        produce_NZVL();
    }
    residue_NZVL -= qty;
}

int residue_VLJWQ = 0;
void produce_VLJWQ() {
    acquire_KRTGD(13);
    acquire_GHQPH(5);
    residue_VLJWQ += 9;
}

void acquire_VLJWQ(int qty) {
    while (residue_VLJWQ < qty) {
        produce_VLJWQ();
    }
    residue_VLJWQ -= qty;
}

int residue_BRXLV = 0;
void produce_BRXLV() {
    acquire_ORE(117);
    residue_BRXLV += 4;
}

void acquire_BRXLV(int qty) {
    while (residue_BRXLV < qty) {
        produce_BRXLV();
    }
    residue_BRXLV -= qty;
}

int residue_MCQS = 0;
void produce_MCQS() {
    acquire_XKTMK(3);
    acquire_PRMR(1);
    residue_MCQS += 2;
}

void acquire_MCQS(int qty) {
    while (residue_MCQS < qty) {
        produce_MCQS();
    }
    residue_MCQS -= qty;
}

int residue_NJFXK = 0;
void produce_NJFXK() {
    acquire_DRWB(3);
    acquire_BVFPF(7);
    acquire_TCPN(4);
    residue_NJFXK += 7;
}

void acquire_NJFXK(int qty) {
    while (residue_NJFXK < qty) {
        produce_NJFXK();
    }
    residue_NJFXK -= qty;
}

int residue_XKTMK = 0;
void produce_XKTMK() {
    acquire_VHFCR(10);
    acquire_JZQJ(13);
    residue_XKTMK += 5;
}

void acquire_XKTMK(int qty) {
    while (residue_XKTMK < qty) {
        produce_XKTMK();
    }
    residue_XKTMK -= qty;
}

int residue_HKCVW = 0;
void produce_HKCVW() {
    acquire_CVJQG(17);
    acquire_GCBR(4);
    residue_HKCVW += 9;
}

void acquire_HKCVW(int qty) {
    while (residue_HKCVW < qty) {
        produce_HKCVW();
    }
    residue_HKCVW -= qty;
}

int residue_WBKQ = 0;
void produce_WBKQ() {
    acquire_DFCT(22);
    acquire_TGJP(17);
    residue_WBKQ += 2;
}

void acquire_WBKQ(int qty) {
    while (residue_WBKQ < qty) {
        produce_WBKQ();
    }
    residue_WBKQ -= qty;
}

int residue_VBHVQ = 0;
void produce_VBHVQ() {
    acquire_JZQJ(2);
    acquire_XFNPT(12);
    acquire_BQGP(1);
    residue_VBHVQ += 2;
}

void acquire_VBHVQ(int qty) {
    while (residue_VBHVQ < qty) {
        produce_VBHVQ();
    }
    residue_VBHVQ -= qty;
}

int residue_JZQJ = 0;
void produce_JZQJ() {
    acquire_HKCVW(12);
    residue_JZQJ += 1;
}

void acquire_JZQJ(int qty) {
    while (residue_JZQJ < qty) {
        produce_JZQJ();
    }
    residue_JZQJ -= qty;
}

int residue_WMCD = 0;
void produce_WMCD() {
    acquire_XSRWM(1);
    residue_WMCD += 3;
}

void acquire_WMCD(int qty) {
    while (residue_WMCD < qty) {
        produce_WMCD();
    }
    residue_WMCD -= qty;
}

int residue_XFNPT = 0;
void produce_XFNPT() {
    acquire_BZFH(12);
    acquire_SKBV(14);
    acquire_CTRH(1);
    residue_XFNPT += 4;
}

void acquire_XFNPT(int qty) {
    while (residue_XFNPT < qty) {
        produce_XFNPT();
    }
    residue_XFNPT -= qty;
}

int residue_VHFCR = 0;
void produce_VHFCR() {
    acquire_ZKCXK(7);
    residue_VHFCR += 6;
}

void acquire_VHFCR(int qty) {
    while (residue_VHFCR < qty) {
        produce_VHFCR();
    }
    residue_VHFCR -= qty;
}

int main(int argc, char *argv[]) {
    while (1) {
        acquire_FUEL(1);
        count++;
    }
    return 0;
}

