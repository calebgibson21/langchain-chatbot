import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import { Configuration } from 'openai';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Container, Form } from 'react-bootstrap';

const configuration = new Configuration({
  apiKey: process.env.REACT_APP_OPENAI_API_KEY,
});

function App() {
  const [questionType, setQuestionType] = useState('text');
  const [modelResponse, setModelResponse] = useState('');
  const [userInput, setUserInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [messageId, setMessageId] = useState(1);

  const handleSendData = async (e) => {
    e.preventDefault();
    console.log("form submitted");
    console.log(userInput)
    const prompt = `This is a prompt`;
    const test = `This is a test`;
    const endpoint = `http://localhost:8000/message/${messageId}`;
    const body = {userInput, prompt, test}
  

    const response = await fetch(endpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body)
    });

    const data = await response.json();
    setModelResponse(data.response)
  console.log(data.response);
  incrementMessageId();
  };

  const incrementMessageId = () => {
    setMessageId(messageId + 1);
  }

  const handleChange = (e) => {
    setUserInput(e.target.value);
  }


  
  return (
    <div className="App">
      <header className="App-header">
        <Container>
          <h1>OpenAI Demo</h1>
          <Form onSubmit={handleSendData}>
            <Form.Control
              type='text'
              value={userInput}
              onChange={handleChange}
              />
            <Button variant='info' type='submit'>Submit</Button>
          </Form>
        </Container>
      </header>
    </div>
  );
}

export default App;
