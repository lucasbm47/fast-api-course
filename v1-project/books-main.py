from fastapi import FastAPI

app = FastAPI()

book_list = {
    'book_1': {'title': 'title one', 'author': 'author one'},
    'book_2': {'title': 'title two', 'author': 'author two'},
    'book_3': {'title': 'title three', 'author': 'author three'},
    'book_4': {'title': 'title four', 'author': 'author four'},
    'book_5': {'title': 'title five', 'author': 'author five'}
}

@app.get("/")
async def read_all_books():
    return book_list

@app.get("/books/{book_name}")
async def read_book(book_name: str):
    return book_list[book_name]

@app.post("/")
async def create_book(book_title, book_author):
    curr_book_id = 0
    if(len(book_list) > 0):
        # Search the max number of book id in the list. We do the for in case the books are not ordered
        for book in book_list:
            x = int(book.split('_')[-1])
            if(x > curr_book_id):
                print(curr_book_id)
                curr_book_id = x
    new_id = "book_" + str(curr_book_id + 1)
    book_list[new_id] = {'title': book_title, 'author': book_author}
    return book_list
        