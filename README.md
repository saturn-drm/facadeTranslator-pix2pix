# facadeTranslator-pix2pix

> This is the work folder for the final project at gsd-6365, by Zihan &amp; Jack

* The main part of the machine learning is forked from [pix2pix-tensorflow](https://github.com/affinelayer/pix2pix-tensorflow).
* There are some tiny change in code regarding Tensorflow version.
* Contained some customized datasets for the project.

## Usage

### Clone to local

```sh
git clone https://github.com/saturn-drm/facadeTranslator-pix2pix.git
```

### Typical training commnad

```sh
python pix2pix.py   --mode train   --output_dir trainRes/westernPic2Seg   --max_epochs 20   --input_dir data/westernPic2Seg/facades/train   --which_direction BtoA
```

### Typical testing command

```sh
python pix2pix.py   --mode test   --output_dir output/westernPic2Seg/facades_test   --input_dir data/westernPic2Seg/facades/val   --checkpoint trainRes/westernPic2Seg
```

### Reverse the input images

> This command will change the location of segment half and photo half in all the photos.

```sh
# switch to the data folder
python reversePic.py path/to/source/folder path/to/target/folder
```

### To push your results to GitHub through command line

```sh
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

git add .
git status
git commit -m 'commite name'
git push origin HEAD:master
# enter your username and pwd with instructions
```

**Note that the results files after training is too large (larger than 100MB) to be uploaded. Just keep it local.**

### Update files in the cloud storage

```sh
git pull https://github.com/saturn-drm/facadeTranslator-pix2pix.git main
# OR
git pull origin main
```

