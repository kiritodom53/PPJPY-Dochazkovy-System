# Dochátkový systém v pythonu

### Popis
Jedná se o databázovou aplikaci v pythonu, ve verzi **3.7**.
<br>Aplikace funguje jako jednoduchý docházkový systém pro zaměstanance.
<br>Gui je tvořeno pomocí tkinter
<br>Aplikace psána v prostředí [PyCharm](https://www.jetbrains.com/pycharm/)

#### Testovací uživatelé
username:heslo
- user1:admin   - zaměstnavatel
- user2:admin   - zaměstnanec

![alt samplpe project image](https://i.imgur.com/lCe8R3T.png)

#### Hlavní funkce:
- Evidování příchodu a odchodu za každý měsíc
- Výpis počet odpracovaných dnů
- Výpis celkové hrubé mzdy
- Výpis počet odpracovaných hodin

#### Dodatečné funkce
- Možnost změna hesla (zaměstnanec)
- Registrace nového zaměstnance (zaměstnavatel)

#### Použité knihovny
- json
- os
- urllib.request
- binascii
- hashlib
- datetime
- tkinter
- tkinter.tkk
- tkcalendar
- pyinstaller

.exe vytovřeno pomocí pyinstaller

#### Projektový adresář

```
dochazkovysystemv2
├── exe_file
│   └── __init__.exe (startup file)
├── src
│   ├── __old (folder with old files)
│   ├── _files (folder with old files)
│   ├── Data (folder with old files)
│   │   ├── presence.json (presence seed data)
│   │   └── SeedData.py
│   ├── Validation (folder with old files)
│   │   └── Helper.py (Helepr static methods)
│   ├── __init__.py (Boot python file)
│   ├── Database.py
│   ├── Dochazka.py
│   ├── dochazkadb.db (local database file)
│   ├── Hire.py
│   ├── Login.py
│   ├── Password.py
│   └── presence.json (presence seed data)
└── README.md
```

#### Popis tříd
- [Helper.py](src/Validation/Helper.py)
    - Pomocná střída se statickýma metodama
- [SeedData.py](src/Data/SeedData.py)
    - Seed dat do databáze
- [__init__.py](src/__init__.py)
    - Boot třída pro spuštění projetku
- [Database.py](src/Database.py)
    - Veškeré oprace prováděně s databází
- [Dochazka.py](src/Dochazka.py)
    - Okno "aplikace" docházky
- [Hire.py](src/Hire.py)
    - Okno "aplikace" registrace uživatele
- [Login.py](src/Login.py)
    - Okno "aplikace" přihlášení uživatele
- [Password.py](src/Password.py)
    - Okno "aplikace" změny hesla

### v0.1

##### Databáze
- [x] Spojení s databází
- [x] Vytvoření tabulek
- [x] CRUD funkce
- [x] SeedData - User
- [x] SeedData - Presence
- [x] Přihlášení pomocí uživatelských údajů

##### Aplikace formulář

- [x] GUI

##### Přihlašovací formulář

- [x] Přihlašovací formulář
- [x] Přihlášení podle účtu z DTB


##### Ostatní

- [x] Registrace
- [x] Hash hesel
- [x] Startup configurace
- [x] Dokumentace kódu

