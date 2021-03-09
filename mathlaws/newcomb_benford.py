"""

 A phenomenological law also called the first digit law, first digit phenomenon,
 or leading digit phenomenon. Benford's law states that in listings, tables of statistics,
  etc., the digit 1 tends to occur with probability ∼30%, much greater than the expected 11.1%
  (i.e., one digit out of 9). Benford's law can be observed, for instance, by examining tables
  of logarithms and noting that the first pages are much more worn and smudged than later pages
  (Newcomb 1881). While Benford's law unquestionably applies to many situations in the real world,
   a satisfactory explanation has been given only recently through the work of Hill (1998).

Benford's law was used by the character Charlie Eppes as an analogy to help solve a series
 of high burglaries in the Season 2 "The Running Man" episode (2006) of the television crime drama NUMB3RS.

 Source : https://mathworld.wolfram.com/BenfordsLaw.html

"""
import numpy as np

def benfords_law(first_digit):
    '''
    Benford's law, also called the Newcomb–Benford law,
    the law of anomalous numbers, or the first-digit law,
    is an observation about the frequency distribution of
    leading digits in many real-life sets of numerical data.
    The law states that in many naturally occurring collections
    of numbers, the leading digit is likely to be small.[1] In sets
    that obey the law, the number 1 appears as the leading significant
    digit about 30% of the time, while 9 appears as the leading significant
    digit less than 5% of the time. If the digits were distributed uniformly,
    they would each occur about 11.1% of the time.[2] Benford's law also makes
    predictions about the distribution of second digits, third digits, digit
    combinations, and so on.

    Source : https://mathworld.wolfram.com/BenfordsLaw.html

    :param first_digit: the digit to find the probability of predominance
    :return: probability of the input first digit

    '''
    if first_digit in range(1,10):
        fd_prob = np.log10(1 + 1/first_digit)
    else:
        raise Exception('First digit given out of range... should be within 1 and 9')
    return fd_prob
