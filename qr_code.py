import qrcode

from path import Path
from PIL import Image, ImageDraw


class QrCode:
    URL_TO_REDIRECT: str
    PATH_IMAGE: Path
    PATH_TO_SAVE_QR_CODE: Path

    def __init__(
            self,
            url_to_redirect: str,
            path_image: Path,
            path_to_sav_qr_code: Path,
        ):
        self.URL_TO_REDIRECT = url_to_redirect
        self.PATH_IMAGE = path_image
        self.PATH_TO_SAVE_QR_CODE = path_to_sav_qr_code

    def get_background(self, length_qr):
        try:
            background = Image.open(self.PATH_IMAGE).resize((length_qr, length_qr)).convert("RGBA")
        except:
            return None

        return background

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=1,
        )
        qr.add_data(self.URL_TO_REDIRECT)
        qr.make(fit=True)
        img = qr.get_matrix()

        coeff = 20
        coeff_small = round(coeff / 3)
        length_qr = len(img) * coeff

        background = self.get_background(length_qr)

        back_im = Image.new('RGBA', (length_qr, length_qr), (0, 0, 0, 0))

        black_1 = (0, 0, 0, 0)
        black_2 = (0, 0, 0, 230)
        white_1 = (255, 255, 255, 50)
        white_2 = (255, 255, 255, 230)

        white_3 = (0, 0, 0, 0)

        idraw = ImageDraw.Draw(back_im, "RGBA")

        x = 0
        y = 0
        for string in qr.get_matrix():
            this_str = ''
            for i in string:
                if i:
                    this_str += '1'
                    # idraw.ellipse((x + coeff_small, y + coeff_small, x + coeff - coeff_small, y + coeff - coeff_small),
                    #               fill=black_2)

                    # idraw.rectangle((x, y, x + coeff, y + coeff), fill=black_1)

                    idraw.rectangle((x + coeff_small, y + coeff_small, x + coeff - coeff_small, y + coeff - coeff_small),
                                    fill=black_2)


                else:
                    this_str += '0'
                    # idraw.ellipse((x + coeff_small, y + coeff_small, x + coeff - coeff_small, y + coeff - coeff_small),
                    #               fill=white_2)
                    # idraw.rectangle((x, y, x + coeff, y + coeff), fill=white_1)
                    idraw.rectangle((x + coeff_small, y + coeff_small, x + coeff - coeff_small, y + coeff - coeff_small),
                                    fill=white_2)
                x += coeff
            x = 0
            y += coeff

        idraw.rectangle((0, 0, coeff * 9, coeff * 9), fill=white_1)
        idraw.rectangle((length_qr, 0, length_qr - coeff * 9, coeff * 9), fill=white_1)
        idraw.rectangle((0, length_qr, coeff * 9, length_qr - coeff * 9), fill=white_1)
        idraw.rectangle((length_qr - coeff * 10, length_qr - coeff * 9, length_qr - coeff * 6, length_qr - coeff * 6),
                        fill=white_1)

        idraw.rectangle((coeff, coeff, coeff * 8, coeff * 2), fill=black_2)
        idraw.rectangle((length_qr - coeff * 8, coeff, length_qr - coeff, coeff * 2), fill=black_2)
        idraw.rectangle((coeff, coeff * 7, coeff * 8, coeff * 8), fill=black_2)
        idraw.rectangle((length_qr - coeff * 8, coeff * 7, length_qr - coeff, coeff * 8), fill=black_2)
        idraw.rectangle((coeff, length_qr - coeff * 7, coeff * 8, length_qr - coeff * 8), fill=black_2)
        idraw.rectangle((coeff, length_qr - coeff * 2, coeff * 8, length_qr - coeff), fill=black_2)
        idraw.rectangle((length_qr - coeff * 7, length_qr - coeff * 7, length_qr - coeff * 8, length_qr - coeff * 8),
                        fill=black_2)
        idraw.rectangle((coeff * 3, coeff * 3, coeff * 6, coeff * 6), fill=black_2)
        idraw.rectangle((length_qr - coeff * 3, coeff * 3, length_qr - coeff * 6, coeff * 6), fill=black_2)
        idraw.rectangle((coeff * 3, length_qr - coeff * 3, coeff * 6, length_qr - coeff * 6), fill=black_2)
        idraw.rectangle((coeff, coeff, coeff * 2, coeff * 8), fill=black_2)
        idraw.rectangle((coeff * 7, coeff, coeff * 8, coeff * 8), fill=black_2)

        idraw.rectangle((length_qr - coeff, coeff, length_qr - coeff * 2, coeff * 8), fill=black_2)
        idraw.rectangle((length_qr - coeff * 7, coeff, length_qr - coeff * 8, coeff * 8), fill=black_2)

        idraw.rectangle((coeff, length_qr - coeff, coeff * 2, length_qr - coeff * 8), fill=black_2)
        idraw.rectangle((coeff * 7, length_qr - coeff, coeff * 8, length_qr - coeff * 8), fill=black_2)

        idraw.rectangle((length_qr - coeff * 10, length_qr - coeff * 10, length_qr - coeff * 9, length_qr - coeff * 5),
                        fill=black_2)
        idraw.rectangle((length_qr - coeff * 6, length_qr - coeff * 10, length_qr - coeff * 5, length_qr - coeff * 5),
                        fill=black_2)

        idraw.rectangle((length_qr - coeff * 6, length_qr - coeff * 10, length_qr - coeff * 10, length_qr - coeff * 9),
                        fill=black_2)
        idraw.rectangle((length_qr - coeff * 6, length_qr - coeff * 6, length_qr - coeff * 10, length_qr - coeff * 5),
                        fill=black_2)

        background.paste(back_im, (0, 0), back_im)
        background.save(self.PATH_TO_SAVE_QR_CODE)
