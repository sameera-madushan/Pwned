# Pwned - Check Your Passwords

Pwned is a simple command-line python script to check if you have a password that has been compromised in a data breach. This script uses [haveibeenpwned](https://haveibeenpwned.com/API/v3) API to check whether your passwords were leaked during one of the many breaches of online services.

This API uses [k-Anonymity model](https://en.wikipedia.org/wiki/K-anonymity) that allows a password to be searched for by partial hash in order to anonymously verify if a password was leaked without disclosing the searched password.

You cn read the medium article that i wrote about this from [here.](https://medium.com/@sameeramadushan/your-password-has-likely-been-stolen-heres-how-to-check-ddc2de86ab8c?source=friends_link&sk=e2467b4903b4916ebb1d6a6f8fdd4f9c)

<p align="center">
  <img src="https://user-images.githubusercontent.com/55880211/78676221-c7131200-7903-11ea-9475-c86fb0be3962.png">
</p>

## How pwned script works
<p align="center">
  <img src="https://user-images.githubusercontent.com/55880211/78675721-1573e100-7903-11ea-8f9d-4e411b897e6f.png">
</p>

## Git Installation
```
# clone the repo
$ git clone https://github.com/sameera-madushan/Pwned.git

# change the working directory to Pwned
$ cd Pwned

# install the requirements
$ pip3 install -r requirements.txt
```

## Usage

```
python pwned.py -p <your password here>
```

## Support & Contributions
- Please ⭐️ this repository if this project helped you!
- Contributions of any kind welcome!

<a href="https://www.buymeacoffee.com/sameeramadushan" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>



## License
Pwned is made with ♥ by [@_\_sa_miya__](https://twitter.com/__sa_miya__) and it is released under the MIT license.
