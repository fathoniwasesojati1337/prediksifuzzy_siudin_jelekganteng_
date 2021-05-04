# prediksifuzzy_siudin_jelekganteng 🚀
Si Udin's predictions about handsome and ugly performances based on body weight and height using fuzzy algorithms


                                   FUZZY LOGIC USING PYTHON PERFORMANCE SI UDIN JELEK BAGUS PREDIKSI

prediksi tinggi badan seseorang.

 -linguistik tinggi badan : tinggi, medium, pendek
 -linguistik berat badan:   berat,ringan, lumayan

 konsekuensi : bagus, jelek

 rules:

- [x] IF tinggi AND berat   THEN ganteng
- [x] IF medium AND berat   THEN ganteng
- [x] IF medium AND ringan  THEN jelek
- [x] IF pendek AND berat  THEN jelek
- [x] IF pendek AND ringan THEN jelek         

-library : scikit-learn (machine learning, AI)

-input : udin memiliki tinggi sekitar 130 cm dan berat 40cm

# membership function (keanggotaan) 🚀

-> untuk keanggotaan pada tinggi badan dengan range dari 0 sampai 200

![alt text](https://github.com/fathoniwasesojati1337/prediksifuzzy_siudin_jelekganteng_/blob/main/image/tinggibadan.png)

-> untuk keanggotaan pada berat badan dengan range dari 0 sampai 100

![alt text](https://github.com/fathoniwasesojati1337/prediksifuzzy_siudin_jelekganteng_/blob/main/image/beratbadan.png)

-> untuk performace dengan range dari 0 sampai 100

![alt text](https://github.com/fathoniwasesojati1337/prediksifuzzy_siudin_jelekganteng_/blob/main/image/performace.png)

- pada rules akan di gabungkan dari rules-rules di atas dengan sebuah array 
  dan dijadikan sebuah node rules

![alt text](https://github.com/fathoniwasesojati1337/prediksifuzzy_siudin_jelekganteng_/blob/main/image/ruleperformace.png)


# hasil outputnya 🚀

![alt text](https://github.com/fathoniwasesojati1337/prediksifuzzy_siudin_jelekganteng_/blob/main/image/outputhasil.png)
