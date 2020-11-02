# Programme de défis artistiques

## Introduction

On va écrire un programme qui affiche des défis. Cecis seront précisés par la lecture d'un fichier regroupant toutes les modalités des différentes catégories. Cela équivaut à écrire un programme qui lit un pseudo-langage ou format.

Le principe de fonctionnement sera le suivant: on veut un générateur de défis, donc qui nous tire aléatoirement des critères. Pour cela, pour chaque catégorie, on va associer un poids, est la probailité d'optenir un certain critère sera inversement proportionnel à ce poids: plus poids est grand, moins on a de "chance" de tomber sur le critère associé. Ainsi, pour chaque critère selectionné, on va augmenter son poids afin de moins retomber dessus lors de tirages ultérieurs. 

### Langage

Le language ou "format" des données que nous auront à traîté aura les règles suivantes:

```
Entrée        := | <Catégorie> ; <Poids> ; <Association>
                 | <Catégorie> ; <Association>

<Catégorie>   := | <Nom>
                 | #<Nom>

<Association> := | <Numéro>@<Élément>
                 | <Numéro><Élément>
                 | @<Élément>
                 | <Élément>

<Élément>     := | <Catégorie>
                 | <Type>
```

On voit que `<poids>` est optionnel, en effet, cela va nous permettre d'avoir une chose en moins à écrire lorsque l'on va peupler le fichier de données 

- `<Numéro>` n'est requis que lorsque `<Catégorie>` est préfixée par `#`, soit de la forme `#<Nom>`.

- `@` nous indique que `Élément` est une sous catégorie

Ainsi, voici des entrées valides:

```
A; 1; B        // (1): Entrée complète
A; B           // (2): Entrée simplifiée
A; @B          // (3): (2) + B est une sous catégorie
#A; 1B         // (4): (2) + A est préfixée d'un '#'
A; @#B         // (5): (2) + B est une sous catégorie préfixée de '#'
#A; 1@#B       // (6): (2) + (4) + (5)
```

Et voici des entrées invalides:

```
A
A; B; 1
A; B; C
#A; B
```

On va réserver la catégorie `_` pour la racine, ou répertoire des catégories principales.

### Comment procéder

Nous allons diviser le programme en 3 parties:

- __Principale__: Qui va "Gérer" le programme, considérer les arguments à l'execution (nous y reviendrons)

- __Lecture/Écriture__: Qui va lire et écrire des fichier mais aussi formater les données

- __Logique__: Soit le coeur du programme

Ces trois parties seront contenues dans 3 fichiers différents, respectivement `main.py`, `io_handler.py` et `logic.py`.

## Programmation

### Lecture

On va commencer par écrire la lecture de notre fichier de données.

##### read_data()

On va écrire une fonction que l'on va appeler `read_data` qui va prendre en entrée une chaîne de caractères `file_name` et qui va nous donner en sortie une liste avec toutes les lignes du fichier de donnée divisées par blocs de `;`.

Exemple:

```
Entrée: "A; B; C"
Sortie: ["A", "B", "C"]
```

Pour cela on va avoir besoin de la fonction `open` de la librairie standard (ou STD/STL), prend en entrée un nom de fichier et une méthode d'ouverture:

```python
open(file_name, open_type) 

# on prend "r" pour "read", et "w" pour "write".
# S'utilise de la façon suivante:
f = open(file_name, "r")
# f est maintenant la liste des lignes du fichier intitulé file_name

# Une fois que l'on a fini de lire le fichier on le ferme:
f.close()
```

Pour itérer sur les lignes du fichier on utilise une boucle `for`:

```python
for line in my_file:
    # Faire quelque chose avec `line`
    # `line` est la chaîne de caractères représentant la ligne.
```

Pour diviser chaque ligne en cellules on utilise la fonction `split`:

```python
# Avec `s` une chaîne de caractères (str)
s.split(séparateur)

# Par exemple, si on veux séparer aux '|':
s.split('|')

# split() renvoie la liste des éléments séparés
>>> s = "A|B|C"
>>> s.split('|')
['A', 'B', 'C']
```

Et enfin, pour retirer les blancs en début et fin de chaîne de caractères, on utilise `strip`:

```python
>>> s = '   asdf '
>>> s.strip()
'asdf'
```

Pour ajouter des éléments à la fin d'une liste on utilise `append`:

```python
>>> l = []            # Initialisation de la liste
>>> l.append("elem1") # Ajout
>>> l                 # Affichage de l
['elem1']
```

`read_data` aura donc la forme:

```python
def read_data(file_name):
    data = []
    # lecture du fichier
    return data
```

###### Comment tester?

Voici des données de test:

```
_; 1; @A
_; 1; @#B
_; 1; @C
A; 1; hello
A; 4; there
A; 3; How
A; 4; How2
A; 6; How23
A; 7; How34
A; 7; How42
A; 8; How424
#B; 1; 1Are
#B; 1; 2You
#B; 1; 3Doing
C; 4; HAHA
```

Il suffit de copier-coller ces données dans un fichier quelconque, par exemple `data` et ensuite nous allons créer le fichier `main.py`.

Dans celui-ci nous allons importer la fonction `read_data` fichier `io_handler.py` de la façon suivante:

```python
import io_handler as ioh
```

Cela va importer toutes les fonctions que l'on pourra écrire dans `io_handler` et nous pourrons les appeler en écrivant:

```py
ioh.ma_fonction(mes_arguments)
```

Pour l'instant, pour tester la fonction `read_data` nous allons simplement écrire:

```py
import io_handler as ioh

file_name = "data" # Ou tout autre nom que porte le fichier test.
data = ioh.read_data(file_name)
print(data) # affiche le contenu de data 
```

Pour exécuter le programme, il suffit (sous Windows) de double cliquer sur le fichier ou (Sous linux et MacOS) d'écrire dans le terminal au répertoire de travail: `python main.py`.  

Ce qui devrait nous donner en sortie:

```py
[['_', '1', 'A'], ['_', '1', 'B'], ['_', '1', 'C'], ['A', '1', 'hello'], ['A', '4', 'there'], ['A', '3', 'How'], ['A', '4', 'How2'], ['A', '6', 'How23'], ['A', '7', 'How34'], ['A', '7', 'How42'], ['A', '8', 'How424'], ['B', '1', 'Are'], ['B', '1', 'You'], ['B', '1', 'Doing'], ['C', '4', 'HAHA']]
```
