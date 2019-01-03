"""
Pikalang to BF translator
@author ymll
"""


class PikalangTranslator():
    def __init__(self):
        self.bf_2_pika_dictionary = {
            '+': 'pi',
            '-': 'ka',
            '[': 'pika',
            ']': 'chu',
            '>': 'pipi',
            '<': 'pichu',
            ',': 'pikapi',
            '.': 'pikachu'
        }
        self.pika_2_bf_dictionary = {v: k for k, v in self.bf_2_pika_dictionary.items()}

    def pika_2_bf(self, pika_code):
        out = ''
        try:
            for c in pika_code:
                out += self.pika_2_bf_dictionary[c]
        except KeyError as e:
            raise Exception('Not a pikachu!') from e
        return out

    def bf_2_pika(self, bf_code):
        out = ''
        for c in bf_code:
            try:
                out += self.bf_2_pika_dictionary[c] + ' '
            except KeyError as e:
                pass
        return out


if __name__ == '__main__':
    bf_code = '+++++++++++++++++++++++++[>++>+++>++++>+++++<<<<-]+++++++++++++++++++++++++>>+++++.>+++++.++.' \
              '----------.++.+++++.>--------..........<<<<++++++++.-----------------------.'
    t = PikalangTranslator()
    pika_code = t.bf_2_pika(bf_code)
    print(pika_code)
