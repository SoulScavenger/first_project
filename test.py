class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt: bool) -> str:
        new_text = ''
        if is_encrypt:
            for char in text:
                if not char.isalpha():
                    new_text += char
                else:
                    char_index = CipherMaster.alphabet.index(
                        char.lower()) + shift
                    if char_index >= len(CipherMaster.alphabet):
                        char_index -= len(CipherMaster.alphabet)
                    new_text += CipherMaster.alphabet[char_index]
        else:
            for char in text:
                if not char.isalpha():
                    new_text += char
                else:
                    char_index = CipherMaster.alphabet.index(
                        char.lower()) - shift
                    if char_index >= len(CipherMaster.alphabet):
                        char_index -= len(CipherMaster.alphabet)
                    new_text += CipherMaster.alphabet[char_index]
        return new_text


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text=('Однажды ревьюер принял проект с первого раза,'
          'с тех пор я его боюсь'),
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))
