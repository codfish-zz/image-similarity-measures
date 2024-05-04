from image_similarity_measures.evaluate import evaluation
from pathlib import Path


def get_file_name(path):
    path = Path(path)
    return path.name


def image_compare(org_img_path, pred_img_path):
    output_dict = evaluation(
        org_img_path=org_img_path,
        pred_img_path=pred_img_path,
        metrics=["ssim", "fsim"],
    )

    print("%s vs %s" % (get_file_name(org_img_path), get_file_name(pred_img_path)))
    print(output_dict)


def main():
    image_compare("example/Book1.jpg", "example/Book2.jpg")
    image_compare("example/Book1.jpg", "example/Book1.jpg")

    image_compare("example/MasterCard1.jpg", "example/MasterCard2.jpg")
    image_compare("example/MasterCard1.jpg", "example/MasterCard1.jpg")

    image_compare("example/Visa1.jpg", "example/Visa2.jpg")
    image_compare("example/Visa1.jpg", "example/Visa1.jpg")


if __name__ == "__main__":
    main()
