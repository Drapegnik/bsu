# Лабораторная работа 6
«Использование регулярных выражений»

## task
Создать приложение для решения следующего задания

## problem
> В корректном `xml`-файле проанализировать, есть ли теги с пустым телом. Если такие будут найдены, то заменить их на теги без тела `<имя …/>`

## demo

```
<note>
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body></body>
    <kek> </kek>
</note>

<note>
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body/>
    <kek/>
</note>
```
