# Задача на должность junior-программист

# Описание данных

Даны стоимости проектов в млрд р по годам, число лет в данных может варьироваться.
Данные иерархические, то есть обладают структурой дерева, где иерархия показана
в колонке код.


# Описание задачм

1. Необходимо прочитать файл и преобразовать его с помощью библиотеки pandas следующим образом:
терминальные вершины ждерева ижут со значением по годам. Необходимо для нетерминальных вершин
вычислить (проект, подпроект) сумму по терминальным для каждого года.
2. Необходимо хранить данные в БД PostgreSQL. Соответственно, для этого необходимо составить DDL.
И написать код, который будет раскладывать данные в физическую модель.

Необходимо реализовать задачу при помощи pandas