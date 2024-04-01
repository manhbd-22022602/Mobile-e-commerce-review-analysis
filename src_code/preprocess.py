#preprocess.py
import regex as re
from underthesea import word_tokenize
import string
import codecs
from pyvi import ViTokenizer

# remove html tags
def remove_html(txt):
    return re.sub(r'<[^>]*>', '', txt)

# unicode stardard
uniChars = "àáảãạâầấẩẫậăằắẳẵặèéẻẽẹêềếểễệđìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵÀÁẢÃẠÂẦẤẨẪẬĂẰẮẲẴẶÈÉẺẼẸÊỀẾỂỄỆĐÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴÂĂĐÔƠƯ"
unsignChars = "aaaaaaaaaaaaaaaaaeeeeeeeeeeediiiiiooooooooooooooooouuuuuuuuuuuyyyyyAAAAAAAAAAAAAAAAAEEEEEEEEEEEDIIIOOOOOOOOOOOOOOOOOOOUUUUUUUUUUUYYYYYAADOOU"

def loaddicchar():
    dic = {}
    char1252 = 'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ'.split(
        '|')
    charutf8 = "à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ".split(
        '|')
    for i in range(len(char1252)):
        dic[char1252[i]] = charutf8[i]
    return dic
dicchar = loaddicchar()

def convert_unicode(txt):
    return re.sub(
        r'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ',
        lambda x: dicchar[x.group()], txt)

# diacritic standard
vowels_to_ids = {}
vowels_table = [
    ['a', 'à', 'á', 'ả', 'ã', 'ạ', 'a' ],
    ['ă', 'ằ', 'ắ', 'ẳ', 'ẵ', 'ặ', 'aw'],
    ['â', 'ầ', 'ấ', 'ẩ', 'ẫ', 'ậ', 'aa'],
    ['e', 'è', 'é', 'ẻ', 'ẽ', 'ẹ', 'e' ],
    ['ê', 'ề', 'ế', 'ể', 'ễ', 'ệ', 'ee'],
    ['i', 'ì', 'í', 'ỉ', 'ĩ', 'ị', 'i' ],
    ['o', 'ò', 'ó', 'ỏ', 'õ', 'ọ', 'o' ],
    ['ô', 'ồ', 'ố', 'ổ', 'ỗ', 'ộ', 'oo'],
    ['ơ', 'ờ', 'ớ', 'ở', 'ỡ', 'ợ', 'ow'],
    ['u', 'ù', 'ú', 'ủ', 'ũ', 'ụ', 'u' ],
    ['ư', 'ừ', 'ứ', 'ử', 'ữ', 'ự', 'uw'],
    ['y', 'ỳ', 'ý', 'ỷ', 'ỹ', 'ỵ', 'y' ]
]

for i in range(len(vowels_table)):
    for j in range(len(vowels_table[i]) - 1):
        vowels_to_ids[vowels_table[i][j]] = (i, j)

def is_valid_vietnamese_word(word):
    chars = list(word)
    vowel_indexes = -1
    for index, char in enumerate(chars):
        x, y = vowels_to_ids.get(char, (-1, -1))
        if x != -1:
            if vowel_indexes == -1: vowel_indexes = index
            else:
                if index - vowel_indexes != 1: return False
                vowel_indexes = index
    return True

def standardize_word_typing(word):
    if not is_valid_vietnamese_word(word): return word
    chars = list(word)
    dau_cau = 0
    vowel_indexes = []
    qu_or_gi = False

    for index, char in enumerate(chars):
        x, y = vowels_to_ids.get(char, (-1, -1))
        if x == -1: continue
        elif x == 9:  # check qu
            if index != 0 and chars[index - 1] == 'q':
                chars[index] = 'u'
                qu_or_gi = True
        elif x == 5:  # check gi
            if index != 0 and chars[index - 1] == 'g':
                chars[index] = 'i'
                qu_or_gi = True

        if y != 0:
            dau_cau = y
            chars[index] = vowels_table[x][0]

        if not qu_or_gi or index != 1:
            vowel_indexes.append(index)

    if len(vowel_indexes) < 2:
        if qu_or_gi:
            if len(chars) == 2:
                x, y = vowels_to_ids.get(chars[1])
                chars[1] = vowels_table[x][dau_cau]
            else:
                x, y = vowels_to_ids.get(chars[2], (-1, -1))
                if x != -1: chars[2] = vowels_table[x][dau_cau]
                else: chars[1] = vowels_table[5][dau_cau] if chars[1] == 'i' else vowels_table[9][dau_cau]
            return ''.join(chars)
        return word

    for index in vowel_indexes:
        x, y = vowels_to_ids[chars[index]]
        if x == 4 or x == 8:  # ê, ơ
            chars[index] = vowels_table[x][dau_cau]
            return ''.join(chars)

    if len(vowel_indexes) == 2:
        if vowel_indexes[-1] == len(chars) - 1:
            x, y = vowels_to_ids[chars[vowel_indexes[0]]]
            chars[vowel_indexes[0]] = vowels_table[x][dau_cau]
        else:
            x, y = vowels_to_ids[chars[vowel_indexes[1]]]
            chars[vowel_indexes[1]] = vowels_table[x][dau_cau]
    else:
        x, y = vowels_to_ids[chars[vowel_indexes[1]]]
        chars[vowel_indexes[1]] = vowels_table[x][dau_cau]
    return ''.join(chars)

def standardize_sentence_typing(text):
    words = text.lower().split()
    for index, word in enumerate(words):
        cw = re.sub(r'(^\p{P}*)([p{L}.]*\p{L}+)(\p{P}*$)', r'\1/\2/\3', word).split('/')
        if len(cw) == 3: cw[1] = standardize_word_typing(cw[1])
        words[index] = ''.join(cw)
    return ' '.join(words)

# remove unnecessary characters
def remove_unnecessary(text):
    text = re.sub(r'[^\s\wáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÉÈẺẼẸÊẾỀỂỄỆÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÍÌỈĨỊÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴĐ_]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip() # Remove extra whitespace
    return text

# special wordings in reviews (e.g., emoji,...)
def normalize_money(sent):
    return re.sub(r'[0-9]+[.,0-9][k-m-b]', 'giá', sent)

def normalize_hastag(sent):
    return re.sub(r'#+\w+', 'tag', sent)

def normalize_website(sent):
    result = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', 'website', sent)
    return re.sub(r'\w+(\.(com|vn|me))+((\/+([\.\w\_\-]+)?)+)?', 'website', result)

def nomalize_emoji(sent):
    emoji_pattern = re.compile("["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                u"\U00002702-\U000027B0"
                u"\U000024C2-\U0001F251"
                u"\U0001f926-\U0001f937"
                u'\U00010000-\U0010ffff'
                u"\u200d"
                u"\u2640-\u2642"
                u"\u2600-\u2B55"
                u"\u23cf"
                u"\u23e9"
                u"\u231a"
                u"\u3030"
                u"\ufe0f"
    "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', sent)

def normalize_elongate(sent):
    patern = r'(.)\1{1,}'
    result = sent
    while(re.search(patern, result) != None):
        repeat_char = re.search(patern, result)
        result = result.replace(repeat_char[0], repeat_char[1])
    return result

def remove_numbers(sent):
    return re.sub(r'[0-9]+', '', sent)

def normalize_acronyms(sent):
    text = sent
    replace_list = {
            "òa": "oà",
        "Òa": "Oà",
        "ÒA": "OÀ",
        "óa": "oá",
        "Óa": "Oá",
        "ÓA": "OÁ",
        "ỏa": "oả",
        "Ỏa": "Oả",
        "ỎA": "OẢ",
        "õa": "oã",
        "Õa": "Oã",
        "ÕA": "OÃ",
        "ọa": "oạ",
        "Ọa": "Oạ",
        "ỌA": "OẠ",
        "òe": "oè",
        "Òe": "Oè",
        "ÒE": "OÈ",
        "óe": "oé",
        "Óe": "Oé",
        "ÓE": "OÉ",
        "ỏe": "oẻ",
        "Ỏe": "Oẻ",
        "ỎE": "OẺ",
        "õe": "oẽ",
        "Õe": "Oẽ",
        "ÕE": "OẼ",
        "ọe": "oẹ",
        "Ọe": "Oẹ",
        "ỌE": "OẸ",
        "ùy": "uỳ",
        "Ùy": "Uỳ",
        "ÙY": "UỲ",
        "úy": "uý",
        "Úy": "Uý",
        "ÚY": "UÝ",
        "ủy": "uỷ",
        "Ủy": "Uỷ",
        "ỦY": "UỶ",
        "ũy": "uỹ",
        "Ũy": "Uỹ",
        "ŨY": "UỸ",
        "ụy": "uỵ",
        "Ụy": "Uỵ",
        "ỤY": "UỴ",
        'ả': 'ả', 'ố': 'ố', 'u´': 'ố','ỗ': 'ỗ', 'ồ': 'ồ', 'ổ': 'ổ', 'ấ': 'ấ', 'ẫ': 'ẫ', 'ẩ': 'ẩ',
        'ầ': 'ầ', 'ỏ': 'ỏ', 'ề': 'ề','ễ': 'ễ', 'ắ': 'ắ', 'ủ': 'ủ', 'ế': 'ế', 'ở': 'ở', 'ỉ': 'ỉ',
        'ẻ': 'ẻ', 'àk': u' à ','aˋ': 'à', 'iˋ': 'ì', 'ă´': 'ắ','ử': 'ử', 'e˜': 'ẽ', 'y˜': 'ỹ', 'a´': 'á',
            #Quy các icon về 2 loại emoj: Tích cực hoặc tiêu cực
            "👹": "Tiêu cực", "👻": "Tích cực", "💃": "Tích cực",'🤙': ' Tích cực ', '👍': ' Tích cực ',
            "💄": "Tích cực", "💎": "Tích cực", "💩": "Tích cực","😕": "Tiêu cực", "😱": "Tiêu cực", "😸": "Tích cực",
            "😾": "Tiêu cực", "🚫": "Tiêu cực",  "🤬": "Tiêu cực","🧚": "Tích cực", "🧡": "Tích cực",'🐶':' Tích cực ',
            '👎': ' Tiêu cực ', '😣': ' Tiêu cực ','✨': ' Tích cực ', '❣': ' Tích cực ','☀': ' Tích cực ',
            '♥': ' Tích cực ', '🤩': ' Tích cực ', 'like': ' Tích cực ', '💌': ' Tích cực ',
            '🤣': ' Tích cực ', '🖤': ' Tích cực ', '🤤': ' Tích cực ', ':(': ' Tiêu cực ', '😢': ' Tiêu cực ',
            '❤': ' Tích cực ', '😍': ' Tích cực ', '😘': ' Tích cực ', '😪': ' Tiêu cực ', '😊': ' Tích cực ',
            '?': ' ? ', '😁': ' Tích cực ', '💖': ' Tích cực ', '😟': ' Tiêu cực ', '😭': ' Tiêu cực ',
            '💯': ' Tích cực ', '💗': ' Tích cực ', '♡': ' Tích cực ', '💜': ' Tích cực ', '🤗': ' Tích cực ',
            '^^': ' Tích cực ', '😨': ' Tiêu cực ', '☺': ' Tích cực ', '💋': ' Tích cực ', '👌': ' Tích cực ',
            '😖': ' Tiêu cực ', '😀': ' Tích cực ', ':((': ' Tiêu cực ', '😡': ' Tiêu cực ', '😠': ' Tiêu cực ',
            '😒': ' Tiêu cực ', '🙂': ' Tích cực ', '😏': ' Tiêu cực ', '😝': ' Tích cực ', '😄': ' Tích cực ',
            '😙': ' Tích cực ', '😤': ' Tiêu cực ', '😎': ' Tích cực ', '😆': ' Tích cực ', '💚': ' Tích cực ',
            '✌': ' Tích cực ', '💕': ' Tích cực ', '😞': ' Tiêu cực ', '😓': ' Tiêu cực ', '️🆗️': ' Tích cực ',
            '😉': ' Tích cực ', '😂': ' Tích cực ', ':v': '  Tích cực ', '=))': '  Tích cực ', '😋': ' Tích cực ',
            '💓': ' Tích cực ', '😐': ' Tiêu cực ', ':3': ' Tích cực ', '😫': ' Tiêu cực ', '😥': ' Tiêu cực ',
            '😃': ' Tích cực ', '😬': ' 😬 ', '😌': ' 😌 ', '💛': ' Tích cực ', '🤝': ' Tích cực ', '🎈': ' Tích cực ',
            '😗': ' Tích cực ', '🤔': ' Tiêu cực ', '😑': ' Tiêu cực ', '🔥': ' Tiêu cực ', '🙏': ' Tiêu cực ',
            '🆗': ' Tích cực ', '😻': ' Tích cực ', '💙': ' Tích cực ', '💟': ' Tích cực ',
            '😚': ' Tích cực ', '❌': ' Tiêu cực ', '👏': ' Tích cực ', ';)': ' Tích cực ', '<3': ' Tích cực ',
            '🌝': ' Tích cực ',  '🌷': ' Tích cực ', '🌸': ' Tích cực ', '🌺': ' Tích cực ',
            '🌼': ' Tích cực ', '🍓': ' Tích cực ', '🐅': ' Tích cực ', '🐾': ' Tích cực ', '👉': ' Tích cực ',
            '💐': ' Tích cực ', '💞': ' Tích cực ', '💥': ' Tích cực ', '💪': ' Tích cực ',
            '💰': ' Tích cực ',  '😇': ' Tích cực ', '😛': ' Tích cực ', '😜': ' Tích cực ',
            '🙃': ' Tích cực ', '🤑': ' Tích cực ', '🤪': ' Tích cực ','☹': ' Tiêu cực ',  '💀': ' Tiêu cực ',
            '😔': ' Tiêu cực ', '😧': ' Tiêu cực ', '😩': ' Tiêu cực ', '😰': ' Tiêu cực ', '😳': ' Tiêu cực ',
            '😵': ' Tiêu cực ', '😶': ' Tiêu cực ', '🙁': ' Tiêu cực ',
            #Chuẩn hóa 1 số sentiment words/English words
            ':))': '  Tích cực ', ':)': ' Tích cực ', 'ô kêi': ' ok ', 'okie': ' ok ', ' o kê ': ' ok ',
            'okey': ' ok ', 'ôkê': ' ok ', 'oki': ' ok ', ' oke ':  ' ok ',' okay':' ok ','okê':' ok ',
            ' tks ': u' cám ơn ', 'thks': u' cám ơn ', 'thanks': u' cám ơn ', 'ths': u' cám ơn ', 'thank': u' cám ơn ',
            '⭐': 'star ', '*': 'star ', '🌟': 'star ', '🎉': u' Tích cực ',
            'kg ': u' không ','not': u' không ', u' kg ': u' không ', '"k ': u' không ',' kh ':u' không ','kô':u' không ','hok':u' không ',' kp ': u' không phải ',u' kô ': u' không ', '"ko ': u' không ', u' ko ': u' không ', u' k ': u' không ', 'khong': u' không ', u' hok ': u' không ',
            'he he': ' Tích cực ','hehe': ' Tích cực ','hihi': ' Tích cực ', 'haha': ' Tích cực ', 'hjhj': ' Tích cực ',
            ' lol ': ' Tiêu cực ',' cc ': ' Tiêu cực ','cute': u' dễ thương ','huhu': ' Tiêu cực ', ' vs ': u' với ', 'wa': ' quá ', 'wá': u' quá', 'j': u' gì ', '“': ' ',
            ' sz ': u' cỡ ', 'size': u' cỡ ', u' đx ': u' được ', 'dk': u' được  ', 'dc': u' được ', 'đk': u' được ',
            'đc': u' được ','authentic': u' chuẩn chính hãng ',u' aut ': u' chuẩn chính hãng ', u' auth ': u' chuẩn chính hãng ', 'thick': u' Tích cực ', 'store': u' cửa hàng ',
            'shop': u' cửa hàng ', 'sp': u' sản phẩm ', 'gud': u' tốt ','god': u' tốt ','wel done':' tốt ', 'good': u' tốt ', 'gút': u' tốt ',
            'sấu': u' xấu ','gut': u' tốt ', u' tot ': u' tốt ', u' nice ': u' tốt ', 'perfect': 'rất tốt', 'bt': u' bình thường ',
            'time': u' thời gian ', 'qá': u' quá ', u' ship ': u' giao hàng ', u' m ': u' mình ', u' mik ': u' mình ',
            'ể': 'ể', 'product': 'sản phẩm', 'quality': 'chất lượng','chat':' chất ', 'excelent': 'hoàn hảo', 'bad': 'tệ','fresh': ' tươi ','sad': ' tệ ',
            'date': u' hạn sử dụng ', 'hsd': u' hạn sử dụng ','quickly': u' nhanh ', 'quick': u' nhanh ','fast': u' nhanh ','delivery': u' giao hàng ',u' síp ': u' giao hàng ',
            'beautiful': u' đẹp tuyệt vời ', u' tl ': u' trả lời ', u' r ': u' rồi ', u' shopE ': u' cửa hàng ',u' order ': u' đặt hàng ',
            'chất lg': u' chất lượng ',u' sd ': u' sử dụng ',u' dt ': u' điện thoại ',u' nt ': u' nhắn tin ',u' tl ': u' trả lời ',u' sài ': u' xài ',u'bjo':u' bao giờ ',
            'thik': u' thích ',u' sop ': u' cửa hàng ', ' fb ': ' facebook ', ' face ': ' facebook ', ' very ': u' rất ',u'quả ng ':u' quảng  ',
            'dep': u' đẹp ',u' xau ': u' xấu ','delicious': u' ngon ', u'hàg': u' hàng ', u'qủa': u' quả ',
            'iu': u' yêu ','fake': u' giả mạo ', 'trl': 'trả lời', '><': u' Tích cực ', 'nv' : 'nhân viên', 'nvien' : 'nhân viên',
            ' por ': u' tệ ',' poor ': u' tệ ', 'ib':u' nhắn tin ', 'rep':u' trả lời ',u'fback':' feedback ','fedback':' feedback ', 'pùn' : 'buồn', 'tuỵt vời' : 'tuyệt vời',
            #dưới 3* quy về 1*, trên 3* quy về 5*
            '6 sao': ' 5star ','6 star': ' 5star ', '5star': ' 5star ','5 sao': ' 5star ','5sao': ' 5star ',
            'starstarstarstarstar': ' 5star ', '1 sao': ' 1star ', '1sao': ' 1star ','2 sao':' 1star ','2sao':' 1star ',
            '2 starstar':' 1star ','1star': ' 1star ', '0 sao': ' 1star ', '0star': ' 1star ',
            }

    for k, v in replace_list.items():
        text = text.replace(k, v)
    return text

# Từ điển tích cực, tiêu cực, phủ định
def load_sentiment_dicts(path_pos, path_nag, path_not):
    with codecs.open(path_pos, 'r', encoding='UTF-8') as f:
        pos = f.readlines()
    pos_list = [n.strip() for n in pos]

    with codecs.open(path_nag, 'r', encoding='UTF-8') as f:
        nag = f.readlines()
    nag_list = [n.strip() for n in nag]

    with codecs.open(path_not, 'r', encoding='UTF-8') as f:
        not_ = f.readlines()
    not_list = [n.strip() for n in not_]

    return pos_list, nag_list, not_list

# Phân tích tình cảm bằng từ điển được xác định trước
def add_sentiment_features(text, pos_list, nag_list, not_list):
    # chuyen punctuation thành space
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    text = text.translate(translator)

    text = ViTokenizer.tokenize(text)
    texts = text.split()
    len_text = len(texts)

    texts = [t.replace('_', ' ') for t in texts]
    for i in range(len_text):
        cp_text = texts[i]
        if cp_text in not_list: # Xử lý vấn đề phủ định (VD: áo này chẳng đẹp--> áo này notpos)
            numb_word = 2 if len_text - i - 1 >= 4 else len_text - i - 1

            for j in range(numb_word):
                if texts[i + j + 1] in pos_list:
                    texts[i] = 'notpos'
                    texts[i + j + 1] = ''

                if texts[i + j + 1] in nag_list:
                    texts[i] = 'notnag'
                    texts[i + j + 1] = ''
        else: #Thêm feature cho những sentiment words (áo này đẹp--> áo này đẹp Tích cực)
            if cp_text in pos_list:
                texts.append('Tích cực')
            elif cp_text in nag_list:
                texts.append('Tiêu cực')

    text = u' '.join(texts)

    #remove nốt những ký tự thừa thãi
    text = text.replace(u'"', u' ')
    text = text.replace(u'️', u'')
    text = text.replace('🏻','')
    return text

# overall preprocessing
def text_preprocess(document, pos_list, nag_list, not_list):
    #đưa về lower
    document = document.lower()
    # xóa html code
    document = remove_html(document)
    # chuẩn hóa unicode
    document = convert_unicode(document)
    
    # chuẩn hóa các ký tự đặc biệt
    document = normalize_money(document)
    document = normalize_hastag(document)
    document = normalize_website(document)
    document = nomalize_emoji(document)
    document = normalize_elongate(document)
    document = normalize_acronyms(document)
    document = remove_numbers(document)

    # chuẩn hóa cách gõ dấu tiếng việt
    document = standardize_sentence_typing(document)
    # tách từ
    document = word_tokenize(document, format="text")
    # đưa về lower
    document = document.lower()
    # xóa các ký tự không cần thiết
    document = remove_unnecessary(document)
    # xử lý vấn đề phủ định
    document = add_sentiment_features(document, pos_list, nag_list, not_list)
    return document.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation))).replace(' '*4, ' ').replace(' '*3, ' ').replace(' '*2, ' ').strip()