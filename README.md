## Homework_16.1 Наследование

### Задачи

#### Задание 1 

Для магазина необходимо выделить две категории товаров и создать под них классы:
+ Смартфон(`Smartphone`)
Помимо имеющихся свойств, необходимо добавить следующие:
- производительность (`efficiency`), 
- модель (`model`),
- объем встроенной памяти (`memory`),
- цвет (`color`).

+ Трава газонная (`LawnGrass`). 
Помимо имеющихся свойств, необходимо добавить следующие:
- страна-производитель (
`country`),
- срок прорастания (`germination_period`),
- цвет (`color`).

Эти оба класса должны быть классами-наследниками от исходного класса`Product`.

#### Задание 2.

Доработайте функционал сложения таким образом, чтобы можно было складывать товары только из одинаковых классов
продуктов. 

То есть новый функционал не должен давать возможность сложить смартфон и траву газонную, вместо этого должна быть выдана
ошибка`TypeError` .

#### Задание 3

Ранее мы реализовали отдельный метод, с помощью которого можно добавлять объекты продуктов в категории. Теперь защитим метод так,
чтобы, кроме смартфонов, травы газонной или других продуктов, в список нельзя было добавлять ничего другого.

Доработайте метод, который добавляет продукт в категорию, таким образом, чтобы не было возможности добавить вместо 
продукта или его наследников любой другой объект.

#### Задание 4

Напишите тесты для нового функционала. При этом убедитесь, что тесты, которые были написаны ранее, выполняются без ошибок.
