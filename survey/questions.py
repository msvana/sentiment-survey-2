from dataclasses import dataclass
import random


@dataclass
class Question:
    base_text: str
    filled_texts: list[str]

    def get_empty(self):
        return self.base_text.replace('%s', '...')

    def get_random_filled(self):
        variant = random.randint(0, len(self.filled_texts) - 1)
        question = self.filled_texts[variant]
        return question, variant


QUESTIONS = [
    Question(
        "Navzdory skutečnosti, že odhadované ... není nejrůžovější, snažím se nepropadat skepsi.",
        [
            "Navzdory skutečnosti, že odhadované <strong>zpoždění vlaku pro můj spoj</strong> není nejrůžovější, snažím se nepropadat skepsi.",
            "Navzdory skutečnosti, že odhadovaný <strong>vývoj české ekonomiky</strong> není nejrůžovější, snažím se nepropadat skepsi.",
            "Navzdory skutečnosti, že odhadované <strong>datum dodání humanitární pomoci do válečné zóny</strong> není nejrůžovější, snažím se nepropadat skepsi.",
        ]
    ),
    Question(
        "Pokud jde o ... bylo dosaženo značného pokroku. Je však na místě být nadále ostražitý.",
        [
            "Pokud jde o <strong>jednání odborů dražní společnosti se zástupci vedení</strong>, bylo dosaženo značného pokroku. Je však na místě být nadále ostražitý.",
            "Pokud jde o <strong>redukci míry inflace</strong>, bylo dosaženo značného pokroku. Je však na místě být nadále ostražitý.",
            "Pokud jde o <strong>mírová jednání</strong>, bylo dosaženo značného pokroku. Je však na místě být nadále ostražitý.",
        ]
    ),
    Question(
        "Pozvolna začíná svítat světlo na konci tunelu. ...  Pokud to nakonec vyjde, bude to výborné.",
        [
            "Pozvolna začíná svítat světlo na konci tunelu. <strong>Ostrava bude modernizovat budovu hlavního nádraží.</strong> Pokud to nakonec vyjde, bude to výborné.",
            "Pozvolna začíná svítat světlo na konci tunelu. <strong>Vláda se s opozicí nalezla společné řešení pro důchodovou reformu.</strong>  Pokud to nakonec vyjde, bude to výborné.",
            "Pozvolna začíná svítat světlo na konci tunelu. <strong>Lídři se domluvili na dočasném příměří.</strong> Pokud to nakonec vyjde, bude to výborné.",
        ]
    ),
    Question(
        "... pohrozil, že pokud ... nepřistoupí na jejich požadavky, budou nuceni sáhnout k odpovídajícím prostředkům. Zdá se mi to, nebo opravdu stoupá nervozita? Uvidíme.",
        [
            "<strong>Šéf odborů</strong> pohrozil, že pokud <strong>vedení firmy</strong> nepřistoupí na jejich požadavky, budou nuceni sáhnout k odpovídajícím prostředkům. Zdá se mi to, nebo opravdu stoupá nervozita? Uvidíme.",
            "<strong>Předseda svazu odborových svazů</strong> pohrozil, že pokud <strong>ministr zemědělství</strong> nepřistoupí na jejich požadavky, budou nuceni sáhnout k odpovídajícím prostředkům. Zdá se mi to, nebo opravdu stoupá nervozita? Uvidíme.",
            "<strong>Prezident</strong> pohrozil, že pokud <strong>agresor vojenského konfliktu</strong> nepřistoupí na jejich požadavky, budou nuceni sáhnout k odpovídajícím prostředkům. Zdá se mi to, nebo opravdu stoupá nervozita? Uvidíme.",
        ]
    ),
    Question(
        "Tak, povedlo se to. ... Cítím mravenčení po celém těle.",
        [

            "Tak, povedlo se to. <strong>Do Ostravy budou jezdit rychlovlaky.</strong> Cítím mravenčení po celém těle.",
            "Tak, povedlo se to. <strong>Nová bezemisní technologie pohonu vozidel v praxi bude fungovat.</strong> Cítím mravenčení po celém těle.",
            "Tak, povedlo se to. <strong>Zástupci znepřátelených stran uzavřeli příměří</strong> Cítím mravenčení po celém těle.",
        ]
    ),
    Question(
        "O krůček zase blíže do propasti... Může mi někdo vysvětlit, jak se něco takového vůbec může stát?",
        [
            "O krůček zase blíže do propasti. <strong>železniční společnost zvýšila svůj dluh meziročně o dalších 30 %</strong>. Může mi někdo vysvětlit, jak se něco takového vůbec může stát?",
            "O krůček zase blíže do propasti. <strong>deficit státního rozpočtu se zvýšil meziročně o dalších 30 %</strong>. Může mi někdo vysvětlit, jak se něco takového vůbec může stát?",
            "O krůček zase blíže do propasti. <strong>zprávy z bojiště ukázaly stále rostoucí ztráty, a to až o 30 %</strong. Může mi někdo vysvětlit, jak se něco takového vůbec může stát?",
        ]
    ),
    Question(
        "Konečně! ... Pocit štěstí je neopisatelný!",
        [
            "Konečně! <strong>Naše město otevírá nový rekreační park.</strong> Pocit štěstí je neopisatelný!",
            "Konečně! <strong>Bylo oznámeno schválení nového balíčku ekonomických stimulů.</strong> Pocit štěstí je neopisatelný!",
            "Konečně! <strong>Osvojení nového mírového usnesení OSN.</strong> Pocit štěstí je neopisatelný!",
        ]
    ),
    Question(
        "Úplná katastrofa ... To je nepřijatelné!",
        [
            "Úplná katastrofa. <strong>Nové městské divadlo se zřítilo pouhý týden po otevření.</strong> To je nepřijatelné!",
            "Úplná katastrofa. <strong>Obrovský pád akciového trhu způsobil masivní finanční ztráty.</strong> To je nepřijatelné!",
            "Úplná katastrofa. <strong>Obrovský pád akciového trhu způsobil masivní finanční ztráty.</strong> To je nepřijatelné!",
        ]
    ),
    Question(
        "Docela dobrý. ... Vidět, že se věci hýbou.",
        [
            "Docela dobrý. <strong>Otevřeli novou knihovnu.</strong> Vidět, že se věci hýbou.",
            "Docela dobrý. <strong>Mírný růst HDP tento kvartál.</strong> Vidět, že se věci hýbou.",
            "Docela dobrý. <strong>Mírný růst HDP tento kvartál.</strong> Vidět, že se věci hýbou.",
        ]
    ),
    Question(
        "Trochu zklamání ... Měli to lépe promyslet.",
        [
            "Trochu zklamání. <strong>Nové kino má neustálé technické problémy.</strong> Měli to lépe promyslet.",
            "Trochu zklamání. <strong>Státní rozpočet vykazuje větší deficit, než se očekávalo.</strong> Měli to lépe promyslet.",
            "Trochu zklamání. <strong>Mírová jednání se zasekla na nečekaných požadavcích.</strong> Měli to lépe promyslet.",
        ]
    )
]
