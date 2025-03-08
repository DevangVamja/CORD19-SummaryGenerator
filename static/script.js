document.getElementById("send-btn").addEventListener("click", sendMessage);
document.getElementById("user-input").addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
        sendMessage();
    }
});

function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;

    // Add user message to chat box
    appendMessage("user", userInput);

    // Clear input field
    document.getElementById("user-input").value = "";

    // Show typing indicator
    showTypingIndicator();

    // Send message to Flask backend
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then((response) => response.json())
    .then((data) => {
        // Hide typing indicator
        hideTypingIndicator();

        // Add bot response to chat box
        appendMessage("bot", data.response);
    })
    .catch((error) => {
        console.error("Error:", error);
        hideTypingIndicator();
    });
}

function appendMessage(sender, message) {
    const chatBox = document.getElementById("chat-box");
    const messageElement = document.createElement("div");
    messageElement.classList.add("message", `${sender}-message`);
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);

    // Scroll to the bottom of the chat box
    chatBox.scrollTop = chatBox.scrollHeight;
}

function showTypingIndicator() {
    const typingIndicator = document.getElementById("typing-indicator");
    typingIndicator.style.display = "block";
}

function hideTypingIndicator() {
    const typingIndicator = document.getElementById("typing-indicator");
    typingIndicator.style.display = "none";
}