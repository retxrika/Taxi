class NumToStrWithRubs():
    def __init__(self, num):
        self.numStr = []
        self.num = self.num_to_str(num)

    def __str__(self):
        return self.num

    numsBeforeTwenty = [ "", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", 
                        "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", 
                        "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать" ]

    dozens = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", 
            "девяносто"]

    hundreds = [ "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот",
                "девятьсот"]

    def _parse_three_digit(self, num): 
        self._parse_two_digit(num)
        num //= 100
        self.numStr.append(self.hundreds[num % 10 - 1])

    def _parse_two_digit(self, num):
        if (num % 100 < 20):
            self.numStr.append(self.numsBeforeTwenty[num % 100])
        else:
            self.numStr.append(self.numsBeforeTwenty[num % 10])
            num //= 10
            self.numStr.append(self.dozens[num % 10 - 2])

    def _get_thousand_with_correct_end(self, lastTwoDigit):
        if lastTwoDigit > 20:
            lastTwoDigit %= 10

        if lastTwoDigit == 1:
            return "тысяча"
        elif lastTwoDigit >= 2 and lastTwoDigit <= 4:
            return "тысячи"
        else:
            return "тысяч"

    def _get_correct_case_ruble(self, lastTwoDigit):
        if lastTwoDigit > 20:
            lastTwoDigit %= 10

        if lastTwoDigit == 1:
            return "рубль"
        elif lastTwoDigit >= 2 and lastTwoDigit <= 4:
            return "рубля"
        else:
            return "рублей"

    def _change_case(self, num):
        for i in range(len(num)):
            if num[i] == "один":
                num[i] = "одна"
                break
            elif num[i] == "два":
                num[i] = "две"
                break

    def num_to_str(self, num): 
        isThousand = isChangeCase = False

        if (num >= 1000):
            isThousand = True
            if ((num // 1000 % 10 == 1 or num // 1000 % 10 == 2) 
                and num // 1000 % 100 != 11 
                and num // 1000 % 100 != 12):
                isChangeCase = True

        self.numStr.append(self._get_correct_case_ruble(num % 100))

        while(num > 0):
            # Добавление слова тысяча со своим окончанием.
            if isThousand and num < 1000:
                self.numStr.append(self._get_thousand_with_correct_end(num % 100))
                
            # Парсинг трехзначного числа.
            if (num % 1000 >= 100):
                self._parse_three_digit(num)
            # Парсинг одно-двузначного числа.
            else:
                self._parse_two_digit(num)
            
            num //= 1000
                
        self.numStr.reverse()

        # Замена при необходимости падежа у окончания тысячи.
        if isChangeCase:
            self._change_case(self.numStr)
        
        self.numStr = list(filter(None, self.numStr))
        return ' '.join(self.numStr).capitalize()