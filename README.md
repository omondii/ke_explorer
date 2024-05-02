# Exploreke
## A Blog website for campers, tourists and explorers to post articles and photos of good camping locations around Kenya. Users can create and delete accounts, post and bookmark other users posts. 


# Pre-Requisites
1. Python installed
2. Nodejs installed

# Installation
1. Clone the repository in your desired folder, the dot(.) is to ensure you don't replicate the repos name
`git clone https://https://github.com/omondii/ExploreKE.git .`

2. Change to the cloned repository
`cd ExploreKE`

3. Start both the frontend and backend.

A. Client
   - Open the terminal and navigate to the frontend folder
   `cd client` 
   - install the required packages
   `npm install`
   - start the local development server
   `npm run start`

B. server
   - On the terminal, navigate to the backend folder
   `cd backend`
   - Create and activate a virtual environment
   ```
   # create a virtual env
   python3 venv 'vitualenv-name'
   # activate it
   source venv/bin/activate
   ```
   - install project dependencies
   `pip install -r requirements.txt`
   - Start the backend development server
   `./server`

4. Visit http://localhost:3000/

>[!IMPORTANT]
>Not all of the mentioned functionalities have been fully implemented. This project is still in active development.