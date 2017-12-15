# lab2

Protected Notebook

## task

Написать программу _«Защищенный блокнот»_ реализующую шифрование и просмотр зашифрованных текстовых
файлов алгоритмом [`AES`](https://ru.wikipedia.org/wiki/Advanced_Encryption_Standard) +
[Режим сцепления блоков (`СВС` — Cipher Block Chaining)](https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D0%B6%D0%B8%D0%BC_%D1%88%D0%B8%D1%84%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F#Cipher_Block_Chaining_.28CBC.29)

1. Серверная часть программы:
   * хранит текстовые файлы
   * генерирует случайный сеансовый ключ по запросу клиента
   * отправляет клиенту зашифрованный сеансовым ключом текстовый файл
   * отправляет клиенту зашифрованный открытым ключом `RSA` сеансовый ключ.
2. Клиентская часть программы:
   * Генерирует и отправляет серверу открытый ключ `RSA` (единожды).
   * Отправляет серверу запрос с именем файла.
   * Расшифровывает сеансовый ключ при помощи закрытого ключа `RSA`.
   * Расшифровывает и отображает текстовый документ при помощи сеансового ключа.
   * Ключ `RSA` сохраняется (генерируется по нажатию кнопки). Придумать свой метод хранения закрыто.

## additional tasks

1. Добавить в программу аутентификацию по паролю
2. Использовать вместо `RSA ECDSA` или `GM` алгоритмы
3. Добавить срок годности к сеансовому ключу
4. Реализовать клиента на платформе `Android`

## demo

<p align="center">
  <img src="http://res.cloudinary.com/dzsjwgjii/image/upload/v1513309821/crypto-lab2-1.png" width="270px"/>
  <img src="http://res.cloudinary.com/dzsjwgjii/image/upload/v1513309820/crypto-lab2-2.png" width="270px"/>
  <img src="http://res.cloudinary.com/dzsjwgjii/image/upload/v1513309822/crypto-lab2-3.png" width="270px"/>
</p>

---

<p align="center">
  <img width="500px" alt="foot shooting prevention agreement" src="https://github.com/Drapegnik/bsu/raw/master/cryptography/lab2/foot-shooting-prevention-agreement.png"/>
</p>
