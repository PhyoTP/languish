class Verb:
    def __init__(self, dictionary, group=2, positive=True, present=True):
        self.dictionary = dictionary
        if dictionary == "する" or dictionary == "来る":
            self.group = 3
        else:
            self.group = group
        self.positive = positive
        self.present = present


    def polite(self):
        possible = {
            (True, True): "ます",
            (True, False): "ました",
            (False, True): "ません",
            (False, False): "ませんでした"
        }
        return self.stem() + possible[(self.positive,self.present)]


    def plain(self):
        if not self.positive:
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
            if not self.present:
                return stem + "なかった"
            return stem + "ない"
        else:
            if not self.present:
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
class Adjective:
    def __init__(self, dictionary, adj_type="na", positive=True, present=True):
        self.dictionary = dictionary
        self.adj_type = adj_type
        self.positive = positive
        self.present = present
    def plain(self):
        if self.positive:
            possible = {
                # i, present
                (True, True): self.dictionary,
                (True, False): self.dictionary[:-1] + "かった",
                (False, True): self.dictionary + "だ",
                (False, False): self.dictionary + "だった"
            }
            return possible[self.adj_type == "i", self.present]
        else:
            stem = ""
            if self.adj_type == "i":
                stem += self.dictionary[:-1] + "く"
            else:
                stem += self.dictionary + "では"
            if self.present:
                stem += "ない"
            else:
                stem += "なかった"
            return stem


    def polite(self):
        if self.positive:
            if self.present:
                return self.dictionary + "です"
            else:
                if self.adj_type == "i":
                    return self.dictionary[:-1] + "かったです"
                else:
                    return self.dictionary + "でした"
        else:
            stem = ""
            if self.adj_type == "i":
                stem += self.dictionary[:-1] + "く"
            else:
                stem += self.dictionary + "では"
            stem += "ありません"
            if not self.present:
                stem += "でした"
            return stem


print(Adjective("いろいろ", present=False).polite())