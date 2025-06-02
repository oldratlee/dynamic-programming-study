from dp_study.idaa3e.ch8_2_ex2_9 import (longest_common_subsequence,
                                         longest_common_subsequence_length)


def test_longest_common_subsequence_length():
    assert longest_common_subsequence_length('abc', '') == 0
    assert longest_common_subsequence_length('', 'abc') == 0

    assert longest_common_subsequence_length('abc', 'b') == 1
    assert longest_common_subsequence_length('abc', 'bc') == 2
    assert longest_common_subsequence_length('abc', 'bcd') == 2


def test_longest_common_subsequence():
    assert longest_common_subsequence('abc', '') == []
    assert longest_common_subsequence('', 'abc') == []

    assert longest_common_subsequence('abc', 'b') == ['b']
    assert longest_common_subsequence('abc', 'bc') == list('bc')
    assert longest_common_subsequence('abc', 'bcd') == list('bc')
