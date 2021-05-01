class Translation(object):
    START_TEXT = """<b>Hallo! Silahkan kirimkan nomor HP kamu dengan awalan +62 untuk mendapatkan kode dari telegram</b>"""
    AFTER_RECVD_CODE_TEXT = """<b>Sekarang tolong kirimkan kode yg baru anda peroleh dari pihak telegram</b>!
<i>kode ini hanya digunakan dengan tujuan mendapatkan API ID dan HASH dari my.telegram.org.</i>

<b>/start untuk memulai kembali</b>"""
    BEFORE_SUCC_LOGIN = "Oke Kode anda sudah diterima, bentar yah😊..."
    ERRED_PAGE = "ada sesuatu yang salah. gagal mendapatkan Api ID dan HASH kamu. \n\n Contact Me @ZendYNS"
    CANCELLED_MESG = "Selamat tinggal! Tolong re /start bot ini untuk memulai kembali"
    IN_VALID_CODE_PVDED = "maaf, tampaknya masukan tersebut bukan kode Login Web Telegram yang valid "
    IN_VALID_PHNO_PVDED = "maaf, masukan tersebut sepertinya bukan nomor telepon yang valid"
