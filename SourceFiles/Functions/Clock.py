from datetime import datetime

from num2words import num2words

from TimeMorph import *


class Clocks:
    @staticmethod
    def time(city: str = "") -> str:
        if city == "":
            now = datetime.now()
            hours, minutes = now.strftime("%H"), now.strftime("%M")
            response = num2words(str(hours), lang="ru") + " " + num2words(str(minutes), lang="ru")
            return "Сейчас " + response
        else:
            return "Не знаю, сам смотри"

    @staticmethod
    def clock_alarm(text: str = ""):
        response = Clocks().__alarm_clock(text)
        new_array = response.split(" ")
        new_text = ""
        for i in new_array:
            try:
                time_ = num2words(i, lang="ru")
                new_text += time_ + " "
            except:
                new_text += i + " "

        del new_array, response
        return new_text

    @staticmethod
    def __alarm_clock(text: str = ""):
        array = []
        if "пол" in text:
            text = text.replace("пол", "пол ")
        time_ = text.split(" ")
        for g in time_:
            if "пол" == g:
                number = (slovar.get(twelve_hours_nomn.get(time_[time_.index(g) + 1]))) - 1  # result два -> 2 -> 1
                if "вечера" in time_:
                    return includer(str(text2num_nomn_vechera[text2num_nomn[slovar[text2num.get(number)]]]) + ":30")

                if "утра" in time_:
                    return includer(str(number) + ":30")
            else:
                if "вечера" in time_:
                    return includer(str(twelve_hours2_digit[g]) + ":0")

                elif "утра" in time_:
                    return includer(str(twelve_hours_digit[g]) + ":0")
                else:
                    array.append(slovar.get(g))
        if len(array) == 3:
            if array[0] < array[1]:
                return includer(str(array[0]) + ":" + str(array[1] + array[2]))
            else:
                return includer(str(array[0] + array[1]) + ":" + str(array[2]))

        elif len(array) == 4:
            return includer(str(array[0] + array[1]) + ":" + str(array[2] + array[3]))
