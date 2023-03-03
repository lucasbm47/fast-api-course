from fastapi import FastAPI

app = FastAPI()

pokemon_list = {
    '1': {'name': 'Bulbasaur', 'Type': 'Grass', 'Previous': None, "evolve_level": 16},
    '2': {'name': 'Ivysaur', 'Type': 'Grass', 'Previous': '1', "evolve_level": 36},
    '3': {'name': 'Venasaur', 'Type': 'Grass', 'Previous': '2', "evolve_level": None},
    '4': {'name': 'Charmander', 'Type': 'Fire', 'Previous': None, "evolve_level": 16},
    '5': {'name': 'Charmeleon', 'Type': 'Fire', 'Previous': '4', "evolve_level": 36}
}

@app.get("/")
async def list_all_pokemon():
    return "Welcome to the frontpage! Go to /pokemon to watch more."

@app.get("/pokemon")
async def read_all_books():
    response = {"message": "You entered the /pokemon dir", 
                "pokelist": pokemon_list}
    return response

@app.get("/pokemon/{number}") # Number is a path parameter. Lets try it in :8000/docs!
async def read_book(number: str):
    return pokemon_list[number]

@app.post("/")
async def add_pokemon(pokemon_number: str, pokemon_name: str):
    pokemon_list[pokemon_number] = pokemon_name
    return pokemon_list[pokemon_number]

"""
Query params vs Path Params

https://fastapi.tiangolo.com/tutorial/query-params/

When we declare a parameter in the function (async def line) that is not declared as a Path Parameter 
(within the curly braces) in the app.get(...) decorator, FastAPI interprets it as a query param authomatically


Example

@app.get("/assignment/") 
async def read_book_assignment(book_name: str): 
    return book_list[book_name]

Here book_name is in the function declaration but is not part of the path parameters, so it's interpreted as
a query parameter. The default values of the query parameters can be set to None in order to say that they are optional.

@app.get("/assignment/{book_name}")  <----- Here the book_name is a path parameter 
async def read_book_assignment(book_name: str): 
    return book_list[book_name]

"""  