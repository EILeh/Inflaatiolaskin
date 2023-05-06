"""
Ohjelma selvittää käyttäjän syöttämistä kuukausittaisista inflaatioprosenteista,
mikä oli kaikkein suurin inflaation muutos ts. kuinka suuri on suurin kahden
peräkkäin syötetyn arvon välinen ero. Käyttäjän on syötettävä arvoja vähintään
kahdelta kuukaudelta tai muuten ohjelma tulostaa virheilmoituksen. Kun käyttäjä
on syöttänyt haluamansa määrän arvoja, syöttämällä tyhjän arvon eli klikkaamalla
enteriä, ohjelma tulostaa suurimman inflaation.

COMP.CS.100 Projekti 1; inflaatiolaskin
Tekijä 1: Margarita N......a
Tekijä 2: EILeh
"""

def main():

    is_input_a_number = True
    greatest_difference = 0
    month_odd = 0
    month_even = 0
    current_month = 1

    while is_input_a_number:

        str_month = input(f"Enter inflation rate for month {current_month}: ")

        # Jos syötteitä on vähemmän kuin kaksi, arvojen kysely lopetetaan
        # ja tulostetaan error-lause.
        if current_month < 3 and str_month == "":
            print("Error: at least 2 monthly inflation rates must be entered.")
            return
        # Jos syöte on tyhjä, arvojen kysely lopetetaan.
        elif current_month >= 3 and str_month == "":
            is_input_a_number = False

        # Jos kuukausi on parillinen, tallennetaan syöte muuttuujaan month_even.
        # Suoritetaan lasku: pariton kuukausi vähennetään parillisesta.
        elif current_month % 2 == 0:
            month_even = float(str_month)
            if (month_even - month_odd) > greatest_difference or \
                    current_month == 2:
                greatest_difference = month_even - month_odd

        # Jos kuukausi on pariton, tallennetaan syöte muuttujaan month_odd.
        # Suoritetaan lasku: parillinen kuukausi vähennetään parittomasta.
        elif current_month % 2 != 0:
            month_odd = float(str_month)
            if (month_odd - month_even) > greatest_difference and \
                    current_month > 1:
                greatest_difference = month_odd - month_even

        current_month += 1

    print(f"Maximum inflation rate change was "
          f"{greatest_difference:.1f} points.")

if __name__ == "__main__":
    main()
