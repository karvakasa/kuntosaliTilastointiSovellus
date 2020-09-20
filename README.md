# kuntosaliTilastointiSovellus
- Tarkoituksena olisi tehdä Kuntosali Tilastointi sovellus johon kirjaudutaan ensiksi sisään jotta näemme vain omat tulokset emmekä kaikkien ihmisten tuloksia.

- Seuraavaksi on mahdollisuus lisätä päivän treenin tulokset. Eli liike, toistojen määrä, likkeen paino määrä, paikka ja päivämäärä otamme suoraan lisäys päivästä.

- On myös mahdollisuus hakea vanhoja tuloksia hakemalla yksittäisiä liikkeitä ja listaa kyseisen liikkeen tulokset päivämäärien mukaan jotta kehitystä voisi seurata tai päivämäärällä esim. mitä tein viime marraskuun seitsemäs päivä joka sitten listaa tulokset haku ehtojen alle.

Tietokanta taulut olisivat 
1. kayttajat: id, nimi, salis 
2. liike: id, nimi 
3. paikka: nimi, id 
4. toistot: määrä liike_id, kayttaja_id, painomäärä, päivämäärä, paikka_id 
5. käyttäjäloki: kayttaja_id, date

Sovellus toimii vielä tönkösti ekalla kerralla. ensiksi joutuu kirjautumaan vaikka tunnuksia ei ole. joka siirtää sinut käyttäjän luomiseen ja siitä takaisin kirjautumis pisteeseen. kirjautumisen jälkeen tulee yleissivu mihin voi lisätä tuloksia (ei toimi vielä, chrashaa), mennä tuloksiin (ei vielä mitään siellä) josta voi napilla mennä takaisin yleissivulle, käyttäjä loki pitää listaa milloin olet kirjautunut sisään (ei myöskään omista sisällään mitään järkevää vielä) ja yleissivun pohjalla on kirjaudu ulos nappi.

heroku sovelluksen linkki:
https://tsoha-punttisalitilastointi.herokuapp.com