from services import DataBaseService
from moks import books_esp

db: DataBaseService = DataBaseService()
# db.create_collection("books_esp")
# db.upload_data("books_esp", books_esp.data)


book = {
    "title": "El Quijote",
    "description": "El ingenioso hidalgo don Quijote de la Mancha narra las aventuras de Alonso Quijano, un hidalgo pobre que de tanto leer novelas de caballería acaba enloqueciendo y creyendo ser un caballero andante, nombrándose a sí mismo como don Quijote de la Mancha.",
    "author": "Miguel de Cervantes",
    "year": 1605,
    "date": "1605-01-01T00:00:00"
}

# db.update_point("books_esp", 1, book)

# db.delete_point("books_esp", 1000)

point = db.get_point("books_esp", 1000)
print(point)