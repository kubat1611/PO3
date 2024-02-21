# PO3

Prosty serwis webowy umożliwiający zarządzanie użytkownikami.

## Funkcje

- Dodawanie nowego użytkownika
- Pobieranie listy wszystkich użytkowników
- Pobieranie informacji o konkretnym użytkowniku
- Aktualizacja danych użytkownika
- Usuwanie użytkownika

## Endpointy

### Pobieranie listy użytkowników
**GET /users**

Zwraca listę wszystkich użytkowników zapisanych w serwisie.

### Pobieranie informacji o użytkowniku
**GET /users/<id>**

Zwraca informacje o użytkowniku o podanym ID.

### Dodawanie nowego użytkownika
**POST /users**


Tworzy nowego użytkownika na podstawie przekazanych danych. Przyjmuje dane w formacie JSON:

```json
{
    "firstName": "Imię",
    "lastName": "Nazwisko",
    "birthYear": 1990,
    "group": "user"
}
```

### Aktualizacja danych użytkownika
**PATCH /users/<id>**

Aktualizuje dane użytkownika o podanym ID. Przyjmuje dane w formacie JSON, które mają zostać zaktualizowane.

### Usuwanie użytkownika
**DELETE /users/<id>**

Usuwa użytkownika o podanym ID.

## Przykładowe użycie

### Dodanie nowego użytkownika

**curl -X POST -H "Content-Type: application/json" -d '{"firstName":"John","lastName":"Doe","birthYear":1990,"group":"user"}' http://localhost:5000/users**

### Pobranie listy użytkowników

**curl http://localhost:5000/users**

### Autor

Jakub Teterycz




