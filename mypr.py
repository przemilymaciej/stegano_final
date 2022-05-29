import time, os
from stegano import lsb

IMAGES_PATH = "./"
IMAGE_NAMES = [
    "78",
    "154",
    "526"
]

def read_img(img_name):
    return lsb.reveal(IMAGES_PATH + img_name + ".png")


def README_append(data):
    with open("README.md", "a") as f:
        f.write(data)


def encrypt_image_with_message(img_name, msg, output_name):
    secret = lsb.hide(IMAGES_PATH + img_name + ".png", msg)
    output_path = IMAGES_PATH + output_name + ".png"
    secret.save(output_path)


if __name__ == "__main__":

    # README Cleanup
    with open("README.md", "w") as f:
        f.close()

    for image in IMAGE_NAMES:
        README_append(f"Nazwa obrazka: {image}.png\n")
        img_path = IMAGES_PATH + image + ".png"
        file_size = os.path.getsize(img_path)
        README_append(f"Rozmiar pliku przed = {file_size}\n")

    README_append("------------------------------------------------------------\n")

    for image in IMAGE_NAMES:
        # Short message
        message = "hello"
        README_append(f"Nazwa obrazka: {image}.png\n")
        README_append(f"Szyfrowanie wiadomosci: {message}\n")
        output_name_short = image + "-short_message"

        start = time.time()
        encrypt_image_with_message(image, message, output_name_short)
        end = time.time()
        encrypt_execution = end - start
        README_append(f"Czas szyfrowania= {encrypt_execution}\n")

        start = time.time()
        read_img(output_name_short)
        end = time.time()
        decrypt_execution = end - start
        README_append(f"Czas deszyfrowania= {decrypt_execution}\n")

        output_path = IMAGES_PATH + output_name_short + ".png"
        file_size = os.path.getsize(output_path)
        README_append(f"Rozmiar pliku po: = {file_size}\n")

        # Long message
        message = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. \
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an \
unknown printer took a galley of type and scrambled it to make a type specimen book. \
It has survived not only five centuries, but also the leap into electronic typesetting, \
remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset \
sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like \
Aldus PageMaker including versions of Lorem Ipsum"
        README_append(f"Nazwa obrazka: {image}.png\n")
        README_append(f"Szyfrowanie wiadomosci: {message}\n")
        output_name_short = image + "-long_message"

        start = time.time()
        encrypt_image_with_message(image, message, output_name_short)
        end = time.time()
        encrypt_execution = end - start
        README_append(f"Czas szyfrowania= {encrypt_execution}\n")

        start = time.time()
        read_img(output_name_short)
        end = time.time()
        decrypt_execution = end - start
        README_append(f"Czas deszyfrowania= {decrypt_execution}\n")

        output_path = IMAGES_PATH + output_name_short + ".png"
        file_size = os.path.getsize(output_path)
        README_append(f"Rozmiar pliku po: = {file_size}\n")

        # Extra long message
        message = "Contrary to popular belief, Lorem Ipsum is not simply random text. \
It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, \
a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, \
from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable \
source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) \
by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. \
The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32.\
There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some \
form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use \
a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. \
All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the \
first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful \
of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum \
is therefore always free from repetition, injected humour, or non-characteristic words etc.\
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its \
layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to \
using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web \
page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many \
web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, \
sometimes on purpose (injected humour and the like)."
        README_append(f"Nazwa obrazka: {image}.png\n")
        README_append(f"Szyfrowanie wiadomosci: {message}\n")
        output_name_short = image + "-extra_long_message"

        start = time.time()
        encrypt_image_with_message(image, message, output_name_short)
        end = time.time()
        encrypt_execution = end - start
        README_append(f"Czas szyfrowania= {encrypt_execution}\n")

        start = time.time()
        read_img(output_name_short)
        end = time.time()
        decrypt_execution = end - start
        README_append(f"Czas deszyfrowania= {decrypt_execution}\n")

        output_path = IMAGES_PATH + output_name_short + ".png"
        file_size = os.path.getsize(output_path)
        README_append(f"Rozmiar pliku po: = {file_size}\n")

        README_append("------------------------------------------------------------\n")
