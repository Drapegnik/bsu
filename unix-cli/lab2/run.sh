gcc -Wall -ggdb lab2.cpp -o lab2.o
echo "#compiled."
./lab2.o
echo "#file contains: \c"
cat lala.txt
echo "#truss:"
sudo dtruss ./lab2.o