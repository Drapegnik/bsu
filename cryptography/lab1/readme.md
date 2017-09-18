# lab1
Vigenere Cipher

## tasks
1. Реализовать программное средство, осуществляющее шифрование и дешифрование текстового файла, содержащего текст на заданном языке.
2. Реализовать программное средство, осуществляющее криптоанализ зашифрованного по [методу Виженера](https://ru.wikipedia.org/wiki/Шифр_Виженера) текста. Для криптоанализа использовать [тест Касиски](https://ru.wikipedia.org/wiki/Метод_Касиски).
3. Провести экспериментальное исследование зависимости вероятности успешного проведения атаки по [методу Касиски](https://ru.wikipedia.org/wiki/Метод_Касиски) от длины шифротекста.
4. Провести экспериментальное исследование зависимости вероятности успешного проведения атаки по [методу Касиски](https://ru.wikipedia.org/wiki/Метод_Касиски) от длины использованного при шифровании ключевого слова.

## demo
```
Caesar:
 data:		Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
 encrypted:	Svylt Pwzbt pz zptwsf kbttf alea vm aol wypuapun huk afwlzlaapun pukbzayf. Svylt Pwzbt ohz illu aol pukbzayf'z zahukhyk kbttf alea lcly zpujl aol 1500z, dolu hu buruvdu wypualy avvr h nhsslf vm afwl huk zjyhtislk pa av thrl h afwl zwljptlu ivvr. Pa ohz zbycpclk uva vusf mpcl jluabyplz, iba hszv aol slhw puav lsljayvupj afwlzlaapun, ylthpupun lzzluaphssf bujohunlk. Pa dhz wvwbshypzlk pu aol 1960z dpao aol ylslhzl vm Slayhzla zollaz jvuahpupun Svylt Pwzbt whzzhnlz, huk tvyl yljluasf dpao klzravw wbispzopun zvmadhyl sprl Hskbz WhnlThrly pujsbkpun clyzpvuz vm Svylt Pwzbt.
 decrypted:	Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Vigenere:
 data:		Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
 encrypted:	Vspoq Stqeq sw cmkzpw hswqw xchx yj dlc tpsrrsre eln ritccirdmlq gxhscxpi. Vspoq Stqeq req fcor dlc mlnyqdvw'w cxyxhybh nykwc divd cfip wgxgc xfo 1500c, glcx yx sxolyal tpsrrov dsmu y kyvpci mp ritc eln qmvywfjoh sx ds weio y xwzi ctcmmkor lsmu. Sx req wsbzgfib rmd mxpw jgfi mildypsiq, zex kpqy rri viyz gxxm ijogrbslsg dcnowcdxgxk, vcwegxmlq ccwcxxgkpji sxgfkreoh. Mr ayc nytsvepswcn gx rri 1960w gmrr rri bijoeqo mp Joxpkwcd qricdw msldegxmlq Jyvcw Gzwsw nkwqkkcc, krb qmbi biaorrvc gmrr bowidsn tslpgclgxk csddaybi vmio Yvhsc NkkcWeiov sravybsre zcbwgyrq sd Pmbik Mncyk.
 decrypted:	Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Kasiski:
 keyword length:	3
 finded keyword:	KEY
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```