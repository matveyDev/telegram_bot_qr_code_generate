from path import Path
from generate_qr_code import gen_qr_code


url_to_redirect = ''
path_to_download = Path().joinpath('.', '38.jpg')
path_to_save = Path().joinpath('.', 'test.png')

gen_qr_code(
    url_to_redirect,
    path_to_download,
    path_to_save
)
