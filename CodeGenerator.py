from barcode import Code128
from barcode.writer import ImageWriter
import qrcode


class CodeGenerator:

    def create_barcode(self, text):
        """
        在other文件夹中创建名为barcode.png的条形码图片
        :param number: 输入的文本
        :return: 图片的相对路径
        """

        my_code = Code128(text, writer=ImageWriter())
        my_code.save("./other/barcode")
        return "./other/barcode.png"

    def create_QRcode(self, text):
        """
        在other文件夹中创建名为QRcode.png的二维码图片
        :param text: 输入的文本/链接
        :return: 图片的相对路径
        """
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        pic_path = './other/QRcode.png'
        img.save(pic_path)
        return pic_path
