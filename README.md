## Chat Server with Colored Terminal Output

This project implements a simple multi-client chat server using Python. It demonstrates how to set up a server that can handle multiple client connections, broadcast messages to all connected clients, and handle client disconnections gracefully. Additionally, the project includes instructions on how to change the text color in the terminal for better readability.

## Demo:-

![alt text](<Screenshot 2024-05-19 022450.png>)

## Features

Multi-client chat server: Allows multiple clients to connect and communicate with each other via the server.

Broadcasting messages: Messages sent by one client are broadcasted to all other connected clients.

Handling client connections and disconnections: Manages clients joining and leaving the chat, ensuring the server remains stable.

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/yourusername/Server-Client_chat.git
   cd Server-Client_chat

   ```

2. **Running the Server**

   ```sh
   python server.py

   ```

3. **Running the Client**
   ```sh
   python client.py
   ```

To start the chat server, execute the server.py script. This will start the server on 127.0.0.1:55555 and begin listening for client connections. Clients can connect to this server and start chatting with each other.

Using ANSI Escape Codes: Directly embed ANSI escape codes in your print statements to change text color. This method is quick and works on most Unix-like systems.

# Server Functionality

Broadcasting Messages: The server relays messages from one client to all other connected clients. This keeps everyone in the chat updated with new messages.

# Handling Connections and Disconnections:

When a client connects, they are prompted to provide a nickname. This nickname is broadcasted to all other clients. If a client disconnects, the server notifies the remaining clients.

# Feel free to adjust this README to better fit the specifics of your project or to add any additional sections that may be necessary.
