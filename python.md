# Introduction à Python

Quelques notions importantes:

### Types

_Python_, comme tout langage de programmation nous fournis un outils essentiel, les _variables_. Une variable est _déclarée_ et _initialisée_ de la façon suivante:

```py
ma_variable = val
```

Une variable a un type, celui de sa valeur. Un type est une "catégorie", ça nous sert à savoir à quoi on a à faire. Par exemple, on ne compare pas des patates et des carottes.

Il existe 6 types dits _primitifs_ en _python_:

- Numérique (nombre) ou `int`, `float` et `complex` (resp. nombres entiers, décimaux et complexes)

- Booléen ou `bool`, soit Vrai et Faux ou `True` et `False`.

- Chaîne de caractères ou `str` (string)

- Liste ou `list`

- Tuple ou `tuple`

- Dictionnaire ou `dict`

On peut déterminer _dynamiquement_ le type d'une variable avec `type()`:

```py
>>> type(10)
<class 'int'>
```

`10`est de type `int`, un _entier_.

#### Numérique

Il y a les nombres entiers et les nombres décimaux:

```py
a = 1
b = 2.0
c = 10 + 3j
type(a)
# <class 'int'>
type(b)
# <class 'float'>
type(c)
# <class 'complex'>
```

On peut effectuer les actions suivantes sur ces type:

```py
a = 3
b = 2

a + b # addition
# 5

a * b # multiplication
# 6

a - b # soustraction
# 1

a / b # division
# 1.5

a // b # division euclidienne
# 1

a % b # modulo ou reste de la division euclidienne
# 1

a ** b # a exposant b
# 9
```

On remarque que bien que `a` et `b` soit des `int`, le type de `a / b` est `float`.

Les opérations ci-dessus nous donne une valeur, mais ni `a` ni `b` ne sont modifié. Si on veut garder le résultat, il nous faut le capturer avec une autre variable:

```py
c = a + b # c vaut 5
```

Mais si on veut par exemple ajouter à `a` la valeur de `b`

```py
a = a + b
```

Mais il existe une façon plus agréable de l'écrire:

```py
a += b
```

C'est équivalent. Cette écriture est présente pour tous les opérateurs:

```py
a += b  # a = a + b
a -= b  # a = a - b
a *= b  # a = a * b
a /= b  # a = a / b
a //= b # a = a // b
a %= b  # a = a % b
a **= b # a = a ** b
```

On peut effectuer les mêmes operations avec les `float` et`complex`.

#### Booléen

Vrai ou Faux.

```py
b = True
b = False

type(b)
# <class 'bool'>
```

On a plusieurs opérateurs, dits 'booléens' ou de 'test', qui retournent un booléens:

```py
a = 1
b = 2

a == b # Teste si a vaut b
# False
a != b # Teste si a est different de b
# True

a < b # Teste si a strictement inférieur à b
# True
a > b # Teste si a strictement supérieur à b
# False
a <= b # Teste si a inférieur à b
# True
a >= b # Teste si a supérieur à b
# False

a = True
b = False

a and b # Teste si a et b sont vrais
# False
a or b  # Teste si a ou b sont vrais
# True
not a # Teste l'inverse de a
# False
```

Un exemple de test complex:

```py
(a < b and b <= c) or (not a == d)
# Teste si soit a < b et b <= c, soit a différent de b (ou les 2)
```

#### Chaîne de caractères

Les chaînes de caractères ou string ou `str` sont des suites de caractères entre guillemets simples ou doubles ou triple guillemets doubles.

```py
s1 = 'Une chaîne'
s2 = "Une autre chaîne"
s3 = """Encore une autre..."""

type(s1)
# <class 'str'>
```

On peut effectuer les opérations suivantes:

```py
a = "Hello "
b = "World!"

a[0] # Accès au premier élément
# 'H'
a[2] # Accès aus 3e élement
# 'l'
a[-1] # Accès au dernier élément
# 'o'

a[0:2] # Sous-chaîne ou 'tranche' du premier au 3e élément
# 'Hel'

a[2:] # Tranche allant du 3e élément au dernier
# 'lo'

a * 2 # Chaîne de 2 fois la chaîne 'a'
# 'HelloHello'

a + b # 'Concaténation' de la chaîne a avec la chaîne b
# 'Hello World!'

len(b) # Nous donne le nombre de caractères (length)
# 6
```

#### Listes

Une liste est un ensemble de différents élément, pas nécessairement du même type. C'est un _conteneur_.

```py
ma_liste = [] # Liste vide
ma_liste = [1, "A"]

type(ma_liste)
# <class 'list'>
```

On peut effectuer les mêmes opérations que pour les chaînes de caractères. Mais on peut aussi ajouter des éléments:

```py
l = []

l.append(1) # [1]`
l.append("A") # [1, 'A']

l.insert(1, 2) # [1, 2, 'A'] On a inséré '2' à la 2nde position

a = l.pop() # [1, 2]
# a vaut 'A'
```

#### Tuples

Les tuples sont aussi des _conteneurs_. Mais ceux-ci ne sont pas modifiables.

```py
t = ("A", 1)
type(t)
# <class 'tuple'>
```

Ils ont les mêmes opérations que les chaînes de caractères.

#### Dictionnaires

Encore un _conteneur_. Mais cette fois ci, au lieu d'accéder aux éléments de celui-ci par indices, on associe à chaque élément une clé.

```py
d = {}  # Dictionnaire vide
d = {"A": 1, "B": 2}

type(d)
# <class 'dict'>
```

Voici les opérations associées:

```py
d = {"A": 1, "B": 2}

d["A"] # Accès à la valeur associée à 'A'
# 1

d["C"] = 3 # Initialisation d'une paire clé-valeur
```

Une clé peut être de n'importe quel type non modifiable: numérique, chaîne de caractères ou tuple en ce qui concerne les types _primitifs_.

```py
d = {}

d["A"] = 1      # chaîne de caractères
d[1] = 2        # numérique
d[("A", 1)] = 3 # tuple

print(d)
# {'A': 1, 1: 2, ('A', 1): 3}
```

Il peut arriver que l'on aie besoin de savoir si une clé existe dans un dictionnaire, pour ce faire:

```py
if cle in d: # Si la clé existe
    # Faire ce que l'on veut


# Ou le contraire
if cle not in d: # Si la clé n'existe pas
    # Faire ce que l'on veut
```

Par exemple si on veut initialiser une clé que si elle n'existe pas sinon incrémenter de 1 la valeur associée (utilisation de la boucle `for` qui sera vue dans un chapitre ultérieur):

```py
d = {'A': 1, 'B': 1}
l = ['A', 'B', 'C']

for cle in l:
    if cle in d:     # Si la clé existe
        d[cle] += 1  # Incrémentation
    else:            # Sinon
        d[cle] = 1   # Initialisation
```

#### None

J'ai menti ! Enfin, pas vraiment... Il existe un autre 'type' primitif, qui est `None`. Il représente le _vide_ ou l'absence de valeur. Tout type peut valoir `None`.

```py
>>> i = None
>>> i is None
True
```

On s'en sert principalement en sortie de fonction lorsque la fonction rencontre une erreur et qu'elle devait retourner un type spécifique. Comme `None` est à la fois tous les types et aucun, il n'y a pas d'erreur d'interprétation de la part du programme. i.e: Le programme ne panique pas lorsqu'il voit un `None` arriver au lieu d'un entier attendu, contrairement à s'il recevait un flottant.

### Cast

Maintenant que l'on a les types _primitifs_, nous allons voir comment transformer un type en un autre.

On peut transformer tout type numérique en un autre:

```py
a = 1

float(a)
# a = 1.0

int(a)
# a = 1

a = 1.5
int(a)
# a = 1
```

On peut transformer une liste en tuple et inversement. 

```py
l = [1, 2, 3]

t = tuple(l)
# t = (1, 2, 3)

l = list(t)
# l = [1, 2, 3]
```

Pour les chaines de caractères:

```py
s = "abc"
l = list(s)
# l = ['a', 'b', 'c']
t = tuple(s)
# t = ('a', 'b', 'c')

i = int("1")
# i = 1
```

### Boucles

Pour effectuer plusieurs fois une même opération, on préfère à l'écriture de 10 mêmes lignes l'utilisation de boucles.

#### Boucle `while`

La boucle `while` ou 'tant que' est une boucle qui va effectuer toutes les opérations dans son _bloc_ tant qu'une certaine condition est vérifiée.

```py
while condition: # Tant que condition est vraie
    # Effectuer le bloc 
```

Une condition est un booléen, c'est à dire qu'elle ne peut avoir pour valeur que Vrai ou Faux, en _python_ `True` ou `False`:

```py
# Boucle infinie
while True:
    # Faire...

# Boucle qui ne s'exécutera jamais
while False:
    # Faire...
```

Par exemple on pourrait faire une opération tant qu'une certaine variable n'a pas atteint une certaine valeur:

```py
val = 0
while val < 10: # Tant que val est inférieur à 10
    #Faire
    print(val)
    val += 1 # On ajoute 1 à val (incrémente)
```

```py
# ================== Sortie =======================
0
1
2
3
4
5
6
7
8
9
```

##### Petite bonus: `break`

Si on veut interrompre la boucle sans vérifier la condition on utilise le mot clé `break`:

```py
val = 0
while True: # Boucle infinie
    print(val)
    if val == 10:
        break; # On "casse" la boucle
    val += 1
```

```py
# ================== Sortie =======================
0
1
2
3
4
5
6
7
8
9
```

On remarque que cette boucle la même chose que la précédente.

`break` fonctionne aussi pour la boucle `for` qui suit.

#### Boucle `for`

Il est souvent utile de parcourir un ensemble d'éléments (itération) ou de borner l'exécution d'une boucle.

En _python_, la boucle `for` ou 'pour tout' parcours un ensemble d'éléments et donne à une variable donnée la valeur successive de ces-dits éléments.

```py
for i in [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9]: # Pour tout 'i' dans ...
    print(i)
```

```py
# ================== Sortie =======================
0
1
2
3
4
5
6
7
8
9
```

Ici, `i` a pris successivement chacune des valeurs de la liste  `[0, 1, 2, 3, 4, 5, 6, 7 ,8, 9]`

On remarquera que l'écriture de la boucle for, bien que faisant la même chose que les boucles `while` précédentes est bien plus succinctes.

Mais on peut faire mieux. Une _fonction_ (élément important de la programmation que nou verrons au chapitre suivant) qui est utilisée pour borner est la suivante:

```py
range(start, stop, step)
```

Par défaut, `start` vaut `0` et `step` vaut `1`. `step` est le _pas_.

```py
# '==' signifie "équivaut à"

range(0, 10, 1) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Que l'on peut simplifier par:
range(0, 10)
# Ou encore par:
range(10)

# 'start' différent:
range(5, 10) == [5, 6, 7, 8, 9]

# 'pas' de 2:
range(0, 10, 2) == [0, 2, 4, 6, 8]
```

Ainsi:

```py
for i in range(10):
 print(i)
```

Est équivalent à la boucle précédente et est encore plus succincte. Ça permet de ne pas avoir à écrire une liste de 100 nombres à la main.

Mais on peut itérer sur n'importe quel ensemble:

```py
for e in ['A', 1, [12, 2]]:
    print(e)
```

```py
# ================== Sortie =======================
A
1
[12, 2]
```

##### Itération sur les dictionnaires

Lorsque l'on itère sur un dictionnaire, on itère sur ses clés:

```py
d = {"A": 1, "B", 2, "C": 3}

for cle in d:
    print(cle)
```

```py
# ================== Sortie =======================
A
B
C
```

Si on veut itérer sur les valeurs associées aux clés il nous faut donc faire:

```py
for cle in d:
    val = d[cle] # On récupère la valeur associée à la clé
    print(val)
```

```py
# ================== Sortie =======================
1
2
3
```

### Fonctions

Une fonction est un bloc de code qui prend des arguments en entrée, fait sa popote et nous sort quelque chose. Il faut voir cela un peu comme une boîte noire. Écrire des fonctions nous permet d'abstraire le fonctionnement du programme et de finalement jouer aux LEGO en assemblant des fonctions les unes avec les autres.

En _Python_, une fonction a la forme suivante:

```py
def ma_fonction(arg1, arg2):
    # Popote
    return sortie
```

Il est à noter qu'une fonction n'est pas obligée de retourner une quelconque sortie, parfois on n'en a pas besoin, par exemple, lorsque l'on veut afficher quelque chose. Il n'y a pas de calcul dont on veut le résultat.

Et on "appelle" une fonction de la façon suivante:

```py
ma_fonction(arg1, arg2)
```

Exemples:

```py
# Additionne a et b
def addition(a, b):
    return a + b
```

```py
# Affiche le contenu d'une liste:
def affiche_liste(liste):
    for e in liste:
        print(e)
```

```py
# Fonction qui somme tous les éléments d'une liste
def somme(liste):
    s = 0
    for e in liste:
        s = addition(s, e) # On appelle la fonction addition().
    return s
```

Execution:

```py
>>> addition(1, 3)
4
>>> affiche_liste(['A', 'B', 'C'])
A
B
C
>>> somme([1, 2, 3, 4, 5])
15
```

### Input/Output

#### Output

Pour afficher quelque chose à l'écran, on utilise la fonction `print`:

```py
>>> print("Hello")
Hello

>>> print("Hello", "There")
Hello There

>>> print("Le nombre vaut:", 3)
Le nombre vaut: 3
```
`print` affiche tous ses arguments séparés par un espace et retourne à la ligne.
On peut utilise la fonction format pour "Formater" une chaîne de caractères:

```py
>>> print("Le nombre vaut: {}".format(3))
Le nombre vaut: 3

>>> print("{} et {} sont partis.".format("Julien", "Marie"))
Julien et Marie sont partis.
```

#### Input

Pour récupérer une entrée utilisateur, on utilise la fonction `input`:

```py
>>> s = input()
Hello
>>> print(s)
Hello

>>> s = input("Entrez un nombre:")
Entrez un nombre: 3
>>> print(s)
3
```
