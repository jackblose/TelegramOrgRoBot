class Translation(object):
    START_TEXT = """**Hallo Kamu!**
_**Terima Kasih sudah menggunakan bot saya**_
Silahkan kirimkan nomor HP kamu dengan awalan +62 untuk mendapatkan kode dari telegram

/start at any stage to re-enter your details"""
    AFTER_RECVD_CODE_TEXT = """**Oke !**
_Sekarang tolong kirimkan kode yg baru anda peroleh dari pihak telegram!_

**kode ini hanya digunakan dengan tujuan mendapatkan _API ID dan HASH_ dari my.telegram.org**

/start at any stage to re-enter your details"""
    BEFORE_SUCC_LOGIN = "Oke Kode anda sudah diterima ..."
    ERRED_PAGE = "ada sesuatu yang salah. gagal mendapatkan id aplikasi. \n\n@SpEcHlDe"
    CANCELLED_MESG = "Selamat tinggal! Tolong re /start bot ini untuk memulai kembali"
    IN_VALID_CODE_PVDED = "maaf, tampaknya masukan tersebut bukan kode Login Web Telegram yang valid "
    IN_VALID_PHNO_PVDED = "maaf, masukan tersebut sepertinya bukan nomor telepon yang valid"
