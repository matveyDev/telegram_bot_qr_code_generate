from qr_code import QrCode


def create_qr_code(
    url_to_redirect,
    path_image,
    path_saved_qr_code
):
    qr_code = QrCode(
        url_to_redirect,
        path_image,
        path_saved_qr_code
    )
    qr_code.generate_qr_code()

    return qr_code
