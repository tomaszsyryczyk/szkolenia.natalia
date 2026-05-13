# Instrukcja – jak uruchomić notebooki z LAB 06

## 1. Zainstaluj Python

1. Wejdź na stronę: **https://www.python.org/downloads/**
2. Kliknij duży żółty przycisk „Download Python 3.x.x".
3. Uruchom pobrany plik `.exe`.
4. **WAŻNE:** Na pierwszym ekranie instalatora zaznacz opcję **„Add Python to PATH"** (na dole okna). Bez tego nic nie będzie działać.
5. Kliknij „Install Now" i poczekaj.

Sprawdź czy instalacja się udała — otwórz wiersz poleceń (`Win + R`, wpisz `cmd`, Enter) i wpisz:
```
python --version
```
Powinno wyświetlić się np. `Python 3.12.0`. Jeśli tak — Python działa.

---

## 2. Zainstaluj wymagane biblioteki

Otwórz wiersz poleceń (`cmd`) i wpisz kolejno:

```
pip install numpy
pip install matplotlib
pip install notebook
```

- **numpy** – obliczenia matematyczne na tablicach liczb
- **matplotlib** – rysowanie wykresów
- **notebook** – środowisko Jupyter do otwierania plików `.ipynb`

Każde polecenie samo pobierze i zainstaluje wszystko co potrzeba. Poczekaj aż skończy (zobaczysz `Successfully installed ...`).

---

## 3. Otwórz notatnik Jupyter

W wierszu poleceń przejdź do folderu z plikami. Wpisz:
```
cd ścieżka\do\folderu\lab06
```
Na przykład:
```
cd C:\Users\natalia\Desktop\lab06
```
Następnie uruchom Jupyter:
```
jupyter notebook
```
Przeglądarka otworzy się automatycznie. Kliknij na wybrany plik `.ipynb` żeby go otworzyć.

---

## 4. Uruchom kod w notatniku

- Kliknij na komórkę z kodem.
- Naciśnij **Shift + Enter** żeby ją wykonać.
- Wykonuj komórki **od góry do dołu** — każda kolejna może zależeć od poprzedniej.

---

## 5. Co robić gdy pojawi się błąd?

### Krok 1 – przeczytaj komunikat błędu

Python zawsze mówi co jest nie tak. Przykłady:

| Komunikat | Co oznacza | Jak naprawić |
|---|---|---|
| `ModuleNotFoundError: No module named 'numpy'` | Biblioteka nie jest zainstalowana | Wpisz w `cmd`: `pip install numpy` |
| `NameError: name 'x' is not defined` | Zmienna `x` nie istnieje | Uruchom komórki od początku (od góry) |
| `SyntaxError` | Błąd w składni kodu (np. brak nawiasu) | Znajdź wskazaną linię i popraw literówkę |
| `ZeroDivisionError` | Dzielenie przez zero | Sprawdź dane wejściowe |
| `ValueError` | Podano złą wartość (np. tekst zamiast liczby) | Sprawdź co przekazujesz do funkcji |

### Krok 2 – sprawdź numer linii

Błąd zawsze podaje numer linii, np.:
```
File "...", line 12, in <module>
```
Idź do tej linii i sprawdź co tam jest.

### Krok 3 – uruchom wszystko od nowa

Jeśli coś działa dziwnie — w menu Jupyter kliknij:
**Kernel → Restart & Run All**

To czyści pamięć i uruchamia wszystkie komórki od początku. Rozwiązuje 80% problemów.

### Krok 4 – skopiuj błąd do wyszukiwarki

Skopiuj dokładny tekst błędu (ostatnią linię komunikatu) i wklej do Google lub ChatGPT. Prawie każdy błąd w Pythonie był już przez kogoś opisany.

---

## Pliki w tym folderze

| Plik | Opis |
|---|---|
| `zadanieI_wykresy_2d.ipynb` | Zadanie I – wykresy f0 i f1 |
| `zadanieII_krzywa_3d.ipynb` | Zadanie II – krzywa parametryczna w 3D |
| `zadanieIII_uklad_rownan.ipynb` | Zadanie III – układ równań liniowych |
| `zadanieIV_funkcja_Fn.ipynb` | Zadanie IV – funkcja F: Rⁿ → R |
| `zadanie1_tensor_eps.ipynb` | Zadanie 1 – tensor Levi-Civita i wyznacznik |
