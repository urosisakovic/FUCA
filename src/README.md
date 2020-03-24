# Instructions for running the FUCA web application


## Clone repository
Have your computer connected to the Internet.  
Open command line interface and navigate to a location where you want to clone this repo.  
Clone this repo:<br />`git clone https://github.com/urosisakovic/FUCA.git`<br />


## Download Miniconda
Follow this [link](https://docs.conda.io/en/latest/miniconda.html) and download Miniconda.


## Created conda environment
Open Conda CLI. Create conda environment for this project: <br />
`conda env create -n fuca python=3.6`<br /><br />
Activate the created environment:<br />`conda activate fuca`<br /><br />

Every future time you wish to start the project, you will have to activate `fuca` environment as well.<br />

## Install needed Python packages
Navigate to the root of this repo using Conda CLI. Download necessary Python packages: <br />`pip install -r requirements.txt`<br />


## Start the application
Navigate to the /src subdirectory of this repo using Conda CLI.
Start the project by runnning the python script:<br />`python run.py`<br />


## Inspect the application in web browser
Open web browser of your choice (Chrome, Firefox, etc.) and visit http://localhost:5000.