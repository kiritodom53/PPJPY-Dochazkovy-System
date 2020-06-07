# Dochátkový systém v pythonu

### Popis
Jedná se o databázovou aplikaci v pythonu.
Aplikace funguje jako jednoduchý docházkový systém pro zaměstanance.
Gui je tvořeno pomocí tkinter
Aplikace psána v prostředí [PyCharm](https://www.jetbrains.com/pycharm/)

#### Testovací uživatelé
username:heslo
- user1:admin   - zaměstnavatel
- user2:admin   - zaměstnanec

![alt samplpe project image](https://i.imgur.com/lCe8R3T.png)

#### Hlavní funkce:
- Evidování příchodu a odchodu za každý měsíc
- Výpis počet odpraovaných dnů
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

