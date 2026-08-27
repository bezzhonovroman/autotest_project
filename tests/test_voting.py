import pytest

from main import Voting


class TestCreation:

    def test_has_no_votes(self, voting, options):
        assert voting.options == options, "Список вариантов не совпадает с переданным в конструктор"
        assert voting.results == {option: 0 for option in options}, (
            "У нового голосования счётчики должны быть нулевыми для всех вариантов"
        )
        assert voting.total_votes() == 0, "У нового голосования не должно быть голосов"

class TestVote:

    @pytest.mark.parametrize(
        "chosen_number, expected_option",
        [
            (1, "Да"),
            (2, "Нет"),
            (3, "Может быть"),
        ],
    )
    def test_vote_counts_chosen_option(self, voting, chosen_number, expected_option):
        voting.vote(chosen_number)

        assert voting.results[expected_option] == 1, (
            f"Голос за номер {chosen_number} должен быть засчитан варианту '{expected_option}'"
        )
        assert voting.total_votes() == 1, "После одного голоса общее число голосов должно быть 1"

    @pytest.mark.parametrize("chosen_number", [0, -1, 4, 100])
    def test_vote_with_number_out_of_range_raises_error(self, voting, chosen_number):
        with pytest.raises(ValueError):
            voting.vote(chosen_number)

        assert voting.total_votes() == 0, (
            f"Голос с некорректным номером {chosen_number} не должен увеличивать счётчик голосов"
        )

    def test_repeated_votes_are_summed(self, voted_voting):
        assert voted_voting.results == {"Да": 2, "Нет": 1, "Может быть": 0}, (
            "Повторные голоса за один и тот же вариант должны суммироваться"
        )
        assert voted_voting.total_votes() == 3, "Общее число голосов должно учитывать все отданные голоса"


class TestWinners:

    def test_no_winners_without_votes(self, voting):
        assert voting.get_winners() is None, "Без голосов get_winners() должен вернуть None"

    def test_single_winner(self, voted_voting):
        assert voted_voting.get_winners() == ["Да"], (
            "При явном лидере get_winners() должен вернуть список из одного варианта-победителя"
        )

    def test_tie_returns_all_leaders(self, voting):
        voting.vote(1)
        voting.vote(2)

        assert sorted(voting.get_winners()) == ["Да", "Нет"], (
            "При равном числе голосов get_winners() должен вернуть всех лидеров"
        )
