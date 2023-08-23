I. For the Backend
  1. If you have cloned this repo. You must have python==3.10 or higher (Download it from https://www.python.org/downloads/ ).
  2. The first step is to create a virtual environment. (You must have Anaconda for it or you can download and install it from https://www.anaconda.com/download for windows.)
    a.To create a virtual environment open anaconda prompt in the location you have cloned the repository.
    b.If you are in the relevant directory run command: conda create -p venv python==3.10 -y (venv is your virtual environment name)
    c.Activate the virtual environment by running command: conda activate venv/
  3. Now install the dependencies by running command in your activated Conda terminal: pip install -r requirements.txt (note that you must have Visual Studio C++ Build tool for install ChromaDB or download it from https://visualstudio.microsoft.com/downloads/?q=build+tools and Select the package Setup Development for C++.)
  4. After all the Dependencies are installed run app.py in your python activate terminal by command: python app.py.
     
II. For the FrontEnd
  1. You must have Node.Js package installed in your system (or Download Node package from https://nodejs.org/en/download ).
  2. In the root directory of the cloned repository.
  3. Navigate into the frontend folder.
  4. Open the command prompt in the folder.
  5. Install dependencies by running command npm install.
  6. After installing the dependencies, to start the app run command npm start.

Notes:
1. Make sure both the apps (frontend and backend) are running for the chatbot to work seamlessly.


A simple preview of the frontend 
![chatbot](https://github.com/survivorzik/secass/assets/95278663/00338868-7f14-4a17-9e7c-892922447f1e)
