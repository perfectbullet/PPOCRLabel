import os
import fitz


def get_images_from_pdf(pdf_path: str, out_path: str):
    '''
    get images from pdf
    '''
    if os.makedirs(out_path, exist_ok=True) == False:
        print('{} has existed'.format(out_path))
    # open the file
    pdf_name = os.path.basename(pdf_path).split('.')[0]
    new_out_path = os.path.join(out_path, pdf_name)
    os.makedirs(new_out_path, exist_ok=True)
    pdf_file = fitz.open(pdf_path)


    # iterate over PDF pages
    for page_index in range(len(pdf_file)):

        # get the page itself
        page = pdf_file.load_page(page_index)  # load the page
        image_list = page.get_images(full=True)  # get images on the page

        # printing number of images found in this page
        if image_list:
            print(f"[+] Found a total of {len(image_list)} images on page {page_index}")
        else:
            print("[!] No images found on page", page_index)

        for image_index, img in enumerate(image_list, start=1):
            # get the XREF of the image
            xref = img[0]

            # extract the image bytes
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]

            # get the image extension
            image_ext = base_image["ext"]

            # save the image
            image_name = f"image_{page_index + 1}_{image_index}.{image_ext}"
            image_path = os.path.join(new_out_path, image_name)
            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)
                print(f"[+] Image saved at {image_path}")


if __name__ == '__main__':
    # # pdf路径
    # pdf_path = 'doc/报销单1.PDF'
    # # 保存的图片路径
    # pic_dir = './output'

    pdf_path = r'D:\zj_work\AI数据整理\AI扫描包样本\报销单样本补充\4.PDF'
    pic_dir = r'D:\zj_work\AI数据整理\AI扫描包样本\报销单样本补充\output'
    pdf_dir = ''
    get_images_from_pdf(pdf_path, pic_dir)
