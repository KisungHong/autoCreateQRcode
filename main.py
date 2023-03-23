import qrcode

# qr_data1 = 'www.naver.com'
# qr_img1 = qrcode.make(qr_data1)
#
# qr_data2 = 'www.zigbang.com'
# qr_img2 = qrcode.make(qr_data2)
#
# save_path1 = 'qr_codes' + qr_data1 + '.png'
# qr_img1.save(save_path1)
#
# save_path2 = 'qr_codes' + qr_data2 + '.png'
# qr_img2.save(save_path2)

file_path = '/Users/kisung/PycharmProjects/autoCreateQRcode/qr_url.txt'
with open(file_path, 'rt', encoding='UTF8') as f:
    read_lines = f.readline()

    for line in read_lines:
        line = line.strip()
        print(line)

        qr_data = line
        qr_image = qrcode.make(qr_data)

        save_path = 'qr_codes' + qr_data + '.png'
        qr_image.save(save_path)
