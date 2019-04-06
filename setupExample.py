from cx_Freeze import setup, Executable
import os
base = None

os.environ['TCL_LIBRARY'] = r'C:\Python 3.6\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python 3.6\tcl\tk8.6'


setup(
    name="pacmanRC",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["bonus.png","ghost_dead.png","ghost_dead2.png","ghost1.png","ghost2.png","ghost3.png","ghost4.png","kolanko_ld.png","kolanko_lg.png","kolanko_pd.png","kolanko_pg.png","pacman_dir1_1.png","pacman_dir1_2.png","pacman_dir1_3.png","pacman_dir2_1.png","pacman_dir2_2.png","pacman_dir2_3.png","pacman_dir3_1.png","pacman_dir3_2.png","pacman_dir3_3.png","pacman_dir4_1.png","pacman_dir4_2.png","pacman_dir4_3.png","pkt.png","rog_dol.png","rog_gora.png","rog_lewy.png","rog_prawy.png","sciana_3_dol.png","sciana_3_gora.png","sciana_3_lewa.png","sciana_3_prawa.png","sciana_zwykla_pion.png","sciana_zwykla_poziom.png"]}},
    description = 'giereczka',
    version="1.0.0",
    executables = [Executable("pacmanRC.py",base=base)]
    )