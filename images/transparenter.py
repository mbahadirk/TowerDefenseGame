from PIL import Image

def remove_background(input_image_path, output_image_path):
    # Resmi açın
    img = Image.open(input_image_path)

    # Resmi RGBA modunda açtığınızdan ve arka planın tamamen şeffaf olduğundan emin olun
    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    # Resmi kaydedin (arka planı kaldırmış bir biçimde)
    img.save(output_image_path, 'PNG')

if __name__ == "__main__":
    input_image = "zombie.png"  # Giriş resminin yolunu değiştirin
    output_image = "output.png"  # Çıktı resmi yolunu belirleyin

    remove_background(input_image, output_image)