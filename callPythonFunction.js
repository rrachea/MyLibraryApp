import axios from 'axios';

const FLASK_URL = 'http://localhost:5000';

const callPythonFunction = async (userInput) => {
    try {
        const response = await axios.post(`${FLASK_URL}/api/data`, {
            userInput: userInput,
        });

        // Handle the response from the Python function here
        console.log(response.data);
        return response.data;
    } catch (error) {
        // Handle any errors here
        throw error;
    }
};

export default callPythonFunction;
