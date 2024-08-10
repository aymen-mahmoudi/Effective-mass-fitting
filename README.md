# Effective mass fitting


## Description
This project allows us to estimate the effective mass of an electronic band by fitting this latter with a parabolic shape.
<br>  
For the bands near the Fermi level, the dispersion relation can be considered as follows:
$$ \frac{1}{2m^{*}} = \frac{1}{\hbar^{2}} \frac{\mathrm{d} E }{\mathrm{d} k^{2}}  $$
<span style="white-space: pre-line"></span>
$$E(k) \propto c\times k^{2} $$</span>
Knowing the concavity of the parabola, the effective mass can be calculated via: 
</span>
$$ m^{*} = \frac{\hbar^{2}}{2c} $$

## Usage
You need to provide an image with the ARPES 2D scan to be opened via the browsing button. Then, you can fit the parabola with the wanted band. The effective mass value is updated via the update button.

<img src="screenshot_app.png"
     alt="gui" width="600" height="450"
      style="float: center"/>


## Installation
To use the app, you can download and directly execute the file mass.exe (just for Windows X64). Otherwise, you can run the main.py script which is available within the necessary resources. I recommend to setup a python 3.8 virtual environment and adding the required libraries using the following command after cloning the rep (you can just download the rep in case you don't use git):
```console
pip install -r requirements.txt
```

## Roadmap
 <ul>
  <li>Avoid the crash of the app in case of empty value</li>
  <li>Transform the project on a desktop application</li>
</ul> 

## Support and Contributing
Let me know if you have any suggestions/ideas to enhance those scripts or add further settings. I want you to know that your suggestions are warmly appreciated.
<br>
In case of a problem, it is strongly recommended that an issue be posted. For a more confidential demand, don't hesitate to email me.

## Acknowledgment
I thank Geoffroy Kremer for testing and verifying the formula.  




