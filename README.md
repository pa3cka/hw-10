# hw-12
Domácí úkol ke cv. 12
> **Upravujte pouze soubor `ukol_12.py`!**

## Zadání
Seřaďte slova načteného textu (věty) podle abecedy a současně zjistěte jejich četnost.

### 1. Načtení dat
* Do souboru `ukol_12.py` implementujte funkci `read_data`.
* Vstupem funkce bude parametr `file_name` s názvem souboru se zdrojovými daty.
* Funkce umožní načíst větu z prvního řádku textového souboru.
* Výstupem funkce bude seznam s načteným textem.

### 2. Seřazení a zjištění četnost slov
* Do souboru `ukol_12.py` implementujte funkci `counting_sort`.
* Funkce s využitím metody Counting Sort zajistí seřazení slov načtené věty dle abecedy.
* Funkce současně spočítá četnosti výskytu jednotlivých slov.
* Funkce bude mít jeden vstup: `unsorted_words`.
* Výstupy funkce budou dva: seznam seřazených slov `sorted_words` a četnost jednotlivých slov `word_counts`

### Jako zdroj dat použijte soubor text.txt!

## A nyní troška teorie:

## Counting Sort - obecné vysvětlení
Counting Sort je řadicí algoritmus, který třídí prvky pole počítáním počtu výskytů každého jedinečného prvku v poli. Počet je uložen v pomocném poli a třídění se provádí mapováním počtu jako indexu pomocného pole.

## Jak Counting Sort pracuje?
### Zjistíme maximální prvek (`max`) ze vstupního pole.
![alt text](https://cdn.programiz.com/cdn/farfuture/_iojSNQFxCvNdbdPPmMVCJZxGFTS0TOZRIt1E4Wte0Y/mtime:1582112622/sites/tutorial2program/files/Counting-sort-0_0.png)

### Inicializujeme pole délky `max+1` se všemi prvky 0. Toto pole bude využito pro ukládání počtu prvků v poli.
![alt text](https://cdn.programiz.com/cdn/farfuture/bRDNfPQG8lie6m7EFXVqPj8w6RzkRhM34XNaAoG2dCs/mtime:1582112622/sites/tutorial2program/files/Counting-sort-1.png)

### Uložíme počet každého prvku v jejich příslušném indexu v poli `count`
Například: je-li počet prvků 3 2, pak je 2 uložen na 3. pozici pole počtu. Pokud prvek „5“ v poli není, je 0 uložen na 5. pozici.
![alt text](https://cdn.programiz.com/cdn/farfuture/CIyC1Lkj5JFln_hjy8U1acmUZ4JST__v4bQBvPcnOkk/mtime:1582112622/sites/tutorial2program/files/Counting-sort-2.png)

### Uložíme kumulativní součet prvků počítacího pole. Pomůže nám při umisťování prvků do správného indexu seřazeného pole.
![alt text](https://cdn.programiz.com/cdn/farfuture/CIyC1Lkj5JFln_hjy8U1acmUZ4JST__v4bQBvPcnOkk/mtime:1582112622/sites/tutorial2program/files/Counting-sort-3.png)

### Najdeme index každého prvku původního pole v poli počítání. To udává kumulativní počet. Umístíme prvek na index vypočítaný podle obrázku níže.
![alt text](https://cdn.programiz.com/cdn/farfuture/CIyC1Lkj5JFln_hjy8U1acmUZ4JST__v4bQBvPcnOkk/mtime:1582112622/sites/tutorial2program/files/Counting-sort-4.png)
### Po umístění každého prvku do správné polohy snížíme jeho počet o jeden.

Pseudokód:

countingSort(array, size)
  max <- nalezni find largest element in array
  initialize count array with all zeros
  for j <- 0 to size
    find the total count of each unique element and 
    store the count at jth index in count array
  for i <- 1 to max
    find the cumulative sum and store it in count array itself
  for j <- size down to 1
    restore the elements to array
    decrease count of each element restored by 1



    

