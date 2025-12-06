class Verb:
    def __init__(self, dictionary, group=2):
        self.dictionary = dictionary
        if dictionary == "する" or dictionary == "来る":
            self.group = 3
        else:
            self.group = group

    def polite(self, negative=False, past=False):
        possible = {
            (False, False): "ます",
            (False, True): "ました",
            (True, False): "ません",
            (True, True): "ませんでした"
        }
        return self.stem() + possible[(negative,past)]


    def plain(self, negative=False, past=False):
        if negative:
            stem = ""
            match self.group:
                case 1:
                    a_to_i = {
                        "る": "ら",
                        "う": "わ",
                        "く": "か",
                        "つ": "た",
                        "ぬ": "な",
                        "ぶ": "ば",
                        "む": "ま",
                        "ぐ": "が",
                        "す": "さ",
                    }
                    stem = self.dictionary[:-1] + a_to_i[self.dictionary[-1]]
                case 2:
                    stem = self.dictionary[:-1]
                case 3:
                    stem = self.stem()
            if past:
                return stem + "なかった"
            return stem + "ない"
        else:
            if past:
                return self.ta_form()
            return self.dictionary


    def stem(self):
        match self.group:
            case 1:
                a_to_i = {
                    "る": "り",
                    "う": "い",
                    "く": "き",
                    "つ": "ち",
                    "ぬ": "に",
                    "ぶ": "び",
                    "む": "み",
                    "ぐ": "ぎ",
                    "す": "し",
                }
                return self.dictionary[:-1] + a_to_i[self.dictionary[-1]]
            case 2:
                return self.dictionary[:-1]
            case 3:
                if self.dictionary == "する":
                    return "し"
                else:
                    return self.dictionary[:-1]
        return self.dictionary[:-1]

    def te_form(self):
        if self.dictionary == "行く":
            return self.dictionary[:-1] + "って"
        match self.group:
            case 1:
                end = ""
                match self.dictionary[-1]:
                    case "う"|"つ"|"る":
                        end = "って"
                    case "ぬ"|"ぶ"|"む":
                        end = "んで"
                    case "く":
                        end = "いて"
                    case "ぐ":
                        end = "いで"
                    case "す":
                        end = "して"
                return self.dictionary[:-1] + end
            case 2:
                return self.dictionary[:-1] + "て"
            case 3:
                if self.dictionary == "する":
                    return "して"
                else:
                    return self.dictionary[:-1] + "て"
        return self.dictionary[:-1] + "て"

    def ta_form(self):
        if self.te_form()[-1] == "て":
            return self.te_form()[:-1] + "た"
        elif self.te_form()[-1] == "で":
            return self.te_form()[:-1] + "だ"
        return self.dictionary[:-1] + "た"

print(Verb("起きる", 2).plain(True))