class Ceasar:
    @staticmethod
    def normalize(st):
        '''Функция убирает лишние знаки и пробелы, и приводит строку к нижнему регистру'''
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        st = st.lower()
        res = ''
        for i in st:
            if i in abc:
                res+=i
        return res
    @staticmethod
    def crypt(st,k):
        '''шифрует шифром цезаря исходную строку st со сдвигом равное k'''
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        st = Ceasar.normalize(st)
        res = ''
        for i in st:
            res+=abc[(abc.find(i) + k)%len(abc)]
        return res
    @staticmethod
    def decrypt(st,k):
        '''дешифрует шифр цезаря'''
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        res = ''
        for i in st:
            res+=abc[(abc.find(i) - k)%len(abc)]
        return res

class Atbash:
    @staticmethod
    def normalize(st):
        '''функция убирает лишние знаки и пробелы, и приводит строку к нижнему регистру'''
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        st = st.lower()
        res = ''
        for i in st:
            if i in abc:
                res+=i
        return res

    @staticmethod
    def crypt(st):
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        st = Atbash.normalize(st)
        res = ''
        for i in st:
            res+=abc[len(abc)-(abc.find(i))]
        return res

    @staticmethod
    def decrypt(st):
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        st = Atbash.normalize(st)
        res = ''
        for i in st:
            res+=abc[len(abc)-(abc.find(i))]
        return res

class Zam_vybor_alf:
    @staticmethod
    def normalize(st):
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        st = st.lower()
        res = ''
        for i in st:
            if i in abc:
                res+=i
        return res
    @staticmethod
    def encrypt(st,abc_zam):
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        st=Zam_vybor_alf.normalize(st)
        crypted = ''
        for i in st:
            index = abc.index(i)
            crypted += abc_zam[index]
        return crypted
    @staticmethod
    def decrypt(st,abc_zam):
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        decrypted = ''
        for i in st:
            index = abc_zam.index(i)
            decrypted += abc[index]
        return decrypted

class Zam_kod_word:
    @staticmethod
    def normalize(st):
        '''функция убирает лишние знаки и пробелы, и приводит строку к нижнему регистру'''
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        st = st.lower()
        res = ''
        for i in st:
            if i in abc:
                res+=i
        return res

    @staticmethod
    def generateabc(key):
        '''Генерирует строку замены по ключевому слову key'''
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        key = Zam_kod_word.normalize(key)
        res=''
        for i in key:
            if i not in res:
                res+=i
        for i in abc:
            if i not in res:
                res+=i
        return res

    @staticmethod
    def codeword(st,key):
        '''шифрует строку st кодовым словом key'''
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        st=Zam_kod_word.normalize(st)
        alfabet = Zam_kod_word.generateabc(key)
        res = '' 
        for i in st:
            res+=alfabet[abc.find(i)]
        return res

    @staticmethod
    def decodeword(st,key):
        '''дешифрует строку st кодовым словом key'''
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        st=Zam_kod_word.normalize(st)
        alfabet = Zam_kod_word.generateabc(key)
        res = ''
        for i in st:
            res+=abc[alfabet.find(i)]
        return res

class Ckytala:
    @staticmethod
    def normalise(st, key):
        '''Функция удаляет ненужные символы в входной сроке '''
        st=st.lower()
        kolon=(len(st)-1)//key+1
        if (key*kolon)>len(st):
            st+='*'*(key-len(st)%key)
        return st
    @staticmethod
    def spisok(mes,key,n):
        '''Преобразуем строку в список'''
        mas=[]
        for i in range(key):
            mas.append(mes[i*n:i*n+n])
        return mas
    @staticmethod
    def cryptSkitala (mes, key):
        '''Функция шифрует шифром Cкитала'''
        res=''
        mes=Ckytala.normalise(mes,key)
        n=(len(mes)-1)//key+1
        mas=Ckytala.spisok(mes,key,n)
        for i in range(n):
            for j in range(key):
                res+=mas[j][i]
        return res
    @staticmethod
    def decryptSkitala(c, key):
        '''Функция дешифрует шифром Скитала'''
        n=(len(c)-1)//key+1
        res=Ckytala.cryptSkitala(c,n)
        res2=''
        for i in res:
            if i=='*':
                break
            res2+=i
        return res2

class Stlbc:
    @staticmethod
    def normalise(st, key):
        '''Функция удаляет ненужные символы в входной сроке '''
        st=st.lower()
        kolon=(len(st)-1)//key+1
        if (key*kolon)>len(st):
            st+='*'*(key-len(st)%key)
        return st
    @staticmethod
    def spisok(mes,key,n):
        '''Преобразуем строку в список'''
        mas=[]
        for i in range(key):
            mas.append(mes[i*n:i*n+n])
        return mas
    @staticmethod
    def crypt(mes, key):
        '''Функция шифрует шифром простой перестановки'''
        res=''
        mes=Stlbc.normalise(mes,key)
        n=(len(mes)-1)//key+1
        mas=Stlbc.spisok(mes,key,n)
        for i in range(n):
            for j in range(key):
                res+=mas[j][i]
        return res
    @staticmethod
    def decrypt(c, key):
        '''Функция дешифрует шифром простой перестановки '''
        n=(len(c)-1)//key+1
        res=Stlbc.crypt(c,n)
        res2=''
        for i in res:
            if i=='*':
                break
            res2+=i
        return res2
    

class Stlbc_key:
    @staticmethod
    def config(M, key):
        '''Функция формирует строки в сообщении'''
        T=[]
        i=0
        while(i<(((len(M))//key))):
            T.append(M[i*key:(i*key+key)])
            i=i+1
        return T
    @staticmethod
    def modific(M, key):
        '''Функция дополняет строку'''
        M=M.lower()
        if(len(M)%key!=0):
            M+='*'*(key-(len(M)%key))
        return M
    @staticmethod
    def crypt(M, key,num):
        '''Функция шифрования'''
        M=Stlbc_key.modific(M,key)
        T=Stlbc_key.config(M, key) 
        res=''
        for i in range(key):
            for j in range(len(M)//key):
                res+=T[j][num[i]]
        return res
    @staticmethod
    def decrypt(M, key, num):
        '''Функция дешифрования'''
        M=Stlbc_key.modific(Stlbc_key.crypt(M,key,num),key)
        T=Stlbc_key.config(M,key)
        res=''
        for i in range(len(M)//key):
            for j in range(key):
                res+=T[i][j]
        return res

class Stlbc_kod_word:
    @staticmethod
    def modif (k):
        '''Функция преобразует кодовое слово в необходимый ключ'''
        alf='абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
        key=''
        key_last=[]
        k=k.lower()
        for i in k:
            if i not in key:
                key+=i
        for i in key:
            if i in alf:
                key_last.append(alf.index(i))
        return key_last
    @staticmethod
    def modific(M, key):
        '''Функция дополняет строку'''
        M=M.lower()
        if(len(M)%key!=0):
            M+='*'*(key-(len(M)%key))
        return M
    @staticmethod
    def normalkey(key):
        '''Функция нормализует ключ для возможности дешифровки'''
        m = len(key)
        for i in range(m):
            key[key.index(min(key))]=i+34
        for i in range(m):
            key[i]-=34
        return key
    @staticmethod
    def crypt(M, key):
        '''Функция шифрует простым перестановочным шифром с ключевым словом'''
        res=''
        key=Stlbc_kod_word.modif(key)
        l=len(key)
        M=Stlbc_kod_word.modific(M,l)
        for i in range(34):
            if i in key:
                res+=M[key.index(i)::l]
        return res
    @staticmethod
    def decrypt(c, key):
        '''Функция дешифрует '''
        res=''
        key=Stlbc_kod_word.modif(key)
        key=Stlbc_kod_word.normalkey(key)
        for i in range(len(c)//len(key)):
            for j in key:
                res+=c[(len(c)//len(key))*j+i]
        res2=''
        for i in res:
            if i=='*':
                break
            res2+=i
        return res2

class Vijener:
    @staticmethod
    def newkey(st,key):
        res=''
        for i in range(len(st)):
            res+=key[i%len(key)]
        return res
    @staticmethod
    def normalize(st):
        abc='абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        res=''
        st=st.lower()
        for i in st:
            if i in abc:
                res+=i
        return res
    @staticmethod
    def vij(st,key):
        abc='абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        st=Vijener.normalize(st)
        key=Vijener.newkey(st,key)
        res=''
        for i in range(len(st)):
            res+=abc[(abc.find(st[i])+abc.find(key[i]))%len(abc)]
        return res
    @staticmethod
    def devij(st,key):
        abc='абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        key=Vijener.newkey(st,key)
        res=''
        for i in range(len(st)):
            res+=abc[(abc.find(st[i])-abc.find(key[i])+len(abc))%len(abc)]
        return res

from random import *
class Odnor_bloknot:
    @staticmethod
    def funx(way1, way2, num):
        '''Функция создаёт или открывает и заполняет блокноты'''
        alf = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя ,.!?=()"-;:*0123456789'
        file1 = open(way1, "w")
        file2 = open(way2, "w")
        string = ''
        for i in range(num):
            string += choice(alf)
        file1.write(string)
        file2.write(string)
        file1.close()
        file2.close()
    @staticmethod
    def normalize(string):
        '''Функция нормализации строки'''
        alf = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя ,.!?=()"-;:*0123456789'
        string = string.lower()
        rez = ""
        for i in string:
            if i in alf:
                rez += i
        return rez
    @staticmethod
    def Keyget(M, way):
        '''Функция получения ключа'''
        file = open(way, "r")
        rez = file.read()
        rezult = rez[:len(M)]
        file.close()
        file = open(way, "w")
        file.write(rez[len(M):])
        return rezult
    @staticmethod
    def crypt(M, way1, way2, n):
        '''Функция шифрования'''
        alf = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя ,.!?=()"-;:*0123456789'
        Odnor_bloknot.funx(way1, way2, n)
        M=Odnor_bloknot.normalize(M)
        K=Odnor_bloknot.Keyget(M,way1)
        if len(M) == len(K):
            rez = ""
            for i in range(len(M)):
                rez += alf[(alf.find(M[i]) + alf.find(K[i]) + len(alf)) % len(alf)]
            return rez
        return "ERROR!"
    @staticmethod
    def decrypt(M, way2):
        '''Функция дешифрования'''
        alf = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя ,.!?=()"-;:*0123456789'
        M=Odnor_bloknot.normalize(M)
        K=Odnor_bloknot.Keyget(M,way2)
        if len(M) == len(K):
            rez = ""
            for i in range(len(M)):
                rez += alf[(alf.find(M[i]) - alf.find(K[i]) + len(alf)) % len(alf)]
            return rez
        return "ERROR!"

class Kvadr_Polib:
    @staticmethod
    def newabc(k):
        abc='абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        k=k.lower()
        res=''
        for i in (k+abc):
            if i not in res:
                res+=i
        return res
    @staticmethod
    def param(word,p):
        abc = Kvadr_Polib.newabc(word)
        d ={}
        if p==1:
            for i in range(len(abc)):
                a = str(int(i//6))
                b = str(i%6)
                d[abc[i]] = str(a + b)
        if p==-1:
            for i in range(len(abc)):
                a = str(int(i//6))
                b = str(i%6)
                d[str(a+b)]=abc[i]
        return d
    @staticmethod
    def crypt1(st,k):
        st=st.lower()
        abc=Kvadr_Polib.newabc(k)
        res=''
        for i in range(len(st)):
            res+=abc[(abc.find(st[i]))+6]
        return res
    @staticmethod
    def decrypt1(st,k):
        abc=Kvadr_Polib.newabc(k)
        res=''
        for i in range(len(st)):
            res+=abc[(abc.find(st[i]))-6]
        return res
    @staticmethod
    def crypt2(st,k):
        st = st.lower()
        abc=Kvadr_Polib.newabc(k)
        d1=Kvadr_Polib.param(abc,1)
        d2=Kvadr_Polib.param(abc,-1)
        res = ''
        strk=''
        for i in st:
            res+=d1[i]
        for i in range(0,(int(len(res))),2):
            strk+=str(res[i])
        for i in range(1,(int(len(res))),2):
            strk+=str(res[i])
        res= ''
        for i in range(0,len(strk),2):
            if (strk[i]+strk[i+1]) in d2:
                res+=d2[(strk[i]+strk[i+1])]
        return res
    @staticmethod
    def decrypt2(st,k):
        abc=Kvadr_Polib.newabc(k)
        res=''
        strk=''
        d=Kvadr_Polib.param(abc,1)
        for i in st:
            res +=d[i]
        a = (int(len(res)/2))
        for i in range(0,a):
            strk+= res[i] + res[i +a]
        res=''
        d=Kvadr_Polib.param(abc,-1)
        for i in range(0,len(strk),2):
            if (strk[i] +strk[i+1]) in d:
                res+=d[(strk[i] +strk[i+1])]
        return res
    @staticmethod
    def crypt3(st,k):
        st=st.lower()
        abc=Kvadr_Polib.newabc(k)
        res=''
        strk=''
        d1=Kvadr_Polib.param(abc,1)
        for i in st:
            res+=d1[i]
        d2=Kvadr_Polib.param(abc,-1)
        for i in range(1,len(res)):
            strk+=str(res[i])
        for i in range(len(strk)):
            if len(strk)%2!=0:
                strk=strk+res[i]
                break
        res=''
        for i in range(0,len(strk),2):
            res+=d2[strk[i]+strk[i+1]]
        return res
    @staticmethod
    def decrypt3(st,k):
        st=st.lower()
        abc=Kvadr_Polib.newabc(k)
        res=''
        strk=''
        d1=Kvadr_Polib.param(abc,1)
        for i in st:
            res+=d1[i]
        d2=Kvadr_Polib.param(abc,-1)
        a=res[len(res)-1]
        strk=a
        for i in range(len(res)-1):
            strk+=res[i]
        res=''
        for i in range(0,len(strk),2):
            res+=d2[strk[i]+strk[i+1]]
        return res
    @staticmethod
    def crypt4(st,k):
        st=st.lower()
        abc=Kvadr_Polib.newabc(k)
        res=''
        for i in range(len(st)):
            res+=abc[(abc.find(st[i]))+1]
        return res
    @staticmethod
    def decrypt4(st,k):
        abc=Kvadr_Polib.newabc(k)
        res=''
        for i in range(len(st)):
            res+=abc[(abc.find(st[i]))-1]
        return res
    @staticmethod
    def crypt5(st,k):
        st=st.lower()
        abc=Kvadr_Polib.newabc(k)
        res=''
        strk=''
        d1=Kvadr_Polib.param(abc,1)
        for i in st:
            res+=d1[i]
        d2=Kvadr_Polib.param(abc,-1)
        obr=res[::-1]
        strk+=obr[0]
        for i in range(len(res)-1):
            strk+=str(res[i])
        res=''
        for i in range(0,len(strk),2):
            res+=d2[strk[i]+strk[i+1]]
        return res
    @staticmethod
    def decrypt5(st,k):
        st=st.lower()
        abc=Kvadr_Polib.newabc(k)
        res=''
        strk=''
        d1=Kvadr_Polib.param(abc,1)
        for i in st:
            res+=d1[i]
        d2=Kvadr_Polib.param(abc,-1)
        for i in range(1,len(res)):
            strk+=str(res[i])
        for i in range(len(strk)):
            if len(strk)%2!=0:
                strk=strk+res[i]
                break
        res=''
        for i in range(0,len(strk),2):
            res+=d2[strk[i]+strk[i+1]]
        return res

class Pleyfer:
    @staticmethod
    def createcode(word):
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        word = word.lower()
        res = ''
        for i in (word + abc):
            if i not in res:
                res +=i
        return res
    @staticmethod
    def dict(word,param = 1):
        abc =Pleyfer.createcode(word)
        d ={}
        if param == 1:
            for i in range(len(abc)):
                a = str(int(i/6))
                b = str(i%6)
                d[abc[i]] = str(a + b)
        if param == -1:
            for i in range(len(abc)):
                a = str(int(i/6))
                b = str(i%6)
                d[str(a + b)] = abc[i]
        return d
    @staticmethod
    def crypt(st,word):
        st = st.lower()
        if len(st)%2 == 1:
            st = st +' '
        d1 =Pleyfer.dict(word,1)
        d2 =Pleyfer.dict(word,-1)
        res = ''
        for i in st:
            res +=d1[i]
        result = ''
        for i in range(0,len(res),4):
            if (res[i] == res[i+2]) and (res[i+1]!=res[i+3]):
                result += res[i] + str((int(res[i+1])+1)%6) + res[i+2] + str((int(res[i+3])+1)%6)
            elif (res[i] != res[i+2]) and (res[i+1]==res[i+3]):
                result += str((int(res[i])+1)%6)+res[i+1] + str((int(res[i+2])+1)%6) + res[i+3]
            elif (res[i] == res[i+2]) and (res[i+1]==res[i+3]):
                result += (str((int(res[i])+1)%6) + res[i+1])*2
            else:
                result += res[i] + res[i+3]+ res[i+2] + res[i+1]
        res = ''
        for i in range(0,len(result),2):
            res +=d2[result[i]+result[i+1]]
        return res
    @staticmethod
    def decrypt(st,word):
        d1 =Pleyfer.dict(word,1)
        d2 =Pleyfer.dict(word,-1)
        res = ''
        for i in st:
            res +=d1[i]
        result = ''
        for i in range(0,len(res),4):
            if (res[i] == res[i+2]) and (res[i+1]!=res[i+3]):
                result += res[i] + str((int(res[i+1])-1)%6) + res[i+2] + str((int(res[i+3])-1)%6)
            elif (res[i] != res[i+2]) and (res[i+1]==res[i+3]):
                result += str((int(res[i])-1)%6)+res[i+1] + str((int(res[i+2])- 1)%6) + res[i+3]
            elif (res[i] == res[i+2]) and (res[i+1]==res[i+3]):
                result += (str((int(res[i])-1)%6) + res[i+1])*2
            else:
                result += res[i] + res[i+3] + res[i+2] + res[i+1]
        res = ''
        for i in range(0,len(result),2):
            res +=d2[result[i]+result[i+1]]
        return res

class Dva_kvadrata:
    @staticmethod
    def createcode(word):
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        word = word.lower()
        res = ''
        for i in (word + abc):
            if i not in res:
                res +=i
        return res
    @staticmethod
    def dict(word,param = 1):
        abc = Dva_kvadrata.createcode(word)
        d ={}
        if param == 1:
            for i in range(len(abc)):
                a = str(int(i/6))
                b = str(i%6)
                d[abc[i]] = str(a + b)
        if param == -1:
            for i in range(len(abc)):
                a = str(int(i/6))
                b = str(i%6)
                d[str(a + b)] = abc[i]
        return d
    @staticmethod
    def crypt(st, word1, word2):
        st = st.lower()
        if len(st)%2 == 1:
            st = st +' '
        d1 = Dva_kvadrata.dict(word1,1)
        d2 =Dva_kvadrata.dict(word1,-1)
        d3 =Dva_kvadrata.dict(word2,1)
        d4 =Dva_kvadrata.dict(word2,-1)
        res = ''
        g=0
        for i in st:
            if((g+1)%2!=0):
                res +=d1[i]
            else:
                res +=d3[i]
            g+=1
        result = ''
        for i in range(0,len(res),4):
            if (res[i] == res[i+2]) and (res[i+1]!=res[i+3]):
                result += res[i] + res[i+3] + res[i+2] + res[i+1]
            elif (res[i] == res[i+2]) and (res[i+1]==res[i+3]):
                result += res[i] + str((int(res[i+1])+1)%6) + res[i+2] + str((int(res[i+3])+1)%6)
            else:
                result += res[i+2] + res[i+1]+ res[i] + res[i+3]
        res = ''
        for i in range(0,len(result),4):
            res +=d2[result[i]+result[i+1]]+d4[result[i+2]+result[i+3]]
        return res
    @staticmethod
    def decrypt(st,word1, word2):
        d1 =Dva_kvadrata.dict(word1,1)
        d2 =Dva_kvadrata.dict(word1,-1)
        d3 =Dva_kvadrata.dict(word2,1)
        d4 =Dva_kvadrata.dict(word2,-1)
        res = ''
        g=0
        for i in st:
            if((g+1)%2!=0):
                res +=d1[i]
            else:
                res +=d3[i]
            g+=1
        result = ''
        for i in range(0,len(res),4):
            if (res[i] == res[i+2]) and (res[i+1]!=res[i+3]):
                result += res[i] + res[i+3] + res[i+2] + res[i+1]
            elif (res[i] == res[i+2]) and (res[i+1]==res[i+3]):
                result += res[i] + str((int(res[i+1])+1)%6) + res[i+2] + str((int(res[i+3])+1)%6)
            else:
                result += res[i+2] + res[i+1]+ res[i] + res[i+3]
        res = ''
        for i in range(0,len(result),4):
            res +=d2[result[i]+result[i+1]]+d4[result[i+2]+result[i+3]]
        return res

class chetyre_kvadrata:
    @staticmethod
    def createcode(word):
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        word = word.lower()
        res = ''
        for i in (word + abc):
            if i not in res:
                res +=i
        return res
    @staticmethod
    def dict(word,param = 1):
        abc =chetyre_kvadrata.createcode(word)
        d ={}
        if param == 1:
            for i in range(len(abc)):
                a = str(int(i/6))
                b = str(i%6)
                d[abc[i]] = str(a + b)
        if param == -1:
            for i in range(len(abc)):
                a = str(int(i/6))
                b = str(i%6)
                d[str(a + b)] = abc[i]
        return d
    @staticmethod
    def crypt(st,word1, word2):
        st = st.lower()
        if len(st)%2 == 1:
            st = st +' '
        d1 =chetyre_kvadrata.dict(word1,1)
        d2 =chetyre_kvadrata.dict(word2,1)
        d3 =chetyre_kvadrata.dict('',-1)
        res = ''
        g=0
        for i in st:
            if((g+1)%2!=0):
                res +=d1[i]
            else:
                res +=d2[i]
            g+=1
        result = ''
        for i in range(0,len(res),4):
            result += res[i+2] + res[i+1] + res[i] + res[i+3]
        res = ''
        for i in range(0,len(result),2):
            res +=d3[result[i]+result[i+1]]
        return res
    @staticmethod
    def decrypt(st,word1, word2):
        d1 =chetyre_kvadrata.dict(word1,-1)
        d2 =chetyre_kvadrata.dict(word2,-1)
        d3 =chetyre_kvadrata.dict('',-1)
        d4 =chetyre_kvadrata.dict('',1)
        res = ''
        g=0
        for i in st:
            res +=d4[i]
        result = ''
        for i in range(0,len(res),4):
            result += res[i+2] + res[i+1] + res[i] + res[i+3]
        res = ''
        for i in range(0,len(result),4):
            res +=d1[result[i]+result[i+1]]+d2[result[i+2]+result[i+3]]
        return res

class shifr_Nigilistov:
    @staticmethod
    def normalize(st):
        abc = "abcdefghiklmnopqrstuvwxyz "
        res=''
        st=st.lower()
        for i in st:
            if i in abc:
                res+=i
        return res
    @staticmethod
    def createcode(word):
        '''Создание шифротаблицы'''
        abc = "abcdefghiklmnopqrstuvwxyz "
        word = shifr_Nigilistov.normalize(word)
        res = ''
        for i in (word + abc):
            if i not in res:
                res +=i
        return res
    @staticmethod
    def dict(word,param = 1):
        '''Создание словаря для шифровки и дешифровки'''
        abc =shifr_Nigilistov.createcode(word)
        d ={}
        if param == 1:
            for i in range(len(abc)):
                a = str(int(i/5))
                b = str(i%5)
                d[abc[i]] = str(a + b)
        if param == -1:
            for i in range(len(abc)):
                a = str(int(i/5))
                b = str(i%5)
                d[str(a + b)] = abc[i]
        return d
    @staticmethod
    def crypt(st, k2, word):
        '''Создание шифротекста'''
        st=shifr_Nigilistov.normalize(st)
        k2=shifr_Nigilistov.normalize(k2)
        d1 = shifr_Nigilistov.dict(word,1)
        if(len(st)!=len(k2)):
            if(len(st)>len(k2)):
                k=len(st)-len(k2)
                k2=k2+('z'*k)
            else:
                k=len(k2)-len(st)
                st=st+('z'*k)
        res = ''
        i=0
        j=0
        g=0
        while(i<(len(st)+len(k2))):
            if((i+1)%2!=0):
                res+=d1[st[j]]
                j+=1
            else:
                res+=d1[k2[g]]
                g+=1
            i+=1
        result = ''
        for i in range(0,len(res),4):
            result+=str(int(res[i])+int(res[i+2]))+str(int(res[i+1])+int(res[i+3]))
        return result
    @staticmethod
    def decrypt(st, k2, word):
        '''Дешифрование'''
        k2=shifr_Nigilistov.normalize(k2)
        d1 =shifr_Nigilistov.dict(word,1)
        d2 = shifr_Nigilistov.dict(word,-1)
        k2r=''
        i=0
        while (i<len(k2)):
            k2r+=d1[k2[i]]
            i+=1
        res = ''
        i=0
        while(i<len(st) and (i<len(k2r))):
            res+=str(int(st[i])-int(k2r[i]))
            i+=1
        result=''
        for i in range(0,len(res),2):
            result+=d2[res[i]+res[i+1]]
        return result

class shifr_ADFGVX_I:
    @staticmethod
    def normalize(st,abc):
        res=''
        st=st.lower()
        for i in st:
            if i in abc:
                res+=i
        return res
    @staticmethod
    def modif (k):
        '''Функция преобразует кодовое слово в необходимый ключ'''
        alf='abcdefghijklmnopqrstuvwxyz '
        key=''
        key_last=[]
        k=k.lower()
        for i in k:
            if i in alf:
                key+=i
        for i in key:
            if i in alf:
                key_last.append(alf.index(i))
        return key_last
    @staticmethod
    def modific(M, key):
        '''Функция дополняет строку'''
        if(len(M)%key!=0):
            M+='*'*(key-(len(M)%key))
        return M
    @staticmethod
    def normalkey(key):
        '''Функция нормализует ключ для возможности дешифровки'''
        m = len(key)
        for i in range(m):
            key[key.index(min(key))]=i+24
        for i in range(m):
            key[i]-=24
        return key
    @staticmethod
    def dict(abc,param = 1):
        '''Создание словаря для шифровки и дешифровки'''
        voc={
            '0': 'A',
            '1': 'D',
            '2': 'F',
            '3': 'G',
            '4': 'X'
            }
        d ={}
        if param == 1:
            for i in range(len(abc)):
                a = str(int(i/5))
                b = str(i%5)
                a = voc[a]
                b = voc[b]
                d[abc[i]] = str(a + b)
        if param == -1:
            for i in range(len(abc)):
                a = str(int(i/5))
                b = str(i%5)
                a = voc[a]
                b = voc[b]
                d[str(a + b)] = abc[i]
        return d
    @staticmethod
    def crypt(st,abc):
        '''Создание шифротекста'''
        st=shifr_ADFGVX_I.normalize(st,abc)
        d1 = shifr_ADFGVX_I.dict(abc,1)
        res=''
        for i in range(len(st)):
            res+=d1[st[i]]
        return res
    @staticmethod
    def decrypt(st1, abc):
        '''Дешифрование'''
        d1 =shifr_ADFGVX_I.dict(abc,1)
        d2 = shifr_ADFGVX_I.dict(abc,-1)
        res=''
        for i in range(0,len(st1),2):
            res+=d2[st1[i]+st1[i+1]]
        return res
    @staticmethod
    def crypt2(M, key):
        '''Функция шифрует простым перестановочным шифром с ключевым словом'''
        res=''
        key=shifr_ADFGVX_I.modif(key)
        l=len(key)
        M=shifr_ADFGVX_I.modific(M,l)
        key_last=[]
        i=0
        while(i<len(key)):
            if (key[i] not in key_last):
                key_last.append(key[i])
            else:
                key_last.append(key[i]+1)
            i+=1
        for i in range(24):
            if i in key_last:
                res+=M[key_last.index(i)::l]
        return res
    @staticmethod
    def decrypt2(c, key, abc):
        '''Функция дешифрует '''
        res=''
        key=shifr_ADFGVX_I.modif(key)
        key=shifr_ADFGVX_I.normalkey(key)
        for i in range(len(c)//len(key)):
            for j in key:
                res+=c[(len(c)//len(key))*j+i]
        res2=''
        for i in res:
            if i=='*':
                break
            res2+=i
        d1 =shifr_ADFGVX_I.dict(abc,1)
        d2 = shifr_ADFGVX_I.dict(abc,-1)
        res=''
        for i in range(0,len(res2),2):
            res+=d2[res2[i]+res2[i+1]]
        return res

class shifr_ADFGVX_II:
    @staticmethod
    def normalize(st,abc):
        res=''
        st=st.lower()
        for i in st:
            if i in abc:
                res+=i
        return res
    @staticmethod
    def modif (k):
        '''Функция преобразует кодовое слово в необходимый ключ'''
        alf='абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        key=''
        key_last=[]
        k=k.lower()
        for i in k:
            if i in alf:
                key+=i
        for i in key:
            if i in alf:
                key_last.append(alf.index(i))
        return key_last
    @staticmethod
    def modific(M, key):
        '''Функция дополняет строку'''
        if(len(M)%key!=0):
            M+='*'*(key-(len(M)%key))
        return M
    @staticmethod
    def normalkey(key):
        '''Функция нормализует ключ для возможности дешифровки'''
        m = len(key)
        for i in range(m):
            key[key.index(min(key))]=i+34
        for i in range(m):
            key[i]-=34
        return key
    @staticmethod
    def dict(abc,param = 1):
        '''Создание словаря для шифровки и дешифровки'''
        voc={
            '0': 'A',
            '1': 'D',
            '2': 'F',
            '3': 'G',
            '4': 'V',
            '5': 'X'
            }
        d ={}
        if param == 1:
            for i in range(len(abc)):
                a = str(int(i/6))
                b = str(i%6)
                a = voc[a]
                b = voc[b]
                d[abc[i]] = str(a + b)
        if param == -1:
            for i in range(len(abc)):
                a = str(int(i/6))
                b = str(i%6)
                a = voc[a]
                b = voc[b]
                d[str(a + b)] = abc[i]
        return d
    @staticmethod
    def crypt(st,abc):
        '''Создание шифротекста'''
        st=shifr_ADFGVX_II.normalize(st,abc)
        d1 = shifr_ADFGVX_II.dict(abc,1)
        res=''
        for i in range(len(st)):
            res+=d1[st[i]]
        return res
    @staticmethod
    def decrypt(st1, abc):
        '''Дешифрование'''
        d1 =shifr_ADFGVX_II.dict(abc,1)
        d2 = shifr_ADFGVX_II.dict(abc,-1)
        res=''
        for i in range(0,len(st1),2):
            res+=d2[st1[i]+st1[i+1]]
        return res
    @staticmethod
    def crypt2(M, key):
        '''Функция шифрует простым перестановочным шифром с ключевым словом'''
        res=''
        key=shifr_ADFGVX_II.modif(key)
        l=len(key)
        M=shifr_ADFGVX_II.modific(M,l)
        for i in range(34):
            if i in key:
                res+=M[key.index(i)::l]
        return res
    @staticmethod
    def decrypt2(c, key, abc):
        '''Функция дешифрует '''
        res=''
        key=shifr_ADFGVX_I.modif(key)
        key=shifr_ADFGVX_I.normalkey(key)
        for i in range(len(c)//len(key)):
            for j in key:
                res+=c[(len(c)//len(key))*j+i]
        res2=''
        for i in res:
            if i=='*':
                break
            res2+=i
        d1 =shifr_ADFGVX_I.dict(abc,1)
        d2 = shifr_ADFGVX_I.dict(abc,-1)
        res=''
        for i in range(0,len(res2),2):
            res+=d2[res2[i]+res2[i+1]]
        return res

import itertools
import random
random.seed(1)

class Becon:
    @staticmethod
    def normalize(st):
        '''Функция удаляет ненужные символы во входящей строке'''
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        newst = ''
        st = st.lower()
        for i in st:
            if i in abc:
                newst += i
        return newst
    @staticmethod
    def normalize2(st):
        '''Функция удаляет ненужные символы во входящей строке'''
        abc2 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        newst = ''
        st = st.lower()
        for i in st:
            if i in abc2:
                newst += i
        return newst
    @staticmethod
    def dvalf():
        '''Функция создает список кодированного алфавита'''
        dvalf=[]
        for i in itertools.product('01',repeat=5):
            k=''
            for j in range(5):
                k+=i[j]
            dvalf.append(k)
        for i in range(len(dvalf)):
            dvalf[i]=dvalf[i].replace('0','A')
            dvalf[i]=dvalf[i].replace('1','B')
        return dvalf
    @staticmethod
    def crypt1(m):
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        voc=Becon.dvalf()
        m=Becon.normalize(m)
        res=''
        for i in m:
            res += voc[abc.index(i)]
        return res
    @staticmethod
    def decrypt1(m):
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        voc=Becon.dvalf()
        res=''
        for i in range(len(m)//5):
            a=m[i*5:i*5+5]
            res += abc[voc.index(a)]
        return res
    @staticmethod
    def crypt2(m):
        st1 = 'В лесу родилась елочка, В лесу она росла, Зимой и летом стройная, Зеленая была. Метель ей пела песенку Спи, елочка, бай-бай. Мороз снежком укутывал Смотри не замерзай. Трусишка зайка серенький под елочкой скакал. Порою волк, сердитый волк Рысцою пробегал. Чу Снег по лесу частому Под полозом скрипит, Лошадка мохноногая Торопится бежит. Везет лошадка дровенки А в дровнях старичок Срубил он нашу елочку Под самый корешок. Теперь, она нарядная, На праздник к нам пришла, И много, много радости Детишкам принесла!'
        st1=Becon.normalize2(st1)
        m=Becon.normalize(m)
        m=Becon.crypt1(m)
        res=st1
        res=list(res)
        y=0
        for i in range(len(m)):
            if res[i+y]==' ':
                y +=1
            if m[i]=='B':
                res[i+y]=res[i+y].upper()
        res=''.join(res)
        res=res[0:len(m)+y]
        return res
    @staticmethod
    def decrypt2(m):
        voc=Becon.dvalf()
        res=''
        m=list(m)
        for i in range(len(m)):
            if m[i]== ' ':
                continue
            if m[i].isupper() == True:
                res+='B'
            else:
                res+='A'
        res=Becon.decrypt1(res)
        return res
    @staticmethod
    def crypt3(m):
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        voc=Becon.dvalf()
        m=Becon.normalize(m)
        m=Becon.crypt1(m)
        res=''
        for i in range(len(m)):
            if m[i]=='A':
                res+=random.choice(abc[0:16])
            else:
                res+=random.choice(abc[16:])
        return res
    @staticmethod
    def decrypt3(m):
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        res=''
        for i in range(len(m)):
            if abc.index(m[i]) < 16:
                res+='A'
            else:
                res+='B'
        res=Becon.decrypt1(res)
        return res
    @staticmethod
    def crypt4(m):
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        voc=Becon.dvalf()
        m=Becon.normalize(m)
        m=Becon.crypt1(m)
        res=''
        for i in range(len(m)):
            if m[i]=='A':
                res+=random.choice(abc[1::2])
            else:
                res+=random.choice(abc[::2])
        return res
    @staticmethod
    def decrypt4(m):
        abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !,.?'
        res=''
        for i in range(len(m)):
            if abc.index(m[i]) %2==1:
                res+='A'
            else:
                res+='B'
        res=Becon.decrypt1(res)
        return res

print('1-шифр Цезаря')
print('2-шифр Атбаш')
print('3-шифр замены с выбранным алфавитом')
print('4-шифр замены с кодовым словом')
print('5-шифр Скитала')
print('6-шифр столбцовый перестановочный')
print('7-шифр столбцовый перестановочный с ключом')
print('8-шифр столбцовый перестановочный с кодовым словом')
print('9-шифр Виженера')
print('10-шифр Одноразовый блокнот')
print('11-Квадрат Полибия')
print('a-1 способ')
print('b-2 способ')
print('c-3 способ')
print('d-4 способ')
print('e-5 способ')
print('12-шифр Плейфера')
print('13-шифр Двух квадратов')
print('14-шифр Четырёх квадратов')
print('15-шифр Нигилистов')
print('16-шифр ADFGVX_I')
print('a-1 способ')
print('b-2 способ')
print('17-шифр ADFGVX_II')
print('a-1 способ')
print('b-2 способ')
print('18-шифр Бэкона')
print('a-1 способ')
print('b-2 способ')
print('c-3 способ')
print('d-4 способ')

n=int(input('Введите номер: '))
if(n==1):
    m=str(input('Введите сообщение: '))
    k=int(input('Введите ключ: '))
    print('Шифрование: ', Ceasar.crypt(m,k))
    d=str(input('Дешифруемое сообщение: '))
    print('Дешифрование: ', Ceasar.decrypt(d,k))
elif(n==2):
    m=str(input('Введите сообщение: '))
    print('Шифрование: ', Atbash.crypt(m))
    d=str(input('Дешифруемое сообщение: '))
    print('Дешифрование: ', Atbash.decrypt(d))
elif(n==3):
    m=str(input('Введите сообщение: '))
    zam_alf=str(input('Введите выбранный алфавит: '))
    print('Шифрование: ', Zam_vybor_alf.encrypt(m,zam_alf))
    d=str(input('Дешифруемое сообщение: '))
    print('Дешифрование: ', Zam_vybor_alf.decrypt(d,zam_alf))
elif(n==4):
    m=str(input('Введите сообщение: '))
    key=str(input('Введите кодовое слово: '))
    print('Шифрование: ', Zam_kod_word.codeword(m,key))
    d=str(input('Дешифруемое сообщение: '))
    print('Дешифрование: ', Zam_kod_word.decodeword(d,key))
elif(n==5):
    m=str(input('Введите сообщение: '))
    key=int(input('Введите ключ: '))
    print('Шифрование: ', Ckytala.cryptSkitala(m,key))
    d=str(input('Дешифруемое сообщение: '))
    print('Дешифрование: ', Ckytala.decryptSkitala(d,key))
elif(n==6):
    m=str(input('Введите сообщение: '))
    key=int(input('Введите ключ: '))
    print('Шифрование: ', Stlbc.crypt(m,key))
    d=str(input('Дешифруемое сообщение: '))
    print('Дешифрование: ', Stlbc.decrypt(d,key))
elif(n==7):
    m=str(input('Введите сообщение: '))
    key=int(input('Введите ключ: '))
    num=[]
    print("Введите ключевую комбинацию от 0 до ", key-1)
    for i in range(key):
        num.append(int(input()))
    print('Шифрование: ', Stlbc_key.crypt(m,key,num))
    с=str(input('Дешифруемое сообщение: '))
    print('Дешифрование: ', Stlbc_key.decrypt(m,key,num))
elif(n==8):
    m=str(input('Введите сообщение: '))
    key=str(input('Введите ключ: '))
    print('Шифрование: ', Stlbc_kod_word.crypt(m,key))
    d=str(input('Дешифруемое сообщение: '))
    print('Дешифрование: ', Stlbc_kod_word.decrypt(d,key))
elif(n==9):
    m=str(input('Введите сообщение: '))
    key=str(input('Введите ключ: '))
    print('Шифрование: ', Vijener.vij(m,key))
    d=str(input('Дешифруемое сообщение: '))
    print('Дешифрование: ', Vijener.devij(d,key))
elif(n==10):
    m=str(input('Введите сообщение: '))
    way1=str(input('Введите первый блокнот: '))
    way2=str(input('Введите второй блокнот: '))
    n=int(input('Введите количество символов: '))
    print('Шифрование: ', Odnor_bloknot.crypt(m,way1,way2,n))
    d=str(input('Дешифруемое сообщение: '))
    print('Дешифрование: ', Odnor_bloknot.decrypt(d,way2)) 
elif(n==11):
    s=str(input('Введите вариант: '))
    if(s=='a'):
        m=str(input('Введите сообщение: '))
        key=str(input('Введите ключ: '))
        print('Шифрование: ', Kvadr_Polib.crypt1(m,key))
        d=str(input('Дешифруемое сообщение: '))
        print('Дешифрование: ', Kvadr_Polib.decrypt1(d,key))
    if(s=='b'):
        m=str(input('Введите сообщение: '))
        key=str(input('Введите ключ: '))
        print('Шифрование: ', Kvadr_Polib.crypt2(m,key))
        d=str(input('Дешифруемое сообщение: '))
        print('Дешифрование: ', Kvadr_Polib.decrypt2(d,key))
    if(s=='c'):
        m=str(input('Введите сообщение: '))
        key=str(input('Введите ключ: '))
        print('Шифрование: ', Kvadr_Polib.crypt3(m,key))
        d=str(input('Дешифруемое сообщение: '))
        print('Дешифрование: ', Kvadr_Polib.decrypt3(d,key))
    if(s=='d'):
        m=str(input('Введите сообщение: '))
        key=str(input('Введите ключ: '))
        print('Шифрование: ', Kvadr_Polib.crypt4(m,key))
        d=str(input('Дешифруемое сообщение: '))
        print('Дешифрование: ', Kvadr_Polib.decrypt4(d,key))
    if(s=='e'):
        m=str(input('Введите сообщение: '))
        key=str(input('Введите ключ: '))
        print('Шифрование: ', Kvadr_Polib.crypt5(m,key))
        d=str(input('Дешифруемое сообщение: '))
        print('Дешифрование: ', Kvadr_Polib.decrypt5(d,key))
elif(n==12):
    m=str(input('Введите сообщение: '))
    key=str(input('Введите ключ: '))
    print('Шифрование: ', Pleyfer.crypt(m,key))
    d=str(input('Дешифруемое сообщение: '))
    print('Дешифрование: ', Pleyfer.decrypt(d,key))
elif(n==13):
    m=str(input('Введите сообщение: '))
    key1=str(input('Введите ключ: '))
    key2=str(input('Введите ключ: '))
    print('Шифрование: ', Dva_kvadrata.crypt(m,key1,key2))
    d=str(input('Дешифруемое сообщение: '))
    print('Дешифрование: ', Dva_kvadrata.decrypt(d,key1,key2))
elif(n==14):
    m=str(input('Введите сообщение: '))
    key1=str(input('Введите ключ: '))
    key2=str(input('Введите ключ: '))
    print('Шифрование: ', chetyre_kvadrata.crypt(m,key1,key2))
    d=str(input('Дешифруемое сообщение: '))
    print('Дешифрование: ', chetyre_kvadrata.decrypt(d,key1,key2))
elif(n==15):
    m=str(input('Введите сообщение: '))
    key1=str(input('Введите ключ: '))
    key2=str(input('Введите ключ: '))
    print('Шифрование: ', shifr_Nigilistov.crypt(m,key1,key2))
    d=str(input('Дешифруемое сообщение: '))
    print('Дешифрование: ', shifr_Nigilistov.decrypt(d,key1,key2))
elif(n==16):
    s=str(input('Введите вариант: '))
    abc=str(input('Введите случайный алфавит: '))
    if(s=='a'):
        m=str(input('Введите сообщение: '))
        print('Шифрование: ', shifr_ADFGVX_I.crypt(m,abc))
        d=str(input('Дешифруемое сообщение: '))
        print('Дешифрование: ', shifr_ADFGVX_I.decrypt(d,abc))
    if(s=='b'):
        m=str(input('Введите сообщение: '))
        key=str(input('Введите ключ: '))
        print('Шифрование: ', shifr_ADFGVX_I.crypt2(m,key))
        d=str(input('Дешифруемое сообщение: '))
        print('Дешифрование: ', shifr_ADFGVX.decrypt2(d,key,abc))
elif(n==17):
    s=str(input('Введите вариант: '))
    abc=str(input('Введите случайный алфавит: '))
    if(s=='a'):
        m=str(input('Введите сообщение: '))
        print('Шифрование: ', shifr_ADFGVX_II.crypt(m,abc))
        d=str(input('Дешифруемое сообщение: '))
        print('Дешифрование: ', shifr_ADFGVX_II.decrypt(d,abc))
    if(s=='b'):
        m=str(input('Введите сообщение: '))
        key=str(input('Введите ключ: '))
        print('Шифрование: ', shifr_ADFGVX_II.crypt2(m,key))
        d=str(input('Дешифруемое сообщение: '))
        print('Дешифрование: ', shifr_ADFGVX_II.decrypt2(d,key,abc))
elif(n==18):
    s=str(input('Введите вариант: '))
    if(s=='a'):
        m=str(input('Введите сообщение: '))
        print('Шифрование: ', Becon.crypt1(m))
        d=str(input('Дешифруемое сообщение: '))
        print('Дешифрование: ', Becon.decrypt1(d))
    if(s=='b'):
        m=str(input('Введите сообщение: '))
        print('Шифрование: ', Becon.crypt2(m))
        d=str(input('Дешифруемое сообщение: '))
        print('Дешифрование: ', Becon.decrypt2(d))
    if(s=='c'):
        m=str(input('Введите сообщение: '))
        print('Шифрование: ', Becon.crypt3(m))
        d=str(input('Дешифруемое сообщение: '))
        print('Дешифрование: ', Becon.decrypt3(d))
    if(s=='d'):
        m=str(input('Введите сообщение: '))
        print('Шифрование: ', Becon.crypt4(m))
        d=str(input('Дешифруемое сообщение: '))
        print('Дешифрование: ', Becon.decrypt4(d))
else:
    print('Ошибка')
    

    
