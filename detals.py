import os

class cpicok:
    def _init_():
        pass

    def all_detals():
        f = open('detals.txt','r')
        with open('detals.txt') as file:
            while (line := file.readline().rstrip()):
                if message == line:
                    return True
                elif message in line:
                    detal.append(line)
                    count += 1
                if count >= 100:
                    break;
    def search(message,detal):
        count = 0
        res = 'Возможно вы имели ввиду:'
        f = open('detals.txt','r')
        with open('detals.txt') as file:
            while (line := file.readline().rstrip()):
                if message == line:
                    return True
                elif message in line:
                    detal.append(line)
                    count += 1
                if count >= 100:
                    break;
        if res == 'Возможно вы имели ввиду:':
            return 'Null'
        return res
    def writeBank(CopterCoin,user):
        pass

    def writeBank(user, CopterCoin):

        fшду = open('bank.txt','r')           # создаём
        os.system("touch %s" % TemporaryFile)    # временный файл
        result = 0 # счетчик измененных строк

        with open('bank.txt', 'r') as f1, open(TemporaryFile, 'w') as f2:
            lines = f1.readlines()

            for line in lines:
                line = line.strip()

                if user in line:
                    f2.write(user + " " + CopterCoin + "CopP"'\n') # меняем строку
                    result = result + 1 # инкрементирование счетчика измененных строк
                else:
                    f2.write(line + '\n') # оставляем прежнюю
            if reresult == 0:
                f2.write(user + " " + CopterCoin + "CopP"'\n')


        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), File)
        os.remove(path) # удаляем основной файл

        os.system("mv %s %s" % (TemporaryFile, File)) # переименовываем временный в основной

    def r():
        pass

