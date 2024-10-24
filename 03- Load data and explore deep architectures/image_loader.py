import os
import shutil


def load_dogs_vs_cats(original_dir, base_dir, clean_up=True):

    # train dataset directory
    train_dir = os.path.join(base_dir, 'train')
    os.makedirs(train_dir, exist_ok=True)

    # validation dataset directory
    validation_dir = os.path.join(base_dir, 'validation')
    os.makedirs(validation_dir, exist_ok=True)

    # test dataset directory
    test_dir = os.path.join(base_dir, 'test')
    os.makedirs(test_dir, exist_ok=True)


    # train directory for cats images
    train_dir_cats = os.path.join(train_dir, 'cats')
    os.makedirs(train_dir_cats, exist_ok=True)

    # validarion directory for cats images
    validarion_dir_cats = os.path.join(validation_dir, 'cats')
    os.makedirs(validarion_dir_cats, exist_ok=True)

    # test directory for cats images
    test_dir_cats = os.path.join(test_dir, 'cats')
    os.makedirs(test_dir_cats, exist_ok=True)


    # train directory for dogs images
    train_dir_dogs = os.path.join(train_dir, 'dogs')
    os.makedirs(train_dir_dogs, exist_ok=True)

    # validarion directory for cats images
    validarion_dir_dogs = os.path.join(validation_dir, 'dogs')
    os.makedirs(validarion_dir_dogs, exist_ok=True)

    # test directory for cats images
    test_dir_dogs = os.path.join(test_dir, 'dogs')
    os.makedirs(test_dir_dogs, exist_ok=True)

    #  Cat images
    # copy first 1000 cat images into train cats directory
    fnames = [f'cat.{i}.jpg' for i in range(1000)]
    for fname in  fnames :
        src = os.path.join(original_dir, fname)
        dest = os.path.join(train_dir_cats, fname)
        shutil.copyfile(src, dest)


    # copy 1000 to 1500 cat images into validation cats directory
    fnames = [f'cat.{i}.jpg' for i in range(1000, 1500)]
    for fname in  fnames :
        src = os.path.join(original_dir, fname)
        dest = os.path.join(validarion_dir_cats, fname)
        shutil.copyfile(src, dest)


    # copy 1500 to 2000 cat images into test cats directory
    fnames = [f'cat.{i}.jpg' for i in range(1500, 2000)]
    for fname in  fnames :
        src = os.path.join(original_dir, fname)
        dest = os.path.join(test_dir_cats, fname)
        shutil.copyfile(src, dest)


    # Dog Images    
    # copy first 1000 cat images into train cats directory
    fnames = [f'dog.{i}.jpg' for i in range(1000)]
    for fname in  fnames :
        src = os.path.join(original_dir, fname)
        dest = os.path.join(train_dir_dogs, fname)
        shutil.copyfile(src, dest)


    # copy 1000 to 1500 cat images into validation cats directory
    fnames = [f'dog.{i}.jpg' for i in range(1000, 1500)]
    for fname in  fnames :
        src = os.path.join(original_dir, fname)
        dest = os.path.join(validarion_dir_dogs, fname)
        shutil.copyfile(src, dest)


    # copy 1500 to 2000 cat images into test cats directory
    fnames = [f'dog.{i}.jpg' for i in range(1500, 2000)]
    for fname in  fnames :
        src = os.path.join(original_dir, fname)
        dest = os.path.join(test_dir_dogs, fname)
        shutil.copyfile(src, dest)

    # Validate Fetch

    print('total training cat images: ', len(os.listdir(train_dir_cats)))
    print('total validation cat images: ', len(os.listdir(validarion_dir_cats)))
    print('total test cat images: ', len(os.listdir(test_dir_cats)))

    print()

    print('total training dog images: ', len(os.listdir(train_dir_dogs)))
    print('total validation dog images: ', len(os.listdir(validarion_dir_dogs)))
    print('total test dog images: ', len(os.listdir(test_dir_dogs)))
 
    # if clean_up:
        # os.path.join(original_dir, 'dogs_vs_cats.zip')
