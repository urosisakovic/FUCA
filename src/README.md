# Instructions for setting up the environment


## Clone repository
Have your computer connected to the Internet.  
Open command line interface and navigate to a location to which you want to clone this repo.  
Clone this repo:<br />`git clone https://github.com/urosisakovic/FUCA.git`<br />


## Download Miniconda
Follow this [link](https://docs.conda.io/en/latest/miniconda.html) and download Miniconda.


## Created conda environment
Open Conda CLI. Create conda environment for this project: <br />
`conda env create -n fuca python=3.6`<br /><br />
Activate the created environment:<br />`conda activate fuca`<br />


## Install needed Python packages
Download necessary Python packages: <br />`pip install -r requirements.txt`<br />


## Start the application
Navigate to the /src subdirectory of this repo using Conda CLI.
Start the project by runnning the python script:<br />`python run.py`<br />


## Inspect the application in web browser
Open web browser of your choice (Chrome, Firefox, etc.) and visit http://localhost:5000.