import React, { useState } from 'react';
import axios from 'axios';

//Styled components
import styled from 'styled-components';

const ChatWindow = styled.div`
  width: 400px;
  height: 500px;  
  border: 1px solid #ddd;
  border-radius: 4px;
  overflow: hidden;
`;

const ChatLog = styled.div`
  height: 90%;
  overflow-y: scroll;
  padding: 10px;
`;

const ChatInput = styled.textarea`
  width: 100%; 
  height: 10%;
  padding: 10px;
  box-sizing: border-box;
  border: none;
  border-top: 1px solid #ddd;
  resize: none;
`;

function Chatbot() {

  const [chatLog, setChatLog] = useState([{
    user: 'bot', 
    message: 'Hi there! I\'m a Chatbot, ask me anything.'
  }]);
  const [input,setInput]=useState("")
  const handleKeyDown = async (e) => {
    if (e.keyCode === 13) {
        // console.log(e,"e")
      handleSubmit(e);
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    const myinput = input
    setChatLog([...chatLog, { user: 'human', message: myinput }]);
const preChat= [...chatLog, { user: 'human', message: myinput }]
    // e.target.children[0].value = ''; 
          setInput("")

    try {
      const response = await axios.post('http://127.0.0.1:5000/data', {
        data:myinput
      });
      console.log(...preChat,"....chatlog")
      setChatLog([...preChat, { user: 'bot', message: response.data.message }]); 


    } catch(err) {
      setChatLog([...chatLog, { user: 'bot', message: 'Sorry, something went wrong.' }]);
    }
  }
  

  return (
    <ChatWindow>
      <ChatLog>
        {chatLog.map((msg, index) => (
          <div key={index}>
            <b>{msg.user}:</b> {msg.message}
          </div>
        ))}
      </ChatLog>

      <form 
    //   onSubmit={handleSubmit} 
      style={{
        width:"100%",
        // display:"flex",
        // height:'100%',
        flexDirection:"column"
      }}>
        <ChatInput placeholder="Ask me anything..." style={{
            // width:"100%",
            // height:"50%",
            resize:"none",
        }}
        value={input}
        onChange={(e)=>setInput(e.target.value)}
        onKeyDown={handleKeyDown} 
        />
        {/* <button className='' style={{
            // width: '100%',
            // height:"50%",
            // background:"red",
            // display:"flex"
            position:"absolute",
            display:"block",

        }} type="submit">Send</button> */}
        
      </form>
    </ChatWindow>
  );
}

export default Chatbot;