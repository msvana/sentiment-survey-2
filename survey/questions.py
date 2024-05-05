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
            "Pozvolna začíná svítat světlo na konci tunelu. Ostrava bude modernizovat budovu hlavního nádraží. Pokud to nakonec vyjde, bude to výborné.",
            "Pozvolna začíná svítat světlo na konci tunelu. Vláda se s opozicí nalezla společné řešení pro důchodovou reformu.  Pokud to nakonec vyjde, bude to výborné.",
            "Pozvolna začíná svítat světlo na konci tunelu. Lídři se domluvili na dočasném příměří. Pokud to nakonec vyjde, bude to výborné.",
        ]
    )
]
