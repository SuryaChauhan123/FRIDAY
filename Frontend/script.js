const input = document.getElementById("userInput");
const chat = document.querySelector(".chat-container");

input.addEventListener("keydown", function(event) {

    if (event.key === "Enter" && input.value.trim() !== "") {

        const message = input.value;

        // User message
        const userMessage = document.createElement("div");
        userMessage.classList.add("user-message");
        userMessage.textContent = message;

        chat.appendChild(userMessage);

        // Temporary FRIDAY response
        const fridayMessage = document.createElement("div");
        fridayMessage.classList.add("friday-message");
        fridayMessage.textContent = "I'm processing that...";

        chat.appendChild(fridayMessage);

        // Clear input
        input.value = "";

        // Scroll down
        window.scrollTo({
            top: document.body.scrollHeight,
            behavior: "smooth"
        });
    }
});