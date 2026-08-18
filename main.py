class Voting:

    def __init__(self, options):
        if not options:
            raise ValueError("Набор вариантов не может быть пустым!")

        self.options = options
        self.results = {option: 0 for option in options}

    def show_options(self):
        print("\nВарианты ответа:")
        for i, option in enumerate(self.options, start=1):
            print(f"  {i}. {option}")

    def vote(self, chosen_number):
        if chosen_number < 1 or chosen_number > len(self.options):
            raise ValueError(f"Выбрать нужно от 1 до {len(self.options)}")

        chosen = self.options[chosen_number-1]
        self.results[chosen] += 1

    def get_winners(self):
        if self.total_votes() == 0:
            return None

        max_votes = max(self.results.values())
        winners = [key for key, value in self.results.items() if value == max_votes ]

        return winners

    def total_votes(self):
        return sum(self.results.values())

    def show_results(self):
        print("=" * 30)
        print("   ИТОГИ ГОЛОСОВАНИЯ")
        print("=" * 30)
        if self.total_votes() == 0:
            print("Голосов не было.")
            return

        for option, count in self.results.items():
            print(f"{option}: {count} голос(ов)")

        print(f"\nВсего голосов: {self.total_votes()}")

        winners = self.get_winners()
        if len(winners) == 1:
            print(f"Победитель: {winners[0]}")
        else:
            print(f"Ничья между: {', '.join(winners)}")


    def get_valid_choice(self):
        while True:
            input_value = input("\nВведите номер варианта (или 'стоп' для завершения): ").strip()

            if not input_value:
                print("Пустой ввод. Если хотите закончить, введите 'стоп'.")
                continue

            if input_value.lower() in ("стоп", "stop"):
                return None

            if not input_value.isdigit():
                print("Ошибка: нужно ввести число.")
                continue

            choice_number = int(input_value)

            if choice_number < 1 or choice_number > len(self.options):
                print(f"Ошибка: номер должен быть от 1 до {len(self.options)}.")
                continue

            return choice_number


def main():
    print("=" * 30)
    print("   ПРОГРАММА ГОЛОСОВАНИЯ")
    print("=" * 30)

    options = ["Да", "Нет", "Может быть"]
    voting = Voting(options)

    while True:
        voting.show_options()
        choice = voting.get_valid_choice()

        if choice is None:
            break

        voting.vote(choice)
        print(f"Голос за '{voting.options[choice - 1]}' принят.")

    voting.show_results()


if __name__ == "__main__":
    main()