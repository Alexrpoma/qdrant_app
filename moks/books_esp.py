from datetime import datetime
import random

adjectives = [
    "Misterioso", "Perdido", "Oscuro", "Silencioso", "Olvidado", "Oculto", "Eterno", "Secreto", "Final",
    "Desconocido", "Tiempo", "Digital", "Mecánico", "Desapareciendo", "Susurrante", "Paralelo", "Roto",
    "Galáctico", "Carmesí", "Encantado", "Infinito", "Cósmico", "Cuántico", "Antiguo", "Futurista",
    "Virtual", "Neón", "Cibernético", "Solar", "Lunar", "Estelar", "Celestial", "Terrestre", "Astral",
    "Interestelar", "Interplanetario", "Interdimensional", "Trascendental", "Sobrenatural",
    "Extraterrestre", "Invisible", "Lejano", "Arcano", "Intemporal", "Inexplorado", "Sombra", "Olvido",
    "Invisible", "Etéreo", "Dimensional", "Mítico", "Espectral", "De otro mundo", "Insondable", "Condenado",
    "Apocalíptico", "Vacío", "Nebuloso", "Esotérico", "Rúnico", "Solaris", "Oscuro", "Errante", "Espeluznante",
    "Espejado", "Metafísico", "Surreal", "Desconocido", "Maldito", "Resonante", "Rotto", "Congelado",
    "Caótico", "Confuso", "Encriptado", "Temporal", "Reliquia", "Distópico", "Post-Apocalíptico",
    "Sintético", "Automatizado", "Omnipresente", "Hipotético", "Armónico", "Eclipsado", "Sumergido",
    "Desconectado", "Inestable", "Embrujado", "Celestino", "No descubierto", "Vórtice", "Fractal",
    "Anómalo", "Divergente", "Deformado", "Roto", "Quimérico", "Singular", "Nexo", "Irreal", "Indefinido",
    "Holográfico", "Encriptado", "Fragmentado", "Aumentado", "Alienígena", "Bio-Mecánico", "Bioluminiscente",
    "Recursivo", "Liminal", "Prismático", "Codificado", "Sintético", "Espectral", "Fantasma", "Onírico",
    "Deformador de mentes", "Paradojal", "Oscurecido", "Eclipsante", "Dimensional", "Gravitacional", "Hiperbólico",
    "Interlaced", "Vibracional", "Nebuloso", "Extrínseco", "Astrológico", "Transhumano", "Energizado",
    "Místico", "Brillante", "Con fallos", "Parpadeante", "Cuántico-enredado", "Más allá", "Críptico",
    "Subatómico", "Faseado", "Decriptado", "Energía solar", "Neural", "Celestíficamente alineado",
    "Electromagnético", "Resonante"
]

nouns = [
    "Montaña", "Río", "Valle", "Cueva", "Desierto", "Selva", "Volcán", "Glaciar", "Cielo",
    "Nube", "Lluvia", "Nieve", "Viento", "Fuego", "Tierra", "Piedra", "Metal", "Gema", "Árbol",
    "Flor", "Animal", "Pájaro", "Pez", "Insecto", "Reptil", "Mamífero", "Arma", "Escudo", "Armadura",
    "Corona", "Trono", "Cetro", "Amuleto", "Poción", "Hechizo", "Pergamino", "Mapa", "Brújula",
    "Llave", "Cerrojo", "Puerta", "Ventana", "Puente", "Camino", "Casa", "Castillo", "Torre", "Jardín",
    "Biblioteca", "Museo", "Escuela", "Hospital", "Mercado", "Restaurante", "Barco", "Bote", "Coche",
    "Avión", "Tren", "Bicicleta", "Computadora", "Teléfono", "Libro", "Pintura", "Escultura", "Música",
    "Danza", "Teatro", "Película", "Juego", "Juguete", "Ropa", "Comida", "Bebida", "Amor", "Odio",
    "Esperanza", "Miedo", "Alegría", "Tristeza", "Ira", "Paz", "Caos", "Verdad", "Mentira", "Recuerdo",
    "Secreto", "Destino", "Suerte", "Alma", "Espíritu", "Fantasma", "Ángel", "Demonio", "Dios", "Diosa",
    "Héroe", "Villano", "Monstruo", "Extraterrestre", "Humano", "Niño", "Adulto", "Anciano", "Familia",
    "Amigo", "Enemigo", "Extraño", "Líder", "Seguidor", "Maestro", "Estudiante", "Doctor", "Paciente",
    "Artista", "Escritor", "Músico", "Científico", "Ingeniero", "Atleta", "Soldado", "Rey", "Reina",
    "Príncipe", "Princesa", "Mago", "Bruja", "Dragón", "Unicornio", "Fénix", "Grifo", "Quimera",
    "Cérbero", "Hidra", "Medusa", "Cíclope", "Titán", "Dioses", "Diosas", "Héroes", "Villanos", "Monstruos",
    "Extraterrestres", "Humanos", "Niños", "Adultos", "Ancianos", "Familias", "Amigos", "Enemigos",
    "Extraños", "Líderes", "Seguidores", "Maestros", "Estudiantes", "Doctores", "Pacientes", "Artistas",
    "Escritores", "Músicos", "Científicos", "Ingenieros", "Atletas", "Soldados", "Reyes", "Reinas", "Príncipes",
    "Princesas", "Magos", "Brujas", "Dragones", "Unicornios", "Fénixes", "Grifos", "Quimeras", "Cérberes",
    "Hidras", "Medusas", "Cíclopes", "Titanes", "Guerra", "Calamidad", "Desastre", "Catástrofe", "Tragedia",
]

actions = [
    "enciende una revolución", "inspira esperanza en la hora más oscura",
    "forja alianzas inquebrantables", "rompe barreras ancestrales", "crea un efecto dominó a través del tiempo",
    "restaura el equilibrio en el mundo", "desciende a las profundidades de la locura",
    "asciende a un plano superior de existencia", "viaja a través del multiverso", "manipula los hilos del destino",
    "se convierte en una leyenda susurrada a través de generaciones", "sacrifica todo por una causa noble",
    "domina los elementos", "comunica con seres de otros mundos", "domina el poder de la creación",
    "borra un evento catastrófico", "reescribe la historia", "descubre la fuente de la juventud",
    "aprende el idioma de los animales", "controla el flujo del tiempo", "predice el futuro", "dobla la realidad a su voluntad",
    "escapa de las garras de la muerte", "encuentra el verdadero amor ante la adversidad",
    "supera obstáculos insuperables", "resuelve un acertijo imposible", "se convierte en un símbolo de esperanza",
    "une facciones dispares", "desenreda una compleja red de engaños", "enfrenta sus demonios internos",
    "encuentra la redención ante la oscuridad", "trasciende sus limitaciones", "deja un legado perdurable",
    "inspira generaciones venideras", "descubre un camino oculto hacia la iluminación", "logra la inmortalidad",
    "descubre el significado de la vida", "se convierte en uno con el universo", "vence a un mal primordial",
    "despierta a un dios dormido", "crea un nuevo universo", "destruye uno existente", "se convierte en guardián del cosmos",
    "abraza su verdadero potencial", "elige entre el amor y el poder", "camina por la línea entre la luz y la oscuridad",
    "realiza el sacrificio final", "encuentra paz en el caos", "se convierte en una fuerza de la naturaleza",
    "moldea el destino de los mundos", "desbloquea los secretos de la conciencia", "explora la naturaleza del libre albedrío",
    "desafía la definición misma de la existencia", "se convierte en una leyenda en su propio tiempo",
    "desafía a los dioses mismos", "gana el respeto de sus enemigos", "encuentra belleza en la destrucción",
    "crea orden del caos", "se convierte en un faro de esperanza en un mundo de desesperación", "encuentra fuerza en la vulnerabilidad",
    "deja el mundo mejor de lo que lo encontró", "trasciende las fronteras del espacio y el tiempo",
    "se convierte en maestro de su propio destino", "alcanza la verdadera iluminación", "encuentra su lugar en el universo",
    "se convierte en parte de algo mayor que ellos mismos", "lucha contra las fuerzas de la oscuridad",
    "desata un poder más allá de la comprensión", "la última esperanza de un mundo moribundo", "la primera luz en un mundo de oscuridad",
    "día de calamidad, noche de destino", "el fin de todas las cosas", "el comienzo de una nueva era",
]

authors = [
    "William Shakespeare", "Charles Dickens", "Emily Brontë", "Charlotte Brontë",
    "Edgar Allan Poe", "Nathaniel Hawthorne", "Herman Melville", "Walt Whitman",
    "Edith Wharton", "T.S. Eliot", "Langston Hughes", "Zora Neale Hurston",
    "Gabriel García Márquez", "Jorge Luis Borges", "Pablo Neruda", "Chinua Achebe",
    "Haruki Murakami", "Kazuo Ishiguro", "Toni Morrison", "Alice Walker",
    "Maya Angelou", "Salman Rushdie", "Arundhati Roy", "Neil Gaiman",
    "Terry Pratchett", "Douglas Adams", "Isaac Newton", "Albert Einstein",
    "Stephen Hawking", "Carl Sagan", "Marie Curie", "Leonardo da Vinci",
    "Vincent van Gogh", "Pablo Picasso", "Ludwig van Beethoven", "Wolfgang Amadeus Mozart",
    "Jane Goodall", "Charles Darwin", "Sigmund Freud", "Platón", "Aristóteles",
    "Homero", "Virgilio", "Dante Alighieri", "Geoffrey Chaucer", "Miguel de Cervantes",
    "Molière", "Johann Wolfgang von Goethe", "Friedrich Schiller", "Víctor Hugo",
    "Alexandre Dumas", "Leo Africanus", "Ibn Khaldun", "Avicena", "Al-Juarismi",
    "Hipatia", "Safo", "Murasaki Shikibu", "Lady Murasaki Shikibu", "Los Hermanos Grimm",
    "Hans Christian Andersen", "Esopo", "Rabindranath Tagore", "Khalil Gibran",
    "Naguib Mahfouz", "Wole Soyinka", "Chinua Achebe", "Ngugi wa Thiong'o",
    "Ayn Rand", "L. Ron Hubbard", "Robert A. Heinlein", "Kurt Vonnegut",
    "Joseph Heller", "J.D. Salinger", "Hunter S. Thompson", "Tom Wolfe",
    "Ernest Gaines", "Alice Munro", "Joyce Carol Oates", "Annie Proulx",
    "David Foster Wallace", "Jonathan Franzen", "Chimamanda Ngozi Adichie", "Ta-Nehisi Coates",
    "Roxane Gay", "Viet Thanh Nguyen", "Ocean Vuong", "Carmen María Machado",
    "Stephen Fry", "Bill Bryson", "Malcolm Gladwell", "Yuval Noah Harari",
    "Michelle Obama", "Barack Obama", "Hillary Clinton", "Elon Musk",
    "Bill Gates", "Steve Jobs", "Mark Zuckerberg", "Jeff Bezos",
    "Oprah Winfrey", "J.K. Rowling"
]

data = [
    {
        "title": "El Hobbit",
        "description": "Una novela de fantasía que sigue la búsqueda del hobbit Bilbo Bolsón para ganar una parte del tesoro guardado por Smaug el dragón.",
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "date": "2010-01-23T09:53:00"
    },
    {
        "title": "Harry Potter y la piedra filosofal",
        "description": "En su cumpleaños, Harry Potter descubre que es hijo de dos conocidos magos, de quienes ha heredado poderes mágicos. Debe asistir a una famosa escuela de magia y hechicería, donde establece una amistad con dos jóvenes que se convertirán en sus compañeros en su aventura. Durante su primer año en Hogwarts, descubre que un mago malévolo y poderoso llamado Voldemort está en busca de la piedra filosofal que prolonga la vida de su dueño.",
        "author": "J. K. Rowling",
        "year": 1997,
        "date": "2011-02-23T09:53:00"
    },
    {
        "title": "Harry Potter y la cámara secreta",
        "description": "Harry Potter y los estudiantes de segundo año investigan una amenaza malévola para sus compañeros de Hogwarts, una bestia amenazante que se oculta dentro del castillo.",
        "author": "J. K. Rowling",
        "year": 1998,
        "date": "2012-03-23T09:53:00"
    },
    {
        "title": "Harry Potter y el prisionero de Azkaban",
        "description": "El tercer año de estudios de Harry en Hogwarts se ve amenazado por la fuga de Sirius Black de la prisión de Azkaban. Aparentemente, es un mago peligroso que fue cómplice de Lord Voldemort y que intentará vengarse de Harry Potter.",
        "author": "J. K. Rowling",
        "year": 1999,
        "date": "2013-04-23T09:53:00"
    },
    {
        "title": "Harry Potter y el cáliz de fuego",
        "description": "Hogwarts se prepara para el Torneo de los Tres Magos, en el que competirán tres escuelas de magia. Para sorpresa de todos, Harry Potter es elegido para participar en la competencia, en la cual debe luchar contra dragones, entrar al agua y enfrentar sus mayores miedos.",
        "author": "J. K. Rowling",
        "year": 2000,
        "date": "2014-05-23T09:53:00"
    },
    {
        "title": "Harry Potter y la Orden del Fénix",
        "description": "En su quinto año en Hogwarts, Harry descubre que muchos miembros de la comunidad mágica no saben la verdad sobre su encuentro con Lord Voldemort. Cornelius Fudge, Ministro de Magia, nombra a Dolores Umbridge como profesora de Defensa contra las Artes Oscuras porque cree que el Profesor Dumbledore planea tomar su trabajo. Pero sus enseñanzas son inadecuadas, por lo que Harry prepara a los estudiantes para defender la escuela contra el mal.",
        "author": "J. K. Rowling",
        "year": 2003,
        "date": "2015-06-23T09:53:00"
    },
    {
        "title": "Harry Potter y el Príncipe Mestizo",
        "description": "Harry descubre un libro poderoso y, mientras intenta descubrir su origen, colabora con Dumbledore en la búsqueda de una serie de objetos mágicos que ayudarán a destruir a Lord Voldemort.",
        "author": "J. K. Rowling",
        "year": 2005,
        "date": "2016-07-23T09:53:00"
    },
    {
        "title": "Harry Potter y las Reliquias de la Muerte",
        "description": "Harry, Ron y Hermione se embarcan en una misión peligrosa para localizar y destruir el secreto de la inmortalidad y destrucción de Voldemort: los Horrocruxes. Solos, sin la guía de sus profesores ni la protección del Profesor Dumbledore, los tres amigos deben apoyarse más que nunca. Pero hay Fuerzas Oscuras en medio que amenazan con separarlos. Harry Potter se acerca cada vez más a la tarea para la cual se ha estado preparando desde el primer día que pisó Hogwarts: la última batalla con Voldemort.",
        "author": "J. K. Rowling",
        "year": 2007,
        "date": "2017-08-23T09:53:00"
    },
    {
        "title": "Harry Potter y el Niño Maldito",
        "description": "El segundo hijo de Harry ingresó a Hogwarts, pero en Slytherin. Su relación con Harry empeora y se hizo gran amigo del hijo de Draco, Scorpius Malfoy, quien se dice que es hijo de Lord Voldemort.",
        "author": "J. K. Rowling",
        "year": 2016,
        "date": "2022-09-23T09:53:00"
    }
]

def random_date():
    return datetime(
                    random.randint(1900, 2022),
                    random.randint(1, 12),
                    random.randint(1, 28)
                    ).isoformat()

for _ in range(1000):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    author = random.choice(authors)

    libro = {
        "title": f"El {adj} {noun}",
        "description": f"Un {adj.lower()} {noun.lower()} que {random.choice(actions)}.",
        "author": author,
        "year": random.randint(1900, 2024),
        "date": random_date()
    }
    data.append(libro)